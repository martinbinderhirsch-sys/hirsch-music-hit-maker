/**
 * Preload-Script: Sicherer Bridge zwischen Electron-Main und Renderer
 * Stellt der App nur erlaubte Funktionen zur Verfügung
 */
const { contextBridge, ipcRenderer } = require('electron');

contextBridge.exposeInMainWorld('electronAPI', {
  // Version abfragen
  getVersion: () => ipcRenderer.invoke('get-version'),

  // Updates
  checkForUpdates: () => ipcRenderer.send('check-for-updates'),
  installUpdate:   () => ipcRenderer.send('install-update'),
  postponeUpdate:  () => ipcRenderer.send('postpone-update'),

  // Events empfangen
  onUpdateAvailable: (cb) => ipcRenderer.on('update-available',       (_, data) => cb(data)),
  onUpdateProgress:  (cb) => ipcRenderer.on('update-progress',        (_, data) => cb(data)),
  onUpdateReady:     (cb) => ipcRenderer.on('update-ready',           (_, data) => cb(data)),
  onUpdateError:     (cb) => ipcRenderer.on('update-error',           (_, data) => cb(data)),
  onUpdateNotAvail:  (cb) => ipcRenderer.on('update-not-available-manual', (_, data) => cb(data)),

  // Cleanup
  removeAllListeners: (channel) => ipcRenderer.removeAllListeners(channel),
});
