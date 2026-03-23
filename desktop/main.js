const { app, BrowserWindow, ipcMain, dialog, shell, safeStorage } = require('electron');
const { autoUpdater } = require('electron-updater');
const path = require('path');
const fs   = require('fs');

// ── App Version ───────────────────────────────────────────────────────────────
const APP_VERSION = app.getVersion();

// ── Persistenz-Pfade ──────────────────────────────────────────────────────────
function getUserDataPath(file) {
  return path.join(app.getPath('userData'), file);
}
const KEY_FILE      = getUserDataPath('apikey.enc');
const PROJECTS_FILE = getUserDataPath('projects.json');

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
    show: false,
    titleBarStyle: 'default',
  });

  mainWindow.loadFile(path.join(__dirname, 'app', 'index.html'));

  mainWindow.once('ready-to-show', () => {
    mainWindow.show();
    setTimeout(checkForUpdates, 2000);
  });

  mainWindow.webContents.setWindowOpenHandler(({ url }) => {
    shell.openExternal(url);
    return { action: 'deny' };
  });
}

// ── API-Key: safeStorage (verschlüsselt auf Disk) ─────────────────────────────
ipcMain.handle('load-api-key', () => {
  try {
    if (!fs.existsSync(KEY_FILE)) return null;
    if (!safeStorage.isEncryptionAvailable()) {
      // Fallback: Plaintext lesen wenn safeStorage nicht verfügbar
      return fs.readFileSync(KEY_FILE, 'utf8').trim() || null;
    }
    const buf = fs.readFileSync(KEY_FILE);
    return safeStorage.decryptString(buf);
  } catch (e) {
    console.error('[Key] Laden fehlgeschlagen:', e.message);
    return null;
  }
});

ipcMain.handle('save-api-key', (_, key) => {
  try {
    if (!key) { if (fs.existsSync(KEY_FILE)) fs.unlinkSync(KEY_FILE); return true; }
    if (!safeStorage.isEncryptionAvailable()) {
      fs.writeFileSync(KEY_FILE, key, 'utf8');
      return true;
    }
    const enc = safeStorage.encryptString(key);
    fs.writeFileSync(KEY_FILE, enc);
    return true;
  } catch (e) {
    console.error('[Key] Speichern fehlgeschlagen:', e.message);
    return false;
  }
});

ipcMain.handle('delete-api-key', () => {
  try { if (fs.existsSync(KEY_FILE)) fs.unlinkSync(KEY_FILE); return true; }
  catch (e) { return false; }
});

// ── Projects: JSON-Datei (Inbox + Versionen + Fusion-History) ────────────────
ipcMain.handle('load-projects', () => {
  try {
    if (!fs.existsSync(PROJECTS_FILE)) return null;
    return JSON.parse(fs.readFileSync(PROJECTS_FILE, 'utf8'));
  } catch (e) {
    console.error('[Projects] Laden fehlgeschlagen:', e.message);
    return null;
  }
});

ipcMain.handle('save-projects', (_, data) => {
  try {
    fs.writeFileSync(PROJECTS_FILE, JSON.stringify(data, null, 2), 'utf8');
    return true;
  } catch (e) {
    console.error('[Projects] Speichern fehlgeschlagen:', e.message);
    return false;
  }
});

// ── Auto-Updater ──────────────────────────────────────────────────────────────
function checkForUpdates() {
  if (!app.isPackaged) { console.log('[Updater] Dev-Modus — kein Auto-Update'); return; }
  autoUpdater.checkForUpdates();
}

autoUpdater.on('update-available', (info) => {
  mainWindow.webContents.send('update-available', {
    version: info.version,
    releaseNotes: info.releaseNotes || 'Neue Verbesserungen und Bug-Fixes.',
  });
});
autoUpdater.on('update-not-available', () => {});
autoUpdater.on('download-progress', (progress) => {
  mainWindow.webContents.send('update-progress', {
    percent: Math.round(progress.percent),
    transferred: formatBytes(progress.transferred),
    total: formatBytes(progress.total),
    speed: formatBytes(progress.bytesPerSecond) + '/s',
  });
});
autoUpdater.on('update-downloaded', (info) => {
  mainWindow.webContents.send('update-ready', { version: info.version });
});
autoUpdater.on('error', (err) => {
  console.error('[Updater] Fehler:', err.message);
  mainWindow.webContents.send('update-error', { message: err.message });
});

// ── IPC Handler ───────────────────────────────────────────────────────────────
ipcMain.on('install-update',     () => autoUpdater.quitAndInstall(false, true));
ipcMain.on('postpone-update',    () => {});
ipcMain.on('check-for-updates',  () => {
  if (app.isPackaged) autoUpdater.checkForUpdates();
  else mainWindow.webContents.send('update-not-available-manual');
});
ipcMain.handle('get-version', () => APP_VERSION);

// ── App-Lifecycle ─────────────────────────────────────────────────────────────
app.whenReady().then(() => {
  createWindow();
  app.on('activate', () => {
    if (BrowserWindow.getAllWindows().length === 0) createWindow();
  });
});
app.on('window-all-closed', () => { if (process.platform !== 'darwin') app.quit(); });

// ── Hilfsfunktionen ───────────────────────────────────────────────────────────
function formatBytes(bytes) {
  if (bytes < 1024) return bytes + ' B';
  if (bytes < 1024 * 1024) return (bytes / 1024).toFixed(1) + ' KB';
  return (bytes / (1024 * 1024)).toFixed(1) + ' MB';
}
