const { app, BrowserWindow, ipcMain, dialog, shell } = require('electron');
const { autoUpdater } = require('electron-updater');
const path = require('path');

// ── App Version ───────────────────────────────────────────────────────────────
const APP_VERSION = app.getVersion();

// ── Haupt-Fenster ─────────────────────────────────────────────────────────────
let mainWindow;

function createWindow() {
  mainWindow = new BrowserWindow({
    width: 1400,
    height: 900,
    minWidth: 900,
    minHeight: 600,
    icon: path.join(__dirname, 'assets', 'icon.ico'),
    title: 'Hirsch Music Hit Maker',
    backgroundColor: '#0d0d0f',
    webPreferences: {
      preload: path.join(__dirname, 'preload.js'),
      nodeIntegration: false,
      contextIsolation: true,
    },
    show: false, // erst nach ready-to-show anzeigen
    titleBarStyle: 'default',
  });

  // App-Dateien laden
  mainWindow.loadFile(path.join(__dirname, 'app', 'index.html'));

  // Fenster smooth einblenden
  mainWindow.once('ready-to-show', () => {
    mainWindow.show();
    // Nach 2 Sekunden auf Updates prüfen
    setTimeout(checkForUpdates, 2000);
  });

  // Externe Links im Browser öffnen
  mainWindow.webContents.setWindowOpenHandler(({ url }) => {
    shell.openExternal(url);
    return { action: 'deny' };
  });
}

// ── Auto-Updater ──────────────────────────────────────────────────────────────
function checkForUpdates() {
  // Nur im gebauten Paket prüfen, nicht in dev
  if (!app.isPackaged) {
    console.log('[Updater] Dev-Modus — kein Auto-Update');
    return;
  }
  autoUpdater.checkForUpdates();
}

// Update verfügbar
autoUpdater.on('update-available', (info) => {
  mainWindow.webContents.send('update-available', {
    version: info.version,
    releaseNotes: info.releaseNotes || 'Neue Verbesserungen und Bug-Fixes.',
  });
});

// Kein Update
autoUpdater.on('update-not-available', () => {
  // Still → kein Dialog
});

// Download-Fortschritt
autoUpdater.on('download-progress', (progress) => {
  mainWindow.webContents.send('update-progress', {
    percent: Math.round(progress.percent),
    transferred: formatBytes(progress.transferred),
    total: formatBytes(progress.total),
    speed: formatBytes(progress.bytesPerSecond) + '/s',
  });
});

// Update heruntergeladen → bereit zum Installieren
autoUpdater.on('update-downloaded', (info) => {
  mainWindow.webContents.send('update-ready', {
    version: info.version,
  });
});

// Fehler
autoUpdater.on('error', (err) => {
  console.error('[Updater] Fehler:', err.message);
  mainWindow.webContents.send('update-error', { message: err.message });
});

// ── IPC Handler ───────────────────────────────────────────────────────────────
// User bestätigt Installation
ipcMain.on('install-update', () => {
  autoUpdater.quitAndInstall(false, true);
});

// User verschiebt Update
ipcMain.on('postpone-update', () => {
  // nichts tun, Update bleibt im Hintergrund
});

// Manuell auf Updates prüfen
ipcMain.on('check-for-updates', () => {
  if (app.isPackaged) {
    autoUpdater.checkForUpdates();
  } else {
    mainWindow.webContents.send('update-not-available-manual');
  }
});

// App-Version abfragen
ipcMain.handle('get-version', () => APP_VERSION);

// ── App-Lifecycle ─────────────────────────────────────────────────────────────
app.whenReady().then(() => {
  createWindow();
  app.on('activate', () => {
    if (BrowserWindow.getAllWindows().length === 0) createWindow();
  });
});

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') app.quit();
});

// ── Hilfsfunktionen ───────────────────────────────────────────────────────────
function formatBytes(bytes) {
  if (bytes < 1024) return bytes + ' B';
  if (bytes < 1024 * 1024) return (bytes / 1024).toFixed(1) + ' KB';
  return (bytes / (1024 * 1024)).toFixed(1) + ' MB';
}
