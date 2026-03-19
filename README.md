# Hirsch Music Hit Maker

**Web-App** — 4.000 Songs · 7 Genres + Klassiker bis 1960

## Dateien
| Datei | Beschreibung |
|---|---|
| `index.html` | Haupt-App (alle Views + JS) |
| `matcher-engine.js` | KI Song-Writer Engine v3 |
| `data-rock.js` | 500 Rock Songs (IDs 1–500) |
| `data-pop.js` | 500 Pop Songs (IDs 501–1000) |
| `data-hiphop.js` | 500 Hip-Hop Songs (IDs 1001–1500) |
| `data-metal.js` | 500 Metal Songs (IDs 1501–2000) |
| `data-country.js` | 500 Country Songs (IDs 2001–2500) |
| `data-edm.js` | 500 EDM Songs (IDs 2501–3000) |
| `data-schlager.js` | 500 Schlager Songs (IDs 3001–3500) |
| `data-classics.js` | 500 Klassiker bis 1960 (IDs 3501–4000) |
| `manifest.json` | PWA Manifest |
| `sw.js` | Service Worker (PWA) |

## Features
- Charts-Ansicht mit 4.000 Songs, sortierbar nach Genre/Artist/Jahr
- Doppelklick auf Song → direkt zu Song Fusion hinzufügen
- Song Fusion Matcher — KI-basiertes Matching + 60% Kompatibilitäts-Score
- Intelligenter Song Writer v3 — generiert neuen Text auf Basis echter Song-Inhalte
- Musik Generator — Prompt für Suno/Udio/Beatoven
- PWA-fähig (Desktop-App installierbar)
- Dark/Light Mode

## Deployed URL
https://www.perplexity.ai/computer/a/hirsch-music-hit-maker-F7MItWnkQMSgsd38D5jWkA

## Neue Songs hinzufügen
- Rock/Pop/etc.: Neue IDs ab 4001 in `data-classics.js` oder neue Datei `data-[genre].js`
- In `index.html` die neue Datei als `<script src="data-xxx.js"></script>` einbinden
- `ALL_SONGS` Array um `...SONGS_XXX` erweitern
