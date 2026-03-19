"""
Hirsch Music Hit Maker — KI Song Writer Backend
Ruft Claude auf um echte, individuelle Song-Texte zu generieren
"""
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from anthropic import Anthropic
import json, re

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

client = Anthropic()

def build_prompt(s1: dict, s2: dict, match_info: dict) -> str:
    """Baut den Prompt so wie ich (Claude) es selbst tun würde."""
    
    g1, g2 = s1.get('genre',''), s2.get('genre','')
    y1, y2 = s1.get('year',''), s2.get('year','')
    a1, a2 = s1.get('artist',''), s2.get('artist','')
    t1, t2 = s1.get('title',''), s2.get('title','')
    score  = match_info.get('score', 0.5)
    themes = match_info.get('sharedThemes', [])
    mood1  = match_info.get('mood1','')
    mood2  = match_info.get('mood2','')

    return f"""You are a world-class songwriter. Your task: write a NEW song that genuinely fuses two existing songs — not just name-drops them, but truly synthesizes their themes, emotional DNA, imagery, and storytelling style into something that could only exist as the intersection of both.

## The Two Songs

**Song 1:** "{t1}" by {a1} ({y1}, {g1})
**Song 2:** "{t2}" by {a2} ({y2}, {g2})

## What you know about these songs
- Compatibility score: {round(score*100)}%
- Shared themes: {', '.join(themes) if themes else 'to be discovered'}
- Mood of Song 1: {mood1}
- Mood of Song 2: {mood2}

## Your approach
1. Think deeply about what "{t1}" is actually about — its real story, core emotion, signature imagery, what makes it unique
2. Think deeply about what "{t2}" is actually about — same process
3. Find the genuine emotional bridge: what do both songs share at their core, even if they sound different?
4. Write a new song that a listener familiar with BOTH originals would immediately recognize as a true fusion — not just references, but the actual thematic and emotional DNA blended

## Output Format
Write the song in BOTH American English AND German (side by side sections).
Structure: Intro, Verse 1, Pre-Chorus, Chorus, Verse 2, Bridge, Outro

Return ONLY valid JSON, no markdown, no explanation:
{{
  "title": "fusion song title",
  "theme": "one sentence about the core theme",
  "en": {{
    "intro": "...",
    "verse1": "...",
    "preChorus": "...",
    "chorus": "...",
    "verse2": "...",
    "bridge": "...",
    "outro": "..."
  }},
  "de": {{
    "intro": "...",
    "verse1": "...",
    "preChorus": "...",
    "chorus": "...",
    "verse2": "...",
    "bridge": "...",
    "outro": "..."
  }}
}}

Rules:
- Each section: 4-8 lines
- NO generic filler ("in a world of...", "where dreams collide...")
- Specific imagery from the actual songs — things a fan would recognize
- The German version should be a natural creative translation, not word-for-word
- The chorus should be singable and memorable
- Make it feel like a REAL song, not an exercise"""


@app.post("/api/generate-lyrics")
async def generate_lyrics(request: Request):
    try:
        body = await request.json()
        s1         = body.get('s1', {})
        s2         = body.get('s2', {})
        match_info = body.get('matchInfo', {})
        regen_seed = body.get('regenSeed', 0)

        prompt = build_prompt(s1, s2, match_info)
        
        # Bei Regen: leicht anderer System-Prompt für Variation
        system = "You are a masterful songwriter who writes with emotional precision and genuine insight into the songs you're fusing. Every lyric must feel earned and specific."
        if regen_seed > 0:
            system += f" Write a distinctly different version than before — try a different angle, different imagery, different structure. Variation seed: {regen_seed}."

        message = client.messages.create(
            model="claude_sonnet_4_6",
            max_tokens=3000,
            system=system,
            messages=[{"role": "user", "content": prompt}]
        )

        raw = message.content[0].text.strip()
        
        # JSON extrahieren (manchmal wrapped in ```json)
        json_match = re.search(r'\{[\s\S]+\}', raw)
        if not json_match:
            return JSONResponse({"error": "No JSON in response", "raw": raw[:500]}, status_code=500)
        
        data = json.loads(json_match.group())
        return JSONResponse(data)

    except json.JSONDecodeError as e:
        return JSONResponse({"error": f"JSON parse error: {str(e)}"}, status_code=500)
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)


@app.get("/health")
async def health():
    return {"status": "ok"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)
