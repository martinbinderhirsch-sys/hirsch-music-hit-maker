/**
 * Preload-Script: Sicherer Bridge zwischen Electron-Main und Renderer
 */
const { contextBridge, ipcRenderer } = require('electron');

contextBridge.exposeInMainWorld('electronAPI', {
  // Version
  getVersion: () => ipcRenderer.invoke('get-version'),

  // API-Key (verschlüsselt auf Disk via safeStorage)
  loadApiKey:   () => ipcRenderer.invoke('load-api-key'),
  saveApiKey:   (key) => ipcRenderer.invoke('save-api-key', key),
  deleteApiKey: () => ipcRenderer.invoke('delete-api-key'),

  // Projects (Inbox + Versionen + History, JSON-Datei)
  loadProjects: () => ipcRenderer.invoke('load-projects'),
  saveProjects: (data) => ipcRenderer.invoke('save-projects', data),

  // Updates
  checkForUpdates: () => ipcRenderer.send('check-for-updates'),
  installUpdate:   () => ipcRenderer.send('install-update'),
  postponeUpdate:  () => ipcRenderer.send('postpone-update'),

  // Events empfangen
  onUpdateAvailable: (cb) => ipcRenderer.on('update-available',            (_, d) => cb(d)),
  onUpdateProgress:  (cb) => ipcRenderer.on('update-progress',             (_, d) => cb(d)),
  onUpdateReady:     (cb) => ipcRenderer.on('update-ready',                (_, d) => cb(d)),
  onUpdateError:     (cb) => ipcRenderer.on('update-error',                (_, d) => cb(d)),
  onUpdateNotAvail:  (cb) => ipcRenderer.on('update-not-available-manual', (_, d) => cb(d)),

  removeAllListeners: (ch) => ipcRenderer.removeAllListeners(ch),
});
