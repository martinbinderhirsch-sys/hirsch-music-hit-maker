"""
Hirsch Music Hit Maker — KI Song Writer Backend v2.0
Nutzt song_knowledge.py (156 Songs) + genre_style_library.py (18 Genres)
für echte, stilgenaue Fusion-Lyrics.
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from anthropic import Anthropic
import json, re

# ─── Bibliotheken laden ───────────────────────────────────────────────────────
try:
    from song_knowledge import SONG_KNOWLEDGE, get_song
    SONG_KB_LOADED = True
except ImportError:
    SONG_KNOWLEDGE = {}
    SONG_KB_LOADED = False

try:
    from genre_style_library import (
        GENRE_STYLE_LIBRARY,
        get_genre_style,
        get_fusion_compatibility,
        get_suno_tags,
    )
    GENRE_LIB_LOADED = True
except ImportError:
    GENRE_STYLE_LIBRARY = {}
    GENRE_LIB_LOADED = False

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

client = Anthropic()


# ─── Song-Wissen nachschlagen ─────────────────────────────────────────────────
def lookup_song(title: str, artist: str = "") -> dict:
    """Sucht Song in der Wissensdatenbank — flexibel nach Titel."""
    if not title:
        return {}
    title_lower = title.lower().strip()

    # 1. Exakter Treffer
    if title in SONG_KNOWLEDGE:
        return SONG_KNOWLEDGE[title]

    # 2. Teilstring-Treffer (Titel enthält DB-Key oder umgekehrt)
    for key, data in SONG_KNOWLEDGE.items():
        key_lower = key.lower()
        if key_lower in title_lower or title_lower in key_lower:
            return data
        # Erste 15 Zeichen vergleichen
        if key_lower[:15] == title_lower[:15]:
            return data

    # 3. Artist-basierte Suche wenn kein Titel-Treffer
    if artist:
        artist_lower = artist.lower()
        for key, data in SONG_KNOWLEDGE.items():
            if artist_lower in data.get("story", "").lower():
                if key_lower[:8] in title_lower or title_lower[:8] in key_lower:
                    return data

    return {}


# ─── Genre-Stil nachschlagen ──────────────────────────────────────────────────
def lookup_genre(genre: str) -> dict:
    """Gibt Genre-Stil-Daten zurück."""
    if not genre:
        return {}
    # Direkt
    if genre in GENRE_STYLE_LIBRARY:
        return GENRE_STYLE_LIBRARY[genre]
    # Case-insensitive
    for key in GENRE_STYLE_LIBRARY:
        if key.lower() == genre.lower():
            return GENRE_STYLE_LIBRARY[key]
    # Teilstring
    for key in GENRE_STYLE_LIBRARY:
        if key.lower() in genre.lower() or genre.lower() in key.lower():
            return GENRE_STYLE_LIBRARY[key]
    return {}


# ─── Song-Wissen-Block für Prompt ────────────────────────────────────────────
def format_song_knowledge(title: str, artist: str, year, genre: str, idx: int) -> str:
    k = lookup_song(title, artist)
    label = f"Song {idx}"

    if k:
        sig = k.get("signature", [])
        sig_str = " / ".join(f'"{s}"' for s in sig[:3]) if sig else ""
        return f"""## {label}: "{title}" by {artist} ({year}, {genre})
CORE EMOTION: {k.get('core_emotion', '')}
KEY IMAGERY: {k.get('key_imagery', '')}
LYRIC FEEL: {k.get('lyric_feel', '')}
STORY: {k.get('story', '')}
SIGNATURE PHRASES (evoke, don't copy): {sig_str}"""
    else:
        return f"""## {label}: "{title}" by {artist} ({year}, {genre})
(Use your knowledge of this song — its real emotional content, imagery, and story.)"""


# ─── Genre-Block für Prompt ───────────────────────────────────────────────────
def format_genre_fusion(g1: str, g2: str) -> str:
    gs1 = lookup_genre(g1)
    gs2 = lookup_genre(g2)

    lines = []

    # Fusion-Kompatibilität
    if GENRE_LIB_LOADED and gs1 and gs2:
        try:
            compat = get_fusion_compatibility(g1, g2)
            compat_label = {"high": "✓ High compatibility", "tension": "⚡ Creative tension", "neutral": "Neutral blend"}.get(compat.get("compatibility","neutral"), "Neutral blend")
            lines.append(f"FUSION COMPATIBILITY: {compat_label}")
            bridges = compat.get("bridge_elements", [])[:5]
            if bridges:
                lines.append(f"BRIDGE ELEMENTS: {', '.join(bridges)}")
            shared = compat.get("shared_vibes", [])[:4]
            if shared:
                lines.append(f"SHARED VIBES: {', '.join(shared)}")
        except Exception:
            pass

    # Genre 1 Stil
    if gs1:
        vibes1 = gs1.get("vibes", [])[:5]
        themes1 = gs1.get("lyric_themes", [])[:4]
        lines.append(f"\n{g1} STYLE: vibes={', '.join(vibes1)} | themes={', '.join(themes1)}")
        lines.append(f"{g1} LYRIC STYLE: {gs1.get('lyric_style','')[:200]}")

    # Genre 2 Stil
    if gs2:
        vibes2 = gs2.get("vibes", [])[:5]
        themes2 = gs2.get("lyric_themes", [])[:4]
        lines.append(f"\n{g2} STYLE: vibes={', '.join(vibes2)} | themes={', '.join(themes2)}")
        lines.append(f"{g2} LYRIC STYLE: {gs2.get('lyric_style','')[:200]}")

    return "\n".join(lines) if lines else ""


# ─── Suno/Udio Prompt bauen ───────────────────────────────────────────────────
def build_suno_prompt(s1: dict, s2: dict, match_info: dict, concept: dict = None) -> str:
    """Baut einen optimierten Suno/Udio Prompt aus Genre-Tags."""
    g1, g2 = s1.get("genre",""), s2.get("genre","")
    gs1, gs2 = lookup_genre(g1), lookup_genre(g2)

    tags1 = gs1.get("suno_tags", [])[:6]
    tags2 = gs2.get("suno_tags", [])[:4]
    all_tags = list(dict.fromkeys(tags1 + tags2))  # dedupliziert, Reihenfolge erhalten

    bpm = match_info.get("bpm", "")
    key = match_info.get("key", "")
    mood = match_info.get("mood1", "")
    themes = ", ".join(match_info.get("sharedThemes", [])[:3])
    title = concept.get("fusionTitle", "") if concept else ""

    parts = []
    if title:
        parts.append(f'"{title}"')
    parts.append(f"{g1}-{g2} fusion")
    if all_tags:
        parts.append(", ".join(all_tags[:10]))
    if bpm:
        parts.append(f"{bpm} BPM")
    if key:
        parts.append(f"key of {key}")
    if mood:
        parts.append(mood)
    if themes:
        parts.append(f"themes: {themes}")

    return ", ".join(parts)


# ─── Haupt-Prompt bauen ───────────────────────────────────────────────────────
def build_prompt(s1: dict, s2: dict, match_info: dict, style: dict = None) -> str:
    g1, g2     = s1.get("genre",""), s2.get("genre","")
    y1, y2     = s1.get("year",""),  s2.get("year","")
    a1, a2     = s1.get("artist",""), s2.get("artist","")
    t1, t2     = s1.get("title",""),  s2.get("title","")
    score      = match_info.get("score", 0.5)
    themes     = match_info.get("sharedThemes", [])
    mood1      = match_info.get("mood1","")
    mood2      = match_info.get("mood2","")

    # Song-Wissen
    song1_block = format_song_knowledge(t1, a1, y1, g1, 1)
    song2_block = format_song_knowledge(t2, a2, y2, g2, 2)

    # Genre-Fusion-Stil
    genre_block = format_genre_fusion(g1, g2)

    # Style-Slider (0-100)
    poetisch = (style or {}).get("poetisch", 50)
    komplex  = (style or {}).get("komplex",  50)
    modern   = (style or {}).get("modern",   50)

    style_hints = []
    if poetisch < 30:
        style_hints.append("Rich metaphorical imagery — feelings expressed through concrete pictures.")
    elif poetisch > 70:
        style_hints.append("Direct and conversational — say exactly what you mean, no forced poetry.")

    if komplex < 30:
        style_hints.append("Layered, sophisticated language with multiple meanings per line.")
    elif komplex > 70:
        style_hints.append("Simple and catchy — words a crowd can sing back instantly.")

    if modern < 30:
        style_hints.append("Timeless classic style — phrasing that could belong to any era.")
    elif modern > 70:
        style_hints.append("Contemporary feel — fresh, current emotional language.")

    style_block = ("\n## Style Direction\n" + " ".join(style_hints) + "\n") if style_hints else ""

    return f"""You are a professional songwriter with deep knowledge of music history and songcraft.
Write a FUSION SONG that blends two real songs into something entirely new.

══════════════════════════════════════════════════
ABSOLUTE RULES — violating any of these ruins the song:
1. NEVER mention song titles or artist names inside the lyrics
2. NEVER use placeholder phrases like "the feeling of X" or "the spirit of Y" — write the actual emotion
3. NEVER write meta-commentary ("a song about...", "[Artist] knew something about...")
4. Every line must be CONCRETE — specific images, things you can see, touch, feel
5. No filler lines — if a line doesn't earn its place, cut it
6. The result must sound like a REAL song someone would perform on a stage
══════════════════════════════════════════════════

{song1_block}

{song2_block}

## Fusion Context
- Compatibility: {round(score*100)}%
- Shared emotional territory: {', '.join(themes) if themes else 'discover it yourself'}
- Mood 1: {mood1 or 'intense'}
- Mood 2: {mood2 or 'celebratory'}

## Genre Style Guide
{genre_block}
{style_block}
## What to Write

Find the TRUE bridge between these two songs — what do they share at their emotional core beneath all surface differences? Write from THAT place.

Deliver a complete fusion song:
- Intro (2-4 lines — set the scene/mood)
- Verse 1 (4-6 lines — establish the story, specific imagery)
- Pre-Chorus (2-4 lines — emotional build, tension rising)
- Chorus (4-6 lines — emotional peak, singable, the hook)
- Verse 2 (4-6 lines — deepen the story, new angle)
- Bridge (3-5 lines — the turn, something shifts)
- Outro (2-4 lines — resolution or open fade)

In BOTH English AND German (German = creative adaptation, not translation).

Return ONLY valid JSON, no markdown wrapper:
{{
  "title": "evocative fusion title — not generic",
  "theme": "one sentence: what this fusion is actually about",
  "en": {{
    "intro": "...", "verse1": "...", "preChorus": "...",
    "chorus": "...", "verse2": "...", "bridge": "...", "outro": "..."
  }},
  "de": {{
    "intro": "...", "verse1": "...", "preChorus": "...",
    "chorus": "...", "verse2": "...", "bridge": "...", "outro": "..."
  }}
}}"""


# ─── API Endpoint ─────────────────────────────────────────────────────────────
@app.post("/api/generate-lyrics")
async def generate_lyrics(request: Request):
    try:
        body       = await request.json()
        s1         = body.get("s1", {})
        s2         = body.get("s2", {})
        match_info = body.get("matchInfo", {})
        regen_seed = body.get("regenSeed", 0)
        style      = body.get("style", {})

        prompt = build_prompt(s1, s2, match_info, style=style)

        system = (
            "You are a professional songwriter with genuine knowledge of music history "
            "and what makes lyrics emotionally resonant. "
            "You write REAL songs — specific, concrete, performable. "
            "You never use a song's title as a lyric. "
            "You never explain what a song is about — you SHOW it through imagery. "
            "Every line you write could be sung on a stage."
        )
        if regen_seed > 0:
            system += (
                f" This is attempt #{regen_seed + 1}. Write a completely different take — "
                "new imagery, new emotional angle, new structural approach. Surprise yourself."
            )

        message = client.messages.create(
            model="claude-sonnet-4-5",
            max_tokens=4000,
            system=system,
            messages=[{"role": "user", "content": prompt}],
        )

        raw = message.content[0].text.strip()
        json_match = re.search(r"\{[\s\S]+\}", raw)
        if not json_match:
            return JSONResponse({"error": "No JSON in response", "raw": raw[:500]}, status_code=500)

        data = json.loads(json_match.group())
        return JSONResponse(data)

    except json.JSONDecodeError as e:
        return JSONResponse({"error": f"JSON parse error: {str(e)}"}, status_code=500)
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)


# ─── Suno Prompt Endpoint ─────────────────────────────────────────────────────
@app.post("/api/suno-prompt")
async def suno_prompt(request: Request):
    """Generiert optimierten Suno/Udio Prompt aus Genre-Tags."""
    try:
        body    = await request.json()
        s1      = body.get("s1", {})
        s2      = body.get("s2", {})
        match_info = body.get("matchInfo", {})
        concept = body.get("concept", {})
        prompt  = build_suno_prompt(s1, s2, match_info, concept)
        return JSONResponse({"prompt": prompt})
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)


# ─── Genre Info Endpoint ──────────────────────────────────────────────────────
@app.get("/api/genre/{genre}")
async def genre_info(genre: str):
    """Gibt alle Stil-Daten eines Genres zurück."""
    data = lookup_genre(genre)
    if not data:
        return JSONResponse({"error": f"Genre '{genre}' not found"}, status_code=404)
    return JSONResponse(data)


# ─── Fusion Compatibility Endpoint ───────────────────────────────────────────
@app.get("/api/fusion-compat/{g1}/{g2}")
async def fusion_compat(g1: str, g2: str):
    """Gibt Kompatibilität + Bridge-Elemente zweier Genres zurück."""
    if not GENRE_LIB_LOADED:
        return JSONResponse({"error": "Genre library not loaded"}, status_code=500)
    try:
        result = get_fusion_compatibility(g1, g2)
        return JSONResponse(result)
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)


# ─── Health ───────────────────────────────────────────────────────────────────
@app.get("/health")
async def health():
    return {
        "status": "ok",
        "song_kb": f"{len(SONG_KNOWLEDGE)} songs" if SONG_KB_LOADED else "not loaded",
        "genre_lib": f"{len(GENRE_STYLE_LIBRARY)} genres" if GENRE_LIB_LOADED else "not loaded",
    }


if __name__ == "__main__":
    import uvicorn
    print(f"Song KB: {len(SONG_KNOWLEDGE)} songs" if SONG_KB_LOADED else "Song KB: not loaded")
    print(f"Genre Lib: {len(GENRE_STYLE_LIBRARY)} genres" if GENRE_LIB_LOADED else "Genre Lib: not loaded")
    uvicorn.run(app, host="0.0.0.0", port=5000)
