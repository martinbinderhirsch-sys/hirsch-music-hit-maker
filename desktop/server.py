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

# ─── SONG KNOWLEDGE BASE ─────────────────────────────────────────────────────
# Detailwissen über bekannte Songs für bessere Lyrics
SONG_KNOWLEDGE = {
    "Still of the Night": {
        "artist": "Whitesnake",
        "core_emotion": "Dark, smoldering sexual tension — the dangerous pull of desire at night",
        "key_imagery": "Shadows, midnight, heat, chains, fire, a woman who controls everything",
        "sonic_dna": "Heavy riff-driven rock, powerful vocals, Led Zeppelin influence, raw intensity",
        "lyric_feel": "Tense, dangerous, masculine vulnerability hidden behind bravado",
        "story": "A man consumed by a woman, awake in the night, unable to escape her hold over him",
        "signature_phrases": ["in the still of the night", "feel my heart beating", "I hear the wind calling", "shadows of the night"]
    },
    "All Night Long (All Night)": {
        "artist": "Lionel Richie",
        "core_emotion": "Pure uninhibited joy — communal celebration, everyone together as one",
        "key_imagery": "Dancing, Caribbean rhythm, crowds, night sky, music uniting people",
        "sonic_dna": "Funk-pop, Caribbean percussion, infectious groove, warm production",
        "lyric_feel": "Open, euphoric, generous, communal — an invitation to everyone",
        "story": "A man calling the world to dance together, forget troubles, celebrate being alive",
        "signature_phrases": ["all night long", "fiesta, forever", "tom bo li de say de moi ya", "once you get started"]
    },
    "Bohemian Rhapsody": {
        "artist": "Queen",
        "core_emotion": "Existential crisis — a young man confessing a terrible act, confronting fate",
        "key_imagery": "Mama, Scaramouche, Fandango, Galileo, Beelzebub, thunder and lightning",
        "sonic_dna": "Opera meets rock meets ballad, multi-layered vocals, piano, full orchestra moments",
        "lyric_feel": "Theatrical, desperate, darkly humorous, operatic tragedy",
        "story": "A man who has killed someone, saying goodbye to his mother, facing judgment",
        "signature_phrases": ["is this the real life", "caught in a landslide", "mama mia", "nothing really matters"]
    },
    "Hotel California": {
        "artist": "Eagles",
        "core_emotion": "Seductive entrapment — the American dream as a beautiful prison you can never leave",
        "key_imagery": "Desert highway, warm smell of colitas, mirrors on the ceiling, pink champagne, 1969",
        "sonic_dna": "Dual guitar harmonies, laid-back groove, West Coast rock, iconic extended solo",
        "lyric_feel": "Hypnotic, ominous, beautiful decay, noir atmosphere",
        "story": "A traveler checks into a mysterious hotel — paradise turns to prison",
        "signature_phrases": ["you can check out any time you like", "we are all just prisoners here", "such a lovely place", "on a dark desert highway"]
    },
    "Stairway to Heaven": {
        "artist": "Led Zeppelin",
        "core_emotion": "Spiritual yearning — the search for meaning, the illusion of shortcuts to truth",
        "key_imagery": "Bustle in hedgerow, May queen, pipers, rings of smoke, piper's tune",
        "sonic_dna": "Acoustic to electric journey, building intensity, mystical folk roots, rock crescendo",
        "lyric_feel": "Mystical, cryptic, prophetic, Celtic imagery",
        "story": "A woman who thinks she can buy her way to heaven — but the path must be walked",
        "signature_phrases": ["there's still time to change the road you're on", "and she's buying a stairway to heaven", "makes me wonder"]
    },
    "Smells Like Teen Spirit": {
        "artist": "Nirvana",
        "core_emotion": "Generational alienation — the absurdity of entertainment and conformity, self-destruction as protest",
        "key_imagery": "Mulatto, albino, mosquito, libido, cheerleaders, guns, pet, entertainment",
        "sonic_dna": "Quiet-loud dynamics, feedback, distortion, raw punk energy, melodic hooks",
        "lyric_feel": "Ironic, exhausted, screaming frustration beneath apathy",
        "story": "A disaffected youth watching the entertainment of rebellion consume itself",
        "signature_phrases": ["here we are now, entertain us", "I feel stupid and contagious", "a mulatto, an albino", "load up on guns"]
    },
    "Johnny B. Goode": {
        "artist": "Chuck Berry",
        "core_emotion": "Pure American optimism — the self-made dreamer, music as escape from poverty",
        "key_imagery": "Louisiana log cabin, railroad tracks, guitar playing in the woods, people stopping to listen",
        "sonic_dna": "Blues-rooted rock and roll, double-string guitar runs, driving beat, call-and-response",
        "lyric_feel": "Celebratory, rhythmic, storytelling, archetypal American mythology",
        "story": "A country boy from poverty plays guitar so well that fame and success find him",
        "signature_phrases": ["go Johnny go", "deep down in Louisiana", "never ever learned to read or write", "carry his guitar in a gunny sack"]
    },
    "Respect": {
        "artist": "Aretha Franklin",
        "core_emotion": "Fierce demand for dignity — a woman claiming her power, setting terms on her own",
        "key_imagery": "Coming home, money, honey, doing her man right, TCP, sock it to me",
        "sonic_dna": "Deep soul horns, gospel roots, call-and-response choir, unstoppable groove",
        "lyric_feel": "Commanding, confident, joyful in its demand, sexually charged self-assertion",
        "story": "A woman telling her man: I give you everything, but I demand respect when you walk in this door",
        "signature_phrases": ["R-E-S-P-E-C-T", "sock it to me", "all I'm asking", "when you come home"]
    },
    "No Woman No Cry": {
        "artist": "Bob Marley",
        "core_emotion": "Tender consolation — comforting loved ones through hardship with memories of community",
        "key_imagery": "Government yard in Trenchtown, cooking cornmeal porridge, fire lights, log wood burning",
        "sonic_dna": "Reggae one-drop rhythm, warm bass, gentle guitar, communal warmth",
        "lyric_feel": "Intimate, nostalgic, spiritually reassuring, deeply personal memory",
        "story": "Marley comforting a woman in Trenchtown, remembering better times, promising it will be alright",
        "signature_phrases": ["no woman no cry", "everything's gonna be alright", "I remember when we used to sit", "in the government yard in Trenchtown"]
    },
    "Purple Rain": {
        "artist": "Prince",
        "core_emotion": "Transcendent heartbreak — love lost elevated to spiritual, almost religious longing",
        "key_imagery": "Purple rain, honey, guide, never meant to cause sorrow, electric word life",
        "sonic_dna": "Gospel-influenced rock ballad, wailing guitar solo, orchestral swells, building catharsis",
        "lyric_feel": "Vulnerable, devotional, aching beauty, spiritual surrender",
        "story": "A man apologizing to a lost love, offering everything in a final act of surrender",
        "signature_phrases": ["I never meant to cause you any sorrow", "honey I know times are changing", "I only wanted to see you laughing in the purple rain"]
    }
}

def get_song_knowledge(title: str, artist: str) -> dict:
    """Sucht bekannte Song-Details — flexible Titelsuche."""
    for key, data in SONG_KNOWLEDGE.items():
        if key.lower() in title.lower() or title.lower() in key.lower():
            return data
    return {}

def build_prompt(s1: dict, s2: dict, match_info: dict, style: dict = None) -> str:
    """Baut einen starken Songwriter-Prompt mit echtem Song-Wissen."""
    
    g1, g2 = s1.get('genre',''), s2.get('genre','')
    y1, y2 = s1.get('year',''), s2.get('year','')
    a1, a2 = s1.get('artist',''), s2.get('artist','')
    t1, t2 = s1.get('title',''), s2.get('title','')
    score  = match_info.get('score', 0.5)
    themes = match_info.get('sharedThemes', [])
    mood1  = match_info.get('mood1','')
    mood2  = match_info.get('mood2','')
    
    # Song-Wissen nachschlagen
    k1 = get_song_knowledge(t1, a1)
    k2 = get_song_knowledge(t2, a2)
    
    # Detailwissen für den Prompt aufbereiten
    k1_block = ""
    if k1:
        k1_block = f"""
WHAT THIS SONG IS ACTUALLY ABOUT:
- Core emotion: {k1.get('core_emotion','')}
- Key imagery: {k1.get('key_imagery','')}
- How it sounds/feels: {k1.get('sonic_dna','')}
- Lyrical style: {k1.get('lyric_feel','')}
- The story: {k1.get('story','')}
- Signature phrases to echo (don't copy, just evoke): {', '.join(k1.get('signature_phrases',[]))}"""
    else:
        k1_block = f"\n(No detailed knowledge — use what you know about {t1} by {a1} from {y1})"

    k2_block = ""
    if k2:
        k2_block = f"""
WHAT THIS SONG IS ACTUALLY ABOUT:
- Core emotion: {k2.get('core_emotion','')}
- Key imagery: {k2.get('key_imagery','')}
- How it sounds/feels: {k2.get('sonic_dna','')}
- Lyrical style: {k2.get('lyric_feel','')}
- The story: {k2.get('story','')}
- Signature phrases to echo (don't copy, just evoke): {', '.join(k2.get('signature_phrases',[]))}"""
    else:
        k2_block = f"\n(No detailed knowledge — use what you know about {t2} by {a2} from {y2})"

    # Style sliders (0-100)
    poetisch = (style or {}).get('poetisch', 50)  # 0=poetisch, 100=direkt
    komplex  = (style or {}).get('komplex', 50)   # 0=komplex, 100=einfach
    modern   = (style or {}).get('modern', 50)    # 0=oldschool, 100=modern
    
    style_hints = []
    if poetisch < 30:
        style_hints.append("Use rich metaphorical imagery — let feelings speak through pictures, not explanations.")
    elif poetisch > 70:
        style_hints.append("Be direct and conversational — say what you mean, no forced poetry.")
    if komplex < 30:
        style_hints.append("Use layered, sophisticated language with multiple meanings per line.")
    elif komplex > 70:
        style_hints.append("Keep language simple and catchy — words a crowd can sing back instantly.")
    if modern < 30:
        style_hints.append("Write in a timeless classic style — phrasing that could have been written in any decade.")
    elif modern > 70:
        style_hints.append("Write with a contemporary feel — fresh phrasing, current emotional language.")
    style_block = ('\n## Style Direction\n' + ' '.join(style_hints) + '\n') if style_hints else ''

    return f"""You are a professional songwriter with deep knowledge of music history. You are writing a FUSION SONG that blends two real songs into something entirely new.

CRITICAL RULES — read these first:
1. NEVER mention the song titles by name in the lyrics
2. NEVER use placeholder phrases like "the euphoria of X" or "the feeling of Y" — write the actual emotion
3. NEVER write meta-commentary about the songs ("a song about...", "Whitesnake knew...")
4. Write REAL lyrics — concrete images, specific details, things you can see and feel
5. Each line must earn its place — no filler, no padding
6. The result should sound like a REAL song someone would actually perform

## Song 1: "{t1}" by {a1} ({y1}, {g1}){k1_block}

## Song 2: "{t2}" by {a2} ({y2}, {g2}){k2_block}

## Fusion Brief
- Compatibility: {round(score*100)}%
- Shared emotional territory: {', '.join(themes) if themes else 'discover it yourself'}
- Mood of Song 1: {mood1 or 'intense/dark'}
- Mood of Song 2: {mood2 or 'joyful/celebratory'}

Find the TRUE bridge between these two songs. What do they actually share beneath their surface differences? Write from THAT place.
{style_block}
## What to deliver

A complete fusion song with these sections: Intro, Verse 1, Pre-Chorus, Chorus, Verse 2, Bridge, Outro.
Write it in BOTH English AND German. The German version must be a genuine creative adaptation — natural German, not a translation.

Return ONLY this JSON (no markdown wrapper, no explanation, just the JSON):
{{
  "title": "a real song title — evocative, not generic",
  "theme": "one sentence: what this fusion song is actually about",
  "en": {{
    "intro": "2-4 lines that set the scene/mood",
    "verse1": "4-6 lines — establish the story, specific imagery",
    "preChorus": "2-4 lines — emotional build, tension rising",
    "chorus": "4-6 lines — the emotional peak, singable, memorable, the hook",
    "verse2": "4-6 lines — deepen the story, new angle on same emotion",
    "bridge": "3-5 lines — the turn, the revelation, something shifts",
    "outro": "2-4 lines — resolution or open-ended fade"
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
}}"""


@app.post("/api/generate-lyrics")
async def generate_lyrics(request: Request):
    try:
        body = await request.json()
        s1         = body.get('s1', {})
        s2         = body.get('s2', {})
        match_info = body.get('matchInfo', {})
        regen_seed = body.get('regenSeed', 0)

        style = body.get('style', {})
        prompt = build_prompt(s1, s2, match_info, style=style)
        
        system = (
            "You are a professional songwriter with genuine knowledge of music history, "
            "songcraft, and what makes lyrics emotionally resonant. "
            "You write REAL songs — not meta-commentary, not placeholder text, not song titles as lyrics. "
            "Every line you write is specific, earned, and could be performed on a stage. "
            "You never use a song's title as a lyric. You never explain what a song is about — you SHOW it."
        )
        if regen_seed > 0:
            system += (
                f" This is attempt #{regen_seed+1}. Write a completely different take — "
                "different imagery, different emotional angle, different structural approach. "
                "Surprise yourself."
            )

        message = client.messages.create(
            model="claude-sonnet-4-5",
            max_tokens=4000,
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
