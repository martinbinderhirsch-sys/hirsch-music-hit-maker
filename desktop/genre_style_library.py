"""
Hirsch Music Hit Maker — Genre Style Library
Umfassende Stilbibliothek für alle 18 Genres

Genres: Rock, Pop, Hip-Hop, Metal, Country, EDM, Schlager, Classical, Jazz,
        Blues, Folk, R&B, Gospel, Latin, Reggae, World, Experimental, Classics

Zweck: Gibt einem KI-Songwriter detaillierte stilistische Leitlinien für
       authentische Lyrics und Musik-Prompts in jedem Genre.

Autor: Hirsch Music Hit Maker — Genre Style Engine
Version: 1.0
"""

GENRE_STYLE_LIBRARY = {

    "Rock": {
        # ── VIBES & ATMOSPHÄRE ──
        "vibes": [
            "rebellious", "raw energy", "cathartic", "powerful", "anthemic",
            "gritty", "passionate", "liberating", "intense", "nostalgic",
            "defiant", "electric"
        ],
        "anti_vibes": [
            "saccharine", "passive", "polished-to-sterility", "submissive",
            "overly cheerful", "delicate", "ambient-ethereal"
        ],

        # ── TONARTEN & HARMONIE ──
        "preferred_keys": ["E minor", "A minor", "D minor", "G major", "E major", "B minor"],
        "chord_progressions": [
            "i-VII-VI-VII",
            "I-IV-V",
            "I-V-vi-IV",
            "i-VI-III-VII",
            "I-bVII-IV",
            "vi-IV-I-V",
            "i-iv-V"
        ],
        "harmonic_feel": (
            "Rock leans heavily on power chords and pentatonic-based harmony, creating a bold, "
            "uncluttered sound. Chromatic passing tones and borrowed chords from parallel modes "
            "(especially the bVII) add grit and surprise. Tension-release is fundamental — "
            "suspension into the chorus is a staple device."
        ),
        "modes": ["Aeolian", "Mixolydian", "Dorian", "Pentatonic minor", "Blues scale"],

        # ── RHYTHMUS & TEMPO ──
        "bpm_ranges": {
            "slow": "60-80",
            "mid":  "100-130",
            "fast": "150-200"
        },
        "time_signatures": ["4/4", "3/4", "6/8", "7/8"],
        "rhythm_feel": (
            "Rock feels driven and forward-moving, anchored by a strong backbeat on beats 2 and 4. "
            "The kick-snare foundation creates a physical, visceral push."
        ),
        "groove_type": "straight, heavy backbeat, occasional shuffle (blues-rock)",

        # ── INSTRUMENTE & SOUND ──
        "core_instruments": [
            "electric guitar", "bass guitar", "drum kit", "lead vocals", "rhythm guitar"
        ],
        "optional_instruments": [
            "Hammond organ", "piano", "harmonica", "acoustic guitar", "synthesizer"
        ],
        "signature_sounds": [
            "distorted power chords", "guitar solo with bends and vibrato",
            "drum fills into chorus", "bass walking lines", "feedback sustain",
            "palm-muted chugging"
        ],
        "production_style": (
            "Rock production ranges from raw and live-sounding (minimal overdubs, room ambience) "
            "to massive arena rock with layered guitars and dense low-end. "
            "Guitar tone is central — amp character, speaker cabinet, and mic placement shape the entire vibe. "
            "Drums are typically large, punchy, and real."
        ),
        "mix_character": "mid-forward, warm low-end, guitars sit in the 2–5kHz presence zone, drums punchy and wide",

        # ── LYRIK & TEXTE ──
        "lyric_themes": [
            "freedom and rebellion", "love and heartbreak", "self-identity", "youth and coming-of-age",
            "disillusionment", "road life and escape", "social critique", "triumph over adversity",
            "nostalgia", "anger and frustration", "dark romance", "existential questioning"
        ],
        "lyric_style": (
            "Rock lyrics favor directness and visceral imagery over complex metaphor. "
            "Hooks are blunt and memorable — the chorus should be singable at a concert. "
            "Verses build a narrative or emotional scene; bridges often deliver a revelation or shift. "
            "Profanity and colloquial language are genre-appropriate."
        ),
        "language_register": "informal, colloquial, direct, occasionally poetic (classic rock)",
        "pov_typical": "first person singular; sometimes collective 'we' for anthems",
        "rhyme_schemes": ["AABB", "ABAB", "ABCB", "AAAA (in choruses)"],
        "line_length": "medium (6–10 syllables), rhythmically punchy, strong stressed syllables",

        # ── SONG-STRUKTUR ──
        "typical_structure": "Intro – Verse – Pre-Chorus – Chorus – Verse – Pre-Chorus – Chorus – Bridge – Solo – Chorus – Outro",
        "intro_style": "Guitar riff or drum intro establishing the groove; 4–16 bars before vocal entry",
        "chorus_character": "Loud, wide, anthemic — full band in, vocals soaring, hook is melodically and lyrically immediate",
        "bridge_role": "Provides tonal/emotional contrast; often stripped back before the final chorus explosion",
        "outro_style": "Fade-out on riff repetition or hard stop; guitar solo reprises common",

        # ── FUSION-KOMPATIBILITÄT ──
        "fuses_well_with": ["Blues", "Country", "Metal", "Pop", "Folk", "Classical"],
        "fusion_tension_with": ["EDM", "Schlager"],
        "bridge_elements": [
            "pentatonic guitar licks (→ Blues, Country)",
            "distorted power chords (→ Metal)",
            "anthemic singalong chorus (→ Pop)",
            "acoustic finger-picking (→ Folk)",
            "orchestral swells (→ Classical)"
        ],

        # ── SUNO/UDIO PROMPT TAGS ──
        "suno_tags": [
            "rock", "electric guitar", "distorted guitar", "power chords", "drum kit",
            "bass guitar", "anthemic", "guitar solo", "raw", "energetic", "backbeat",
            "arena rock", "stadium rock", "riff-based"
        ],
        "negative_tags": ["soft", "ambient", "electronic drums", "auto-tune heavy", "delicate"],

        # ── EMOTIONALE DNA ──
        "emotional_spectrum": {
            "primary": ["defiance", "passion", "catharsis"],
            "secondary": ["longing", "pride", "frustration"],
            "forbidden": ["complacency", "saccharine joy", "passivity"]
        },
        "listener_state": "The listener wants to feel alive, empowered, or emotionally released — driving fast, working out, or letting go.",
        "cultural_context": (
            "Rock emerged from American blues and R&B in the 1950s, becoming the dominant Western youth "
            "music from the 1960s through the 1990s. It carries the mythology of the counterculture, "
            "the British Invasion, and the stadium era. Today it fragments into dozens of sub-genres "
            "while retaining guitar-driven identity as its cultural signature."
        ),

        # ── SUB-GENRES & VARIANTEN ──
        "sub_genres": {
            "Classic Rock":      "1960s–80s guitar-driven rock; Beatles, Zeppelin, Stones blueprint",
            "Hard Rock":         "Heavy riffs, loud production, blues-derived aggression; AC/DC, Aerosmith",
            "Punk Rock":         "Fast, short, raw, anti-establishment; Ramones, Sex Pistols",
            "Alternative Rock":  "Post-punk indie ethos, diverse sounds; Nirvana, R.E.M., Radiohead",
            "Grunge":            "Distorted, sludgy, emotionally raw; Seattle sound, flannel aesthetic",
            "Indie Rock":        "Lo-fi to hi-fi, guitar-centric, DIY spirit; Strokes, Arctic Monkeys",
            "Progressive Rock":  "Complex time signatures, suites, concept albums; Yes, Rush, Genesis",
            "Southern Rock":     "Blues-roots, slide guitar, Americana storytelling; Lynyrd Skynyrd",
        },

        # ── REPRÄSENTATIVE KÜNSTLER ──
        "iconic_artists": [
            "Led Zeppelin", "The Rolling Stones", "The Beatles", "Jimi Hendrix",
            "AC/DC", "Nirvana", "The Who", "Bruce Springsteen", "Pink Floyd", "Queen"
        ],
        "modern_artists": [
            "Foo Fighters", "Arctic Monkeys", "Jack White", "The Black Keys", "Greta Van Fleet"
        ],

        # ── SONG-WRITING TIPPS ──
        "writing_tips": [
            "Lead with the hook — the title or central image should appear in the first chorus",
            "Build verses around a single dominant emotion or narrative tension",
            "Use the pre-chorus to raise energy with rhythmic acceleration or a melodic climb",
            "Write the guitar riff first and let it dictate the vocal melody's rhythm",
            "Contrasting dynamics between verse and chorus are essential — go quieter in verses",
            "The bridge should shift key, tempo, or lyric perspective to reset before the finale",
            "Keep chorus lyrics short, punchy, and vowel-heavy for singability"
        ],
        "avoid": [
            "Over-produced sterile sound that strips the live grit",
            "Generic 'I love you baby' pop lyrics without specificity",
            "All verses at the same dynamic level — contrast is everything",
            "Solos that are technically impressive but emotionally disconnected from the song",
            "Timid vocals — rock demands conviction and commitment",
        ],
    },

    "Pop": {
        # ── VIBES & ATMOSPHÄRE ──
        "vibes": [
            "uplifting", "catchy", "relatable", "feel-good", "bittersweet",
            "empowering", "romantic", "danceable", "bright", "polished",
            "euphoric", "accessible"
        ],
        "anti_vibes": [
            "deliberately obscure", "abrasive", "dissonant", "lo-fi raw",
            "overly dark", "experimental-alienating", "monotonous"
        ],

        # ── TONARTEN & HARMONIE ──
        "preferred_keys": ["C major", "G major", "D major", "A major", "F major", "E major"],
        "chord_progressions": [
            "I-V-vi-IV",
            "vi-IV-I-V",
            "I-IV-V-I",
            "I-ii-IV-V",
            "IV-I-V-vi",
            "I-iii-IV-V",
            "ii-V-I"
        ],
        "harmonic_feel": (
            "Pop harmony is fundamentally diatonic and emotionally transparent — major keys for joy/dance, "
            "minor keys or vi-pivot for emotional depth. The I-V-vi-IV progression is so universal it's "
            "become a genre archetype. Modulations are rare but used for emotional uplift (key change into final chorus)."
        ),
        "modes": ["Ionian (major)", "Aeolian (relative minor)", "Mixolydian (modern pop)"],

        # ── RHYTHMUS & TEMPO ──
        "bpm_ranges": {
            "slow": "60-80",
            "mid":  "90-120",
            "fast": "120-140"
        },
        "time_signatures": ["4/4", "3/4 (power ballad)"],
        "rhythm_feel": (
            "Pop rhythm is clean, grid-aligned, and designed for dancefloor or emotional resonance. "
            "The groove is immediate and never challenges the listener rhythmically."
        ),
        "groove_type": "straight, quantized, four-on-the-floor or backbeat, programmed or live feel",

        # ── INSTRUMENTE & SOUND ──
        "core_instruments": [
            "lead vocals", "synthesizer", "programmed drums/drum machine",
            "bass (synth or electric)", "acoustic or electric guitar"
        ],
        "optional_instruments": [
            "strings (real or sampled)", "piano", "brass stabs", "backing vocals", "synth pads"
        ],
        "signature_sounds": [
            "pitch-corrected, smooth lead vocal", "layered harmonies in chorus",
            "four-on-the-floor kick", "synth pad swell into chorus", "clap on beats 2&4",
            "vocal chop/stutter effect (modern pop)"
        ],
        "production_style": (
            "Pop production is meticulous and maximalist — every element is placed intentionally. "
            "The mix is loud, wide, and spectrally balanced for streaming playback on earbuds and speakers. "
            "Sidechaining, parallel compression, and precise automation are standard. "
            "The drop from verse to chorus is a key production moment."
        ),
        "mix_character": "bright, open, wide stereo field, strong low-end, clear vocal always on top",

        # ── LYRIK & TEXTE ──
        "lyric_themes": [
            "romantic love and desire", "heartbreak and healing", "self-confidence and empowerment",
            "friendship and belonging", "partying and celebration", "vulnerability and longing",
            "chasing dreams", "identity and self-discovery", "obsession and infatuation",
            "nostalgia and summer memories", "toxic relationships", "social media life"
        ],
        "lyric_style": (
            "Pop lyrics prioritize universality — the listener should immediately identify with the emotion. "
            "Imagery is concrete but not overly literary; metaphors are familiar and emotionally direct. "
            "The hook must be the most memorable line, repeated multiple times. "
            "Conversational phrasing that sounds natural when sung aloud."
        ),
        "language_register": "conversational, accessible, contemporary slang welcome, emotionally honest",
        "pov_typical": "first person singular; direct address to 'you' extremely common",
        "rhyme_schemes": ["AABB", "ABAB", "ABCB", "internal rhyme in hook lines"],
        "line_length": "medium-short (6–9 syllables), rhythmically tight, vowel sounds on strong beats",

        # ── SONG-STRUKTUR ──
        "typical_structure": "Verse – Pre-Chorus – Chorus – Verse – Pre-Chorus – Chorus – Bridge – Chorus (×2)",
        "intro_style": "Short (4–8 bars), often hooks straight into verse; may open with vocal or percussion loop",
        "chorus_character": "Highest energy point, fullest production, singable hook repeated 3–4 times; often 8 bars",
        "bridge_role": "Breaks the loop, provides lyrical twist or new emotional angle; often half-time or stripped",
        "outro_style": "Chorus repetition fading out or cold stop; sometimes acapella final line",

        # ── FUSION-KOMPATIBILITÄT ──
        "fuses_well_with": ["R&B", "EDM", "Hip-Hop", "Rock", "Latin", "Country"],
        "fusion_tension_with": ["Metal", "Experimental"],
        "bridge_elements": [
            "catchy melodic hook (→ any genre)",
            "four-on-the-floor beat (→ EDM)",
            "verse rap section (→ Hip-Hop)",
            "acoustic guitar texture (→ Country, Folk)",
            "Latin percussion groove (→ Latin)"
        ],

        # ── SUNO/UDIO PROMPT TAGS ──
        "suno_tags": [
            "pop", "catchy", "upbeat", "polished production", "vocal melody",
            "synth", "programmed drums", "four-on-the-floor", "melodic hook",
            "bright", "radio-ready", "modern pop", "harmonies", "anthemic chorus"
        ],
        "negative_tags": ["noise", "atonal", "lo-fi", "abrasive", "unpredictable structure"],

        # ── EMOTIONALE DNA ──
        "emotional_spectrum": {
            "primary": ["joy", "longing", "empowerment"],
            "secondary": ["vulnerability", "excitement", "nostalgia"],
            "forbidden": ["alienation", "nihilism", "intellectual detachment"]
        },
        "listener_state": "The listener wants to feel understood, uplifted, or emotionally validated — commuting, working out, or processing feelings.",
        "cultural_context": (
            "Pop is the lingua franca of commercial music, perpetually absorbing influences from "
            "every other genre to stay current. It has defined mainstream radio since the 1950s, "
            "evolving through Motown, New Wave, teen pop, and streaming-era maximalism. "
            "Its globalization is unprecedented — K-Pop, Afropop, and Latin pop now share the global charts."
        ),

        # ── SUB-GENRES & VARIANTEN ──
        "sub_genres": {
            "Teen Pop":       "Bright, innocent energy; high-production; Britney, NSYNC, early Taylor Swift",
            "Synth-Pop":      "Electronic textures dominate; melodic leads; Depeche Mode, Robyn, Dua Lipa",
            "Indie Pop":      "Softer production, introspective lyrics; Lorde, Vampire Weekend",
            "Dance-Pop":      "Dancefloor-optimized, 4-on-the-floor; Kylie Minogue, Dua Lipa, BLACKPINK",
            "Power Pop":      "Guitar-driven hooks with pop polish; Weezer, Tom Petty",
            "Art Pop":        "Experimental concepts with pop structure; Björk, Kate Bush, FKA Twigs",
            "K-Pop":          "Highly choreographed, group-focused, dramatic production; BTS, BLACKPINK",
            "Electropop":     "Synth-heavy, cold yet catchy; Ellie Goulding, Halsey, Grimes",
        },

        # ── REPRÄSENTATIVE KÜNSTLER ──
        "iconic_artists": [
            "Michael Jackson", "Madonna", "Whitney Houston", "The Beatles",
            "ABBA", "Mariah Carey", "Britney Spears", "Taylor Swift", "Beyoncé", "Prince"
        ],
        "modern_artists": [
            "Dua Lipa", "Olivia Rodrigo", "Harry Styles", "Billie Eilish", "The Weeknd"
        ],

        # ── SONG-WRITING TIPPS ──
        "writing_tips": [
            "Write the chorus title/hook first — everything else serves it",
            "The pre-chorus should create an irresistible pull into the chorus — rhythmically tighten it",
            "Use conversational phrases that feel spoken but sing perfectly",
            "Think about the 'relatable moment' — the lyric everyone will share on social media",
            "Leave space in the melody — don't over-syllabize; let the listener breathe",
            "The bridge should subvert or deepen the chorus hook with a new lyrical angle",
            "Test your hook by singing it acapella — if it works naked, it works in the full production"
        ],
        "avoid": [
            "Obscure imagery that requires explanation",
            "Over-complex chord changes that distract from the melody",
            "Verses that are longer than the listener's attention span (max 16 bars)",
            "Forgetting the melodic lift — the chorus must reach higher than the verse",
            "Derivative hooks that too obviously echo existing hits"
        ],
    },

    "Hip-Hop": {
        # ── VIBES & ATMOSPHÄRE ──
        "vibes": [
            "confident", "street-smart", "narrative", "boastful", "introspective",
            "gritty", "celebratory", "politically charged", "cinematic", "raw",
            "hustler energy", "community pride"
        ],
        "anti_vibes": [
            "timid", "overly melodic without purpose", "acoustic-pastoral",
            "orchestral-heavy without sampling context", "naïve", "apolitical softness"
        ],

        # ── TONARTEN & HARMONIE ──
        "preferred_keys": ["C minor", "F minor", "G minor", "D minor", "Bb major", "Eb major"],
        "chord_progressions": [
            "i-VII-VI-VII (minor loop)",
            "i-iv (two-chord vamp)",
            "I-IV-I-V (jazz-derived samples)",
            "single-chord drone with harmonic color",
            "ii-V-I (jazz sample source)",
            "i-bVII-bVI-bVII",
            "looped single-bar progression"
        ],
        "harmonic_feel": (
            "Hip-hop harmony is often derived from samples — soul, jazz, funk, and R&B records provide "
            "the harmonic vocabulary. Original beats frequently loop short 2–4 bar progressions, "
            "letting rhythmic and lyrical interest carry the song. Minor tonality dominates for emotional depth; "
            "major is used for celebratory or summer tracks."
        ),
        "modes": ["Aeolian", "Dorian", "Blues scale", "Pentatonic minor", "Mixolydian (samples)"],

        # ── RHYTHMUS & TEMPO ──
        "bpm_ranges": {
            "slow": "60-80",
            "mid":  "85-100",
            "fast": "130-160"
        },
        "time_signatures": ["4/4", "implicit 3/4 triplet feel (trap)"],
        "rhythm_feel": (
            "The rhythmic foundation is the beat — kick, snare, and hi-hat patterns define sub-genre identity. "
            "The MC's flow creates a second rhythmic layer above the beat, often syncopating across bar lines."
        ),
        "groove_type": "syncopated, programmed, quantized or swung; trap: hi-hat rolls and sparse kicks",

        # ── INSTRUMENTE & SOUND ──
        "core_instruments": [
            "drum machine (808, MPC)", "sampler", "bass (808 bass or sampled)",
            "lead rapper/vocalist", "synthesizer or sample-derived melody"
        ],
        "optional_instruments": [
            "live strings (sample or real)", "piano", "brass section (sampled)",
            "electric guitar (sampled or live)", "scratch DJ turntable"
        ],
        "signature_sounds": [
            "808 bass kick with sub-bass resonance", "vinyl crackle and sample chops",
            "hi-hat triplet rolls (trap)", "layered vocal ad-libs",
            "pitched vocal sample hook", "handclap on 2 and 4"
        ],
        "production_style": (
            "Hip-hop production centers on beat construction — layering loops, chops, and original synthesis. "
            "Sample clearance culture has pushed modern producers toward original composition that mimics vintage sources. "
            "Low end is massively emphasized; 808 bass and kick interact as one element. "
            "The mix is dense yet the vocal always sits prominently in the center."
        ),
        "mix_character": "heavy sub-bass, punchy mid-bass, vocal center-forward, hi-hats crispy and detailed",

        # ── LYRIK & TEXTE ──
        "lyric_themes": [
            "hustle and ambition", "street life and survival", "wealth and success",
            "systemic racism and social justice", "loyalty and betrayal", "flexing and status",
            "love and relationships (often complex)", "mental health and trauma",
            "community and roots", "identity and authenticity", "violence and consequences",
            "spiritual and philosophical reflection"
        ],
        "lyric_style": (
            "Hip-hop lyricism values wordplay, multisyllabic rhymes, internal rhymes, and flow — "
            "the rhythm and cadence of delivery is as important as the words. "
            "Storytelling, boasting, social commentary, and confessional modes all coexist. "
            "Slang and vernacular are authenticity markers. Literary references and metaphor coexist with street vocabulary."
        ),
        "language_register": "AAVE, street slang, regional dialect, code-switching, elevated literary in conscious rap",
        "pov_typical": "first person singular dominant; third-person narrative in storytelling tracks",
        "rhyme_schemes": [
            "multisyllabic end rhyme", "internal rhyme chains",
            "assonance and consonance clusters", "AABB couplets", "triplet schemes"
        ],
        "line_length": "variable — the bar is the unit; 8–16 syllables per bar, flow manipulates rhythm",

        # ── SONG-STRUKTUR ──
        "typical_structure": "Intro – Verse 1 – Hook – Verse 2 – Hook – Bridge/Verse 3 – Hook – Outro",
        "intro_style": "Beat plays alone 4–8 bars; producer tag or sample intro; artist ad-libs entry",
        "chorus_character": "Hook is short (4–8 bars), often sung or melodic; high repeatability is key",
        "bridge_role": "Often a third verse or a feature artist verse; rarely a traditional melody bridge",
        "outro_style": "Beat fade, repeated ad-libs and improvisations, shoutouts",

        # ── FUSION-KOMPATIBILITÄT ──
        "fuses_well_with": ["R&B", "Pop", "Jazz", "Blues", "Latin", "Reggae"],
        "fusion_tension_with": ["Metal", "Classical"],
        "bridge_elements": [
            "sample-based harmonic loop (→ Jazz, Soul, R&B)",
            "melodic sung hook (→ R&B, Pop)",
            "dancehall rhythm pattern (→ Reggae)",
            "Latin percussion (→ Latin)",
            "spoken word/narrative verse (→ Folk, Spoken Word)"
        ],

        # ── SUNO/UDIO PROMPT TAGS ──
        "suno_tags": [
            "hip-hop", "rap", "808 bass", "trap beat", "boom bap", "sampled loop",
            "lyrical", "flow", "drum machine", "hi-hat rolls", "bass-heavy",
            "urban", "street", "mc vocals", "punchy snare"
        ],
        "negative_tags": ["acoustic guitar", "orchestral only", "folk", "soft", "no bass"],

        # ── EMOTIONALE DNA ──
        "emotional_spectrum": {
            "primary": ["confidence", "defiance", "pride"],
            "secondary": ["vulnerability", "anger", "joy (celebration)"],
            "forbidden": ["timidity", "obsequiousness", "naïveté"]
        },
        "listener_state": "The listener wants to feel empowered, represented, or immersed in a narrative world — driving, working out, or reflecting.",
        "cultural_context": (
            "Born in the South Bronx in the mid-1970s from DJ culture, breakdancing, and MC battles, "
            "hip-hop became the dominant global youth music of the 21st century. "
            "It carries deep roots in Black American experience, resistance, and creativity, "
            "and has spawned regional variants worldwide — UK grime, Afrobeats rap, French hip-hop, Brazilian funk."
        ),

        # ── SUB-GENRES & VARIANTEN ──
        "sub_genres": {
            "Boom Bap":         "Classic East Coast sound; jazz/soul samples, complex lyricism; Nas, Biggie, ATCQ",
            "Trap":             "808-heavy, hi-hat triplets, sparse melodies; Gucci Mane, Future, Travis Scott",
            "Conscious Rap":    "Political and social commentary; Kendrick Lamar, J. Cole, Mos Def",
            "Cloud Rap":        "Atmospheric, lo-fi, dreamy textures; A$AP Rocky early work, Yung Lean",
            "Drill":            "Dark, menacing, staccato flow; Chicago drill (Chief Keef), UK drill",
            "Gangsta Rap":      "Street narrative, West Coast G-funk or East Coast raw; NWA, Biggie, Jay-Z",
            "Alternative Rap":  "Experimental, anti-commercial; Tyler the Creator, Childish Gambino, Earl Sweatshirt",
            "Mumble Rap":       "Melody over lyrical complexity, melodic flow, Auto-Tune; Young Thug, Lil Uzi Vert",
        },

        # ── REPRÄSENTATIVE KÜNSTLER ──
        "iconic_artists": [
            "Tupac Shakur", "The Notorious B.I.G.", "Jay-Z", "Eminem", "Nas",
            "Dr. Dre", "Rakim", "Public Enemy", "A Tribe Called Quest", "Lauryn Hill"
        ],
        "modern_artists": [
            "Kendrick Lamar", "Drake", "J. Cole", "Travis Scott", "Cardi B"
        ],

        # ── SONG-WRITING TIPPS ──
        "writing_tips": [
            "Write in bars — think rhythmically before lyrically; the beat dictates the flow",
            "Stack internal rhymes within the bar for density and sophistication",
            "The hook must be simpler and more melodic than the verses — contrast is the key",
            "Tell a specific story; concrete details beat vague abstraction",
            "Find your unique voice/flow — cadence differentiation is how MCs stand out",
            "Use double meanings, wordplay, and puns — reward repeated listening",
            "Study the beat's pockets — where the kick and snare land determines your emphasis points"
        ],
        "avoid": [
            "Copying existing artists' flows too closely — originality is currency",
            "Over-stuffing every bar with forced rhymes at the expense of meaning",
            "Ignoring the hook — a great verse with a forgettable hook will be forgotten",
            "Using slang that isn't authentic to your experience",
            "Mixing metaphors that clash or confuse the central image"
        ],
    },

    "Metal": {
        # ── VIBES & ATMOSPHÄRE ──
        "vibes": [
            "crushing", "epic", "dark", "aggressive", "primal", "cathartic",
            "theatrical", "powerful", "nihilistic", "brutal", "majestic", "intense"
        ],
        "anti_vibes": [
            "lightweight", "cheerful", "delicate", "saccharine", "passive",
            "polished-generic", "emotionally shallow"
        ],

        # ── TONARTEN & HARMONIE ──
        "preferred_keys": ["E minor", "D minor", "B minor", "C# minor", "A minor", "F# minor"],
        "chord_progressions": [
            "i-bVI-bVII-i",
            "i-bVII-i (power riff vamp)",
            "i-iv-bVII-bVI",
            "Tritone substitution (Devil's interval)",
            "i-bII (Neapolitan, dark menace)",
            "Chromatic descent: i–VII–bVII–VI",
            "Diminished and augmented chord tension"
        ],
        "harmonic_feel": (
            "Metal harmony is built on darkness and dissonance — tritones, diminished chords, and chromatic "
            "motion create the characteristic menace. Power chords (dyads without third) give low-tuned "
            "guitars their crushing sound. Classical influence brings modal complexity (Phrygian, Locrian) "
            "in progressive and melodic metal. Harmonic contrast between crushing riffs and melodic leads is essential."
        ),
        "modes": ["Aeolian", "Phrygian", "Locrian", "Harmonic minor", "Diminished scale", "Phrygian dominant"],

        # ── RHYTHMUS & TEMPO ──
        "bpm_ranges": {
            "slow": "40-70",
            "mid":  "100-160",
            "fast": "180-260"
        },
        "time_signatures": ["4/4", "6/8", "7/8", "5/4", "odd meters (prog metal)", "12/8 (doom)"],
        "rhythm_feel": (
            "Metal rhythm is defined by precise, powerful execution. The double-bass drum kick drives "
            "extreme tempos; syncopated riff patterns create tension. "
            "Groove metal swings; thrash is relentless 16th notes; doom breathes slowly."
        ),
        "groove_type": "palm-muted syncopated riffing, double-bass drive, blast beats (extreme), rhythmic precision",

        # ── INSTRUMENTE & SOUND ──
        "core_instruments": [
            "downtuned electric guitar (7-string or drop-tuned)", "electric bass",
            "double-bass drum kit", "lead vocals (clean or extreme)", "rhythm guitar"
        ],
        "optional_instruments": [
            "orchestral strings/keyboards (symphonic)", "choir (black/symphonic metal)",
            "synthesizer", "acoustic guitar (progressive)", "Hammond organ (doom)"
        ],
        "signature_sounds": [
            "palm-muted chug", "pinch harmonics (squeals)", "tremolo picking",
            "double-bass drum blast beats", "death growl or black metal shriek",
            "power chord with high-gain amp distortion", "guitar sweep arpeggios"
        ],
        "production_style": (
            "Modern metal production emphasizes mechanical precision — drums are often sample-reinforced "
            "or triggered, guitars are layered for a wall-of-sound. "
            "Tuning and timing are surgically corrected. The mix is dense, with enormous low-end from bass "
            "and kick working together. Older metal (70s–80s) was rawer and more organic."
        ),
        "mix_character": "dense, dark, heavy low-mid emphasis, guitars saturate the mid-range, drums clinical and powerful",

        # ── LYRIK & TEXTE ──
        "lyric_themes": [
            "death and mortality", "war and conflict", "Satanism and the occult (theatrical)",
            "mythological epics", "social collapse and apocalypse", "inner darkness and psychological horror",
            "nature's brutality", "anti-religion and anti-authority", "Norse/Viking mythology",
            "sci-fi and fantasy narratives", "nihilism and existentialism", "grief and isolation"
        ],
        "lyric_style": (
            "Metal lyrics range from direct aggression to elaborate fantasy world-building. "
            "Vocabulary can be archaic and poetic (black metal, power metal) or viscerally physical (death metal). "
            "Literary and mythological references reward the devoted listener. "
            "Theatricality and grandiosity are embraced — the lyric is part of the performance art."
        ),
        "language_register": "elevated-archaic (power/black metal) to visceral-vernacular (death/thrash); theatrical throughout",
        "pov_typical": "first person (personal darkness) or third person epic narrative; 'we' for anthemic calls",
        "rhyme_schemes": ["AABB", "ABAB", "free verse (experimental/black metal)", "internal rhyme for aggression"],
        "line_length": "variable — short aggressive punches in thrash, long flowing lines in power/prog metal",

        # ── SONG-STRUKTUR ──
        "typical_structure": "Intro Riff – Verse – Chorus – Verse – Chorus – Solo – Bridge – Chorus – Outro",
        "intro_style": "Heavy riff or atmospheric build (30s–2min); establishes the sonic world before vocals",
        "chorus_character": "Epic, wide, memorable — clean vocals soaring (power metal) or gang shout (thrash); maximum impact",
        "bridge_role": "Often contains the guitar solo or an atmospheric breakdown; maximum dynamic contrast",
        "outro_style": "Riff reprise, fade into noise, or abrupt stop; sometimes solo extends to outro",

        # ── FUSION-KOMPATIBILITÄT ──
        "fuses_well_with": ["Classical", "Rock", "Blues", "Folk", "Industrial"],
        "fusion_tension_with": ["Pop", "EDM", "Schlager"],
        "bridge_elements": [
            "orchestral arrangement (→ Classical, Film Score)",
            "blues-scale lead guitar (→ Blues, Rock)",
            "acoustic folk passages (→ Folk, Celtic)",
            "industrial electronic programming (→ Industrial, EDM)",
            "jazz-influenced odd meter (→ Jazz, Prog)"
        ],

        # ── SUNO/UDIO PROMPT TAGS ──
        "suno_tags": [
            "metal", "heavy metal", "distorted guitar", "downtuned", "double bass drum",
            "powerful", "dark", "aggressive", "guitar riff", "heavy", "crushing",
            "epic", "guitar solo", "palm mute", "high-gain amp"
        ],
        "negative_tags": ["soft", "acoustic only", "pop production", "upbeat cheerful", "ukulele"],

        # ── EMOTIONALE DNA ──
        "emotional_spectrum": {
            "primary": ["rage", "darkness", "catharsis"],
            "secondary": ["awe", "grief", "power"],
            "forbidden": ["contentment", "lightness", "irony (except glam/stoner)"]
        },
        "listener_state": "The listener wants to externalize anger, feel visceral physical power, or escape into an epic dark world.",
        "cultural_context": (
            "Metal grew from hard rock and blues in the late 1960s (Black Sabbath, Led Zeppelin's heavy moments) "
            "and diversified into dozens of micro-genres with devoted global communities. "
            "It carries an anti-mainstream ethos despite massive commercial success in its heavier forms. "
            "Its global reach spans Scandinavia (black/death), Japan (visual kei), Latin America, and beyond."
        ),

        # ── SUB-GENRES & VARIANTEN ──
        "sub_genres": {
            "Heavy Metal":       "Classic 70s-80s blueprint; Sabbath, Priest, Maiden; riffs and melody balance",
            "Thrash Metal":      "Fast, aggressive, political; Metallica, Slayer, Megadeth, Anthrax",
            "Death Metal":       "Extreme speed, growled vocals, technical complexity; Death, Morbid Angel",
            "Black Metal":       "Atmospheric, lo-fi, tremolo, shrieked vocals; Mayhem, Burzum, Darkthrone",
            "Doom Metal":        "Slow, crushing, dirge-like; Black Sabbath roots; Sleep, Candlemass",
            "Power Metal":       "Operatic clean vocals, fast, fantasy themes; Blind Guardian, Helloween",
            "Progressive Metal": "Complex, odd meters, technical; Dream Theater, Tool, Opeth",
            "Symphonic Metal":   "Orchestral + metal; female operatic vocals; Nightwish, Epica",
        },

        # ── REPRÄSENTATIVE KÜNSTLER ──
        "iconic_artists": [
            "Black Sabbath", "Metallica", "Iron Maiden", "Judas Priest",
            "Pantera", "Slayer", "Megadeth", "Tool", "Ozzy Osbourne", "Dio"
        ],
        "modern_artists": [
            "Mastodon", "Gojira", "Ghost", "Bloodbath", "Spiritbox"
        ],

        # ── SONG-WRITING TIPPS ──
        "writing_tips": [
            "Build the riff first — it is the hook; every other element serves the riff",
            "Layer dynamic contrast: crushing verse riff vs. melodic chorus or vice versa",
            "Match lyrical imagery to the sonic texture — dark harmonics need dark words",
            "Use odd time signatures to create instability and resolution pay-off",
            "Vocal melody in extreme metal should work counter-intuitively to the rhythm for maximum tension",
            "The solo should be the emotional climax, not just a technical exercise",
            "Intro world-building pays off — set the atmosphere before the first strike"
        ],
        "avoid": [
            "Generic 'darkness for darkness's sake' without lyrical depth",
            "Over-triggered drums that remove all humanity from the performance",
            "Mixing too cleanly — some grit in the distortion is essential to the genre's character",
            "Burying the bass guitar — it should lock with the kick and be felt",
            "Ignoring dynamics — even the heaviest albums have light-dark contrast"
        ],
    },

    "Country": {
        # ── VIBES & ATMOSPHÄRE ──
        "vibes": [
            "nostalgic", "heartfelt", "storytelling", "down-to-earth", "sincere",
            "bittersweet", "celebratory", "rugged", "warm", "patriotic",
            "longing", "communal"
        ],
        "anti_vibes": [
            "urban-detached", "ironic", "coldly electronic", "aggressive",
            "abstract", "hedonistic (without redemption)", "over-produced plastic"
        ],

        # ── TONARTEN & HARMONIE ──
        "preferred_keys": ["G major", "D major", "A major", "E major", "C major", "B minor"],
        "chord_progressions": [
            "I-IV-V-I",
            "I-V-ii-IV",
            "I-IV-I-V",
            "I-vi-IV-V",
            "I-bVII-IV-I (outlaw country)",
            "ii-V-I (country ballad)",
            "I-IV-V (3-chord classic)"
        ],
        "harmonic_feel": (
            "Country harmony is diatonic, warm, and often pentatonic-influenced. "
            "Open guitar voicings and capo use create a bright, ringing quality. "
            "Pedal steel adds characteristic major-7 and passing tones; "
            "blue notes from country's blues roots add emotional color to ballads."
        ),
        "modes": ["Ionian (major)", "Mixolydian", "Pentatonic major", "Blues scale (blue notes)"],

        # ── RHYTHMUS & TEMPO ──
        "bpm_ranges": {
            "slow": "55-75",
            "mid":  "90-120",
            "fast": "130-180"
        },
        "time_signatures": ["4/4", "3/4 (waltz — bluegrass/classic)", "2/4 (train rhythm)"],
        "rhythm_feel": (
            "Country rhythm ranges from two-step bounce to half-time ballad. "
            "The boom-chick (bass note – chord strum) pattern is fundamental to acoustic country."
        ),
        "groove_type": "boom-chick strum, shuffle, two-step, straight 4/4, train rhythm",

        # ── INSTRUMENTE & SOUND ──
        "core_instruments": [
            "acoustic guitar (or electric)", "steel guitar (pedal steel or dobro)",
            "fiddle", "banjo", "lead vocals"
        ],
        "optional_instruments": [
            "mandolin", "upright bass", "piano", "harmonica", "drum kit (modern country)"
        ],
        "signature_sounds": [
            "pedal steel glide and sustain", "chicken-pickin' telecaster tone",
            "fiddle breakdown", "open-tuned acoustic strum",
            "vocal twang and nasal resonance", "train-beat kick and snare"
        ],
        "production_style": (
            "Nashville production ('Nashville Sound') is polished and lush with session musicians. "
            "Americana and outlaw country lean raw and live-sounding. "
            "Modern bro-country adds programmed drums, heavy bass, and pop song structures. "
            "The vocal is always the star; production supports rather than overwhelms."
        ),
        "mix_character": "warm, mid-rich, acoustic clarity, vocal intimacy, pedal steel sits in the upper mid-range",

        # ── LYRIK & TEXTE ──
        "lyric_themes": [
            "small-town life", "truck and road", "love and marriage", "heartbreak and loss",
            "drinking and bars", "God and faith", "America and patriotism",
            "working-class pride", "nostalgia for the past", "family and roots",
            "nature and the land", "redemption and second chances"
        ],
        "lyric_style": (
            "Country lyrics are the genre's greatest strength — narrative-driven, specific, and cinematic. "
            "The story matters: characters have names, places are named, scenes are vivid. "
            "Humor, irony, and pathos coexist in the best lyrics. "
            "Universality is achieved through hyper-specific detail — the listener imagines themselves there."
        ),
        "language_register": "colloquial Southern/rural American, plain-spoken, honest, occasional biblical reference",
        "pov_typical": "first person singular; narrative third person in story songs",
        "rhyme_schemes": ["AABB", "ABAB", "ABCB (most common in country)"],
        "line_length": "medium, syllabically consistent for singability, often 8–10 syllables",

        # ── SONG-STRUKTUR ──
        "typical_structure": "Verse – Chorus – Verse – Chorus – Bridge – Chorus",
        "intro_style": "Acoustic guitar or steel guitar lick; establishes emotional tone; often 4–8 bars",
        "chorus_character": "Title-first hook, emotionally climactic, full band, broad singable melody",
        "bridge_role": "Delivers the lyrical twist or revelation; often chord change; emotional payoff before final chorus",
        "outro_style": "Final chorus repeat, instrumental steel fade, or quiet acoustic tag",

        # ── FUSION-KOMPATIBILITÄT ──
        "fuses_well_with": ["Rock", "Folk", "Blues", "Pop", "Bluegrass", "Gospel"],
        "fusion_tension_with": ["Metal", "Hip-Hop"],
        "bridge_elements": [
            "acoustic guitar and storytelling lyric (→ Folk)",
            "blue note and bottleneck guitar (→ Blues)",
            "pedal steel and open chord (→ Americana, Folk)",
            "backbeat and electric guitar (→ Rock)",
            "call-and-response vocal (→ Gospel)"
        ],

        # ── SUNO/UDIO PROMPT TAGS ──
        "suno_tags": [
            "country", "acoustic guitar", "pedal steel", "fiddle", "twang",
            "Nashville", "heartfelt", "storytelling", "country vocals", "banjo",
            "americana", "southern", "boots and dust", "warmth"
        ],
        "negative_tags": ["electronic beats", "808 bass", "distorted metal guitar", "synthesizer pad", "cold"],

        # ── EMOTIONALE DNA ──
        "emotional_spectrum": {
            "primary": ["nostalgia", "heartfelt sincerity", "pride"],
            "secondary": ["longing", "joy (community)", "grief"],
            "forbidden": ["ironic detachment", "coldness", "urban alienation"]
        },
        "listener_state": "The listener wants to feel grounded, moved by a story, or connected to roots — driving on a highway, sitting on a porch, at a bar.",
        "cultural_context": (
            "Country music grew from the folk and string band traditions of the rural American South and Appalachia, "
            "absorbing blues, gospel, and Western swing. It has been Nashville-centralized since the 1950s "
            "but retains regional variants in Texas, Oklahoma, and the West Coast. "
            "Its core mythology is working-class authenticity, land, and faith — a direct counterpoint to urban pop."
        ),

        # ── SUB-GENRES & VARIANTEN ──
        "sub_genres": {
            "Classic Country":   "Pre-1980 Nashville Sound; Hank Williams, Patsy Cline, Merle Haggard",
            "Outlaw Country":    "Raw, rebellious, Texas-rooted; Willie Nelson, Waylon Jennings, Kris Kristofferson",
            "Bluegrass":         "Acoustic acoustic, fast, intricate; Bill Monroe, Flatt & Scruggs, Alison Krauss",
            "Country Rock":      "Rock energy, country heart; Eagles, Marshall Tucker, Dwight Yoakam",
            "Americana":         "Roots-focused, anti-commercial; Townes Van Zandt, Jason Isbell, Brandi Carlile",
            "Bro-Country":       "Party-focused, modern production, stadium sound; Luke Bryan, Florida Georgia Line",
            "Country Pop":       "Nashville polish, pop crossover; Shania Twain, Taylor Swift (early), Kacey Musgraves",
            "Honky-Tonk":        "Bar-room style, two-step, shuffle beat; Ernest Tubb, Dwight Yoakam",
        },

        # ── REPRÄSENTATIVE KÜNSTLER ──
        "iconic_artists": [
            "Hank Williams", "Patsy Cline", "Johnny Cash", "Dolly Parton",
            "Willie Nelson", "Merle Haggard", "Waylon Jennings", "Loretta Lynn",
            "George Strait", "Kenny Rogers"
        ],
        "modern_artists": [
            "Kacey Musgraves", "Jason Isbell", "Chris Stapleton", "Zach Bryan", "Margo Price"
        ],

        # ── SONG-WRITING TIPPS ──
        "writing_tips": [
            "Start with a specific image or scene — the story must be visual and concrete",
            "Name the character, the bar, the town — specificity is authenticity",
            "The title should be the central metaphor or the most emotionally loaded phrase",
            "Use the bridge to reveal what the narrator truly feels or realizes",
            "Rhyme naturally — forced rhymes immediately break the spell of sincerity",
            "A great country song tells a complete story in 3 minutes — economy of language is prized",
            "Consider the perspective of the listener on a long drive — write for that quiet, reflective space"
        ],
        "avoid": [
            "Generic truck/beer references without authentic context",
            "Over-produced pop production that strips the warmth and grit",
            "Abandoning the storytelling tradition for pure hook-repetition",
            "Ignoring the harmonic color of the pedal steel — use it as an emotional narrator",
            "Lyrics that could be from any genre — country must feel like it could only be country"
        ],
    },

    "EDM": {
        # ── VIBES & ATMOSPHÄRE ──
        "vibes": [
            "euphoric", "hypnotic", "energetic", "transcendent", "danceable",
            "futuristic", "communal", "intense", "relentless", "liberating",
            "hedonistic", "massive"
        ],
        "anti_vibes": [
            "intimate-acoustic", "narrative-storytelling", "melancholic-slow",
            "gritty-raw", "organic", "complex lyricism", "quiet"
        ],

        # ── TONARTEN & HARMONIE ──
        "preferred_keys": ["A minor", "C major", "F major", "G major", "D minor", "Bb major"],
        "chord_progressions": [
            "i-VII-VI-VII (minor euphoria — house/trance)",
            "I-V-vi-IV (progressive house pop)",
            "i-iv-i-VII (dark techno loop)",
            "Single-chord or two-chord vamp (techno/minimal)",
            "I-IV-V (anthemic EDM chorus)",
            "i-bVI-bVII-i (trance build)",
            "Pedal point with moving upper harmony"
        ],
        "harmonic_feel": (
            "EDM harmony serves the drop — chords build tension through repetition and layering. "
            "Suspended chords and unresolved 7ths create anticipation during builds. "
            "The drop often strips harmony to bass + percussion, releasing tension. "
            "Melodic leads carry emotional weight above a rhythmic harmonic foundation."
        ),
        "modes": ["Aeolian", "Ionian", "Mixolydian", "Phrygian (dark techno)", "Dorian (funk-house)"],

        # ── RHYTHMUS & TEMPO ──
        "bpm_ranges": {
            "slow": "70-90",
            "mid":  "120-135",
            "fast": "145-180"
        },
        "time_signatures": ["4/4 (universal)", "3/4 (waltz house — rare)", "6/8 (DnB implied triplet)"],
        "rhythm_feel": (
            "EDM rhythm is machine-precise. The four-on-the-floor kick is the universal heartbeat. "
            "Off-beat hi-hats, syncopated percussion, and tension-release in the build/drop structure define the experience."
        ),
        "groove_type": "four-on-the-floor, syncopated percussion layers, programmed 100% grid or micro-quantized shuffle",

        # ── INSTRUMENTE & SOUND ──
        "core_instruments": [
            "synthesizer (lead, pad, bass)", "drum machine (kick, snare, hi-hat)",
            "sampler", "bass synthesizer", "vocoder/vocal chop"
        ],
        "optional_instruments": [
            "real guitar (chord stabs — house)", "piano (progressive house)", "brass samples",
            "live drums (hybrid EDM)", "strings (orchestral EDM)"
        ],
        "signature_sounds": [
            "supersaw lead synth (trance/progressive house)", "sidechain pumping compression",
            "white noise riser into drop", "sub-bass wobble (dubstep/trap)",
            "vocal chop arpeggiation", "kick with long sub-bass tail (techno)",
            "snare roll / crash cymbal into drop"
        ],
        "production_style": (
            "EDM production is entirely in-the-box and meticulous. The arrangement is a narrative "
            "of energy management — intro, builds, drops, breakdowns, and outros are precisely calibrated. "
            "Sidechain compression pumping against the kick is the genre's signature breath. "
            "Mix must translate perfectly on a club system — massive sub-bass, clear highs."
        ),
        "mix_character": "sub-bass dominant, wide stereo field, sidechain pump, sharp transients on kick, bright high synths",

        # ── LYRIK & TEXTE ──
        "lyric_themes": [
            "dancing and the night out", "euphoria and transcendence", "love and desire",
            "unity and collective experience", "freedom and escape", "raving and the moment",
            "hedonism and excess", "longing and separation", "motivational uplift",
            "futurism and technology", "spiritual release through music"
        ],
        "lyric_style": (
            "EDM lyrics are deliberately simple and universally interpretable — they function as "
            "melodic ingredients rather than literary content. "
            "Short repeated phrases, vowel-rich hooks, and emotionally direct sentiment work best. "
            "The vocal is often processed (vocoder, pitch-shift, chop) as a textural element."
        ),
        "language_register": "simple, direct, universal English; emotional keywords; repetition is intentional",
        "pov_typical": "first person or direct address 'you'; plural 'we' for unity anthems",
        "rhyme_schemes": ["AABB (simple hook)", "single phrase repeated", "syllabic chant over rhythm"],
        "line_length": "very short (3–7 syllables), sung on long notes; syllabic chant on percussion",

        # ── SONG-STRUKTUR ──
        "typical_structure": "Intro – Build 1 – Drop 1 – Breakdown – Build 2 – Drop 2 – Outro",
        "intro_style": "Atmospheric pad + filtered elements gradually introduced; builds tension over 32–64 bars",
        "chorus_character": "The DROP — maximum energy, full bass, full percussion, melodic hook at peak volume",
        "bridge_role": "Breakdown — strips elements for emotional breath; often vocal-only or pad-only",
        "outro_style": "Gradual element removal, filtered/high-pass fade; sometimes immediate cut",

        # ── FUSION-KOMPATIBILITÄT ──
        "fuses_well_with": ["Pop", "Hip-Hop", "R&B", "Latin", "Experimental", "Reggae"],
        "fusion_tension_with": ["Folk", "Classical acoustic", "Metal (except industrial)"],
        "bridge_elements": [
            "melodic vocal hook (→ Pop, R&B)",
            "rap verse over trap beat (→ Hip-Hop)",
            "Latin percussion pattern (→ Latin)",
            "reggaeton dembow rhythm (→ Latin, Reggae)",
            "orchestral sample/pad (→ Classical, Cinematic)"
        ],

        # ── SUNO/UDIO PROMPT TAGS ──
        "suno_tags": [
            "EDM", "electronic dance music", "synthesizer", "four-on-the-floor",
            "drop", "build-up", "sidechain", "bass drop", "euphoric",
            "club music", "synthesizer lead", "programmed drums", "festival",
            "dance floor", "supersaw"
        ],
        "negative_tags": ["acoustic guitar", "organic", "live drums only", "folk", "spoken word narrative"],

        # ── EMOTIONALE DNA ──
        "emotional_spectrum": {
            "primary": ["euphoria", "ecstasy", "release"],
            "secondary": ["longing", "energy", "unity"],
            "forbidden": ["melancholy introspection", "anger", "intellectual complexity"]
        },
        "listener_state": "The listener is (or wants to be) on a dancefloor or festival stage — peak physical and emotional energy, communal transcendence.",
        "cultural_context": (
            "EDM grew from Chicago house and Detroit techno in the 1980s, absorbed European rave culture, "
            "and exploded into a global billion-dollar festival industry. "
            "Ibiza, Berlin, and Amsterdam are cultural capitals. "
            "Sub-genre tribalism is intense — house heads, techno purists, and trance devotees see their "
            "genres as distinct identities. EDM as a term is often seen as a commercial umbrella."
        ),

        # ── SUB-GENRES & VARIANTEN ──
        "sub_genres": {
            "House":              "4/4 soulful; Chicago-born; Roland 909 kick; deep, tech, progressive variants; Frankie Knuckles, Daft Punk",
            "Techno":             "Functional, repetitive, industrial; Berlin-born; Robert Hood, Jeff Mills, Richie Hawtin",
            "Trance":             "Melodic, euphoric, 138–145 BPM; supersaw leads, arpeggios; Armin van Buuren, Tiësto",
            "Drum & Bass":        "170 BPM, syncopated Amen break, heavy basslines; LTJ Bukem, Goldie, Noisia",
            "Dubstep":            "140 BPM half-time, bass wobble; Benga, Skream, (brostep: Skrillex)",
            "Progressive House":  "Building melodic arcs, 128 BPM, emotional drops; Eric Prydz, Swedish House Mafia",
            "Electro House":      "Hard sidechained kick, electro bassline, mid-tempo; Daft Punk, Justice",
            "Future Bass":        "Lush chords, pitched vocal chops, emotional drops; Flume, San Holo, Marshmello",
        },

        # ── REPRÄSENTATIVE KÜNSTLER ──
        "iconic_artists": [
            "Daft Punk", "Kraftwerk", "Aphex Twin", "The Chemical Brothers",
            "Tiësto", "Armin van Buuren", "Deadmau5", "Fatboy Slim",
            "Carl Cox", "Jeff Mills"
        ],
        "modern_artists": [
            "Flume", "Fred again..", "Four Tet", "Disclosure", "Bicep"
        ],

        # ── SONG-WRITING TIPPS ──
        "writing_tips": [
            "Design the drop first — the entire track is a delivery system for that moment",
            "Use the build to create genuine sonic tension — automation, pitch risers, drum fills",
            "The vocal hook must work as a 2–4 bar loop; strip it to its essence",
            "Sidechain every melodic element to the kick for that pumping heartbeat feel",
            "Plan your frequency spectrum: bass owns 20–200Hz, leads live in 1–5kHz",
            "The breakdown is as important as the drop — emotional contrast makes the drop land harder",
            "Study club acoustics: what sounds huge in headphones must still work on 10kHz line array"
        ],
        "avoid": [
            "Complex lyrical content that competes with the musical experience",
            "Over-complicated arrangements that lose the dancefloor energy",
            "Weak drops — the payoff must be proportional to the buildup",
            "Ignoring the low-end — sub-bass is the physical experience of EDM",
            "Unquantized timing in the groove elements — precision is non-negotiable"
        ],
    },

    "Schlager": {
        # ── VIBES & ATMOSPHÄRE ──
        "vibes": [
            "nostalgic", "warm", "gemütlich", "sentimental", "joyful",
            "kitschy (self-aware)", "romantic", "celebratory", "heimelig",
            "bittersweet", "folksy", "communal sing-along"
        ],
        "anti_vibes": [
            "aggressively dark", "experimental-dissonant", "ironic-detached",
            "politically radical", "cold-electronic", "avant-garde", "urban-alienated"
        ],

        # ── TONARTEN & HARMONIE ──
        "preferred_keys": ["C major", "G major", "F major", "D major", "A major", "Bb major"],
        "chord_progressions": [
            "I-IV-V-I (Oom-pah Schlager)",
            "I-V-vi-IV (moderner Schlager)",
            "I-ii-V-I (Cabaret-influenced)",
            "I-IV-I-V-I (Volksmusik-style)",
            "I-bVII-IV-I (NDW-inflected)",
            "vi-IV-I-V (Neue Deutsche Welle)",
            "I-I-IV-V (simple Tanz-Schlager)"
        ],
        "harmonic_feel": (
            "Schlager harmony is fundamentally diatonic and emotionally immediate — dissonance is avoided "
            "or resolved instantly. Major keys dominate for celebration; minor used sparingly for pathos. "
            "Waltz-time harmonic rhythm (one chord per bar) is common in classic Schlager. "
            "Modern Schlager borrows pop progressions while retaining warm, full harmonic voicings."
        ),
        "modes": ["Ionian (major)", "Aeolian (selten, für Balladen)", "Mixolydian (NDW-Einfluss)"],

        # ── RHYTHMUS & TEMPO ──
        "bpm_ranges": {
            "slow": "60-80",
            "mid":  "100-128",
            "fast": "130-160"
        },
        "time_signatures": ["4/4", "3/4 (Walzer — klassischer Schlager)", "6/8"],
        "rhythm_feel": (
            "Klassischer Schlager hat einen wippenden, tänzerischen Groove — Oom-pah oder Oom-pah-pah. "
            "Moderner Schlager (nach 2000) adaptiert Pop-Rhythmik mit programmierten Beats, "
            "behält aber den zugänglichen, vorhersehbaren Schwung bei."
        ),
        "groove_type": "oom-pah (Blaskapelle), tanzbarer 4/4-Pop-Beat, Walzer-Dreier, Polka-Swing",

        # ── INSTRUMENTE & SOUND ──
        "core_instruments": [
            "Akkordeon oder Keyboard", "Melodie-Lead (Violine, Trompete oder Synthesizer)",
            "E-Bass oder Tuba", "Schlagzeug oder Drum-Computer", "Lead-Vocals"
        ],
        "optional_instruments": [
            "Blaskapelle (Trompete, Posaune, Tuba)", "Streicher (live oder Keyboard)",
            "Akustik-Gitarre", "Elektrische Gitarre (moderner Schlager)", "Backing Vocals (Chor)"
        ],
        "signature_sounds": [
            "Akkordeon-Melodie", "Oom-pah Tuba-Bass", "Geigen-Einwurf",
            "Blechbläser-Fills", "Jubelnder Chor-Refrain", "Synthesizer-Melodie (modern)"
        ],
        "production_style": (
            "Klassischer Schlager klingt orchestral und live, oft mit großem Orchester aufgenommen. "
            "Neue Deutsche Welle nutzte Synthesizer und minimale Produktion mit Ironie. "
            "Moderner Schlager (Helene Fischer-Ära) ist hochproduziert, EBU-laut, mit dramatischen "
            "Streichern, elektronischen Elementen und poliertem Vocal-Sound."
        ),
        "mix_character": "warm, midrange-betont, Streicher oben, Gesang zentral und klar, Tuba/Bass fundiert",

        # ── LYRIK & TEXTE ──
        "lyric_themes": [
            "Heimweh und Heimat", "romantische Liebe", "Sommer und Urlaub",
            "Feste und Feiern", "das einfache Leben", "Freundschaft und Gemeinschaft",
            "Tanzen und Ausgelassenheit", "verlorene Liebe mit Hoffnung",
            "Berge und Natur (besonders österreichisch-bayerisch)", "Lebensfreude",
            "Melancholie mit versöhnlichem Ende"
        ],
        "lyric_style": (
            "Schlager-Texte sind direkt, reimstark und emotional transparent. "
            "Metaphern sind vertraut und nie abstrakt — der Hörer soll sofort verstehen und mitsingen. "
            "Diminutivformen, Dialektwörter (österreichisch/bayerisch) und herzliche Anrede sind typisch. "
            "NDW-Texte können surreal oder ironisch sein (Nena, Falco). "
            "Moderner Schlager schreibt mit zeitgenössischem Selbstbewusstsein."
        ),
        "language_register": "alltagssprachlich-herzlich, Hochdeutsch mit regionalen Einsprengseln; NDW: ironisch-surreal",
        "pov_typical": "erste Person singular; direkte Anrede 'du'; Wir-Gefühl im Refrain",
        "rhyme_schemes": ["AABB", "ABAB", "ABCB", "AAAA (Refrain-Chant)"],
        "line_length": "mittel-kurz (6–9 Silben), singbar, oft daktylisch oder trochäisch",

        # ── SONG-STRUKTUR ──
        "typical_structure": "Strophe – Refrain – Strophe – Refrain – Bridge – Refrain (2×)",
        "intro_style": "Instrumentalthema (Melodie-Intro, 4–8 Takte); Bläser oder Akkordeon typisch",
        "chorus_character": "Breiter, jubelnder Refrain — Mitsinghook, einfache eingängige Melodie, voll besetzt",
        "bridge_role": "Modulationsbrücke oder emotionale Vertiefung; oft kurze Modulation nach Moll",
        "outro_style": "Wiederholung des Refrains, Ritardando zum Ende oder Fade-out; Bläser-Coda",

        # ── FUSION-KOMPATIBILITÄT ──
        "fuses_well_with": ["Pop", "Folk", "Classical", "Country (Americana)", "EDM (Eurodance)"],
        "fusion_tension_with": ["Metal", "Hip-Hop", "Experimental"],
        "bridge_elements": [
            "orchestrale Streicher (→ Classical, Pop)",
            "Akkordeon-Melodie (→ Folk, Weltmusik)",
            "Tanzbarer 4/4-Beat (→ Pop, EDM)",
            "einfache Diatonie (→ Country, Gospel)",
            "Bläser-Arrangement (→ Jazz, Brass Band)"
        ],

        # ── SUNO/UDIO PROMPT TAGS ──
        "suno_tags": [
            "schlager", "german pop", "accordion", "orchestral pop", "singalong",
            "waltz", "brass band", "melodic", "cheerful", "german vocals",
            "oom-pah", "folksy", "sentimental", "danceable", "Austria"
        ],
        "negative_tags": ["metal", "aggressive", "atonal", "hip-hop beat", "dark ambient"],

        # ── EMOTIONALE DNA ──
        "emotional_spectrum": {
            "primary": ["Freude", "Nostalgie", "Wärme"],
            "secondary": ["Sehnsucht", "Stolz", "Gemeinschaft"],
            "forbidden": ["Nihilismus", "Kälte", "aggressive Negativität"]
        },
        "listener_state": "Der Hörer will sich geborgen, ausgelassen oder nostalgisch fühlen — beim Volksfest, beim Tanzen, in Gesellschaft oder in Erinnerungen versunken.",
        "cultural_context": (
            "Schlager entstand in der deutschen Unterhaltungsmusik der 1920er–1950er Jahre als leichte, "
            "zugängliche Volksmusik für Radio und Tanzlokal. Die österreichisch-bayerische Variante "
            "integriert Blasmusik, Jodeln und Volksmusik. Die Neue Deutsche Welle (1980–84) brach "
            "den Schlager-Code mit Synthesizern und Ironie auf (Falco, Nena, Nina Hagen). "
            "Moderner Schlager (Helene Fischer, Andreas Gabalier) ist ein Milliardengeschäft — "
            "hochproduziert, festivaltauglich und international."
        ),

        # ── SUB-GENRES & VARIANTEN ──
        "sub_genres": {
            "Klassischer Schlager":      "1950er–70er Orchesterpop; Peter Alexander, Udo Jürgens, Freddy Quinn",
            "Volksmusik/Alpenrock":      "Bayerisch-österreichisch, Tracht, Blasmusik, Jodeln; Andreas Gabalier, Haindling",
            "Neue Deutsche Welle (NDW)": "1980–84, Synthesizer, Ironie, Englisch/Deutsch Mix; Falco, Nena, Trio",
            "Moderner Schlager":         "Post-2000 Hochproduktion, Stadion-Pop; Helene Fischer, Florian Silbereisen",
            "Eurodance-Schlager":        "EDM-Beats mit deutschem Schlager-Charme; DJ Ötzi, Atemlos",
            "Austropop":                 "Österreichischer Dialekt-Pop; Rainhard Fendrich, Georg Danzer, Wolfgang Ambros",
            "Discofox-Schlager":         "Tanzschulstyle, mittleres Tempo, 4/4; Semino Rossi, Andrea Berg",
        },

        # ── REPRÄSENTATIVE KÜNSTLER ──
        "iconic_artists": [
            "Udo Jürgens", "Helene Fischer", "Falco", "Nena", "Peter Alexander",
            "Roy Black", "Heino", "Marianne Rosenberg", "Roberto Blanco", "Costa Cordalis"
        ],
        "modern_artists": [
            "Helene Fischer", "Andreas Gabalier", "DJ Ötzi", "Andrea Berg", "Semino Rossi"
        ],

        # ── SONG-WRITING TIPPS ──
        "writing_tips": [
            "Der Refrain muss beim ersten Hören mitsingbar sein — Silben auf starke Zählzeiten",
            "Nutze klangvolle, warme Vokale (a, o, e) für die Hochpunkte der Melodie",
            "Erzähl von konkreten Momenten — Ortsangaben, Bilder, konkrete Erlebnisse",
            "Der Mitsingeffekt ist alles — mind. einen Phrase, die jeder nach einem Hören kennt",
            "Moduliere im letzten Refrain einen Halbton höher für emotionalen Schub",
            "Dialektwörter (beim österreichischen Schlager) schaffen Authentizität und Charme",
            "Einfache Reimpaare — erzwungene oder überraschende Reime wirken unecht"
        ],
        "avoid": [
            "Zu komplexe Harmonik oder unerwartete Akkordwechsel — Vorhersehbarkeit ist Tugend",
            "Zynismus oder Ironie (außer NDW — dort ist es Stilmittel)",
            "Zu abstraktes oder intellektuelles Textmaterial",
            "Beats oder Sounds, die das behagliche Grundgefühl zerstören",
            "Englische Texte für den klassischen Schlager — deutsche Sprache ist identitätsstiftend"
        ],
    },

    "Classical": {
        # ── VIBES & ATMOSPHÄRE ──
        "vibes": [
            "majestic", "transcendent", "intellectual", "emotional depth",
            "timeless", "dramatic", "serene", "complex", "spiritual",
            "powerful", "intimate", "architectural"
        ],
        "anti_vibes": [
            "disposable", "repetitive-simple", "gimmicky", "commercial-shallow",
            "rhythmically monotonous (without purpose)", "lyrically trivial", "improvised-casual"
        ],

        # ── TONARTEN & HARMONIE ──
        "preferred_keys": [
            "C major", "G major", "D major", "F major", "Bb major",
            "C minor", "G minor", "D minor", "A minor"
        ],
        "chord_progressions": [
            "I-IV-V-I (Tonal cadence)",
            "ii-V-I (Standard cadence)",
            "I-vi-IV-V (Classical period)",
            "Neapolitan 6th → V7 → I (dramatic)",
            "Augmented 6th chords (It6, Ger6, Fr6)",
            "Circle of 5ths progression",
            "Chromatic mediant (Romantic period)",
            "12-tone row (20th century)"
        ],
        "harmonic_feel": (
            "Classical harmony follows the rigorous grammar of functional tonality in Baroque and Classical periods — "
            "every dissonance is prepared and resolved. The Romantic period expands chromaticism dramatically, "
            "using distant key relationships and ambiguous tonality. Modern/contemporary classical ranges from "
            "neo-tonal to fully atonal, spectral, and microtonally-explored territory."
        ),
        "modes": [
            "All major and minor scales", "Church modes (Baroque polyphony)", "Dorian", "Phrygian",
            "Whole-tone scale (Debussy)", "Octatonic/diminished (20th c.)", "12-tone serialism"
        ],

        # ── RHYTHMUS & TEMPO ──
        "bpm_ranges": {
            "slow": "40-66",
            "mid":  "80-120",
            "fast": "132-200"
        },
        "time_signatures": ["4/4", "3/4", "6/8", "2/2", "5/4", "7/4", "complex mixed meters (20th c.)"],
        "rhythm_feel": (
            "Classical rhythm is shaped by phrasing and breath — not groove. "
            "Tempo is expressive (rubato in Romantic), metrically strict in Baroque dance forms. "
            "Rhythmic drama is achieved through hemiola, syncopation, and metric displacement."
        ),
        "groove_type": "non-groove — phrase-driven, rubato, tempo fluctuation as expressive tool",

        # ── INSTRUMENTE & SOUND ──
        "core_instruments": [
            "strings (violin, viola, cello, double bass)", "woodwinds (flute, oboe, clarinet, bassoon)",
            "brass (horn, trumpet, trombone, tuba)", "piano/harpsichord", "timpani/percussion"
        ],
        "optional_instruments": [
            "organ (Baroque, sacred)", "choir/voice", "harp", "guitar (Classical guitar solo)",
            "extended orchestra instruments (saxophone — 20th c.)"
        ],
        "signature_sounds": [
            "string section tutti attack", "legato woodwind melody over pizzicato strings",
            "piano sustain pedal harmonic wash", "brass chorale chord",
            "timpani roll crescendo", "harpsichord continuo (Baroque)",
            "soprano coloratura (opera)"
        ],
        "production_style": (
            "Classical recording prioritizes acoustic authenticity — minimal processing, natural room acoustics, "
            "microphone placement for tonal balance without compression or limiting. "
            "The hall or church acoustic is part of the instrument. "
            "Dynamic range is preserved; no loudness war. Contemporary classical may use electronics as compositional element."
        ),
        "mix_character": "wide, natural room reverb, full dynamic range, no compression, spatial depth front-to-back",

        # ── LYRIK & TEXTE ──
        "lyric_themes": [
            "nature and its drama", "mythology and legend", "divine and spiritual",
            "love (both earthly and transcendent)", "death and immortality",
            "heroism and tragedy", "political idealism (Beethoven era)",
            "inner psychological states (Romantic Lied)", "folk tales and nationalism",
            "abstract emotion without narrative (pure instrumental)"
        ],
        "lyric_style": (
            "When text is present (Lied, opera, choral), it is literary — often settings of great poetry "
            "(Goethe, Schiller, Heine, Shakespeare). The music amplifies and interprets the text's meaning, "
            "with word-painting a compositional technique (text-music relationship). "
            "Opera text (libretto) uses elevated theatrical language; oratorios use biblical or sacred texts."
        ),
        "language_register": "literary, elevated, often archaic or poetic; Latin in sacred works; vernacular in folk-influenced Lieder",
        "pov_typical": "third person narrative (opera, oratorio) or introspective first person (Lied, art song)",
        "rhyme_schemes": ["ABAB (Lied poetry)", "terza rima (opera — Italian)", "free verse (20th c. art song)"],
        "line_length": "variable — determined by poetic meter; classical prosody governs syllable stress",

        # ── SONG-STRUKTUR ──
        "typical_structure": "Sonata Form / Theme-and-Variations / Rondo / Strophic (Lied) / Through-composed",
        "intro_style": "Slow introduction (orchestral) or direct thematic statement; Baroque begins with continuo texture",
        "chorus_character": "Recapitulation (sonata) or refrain (rondo) — return of primary theme, often in tonic, with full orchestration",
        "bridge_role": "Development section (sonata form) — the primary site of harmonic adventure and motivic transformation",
        "outro_style": "Coda — thematic resolution, scale runs, plagal or perfect authentic cadence; often dramatic final gesture",

        # ── FUSION-KOMPATIBILITÄT ──
        "fuses_well_with": ["Jazz", "Metal (Symphonic)", "Folk", "Experimental", "Film Score"],
        "fusion_tension_with": ["Hip-Hop", "EDM (pure)", "Schlager (naively)"],
        "bridge_elements": [
            "harmonic language and voice leading (→ Jazz, Pop sophisticated harmony)",
            "orchestral arrangement (→ Metal symphonic, Film Score)",
            "motivic development technique (→ Progressive Rock, Metal)",
            "contrapuntal texture (→ Jazz, Experimental)",
            "formal structures (→ Art Pop, Progressive)"
        ],

        # ── SUNO/UDIO PROMPT TAGS ──
        "suno_tags": [
            "classical", "orchestral", "strings", "piano", "symphony",
            "chamber music", "dramatic", "majestic", "emotional depth",
            "baroque", "romantic era", "concert hall", "no drums", "acoustic"
        ],
        "negative_tags": ["drum machine", "808 bass", "distorted guitar", "hip-hop beat", "auto-tune"],

        # ── EMOTIONALE DNA ──
        "emotional_spectrum": {
            "primary": ["awe", "deep emotion", "intellectual satisfaction"],
            "secondary": ["grief", "triumph", "serenity"],
            "forbidden": ["banality", "disposability", "ironic detachment"]
        },
        "listener_state": "The listener wants to experience the full range of human emotion through pure sound — in a concert hall, in contemplation, or in a transcendent moment.",
        "cultural_context": (
            "Western classical music is a 1,000-year tradition from Gregorian chant through polyphony, "
            "tonal harmony, Romantic expansion, and 20th-century fragmentation. "
            "It carries institutional authority (conservatories, orchestras, opera houses) and cultural capital. "
            "Its global influence is immense — Japanese, Korean, and Chinese musicians now lead world stages. "
            "Contemporary classical continues to evolve in dialogue with electronics, jazz, and global music."
        ),

        # ── SUB-GENRES & VARIANTEN ──
        "sub_genres": {
            "Baroque":          "Contrapuntal, ornate, basso continuo; Bach, Handel, Vivaldi, Telemann (1600–1750)",
            "Klassik (Wiener)": "Formal clarity, sonata form, chamber music; Haydn, Mozart, Beethoven (1750–1820)",
            "Romantik":         "Emotional expansion, chromaticism, tone poems; Brahms, Chopin, Schubert, Wagner (1820–1900)",
            "Impressionismus":  "Color, texture, modal harmony; Debussy, Ravel, early Bartók (1890–1920)",
            "Moderne":          "Atonality, serialism, neo-classicism; Schoenberg, Stravinsky, Prokofiev (1900–1960)",
            "Zeitgenössisch":   "Spectral, minimal, post-minimalist, electronic; Arvo Pärt, Sofia Gubaidulina, Thomas Adès",
            "Minimalismus":     "Repetition with gradual change; Philip Glass, Steve Reich, John Adams",
            "Kammermusik":      "String quartet, piano trio, intimate ensemble; from Haydn to contemporary",
        },

        # ── REPRÄSENTATIVE KÜNSTLER ──
        "iconic_artists": [
            "Johann Sebastian Bach", "Wolfgang Amadeus Mozart", "Ludwig van Beethoven",
            "Johannes Brahms", "Frédéric Chopin", "Pyotr Tchaikovsky",
            "Claude Debussy", "Igor Stravinsky", "Richard Wagner", "Franz Schubert"
        ],
        "modern_artists": [
            "Arvo Pärt", "Philip Glass", "Thomas Adès", "Max Richter", "Nico Muhly"
        ],

        # ── SONG-WRITING TIPPS ──
        "writing_tips": [
            "Establish a clear primary theme (Hauptthema) — every development must grow from it",
            "Use counterpoint — two independent melodic lines create richer texture than melody + chords",
            "Dynamic contrast is form — the architecture of loud and soft IS the emotional narrative",
            "Harmonic rhythm (how often chords change) controls tension — slower harmonic rhythm = more tension",
            "The development section should take the listener somewhere unexpected and return convincingly",
            "Study voice leading — every note transition should be purposeful, smooth, or dramatically dissonant",
            "In vocal writing: honor the natural stress patterns of the language in note lengths"
        ],
        "avoid": [
            "Over-orchestration — silence and sparse texture are as powerful as full tutti",
            "Neglecting form — beautiful material without structural logic doesn't sustain attention",
            "Ignoring the instrument's natural idiom — write idiomatically for each voice",
            "Harmonic stasis — even pedal points need melodic movement above them",
            "Copying period surface features (harpsichord sound) without understanding the underlying grammar"
        ],
    },

    "Jazz": {
        # ── VIBES & ATMOSPHÄRE ──
        "vibes": [
            "sophisticated", "spontaneous", "cool", "intellectual", "sensual",
            "nocturnal", "introspective", "joyful (swing)", "melancholic",
            "improvisational", "conversational", "urban"
        ],
        "anti_vibes": [
            "rigidly predictable", "over-compressed", "simplistic", "rural",
            "aggressive (non-free)", "saccharine", "repetitive without development"
        ],

        # ── TONARTEN & HARMONIE ──
        "preferred_keys": [
            "Bb major", "Eb major", "F major", "C major", "Ab major",
            "G major", "D minor", "G minor"
        ],
        "chord_progressions": [
            "ii-V-I (the DNA of jazz)",
            "I-vi-ii-V (rhythm changes) ",
            "I-IV-I-V-I (blues form, 12-bar)",
            "iii-VI-ii-V (turnaround)",
            "I-bVII7-IV (modal jazz vamp)",
            "Giant Steps cycle (Coltrane changes)",
            "Rhythm Changes (Bb, AABA form)"
        ],
        "harmonic_feel": (
            "Jazz harmony is the most sophisticated in popular music — extended chords (7ths, 9ths, 11ths, 13ths), "
            "altered dominants (b9, #9, b13), substitutions (tritone sub), and reharmonization are standard vocabulary. "
            "The ii-V-I progression is the gravitational center of all tonal jazz. "
            "Modal jazz moves away from functional progression into pure modal color and improvisation."
        ),
        "modes": [
            "Dorian (ii chord)", "Mixolydian (V chord)", "Lydian (IV chord)",
            "Locrian (ii° chord)", "Altered scale (V7alt)", "Bebop scale",
            "Whole-tone", "Diminished (octatonic)", "Lydian Dominant"
        ],

        # ── RHYTHMUS & TEMPO ──
        "bpm_ranges": {
            "slow": "40-70",
            "mid":  "100-160",
            "fast": "200-350"
        },
        "time_signatures": ["4/4", "3/4 (jazz waltz)", "5/4", "7/4", "6/8", "odd meter (post-bop)"],
        "rhythm_feel": (
            "The jazz feel is defined by swing — the subdivision of beats into a long-short triplet pattern "
            "that creates a characteristic lilt. Straight-eighth feel is used in bossa nova, fusion, and post-bop. "
            "The rhythm section (piano, bass, drums) is a collective conversation, not a static backdrop."
        ),
        "groove_type": "swung 8ths (traditional/bebop), straight 8ths (bossa/fusion), polyrhythmic (post-bop/free)",

        # ── INSTRUMENTE & SOUND ──
        "core_instruments": [
            "jazz drums (ride cymbal, brushes)", "upright bass (or electric in fusion)",
            "piano or organ (Hammond B3)", "saxophone (alto, tenor, soprano)",
            "trumpet or flugelhorn"
        ],
        "optional_instruments": [
            "jazz guitar (archtop, clean)", "vibraphone", "trombone",
            "violin (gypsy jazz)", "clarinet (New Orleans, klezmer-jazz)"
        ],
        "signature_sounds": [
            "ride cymbal 'ding-da-ding' jazz pattern", "walking bass line",
            "piano comping (sparse, syncopated)", "saxophone with vibrato and bends",
            "trumpet harmon mute (Miles Davis)", "brushed snare whisper texture"
        ],
        "production_style": (
            "Jazz recording values authenticity of acoustic performance — live ensemble playing, natural room sound, "
            "and minimal editing. Classic jazz recordings (Blue Note, Impulse!) are warm, intimate, and slightly compressed. "
            "Fusion jazz uses electric instruments and studio production. "
            "Contemporary jazz spans all production styles from pure acoustic to electronic hybrid."
        ),
        "mix_character": "intimate, warm, natural reverb, midrange-rich, drums in the room not triggered, bass felt",

        # ── LYRIK & TEXTE ──
        "lyric_themes": [
            "romantic love and longing", "urban night life", "travel and wandering",
            "loss and nostalgia", "joy and celebration (swing)", "social commentary (protest jazz)",
            "nature and seasons", "spiritual yearning", "solitude and reflection",
            "the music itself (jazz about jazz)", "rain and weather as metaphor"
        ],
        "lyric_style": (
            "Jazz lyrics carry a literary quality — poetic imagery, metaphor, and the American Songbook tradition "
            "of elegant understatement. Melody determines phrasing; lyrics breathe with the horn-like vocal line. "
            "Scat singing bypasses words entirely, using the voice as instrument. "
            "Blues-influenced jazz uses plain-spoken double meanings and earthier language."
        ),
        "language_register": "literary-elegant (standards), vernacular (blues-jazz), abstract (scat/vocalese)",
        "pov_typical": "first person longing or reflection; direct address to 'you' in ballads",
        "rhyme_schemes": ["AABA (standard song form — 32 bars)", "ABAB", "AAB (blues couplet)"],
        "line_length": "follows melodic phrase — medium, shaped by harmonic rhythm; breath and pause are structural",

        # ── SONG-STRUKTUR ──
        "typical_structure": "Head (melody) – Solos (chorus improvisations) – Head (out) | AABA or ABAB 32-bar form",
        "intro_style": "Piano or bass intro; sometimes band tutti intro; often begins with the melody directly",
        "chorus_character": "The head (melody) returns — familiar, but varied by soloist's interpretation; emotional peak",
        "bridge_role": "The B section of AABA — harmonic adventure, key change, rhythmic intensification before return to A",
        "outro_style": "Final head, ritard, tag (last 4 bars repeated), or sudden stop; sometimes solo piano or bass tag",

        # ── FUSION-KOMPATIBILITÄT ──
        "fuses_well_with": ["Blues", "Classical", "Hip-Hop", "R&B", "Latin", "Experimental"],
        "fusion_tension_with": ["Metal", "Schlager", "Country (traditional)"],
        "bridge_elements": [
            "ii-V-I harmonic movement (→ Pop sophisticated, R&B, Classical)",
            "swing rhythm (→ Blues, Gospel, Big Band)",
            "improvisation concept (→ Experimental, Prog Rock)",
            "Latin clave (→ Latin Jazz, Bossa Nova)",
            "sampled jazz chords (→ Hip-Hop, lo-fi)"
        ],

        # ── SUNO/UDIO PROMPT TAGS ──
        "suno_tags": [
            "jazz", "saxophone", "upright bass", "swing", "bebop",
            "jazz piano", "walking bass", "trumpet", "ride cymbal", "improvisation",
            "cool jazz", "jazz standard", "blue note", "nocturnal", "smoky bar"
        ],
        "negative_tags": ["distorted guitar", "808 bass", "drum machine quantized", "EDM synth", "auto-tune"],

        # ── EMOTIONALE DNA ──
        "emotional_spectrum": {
            "primary": ["sophistication", "longing", "joy (swing)"],
            "secondary": ["melancholy", "sensuality", "intellectual delight"],
            "forbidden": ["naïveté", "brashness", "emotional superficiality"]
        },
        "listener_state": "The listener is in a contemplative, sophisticated, or sensually aware state — late evening, cocktail in hand, or deeply attentive to musical craft.",
        "cultural_context": (
            "Jazz was born in New Orleans around 1900 from the convergence of African rhythms, blues, "
            "European harmony, and the American experience. It is the foundational American art form — "
            "a music of freedom, improvisation, and collective creation. "
            "Jazz gave birth to R&B, rock, and hip-hop. Its intellectual and emotional depth has made it "
            "the music of academic study and devoted connoisseurship globally."
        ),

        # ── SUB-GENRES & VARIANTEN ──
        "sub_genres": {
            "Swing/Big Band":    "Large ensemble, arranged, danceable; Count Basie, Duke Ellington, Benny Goodman",
            "Bebop":             "Fast, complex, small group, anti-commercial; Charlie Parker, Dizzy Gillespie, Thelonious Monk",
            "Cool Jazz":         "Relaxed, understated, lyrical; Miles Davis (Birth of the Cool), Dave Brubeck, Chet Baker",
            "Hard Bop":          "Blues-rooted, soulful bebop; Art Blakey, Clifford Brown, Horace Silver",
            "Modal Jazz":        "Mode-based, open, free-flowing; Miles Davis (Kind of Blue), John Coltrane (A Love Supreme)",
            "Free Jazz":         "Avant-garde, no fixed harmony/tempo; Ornette Coleman, Albert Ayler",
            "Fusion":            "Jazz + rock/funk, electric instruments; Miles Davis (Bitches Brew), Weather Report, Mahavishnu Orchestra",
            "Latin Jazz":        "Afro-Cuban and Brazilian rhythms + jazz harmony; Dizzy Gillespie, Chucho Valdés, Irakere",
        },

        # ── REPRÄSENTATIVE KÜNSTLER ──
        "iconic_artists": [
            "Miles Davis", "John Coltrane", "Duke Ellington", "Charlie Parker",
            "Thelonious Monk", "Billie Holiday", "Louis Armstrong", "Ella Fitzgerald",
            "Bill Evans", "Charles Mingus"
        ],
        "modern_artists": [
            "Kamasi Washington", "Esperanza Spalding", "Robert Glasper", "Nubya Garcia", "Snarky Puppy"
        ],

        # ── SONG-WRITING TIPPS ──
        "writing_tips": [
            "Know the ii-V-I in every key — it is the fundamental movement of all jazz writing",
            "Write for the improviser: leave harmonic space and avoid over-specifying melody",
            "Compose melodies that suggest the underlying harmony without spelling it out",
            "Think in 8-bar phrases; AABA form creates natural tension-release-tension-resolution",
            "Voice chords in fourths and seconds for modern jazz sound (post-McCoy Tyner)",
            "The bass line carries as much melody as the horns — give it a life of its own",
            "Silence is an improviser's tool — not every beat needs to be filled"
        ],
        "avoid": [
            "Over-specifying every note — jazz needs breathing room for interpretation",
            "Forcing bebop complexity onto a lyrical ballad",
            "Ignoring the rhythm section conversation — it's not accompaniment, it's dialogue",
            "Quantizing jazz piano or drum performances — the micro-timing IS the feel",
            "Writing solos note-for-note rather than providing a harmonic map"
        ],
    },

    "Blues": {
        # ── VIBES & ATMOSPHÄRE ──
        "vibes": [
            "soulful", "raw", "melancholic", "cathartic", "authentic",
            "gutsy", "longing", "earthly", "sexual tension", "resigned wisdom",
            "late-night", "intimate"
        ],
        "anti_vibes": [
            "superficial", "over-polished", "cold-electronic", "rigid", "joyless-without-soul",
            "overly complex (without feeling)", "inauthentic"
        ],

        # ── TONARTEN & HARMONIE ──
        "preferred_keys": ["E major", "A major", "B minor", "G major", "C major", "D major"],
        "chord_progressions": [
            "I-IV-V-I (12-bar blues)",
            "I7-I7-I7-I7 / IV7-IV7-I7-I7 / V7-IV7-I7-V7 (standard 12-bar)",
            "I-IV-I-V-IV-I (8-bar blues)",
            "I7-bVII7-IV7-I7 (Texas shuffle variant)",
            "i7-iv7-V7 (minor blues)",
            "Quick IV in bar 2 variant",
            "Jazz-blues with II-V-I turnaround"
        ],
        "harmonic_feel": (
            "Blues harmony revolves around dominant 7th chords — even the I chord is a dominant 7, "
            "creating perpetual unresolved tension that is the genre's emotional core. "
            "Blue notes (flattened 3rd, 5th, 7th) exist in the crack between major and minor, "
            "giving blues its uniquely human, bending vocal and guitar expression."
        ),
        "modes": ["Blues scale", "Pentatonic minor over dominant 7ths", "Mixolydian", "Dorian (minor blues)"],

        # ── RHYTHMUS & TEMPO ──
        "bpm_ranges": {
            "slow": "40-65",
            "mid":  "80-120",
            "fast": "140-200"
        },
        "time_signatures": ["4/4", "12/8 (shuffle/triplet feel)", "6/8"],
        "rhythm_feel": (
            "The blues shuffle (long-short swing) is the quintessential feel — triplet subdivision with "
            "accented off-beats. Slow blues breathes deeply; Chicago blues drives relentlessly forward."
        ),
        "groove_type": "shuffle (triplet swing), boogie woogie (left-hand piano pattern), straight Chicago drive",

        # ── INSTRUMENTE & SOUND ──
        "core_instruments": [
            "electric guitar (often slide)", "vocals", "harmonica",
            "piano or B3 organ", "upright or electric bass"
        ],
        "optional_instruments": [
            "horns (trumpet, sax — Chicago blues)", "drums (shuffle or straight)",
            "acoustic guitar (Delta blues)", "washboard (early blues)"
        ],
        "signature_sounds": [
            "bent guitar note with vibrato", "harmonica bent draw note",
            "tube amp overdrive (natural breakup)", "slide guitar glissando",
            "piano boogie-woogie left hand", "call-and-response between vocal and guitar",
            "stop-time breaks"
        ],
        "production_style": (
            "Delta and early blues is raw and live — often mono recordings with room noise, vocal distortion. "
            "Chicago electric blues (Chess Records sound) is punchy, mid-forward, with warm room ambience. "
            "British blues and Southern rock variations add more production polish. "
            "The key is authentic imperfection — the human breath, the string squeak, the amp hum."
        ),
        "mix_character": "raw, mid-forward, natural harmonic distortion, vocal very present, no sterile sheen",

        # ── LYRIK & TEXTE ──
        "lyric_themes": [
            "heartbreak and infidelity", "poverty and hardship", "travel and leaving",
            "supernatural and the devil", "sexual desire and tension", "alcohol and addiction",
            "racial injustice (coded)", "loneliness and isolation", "death and mortality",
            "work and labor", "redemption and faith", "natural disaster (floods, drought)"
        ],
        "lyric_style": (
            "Blues lyrics use the AAB couplet form — the first line is stated, repeated (with variation), "
            "then answered in a third line. This call-and-response structure mirrors the guitar-vocal conversation. "
            "Plain-spoken, direct, and often deeply metaphorical in oblique ways. "
            "Double entendres and coded language are historical staples. "
            "The singer speaks from direct personal experience — first-person witness."
        ),
        "language_register": "vernacular African American English, direct, plain-spoken, earthy, coded metaphor",
        "pov_typical": "first person; direct, personal — 'I woke up this morning'",
        "rhyme_schemes": ["AAB (blues couplet with repeated A line)", "AABB (popular blues ballad)"],
        "line_length": "medium, phrase-based — follows the vocal breath; the repeated A line often varied in delivery",

        # ── SONG-STRUKTUR ──
        "typical_structure": "12-bar blues form (repeating) | 8-bar blues | 16-bar blues",
        "intro_style": "Guitar or harmonica riff establishing the shuffle; sometimes unaccompanied solo",
        "chorus_character": "The refrain emerges from the AAB lyric cycle — often the B line contains the title/hook",
        "bridge_role": "Instrumental solo break (guitar/harmonica) serves as the bridge — emotional statement without words",
        "outro_style": "Turnaround phrase back to the top, or slow fade; tag with final guitar flourish",

        # ── FUSION-KOMPATIBILITÄT ──
        "fuses_well_with": ["Rock", "Jazz", "Country", "R&B", "Gospel", "Folk"],
        "fusion_tension_with": ["EDM (pure)", "Classical (atonal)", "Hip-Hop (without samples)"],
        "bridge_elements": [
            "12-bar form and blues scale (→ Rock, Country, Jazz)",
            "call-and-response vocal-instrument (→ Gospel, R&B)",
            "bent note guitar technique (→ Rock, Country)",
            "dominant 7th harmony (→ Jazz, Funk, R&B)",
            "raw vocal delivery (→ Soul, Gospel, R&B)"
        ],

        # ── SUNO/UDIO PROMPT TAGS ──
        "suno_tags": [
            "blues", "electric guitar", "harmonica", "shuffle", "12-bar blues",
            "soulful", "raw vocals", "slide guitar", "boogie", "tube amp",
            "Chicago blues", "Delta blues", "call and response", "bent notes"
        ],
        "negative_tags": ["electronic beats", "synthesizer pad", "clean digital production", "pop chorus", "auto-tune"],

        # ── EMOTIONALE DNA ──
        "emotional_spectrum": {
            "primary": ["sorrow", "catharsis", "longing"],
            "secondary": ["resilience", "desire", "rueful humor"],
            "forbidden": ["innocence", "over-polish", "emotional superficiality"]
        },
        "listener_state": "The listener wants to process pain or desire through the recognition of shared human suffering — the blues externalizes interior feeling.",
        "cultural_context": (
            "Blues is the root of virtually all American popular music — it gave birth to jazz, rock, R&B, "
            "country, and hip-hop. Born from African American experience in the Deep South post-slavery, "
            "it carries the entire weight of that history in its bends and cries. "
            "The Delta, Chicago, and Texas traditions each developed distinct regional voices. "
            "The British Invasion carried blues to global audiences; today it's a living international tradition."
        ),

        # ── SUB-GENRES & VARIANTEN ──
        "sub_genres": {
            "Delta Blues":       "Raw, solo acoustic, slide guitar; Robert Johnson, Son House, Charley Patton",
            "Chicago Blues":     "Electric, band format, urban grit; Muddy Waters, Howlin' Wolf, Little Walter",
            "Texas Blues":       "Soulful, sophisticated, single-string lead; Stevie Ray Vaughan, T-Bone Walker",
            "Piedmont Blues":    "Ragtime-influenced, fingerpicking, East Coast; Rev. Gary Davis, Blind Blake",
            "British Blues":     "American blues filtered through rock; John Mayall, Clapton, Peter Green",
            "Soul Blues":        "R&B crossover, horns, emotional; Bobby Bland, B.B. King, Albert King",
            "Blues Rock":        "High-energy, rock production; Hendrix, ZZ Top, The Black Keys",
        },

        # ── REPRÄSENTATIVE KÜNSTLER ──
        "iconic_artists": [
            "Robert Johnson", "Muddy Waters", "B.B. King", "Howlin' Wolf",
            "Bessie Smith", "Son House", "John Lee Hooker", "Buddy Guy",
            "Stevie Ray Vaughan", "T-Bone Walker"
        ],
        "modern_artists": [
            "Gary Clark Jr.", "Joe Bonamassa", "Tedeschi Trucks Band", "Marcus King", "Christone 'Kingfish' Ingram"
        ],

        # ── SONG-WRITING TIPPS ──
        "writing_tips": [
            "Live in the 12-bar form — learn to tell a complete story in its 3-section structure",
            "The repeated A line is not lazy — vary the delivery, timing, and note choice",
            "The B response line should surprise, answer, or deepen the A line's meaning",
            "Write from personal truth — blues that isn't felt is heard as fake immediately",
            "The guitar/harmonica is a second voice — compose the instrumental response to the vocal",
            "Use blue notes (b3, b5, b7) as melodic tension points, not just generic decoration",
            "Slow blues especially — take your time; silence between phrases is as expressive as the notes"
        ],
        "avoid": [
            "Over-production that removes the rawness — distortion and breath are essential",
            "Forcing rhymes at the expense of the natural conversational feel",
            "Playing too many notes in the solo — space and silence define great blues guitar",
            "Ignoring the shuffle feel — straight 8ths rarely capture the blues spirit",
            "Surface-level 'sad lyrics' without the specific emotional authenticity of the tradition"
        ],
    },

    "Folk": {
        # ── VIBES & ATMOSPHÄRE ──
        "vibes": [
            "intimate", "authentic", "storytelling", "nostalgic", "earthy",
            "melancholic", "communal", "timeless", "quiet strength", "pastoral",
            "vulnerable", "acoustic warmth"
        ],
        "anti_vibes": [
            "over-produced", "aggressive", "electronic-cold", "superficial",
            "danceable-without-story", "glossy", "rhythmically dominant"
        ],

        # ── TONARTEN & HARMONIE ──
        "preferred_keys": ["G major", "D major", "C major", "A minor", "E minor", "Dm"],
        "chord_progressions": [
            "I-IV-V-I",
            "I-V-vi-IV",
            "i-VII-VI-VII (modal folk)",
            "I-ii-IV-V",
            "I-bVII-IV (Mixolydian folk)",
            "i-VI-III-VII (Dorian folk)",
            "I-IV-I-V (simple 4-chord)"
        ],
        "harmonic_feel": (
            "Folk harmony is open and often modal — Dorian and Mixolydian modes give traditional folk its "
            "distinctively non-pop sound. Capo and open tunings create ringing sympathetic resonance. "
            "Chords are often voiced simply; the acoustic guitar's natural resonance fills the harmonic space. "
            "Drone strings and pedal tones are common in Celtic and Appalachian variants."
        ),
        "modes": ["Ionian", "Dorian", "Mixolydian", "Aeolian", "Pentatonic (Anglo-American)", "Lydian (Celtic)"],

        # ── RHYTHMUS & TEMPO ──
        "bpm_ranges": {
            "slow": "50-75",
            "mid":  "80-120",
            "fast": "130-180"
        },
        "time_signatures": ["4/4", "3/4 (waltz, Celtic jig base)", "6/8", "9/8 (slip jig)"],
        "rhythm_feel": (
            "Folk rhythm is human and breath-led. Strumming patterns are varied and often picked. "
            "Dance tunes (jigs, reels, polkas) have a distinct rhythmic lilt; "
            "ballads breathe with the lyric."
        ),
        "groove_type": "fingerpicked or strummed acoustic, breath-led, Celtic dance lilt, simple back-beat in contemporary folk",

        # ── INSTRUMENTE & SOUND ──
        "core_instruments": [
            "acoustic guitar (steel-string or nylon)", "vocals", "acoustic bass or upright bass",
            "fiddle", "banjo or mandolin"
        ],
        "optional_instruments": [
            "dulcimer", "bodhrán (frame drum)", "tin whistle/flute",
            "harmonica", "accordion (Celtic, Cajun)", "piano"
        ],
        "signature_sounds": [
            "open-tuned acoustic guitar resonance", "fingerpicking pattern",
            "fiddle ornamentation (cuts, rolls)", "vocal harmony in thirds or fourths",
            "bodhrán hand drum texture", "unaccompanied a cappella verse"
        ],
        "production_style": (
            "Folk recording values intimacy and honesty — close-mic'd acoustic instruments, "
            "minimal reverb or natural room sound, and audible breathing and string noise. "
            "Contemporary folk-pop adds light production with loops and subtle electronics. "
            "The vocal must feel like the singer is in the room with the listener."
        ),
        "mix_character": "intimate, warm, close-mic'd acoustic, vocals very present, natural room noise welcome",

        # ── LYRIK & TEXTE ──
        "lyric_themes": [
            "love and loss", "historical events and social protest", "nature and seasons",
            "migration and displacement", "death and mourning", "community and tradition",
            "mythology and folklore", "labor and working life", "political injustice",
            "personal journey and self-discovery", "spiritual questioning", "the sea and travel"
        ],
        "lyric_style": (
            "Folk lyrics are narrative-driven and often ballad-structured — they tell a story from beginning "
            "to end with economy and clarity. Imagery is rooted in the natural world. "
            "The tradition honors both simple directness and poetic complexity (Dylan, Joni Mitchell). "
            "Repetition (refrain, chorus) serves as communal anchor and emotional emphasis."
        ),
        "language_register": "plain-spoken, poetic without pretension, Anglo-American vernacular, archaic in traditional ballads",
        "pov_typical": "first person narrator; third person in traditional ballads",
        "rhyme_schemes": ["ABAB", "AABB", "ABCB (ballad stanza — most traditional)", "AAAA"],
        "line_length": "consistent syllabic ballad meter (7–10 syllables), singable, iambic tendency",

        # ── SONG-STRUKTUR ──
        "typical_structure": "Verse (×4–6 for ballads) or Verse–Chorus–Verse–Chorus–Bridge–Chorus (contemporary folk)",
        "intro_style": "Solo guitar picking or unaccompanied voice; establishes intimacy immediately",
        "chorus_character": "Emotionally crystallized refrain — often a single repeated line or short repeated phrase",
        "bridge_role": "Tonal shift or narrative revelation; often drops to acoustic solo or changes key",
        "outro_style": "Final verse or chorus, diminuendo to nothing, guitar fade; sometimes unaccompanied final line",

        # ── FUSION-KOMPATIBILITÄT ──
        "fuses_well_with": ["Country", "Rock", "Classical", "Blues", "World", "Indie Pop"],
        "fusion_tension_with": ["EDM", "Metal", "Hip-Hop"],
        "bridge_elements": [
            "acoustic guitar and vocal (→ any acoustic genre)",
            "Celtic modal melody (→ World, Classical)",
            "protest lyric tradition (→ Hip-Hop, Rock)",
            "fingerpicking texture (→ Country, Classical guitar)",
            "communal sing-along (→ Gospel, Country)"
        ],

        # ── SUNO/UDIO PROMPT TAGS ──
        "suno_tags": [
            "folk", "acoustic guitar", "fingerpicking", "fiddle", "intimate",
            "storytelling", "heartfelt", "acoustic", "vocal harmony", "earthy",
            "banjo", "Americana", "singer-songwriter", "warm", "unplugged"
        ],
        "negative_tags": ["electronic beats", "synthesizer", "808 bass", "distorted guitar", "auto-tune"],

        # ── EMOTIONALE DNA ──
        "emotional_spectrum": {
            "primary": ["longing", "authenticity", "community"],
            "secondary": ["grief", "wonder", "resilience"],
            "forbidden": ["slick commercialism", "emotional artifice", "over-production"]
        },
        "listener_state": "The listener wants to be moved by a story, feel connected to something ancient and real, or experience quiet emotional truth — alone or around a fire.",
        "cultural_context": (
            "Folk music encompasses the oral traditions of every culture, but in Western popular music it "
            "refers primarily to the Anglo-American tradition of ballads, work songs, and topical song. "
            "The American Folk Revival (1940s–60s: Pete Seeger, Woody Guthrie, Joan Baez, Bob Dylan) "
            "politicized the form. British folk revival (Fairport Convention, Pentangle) followed. "
            "Today the singer-songwriter tradition carries folk DNA into every corner of popular music."
        ),

        # ── SUB-GENRES & VARIANTEN ──
        "sub_genres": {
            "Traditional Ballad":    "Ancient narrative songs; Child Ballads, Appalachian tradition",
            "Protest Folk":          "Political, topical; Woody Guthrie, Pete Seeger, Bob Dylan (early)",
            "Singer-Songwriter":     "Intimate, personal, literary; Joni Mitchell, Nick Drake, Elliott Smith",
            "Contemporary Folk":     "Modern production sensibility; Fleet Foxes, Iron & Wine, The Lumineers",
            "Celtic Folk":           "Irish/Scottish/Welsh; fiddle, bodhrán, tin whistle; Planxty, Clannad",
            "Appalachian Folk":      "American mountain tradition; dulcimer, banjo, modal tunings; Doc Watson",
            "Folk Rock":             "Electric folk fusion; Fairport Convention, Buffalo Springfield, Fleet Foxes",
            "Indie Folk":            "Post-millennial acoustic indie; Bon Iver, Sufjan Stevens, The National",
        },

        # ── REPRÄSENTATIVE KÜNSTLER ──
        "iconic_artists": [
            "Bob Dylan", "Joni Mitchell", "Woody Guthrie", "Joan Baez",
            "Pete Seeger", "Nick Drake", "Simon & Garfunkel", "Fairport Convention",
            "John Denver", "Neil Young (acoustic)"
        ],
        "modern_artists": [
            "Fleet Foxes", "Bon Iver", "Phoebe Bridgers", "Iron & Wine", "Sufjan Stevens"
        ],

        # ── SONG-WRITING TIPPS ──
        "writing_tips": [
            "Start with the story — what is the specific incident, journey, or moment you're capturing",
            "Every verse should advance the narrative or deepen the emotional understanding",
            "The refrain or chorus earns its repetition — make it the emotional truth of the song",
            "Use the natural cadences of spoken language; avoid forcing syllables",
            "Silence and space in the arrangement honor the lyric — don't fill every beat",
            "Traditional imagery (seasons, weather, roads) gains power from specific detail",
            "Test the song unaccompanied — if the melody and lyric don't work alone, they don't work"
        ],
        "avoid": [
            "Over-production that removes the intimate quality of acoustic folk",
            "Forced rhymes that distort natural speech patterns",
            "Abandoning the narrative structure for repetitive pop hooks",
            "Generic imagery without personal specificity",
            "Artificially archaic language that doesn't serve the song's communication"
        ],
    },

    "R&B": {
        # ── VIBES & ATMOSPHÄRE ──
        "vibes": [
            "sensual", "smooth", "soulful", "emotional", "intimate",
            "confident", "sultry", "groove-driven", "vulnerable", "romantic",
            "sophisticated", "powerful"
        ],
        "anti_vibes": [
            "cold", "harsh", "abrasive", "intellectually-detached",
            "rural", "aggressive-without-soul", "acoustic-only"
        ],

        # ── TONARTEN & HARMONIE ──
        "preferred_keys": ["Ab major", "Eb major", "Bb major", "F minor", "G minor", "C minor", "D minor"],
        "chord_progressions": [
            "ii-V-I (soul-jazz influence)",
            "i-VII-VI-V (neo-soul)",
            "I-iii-IV-V",
            "i-iv-I-V",
            "Imaj7-IVmaj7-iii7-VI7 (smooth R&B)",
            "i-bVII-bVI-bVII (90s R&B)",
            "IV-V-iii-vi (gospel-influenced)"
        ],
        "harmonic_feel": (
            "R&B harmony is lush and extended — 7ths, 9ths, and 11th chords are standard. "
            "The goal is harmonic richness that supports emotional delivery without overwhelming the vocal. "
            "Gospel-influenced chord movement (IV-V-I) creates moments of uplift. "
            "Neo-soul adds jazz complexity; contemporary R&B simplifies for streamed intimacy."
        ),
        "modes": ["Dorian (neo-soul)", "Aeolian", "Mixolydian", "Pentatonic (vocal melisma)", "Blues scale (expressive)"],

        # ── RHYTHMUS & TEMPO ──
        "bpm_ranges": {
            "slow": "55-75",
            "mid":  "85-110",
            "fast": "100-130"
        },
        "time_signatures": ["4/4", "12/8 (soul ballad)", "6/8"],
        "rhythm_feel": (
            "R&B groove is sensual and behind-the-beat — the pocket creates a luxurious, unhurried sense of time. "
            "Contemporary R&B uses programmed beats with trap hi-hat influence but retains soulful warmth."
        ),
        "groove_type": "behind-the-beat pocket, syncopated programmed beat, live funk groove, 12/8 soul triplet feel",

        # ── INSTRUMENTE & SOUND ──
        "core_instruments": [
            "lead vocals", "bass guitar (or bass synth)", "drums/drum machine",
            "electric piano (Rhodes, Wurlitzer)", "synthesizer (pads, leads)"
        ],
        "optional_instruments": [
            "guitar (clean funk stab or warm chords)", "horns (soul brass section)",
            "strings", "backing vocalists", "saxophone"
        ],
        "signature_sounds": [
            "Rhodes electric piano chord voicing", "vocal melisma and run",
            "snapping hi-hat pattern (contemporary)", "syncopated bass groove",
            "falsetto vocal break", "smooth saxophone fill",
            "warm string pad"
        ],
        "production_style": (
            "Classic R&B (Motown, Stax) was live band with warm room sound. "
            "90s R&B introduced programmed beats, lush orchestration, and produced vocal stacks (Babyface, Teddy Riley). "
            "Neo-soul (Erykah Badu, D'Angelo) returned to organic instrumentation with hip-hop beats. "
            "Contemporary R&B blends trap production with melodic sensibility."
        ),
        "mix_character": "warm, smooth, vocal-forward, rich low-mid, polished but not sterile, intimate room feel",

        # ── LYRIK & TEXTE ──
        "lyric_themes": [
            "romantic love and attraction", "sexual desire and intimacy", "heartbreak and healing",
            "relationship dynamics (power, vulnerability)", "loyalty and betrayal",
            "self-love and confidence", "missing someone", "the night and sensuality",
            "empowerment and resilience", "nostalgia for past love",
            "spiritual love (gospel-influenced)", "money and success"
        ],
        "lyric_style": (
            "R&B lyrics balance emotional honesty with sensual sophistication. "
            "The voice is everything — lyrics are often composed around melismatic phrasing, "
            "with key words landing on extended vocal runs. "
            "Direct emotional statements coexist with poetic imagery. "
            "Vulnerability and confidence alternate — the tension between the two is the genre's emotional engine."
        ),
        "language_register": "conversational, emotionally direct, contemporary AAVE, occasionally literary (neo-soul)",
        "pov_typical": "first person; direct address to 'you'; intimate confessional",
        "rhyme_schemes": ["AABB", "ABAB", "internal rhyme within melismatic phrases", "conversational near-rhyme"],
        "line_length": "medium-short, shaped by melodic phrase; key words receive melismatic extension",

        # ── SONG-STRUKTUR ──
        "typical_structure": "Verse – Pre-Chorus – Chorus – Verse – Pre-Chorus – Chorus – Bridge – Chorus",
        "intro_style": "Groove establishes first (drums + bass or Rhodes); vocal may enter immediately with a lick",
        "chorus_character": "Melodically peak, harmonically full, vocally most powerful; title in first line",
        "bridge_role": "Emotional deepening or twist; often drops to sparse instrumentation; ad-lib vocal moment",
        "outro_style": "Vocal ad-libs over groove, melismatic improvisations, fade or coda",

        # ── FUSION-KOMPATIBILITÄT ──
        "fuses_well_with": ["Hip-Hop", "Pop", "Jazz", "Gospel", "Soul", "EDM"],
        "fusion_tension_with": ["Metal", "Folk (traditional)", "Classical (rigid)"],
        "bridge_elements": [
            "gospel chord movement (→ Gospel, Soul)",
            "jazz extended chords (→ Jazz, Neo-Soul)",
            "trap hi-hat and 808 (→ Hip-Hop)",
            "danceable groove (→ EDM, Pop)",
            "vocal melisma tradition (→ Gospel, Soul)"
        ],

        # ── SUNO/UDIO PROMPT TAGS ──
        "suno_tags": [
            "R&B", "soul", "smooth", "Rhodes piano", "vocal melisma",
            "groove", "sensual", "bass groove", "neo-soul", "soulful vocals",
            "contemporary R&B", "emotional", "warm", "intimate", "harmonies"
        ],
        "negative_tags": ["distorted guitar", "metal", "country twang", "folk", "cold electronic"],

        # ── EMOTIONALE DNA ──
        "emotional_spectrum": {
            "primary": ["sensuality", "vulnerability", "soul"],
            "secondary": ["confidence", "longing", "joy"],
            "forbidden": ["coldness", "ironic detachment", "aggression (non-genre-appropriate)"]
        },
        "listener_state": "The listener wants to feel sensually alive, emotionally seen, or romantically moved — in an intimate setting, dressing for the night, or processing a relationship.",
        "cultural_context": (
            "Rhythm and Blues emerged from African American music in the 1940s as a commercial umbrella "
            "encompassing blues, gospel, jazz, and dance music. "
            "Motown, Stax, and Atlantic Records built the classic soul-R&B sound. "
            "New Jack Swing, Neo-Soul, and contemporary R&B each represent generational reinventions. "
            "R&B is the emotional heartbeat of Black American popular culture and one of the most globally influential genres."
        ),

        # ── SUB-GENRES & VARIANTEN ──
        "sub_genres": {
            "Classic Soul":          "Motown/Stax era live-band R&B; Aretha Franklin, Otis Redding, Marvin Gaye",
            "New Jack Swing":        "Hip-hop-influenced production; Teddy Riley, Bobby Brown, TLC, Janet Jackson",
            "Neo-Soul":              "Jazz and hip-hop meets classic soul; Erykah Badu, D'Angelo, Maxwell, Lauryn Hill",
            "Contemporary R&B":      "Modern production, trap influence, melodic; The Weeknd, SZA, Frank Ocean",
            "Quiet Storm":           "Smooth, romantic, adult contemporary; Anita Baker, Luther Vandross",
            "Alternative R&B":       "Experimental, unconventional; Frank Ocean, Solange, Daniel Caesar",
            "Southern Soul":         "Blues-R&B crossover, Deep South; Denise LaSalle, Tyrone Davis",
        },

        # ── REPRÄSENTATIVE KÜNSTLER ──
        "iconic_artists": [
            "Aretha Franklin", "Marvin Gaye", "Stevie Wonder", "Whitney Houston",
            "James Brown", "Al Green", "D'Angelo", "Erykah Badu",
            "Beyoncé", "Prince"
        ],
        "modern_artists": [
            "The Weeknd", "SZA", "Frank Ocean", "H.E.R.", "Daniel Caesar"
        ],

        # ── SONG-WRITING TIPPS ──
        "writing_tips": [
            "Write the vocal melody first — the groove should breathe around and beneath it",
            "Plan the ad-lib runs — they are composed, not improvised; identify the key emotional words",
            "The pre-chorus should squeeze tension until the chorus releases it",
            "Layer harmonic complexity beneath a simple surface — the sophistication is in the chords, not the lyric",
            "Use dynamics in the vocal delivery — not every phrase should be at full intensity",
            "The bridge is the emotional center — strip it back to one instrument and full vulnerability",
            "Think about the falsetto-to-chest-voice transition — it marks the emotional peak"
        ],
        "avoid": [
            "Over-quantized drums that remove the pocket and human feel",
            "Generic 'girl I love you' lyrics without specificity or vulnerability",
            "Ignoring the rhythm section conversation — bass and drums must groove as one",
            "Over-producing the vocal to the point of removing emotional authenticity",
            "Copying melismatic runs without serving the emotional narrative of the moment"
        ],
    },

    "Gospel": {
        # ── VIBES & ATMOSPHÄRE ──
        "vibes": [
            "uplifting", "transcendent", "celebratory", "communal", "powerful",
            "joyful", "spiritual", "testimonial", "passionate", "redemptive",
            "call-and-response", "surrender"
        ],
        "anti_vibes": [
            "nihilistic", "purely secular", "cold", "ironic", "hedonistic",
            "intellectually detached", "individualistic-without-community"
        ],

        # ── TONARTEN & HARMONIE ──
        "preferred_keys": ["Bb major", "Eb major", "F major", "Ab major", "C major", "G major"],
        "chord_progressions": [
            "I-IV-I-V (traditional gospel)",
            "I-bVII-IV-I (gospel rock)",
            "I-iii-IV-V (uplift progression)",
            "IV-V-iii-vi (gospel turnaround)",
            "I-IV-V-IV-I (simple testimony)",
            "I-I7-IV-iv-I (blues-gospel)",
            "vi-IV-I-V (contemporary worship crossover)"
        ],
        "harmonic_feel": (
            "Gospel harmony is rich with added tones — 7ths, 9ths, and 11ths are standard in the choir voicings. "
            "The characteristic 'gospel chord' (I7 moving to IV) borrows from blues. "
            "Call-and-response harmonic movement between soloist and choir is structural. "
            "Modulation upward (a half or whole step) at the final chorus is an expected emotional device."
        ),
        "modes": ["Ionian (major dominant)", "Blues scale (blues-gospel)", "Pentatonic major (shouting)", "Mixolydian"],

        # ── RHYTHMUS & TEMPO ──
        "bpm_ranges": {
            "slow": "55-75",
            "mid":  "80-110",
            "fast": "120-160"
        },
        "time_signatures": ["4/4", "6/8 (hymn and slow gospel)", "12/8 (traditional jubilee)"],
        "rhythm_feel": (
            "Gospel rhythm has a joyful, swinging lilt — even slow gospel breathes with spiritual weight. "
            "Hand claps on beats 2 and 4 are central. Fast gospel ('shoutin' music') drives hard. "
            "Contemporary gospel incorporates hip-hop and trap rhythms."
        ),
        "groove_type": "hand-clap backbeat, swinging triplet feel, call-and-response rhythmic punctuation, contemporary hip-hop gospel",

        # ── INSTRUMENTE & SOUND ──
        "core_instruments": [
            "lead vocals and choir", "Hammond B3 organ", "piano",
            "bass guitar", "drum kit"
        ],
        "optional_instruments": [
            "brass section (contemporary gospel)", "acoustic guitar",
            "strings (contemporary worship)", "synthesizer (modern gospel)",
            "tambourine and hand percussion"
        ],
        "signature_sounds": [
            "Hammond B3 organ Leslie cabinet swirl", "choir three-part harmony swell",
            "piano cluster gospel run", "handclap congregation",
            "falsetto soloist cry-break", "choir call-and-response shout",
            "Hammond bass pedals and choir combo"
        ],
        "production_style": (
            "Traditional gospel is recorded live in church with choir, organ, and congregation ambience. "
            "Contemporary gospel (Kirk Franklin era) is slickly produced with hip-hop beats, "
            "string sections, and full orchestral arrangements. "
            "The choir response is always present, whether live or layered in the studio."
        ),
        "mix_character": "warm, powerful, choir-wide in the stereo field, organ/piano prominent, vocals reverberant",

        # ── LYRIK & TEXTE ──
        "lyric_themes": [
            "praise and worship", "salvation and redemption", "personal testimony",
            "God's grace and mercy", "suffering and faith", "call to community",
            "Jesus and the Holy Spirit", "overcoming adversity through faith",
            "joy in the Lord", "the afterlife and heaven", "prayer and surrender",
            "racial justice and liberation theology"
        ],
        "lyric_style": (
            "Gospel lyrics testify — they speak from personal experience of the divine and invite the congregation "
            "to share that experience. Simple, repeated phrases create communal participation. "
            "Metaphors are biblical and familiar to the congregation. "
            "The call-and-response structure (preacher/choir) translates directly into lyric construction. "
            "Contemporary gospel can use secular emotional language applied to spiritual context."
        ),
        "language_register": "devotional, testimonial, accessible, often African American vernacular with biblical reference",
        "pov_typical": "first person testimonial ('I was lost'), second person praise ('You are'), collective 'we'",
        "rhyme_schemes": ["AABB", "ABCB", "simple end rhyme for memorability; internal rhyme in fast passages"],
        "line_length": "medium, syllabically singable in unison by a choir; strong stress on theologically key words",

        # ── SONG-STRUKTUR ──
        "typical_structure": "Verse – Chorus – Verse – Chorus – Vamp/Testimony – Chorus – Modulation – Final Chorus",
        "intro_style": "Organ chord or piano intro; church ambience; choir hum or congregational sound optional",
        "chorus_character": "Maximum communal power — choir + soloist, full band, emotionally at peak; designed for congregational singing",
        "bridge_role": "Vamp or testimony section — space for spontaneous musical expansion; builds to final modulation",
        "outro_style": "Modulated final chorus at full power; may fade or ritard to organ chord and silence",

        # ── FUSION-KOMPATIBILITÄT ──
        "fuses_well_with": ["R&B", "Soul", "Blues", "Hip-Hop (Gospel Rap)", "Country (Southern Gospel)", "Pop (Contemporary Worship)"],
        "fusion_tension_with": ["Metal", "EDM (pure)", "Experimental"],
        "bridge_elements": [
            "call-and-response vocal structure (→ Blues, Soul, R&B)",
            "Hammond organ (→ Rock, Jazz, Blues)",
            "choir harmony (→ Classical choral, Pop backing vocals)",
            "uplifting major-key progressions (→ Pop, Country)",
            "testimony lyric structure (→ Folk, Singer-Songwriter)"
        ],

        # ── SUNO/UDIO PROMPT TAGS ──
        "suno_tags": [
            "gospel", "choir", "Hammond organ", "uplifting", "spiritual",
            "call and response", "handclap", "powerful vocals", "sacred",
            "praise", "church music", "soulful", "inspirational", "communal"
        ],
        "negative_tags": ["secular nihilism", "heavy metal", "atonal", "cold electronic", "ironic"],

        # ── EMOTIONALE DNA ──
        "emotional_spectrum": {
            "primary": ["joy", "transcendence", "community"],
            "secondary": ["hope", "gratitude", "surrender"],
            "forbidden": ["nihilism", "isolation", "ironic detachment"]
        },
        "listener_state": "The listener wants to feel spiritually elevated, communally bonded, or emotionally released — in church, in communal worship, or in a moment of personal faith.",
        "cultural_context": (
            "Gospel music is rooted in the spirituals and hymns of African American enslaved people, "
            "evolving through Thomas A. Dorsey's fusion of blues and sacred music in the 1930s into a distinct genre. "
            "It profoundly shaped soul, R&B, and rock through shared vocal techniques and emotional directness. "
            "Contemporary gospel (Kirk Franklin, Tye Tribbett) is a global entertainment genre as much as worship music. "
            "White Southern Gospel and Contemporary Christian Music are parallel traditions."
        ),

        # ── SUB-GENRES & VARIANTEN ──
        "sub_genres": {
            "Traditional Gospel":       "Dorsey-era choir and piano; Mahalia Jackson, Clara Ward, Sister Rosetta Tharpe",
            "Southern Gospel":          "White Baptist/Pentecostal tradition; quartets, country influence; Gaither Vocal Band",
            "Contemporary Gospel":      "Hip-hop production, pop arrangement; Kirk Franklin, Yolanda Adams, Fred Hammond",
            "Gospel Rap":               "Hip-hop meets gospel testimony; Lecrae, Trip Lee, KB",
            "Praise & Worship":         "Charismatic church music, repetitive, intimate; Hillsong, Elevation Worship",
            "Urban Contemporary Gospel":"R&B and trap production with gospel message; Travis Greene, Todd Dulaney",
        },

        # ── REPRÄSENTATIVE KÜNSTLER ──
        "iconic_artists": [
            "Mahalia Jackson", "Aretha Franklin", "Thomas A. Dorsey", "Sister Rosetta Tharpe",
            "Andraé Crouch", "James Cleveland", "The Staple Singers", "Al Green"
        ],
        "modern_artists": [
            "Kirk Franklin", "Tye Tribbett", "Travis Greene", "Elevation Worship", "CeCe Winans"
        ],

        # ── SONG-WRITING TIPPS ──
        "writing_tips": [
            "Write the testimony — what is the specific moment of transformation or grace the song describes",
            "The vamp section should have room for musical expansion — don't over-compose it",
            "Call-and-response phrases must be short enough for a choir to repeat easily",
            "The modulation must feel earned — build to it through heightening intensity",
            "Simple repeated phrases are more powerful than complex verses in corporate worship",
            "Keep the central theological message singular — one truth, powerfully stated, repeatedly",
            "The soloist's improvisation space is sacred — write freedom into the structure"
        ],
        "avoid": [
            "Over-complex harmonies that a congregation cannot follow",
            "Lyrics that are theologically vague or could apply to secular romance",
            "Removing the call-and-response element — it is the architectural soul of the genre",
            "Production so polished it removes the spontaneous spiritual energy",
            "Modulation that comes too early before sufficient buildup"
        ],
    },

    "Latin": {
        # ── VIBES & ATMOSPHÄRE ──
        "vibes": [
            "passionate", "rhythmic", "sensual", "festive", "energetic",
            "romantic", "tropical", "nostalgic", "defiant", "joyful",
            "melancholic (ballad)", "communal"
        ],
        "anti_vibes": [
            "cold", "static", "non-rhythmic", "sterile-electronic",
            "deliberately atonal", "withdrawn", "ironic-detached"
        ],

        # ── TONARTEN & HARMONIE ──
        "preferred_keys": ["A minor", "D minor", "E minor", "C major", "G major", "F major", "Bb major"],
        "chord_progressions": [
            "i-VII-VI-VII (flamenco-Spanish)",
            "I-IV-V-I (cumbia, salsa)",
            "ii-V-I (Latin jazz)",
            "i-bVI-bVII-i (reggaeton/modern)",
            "I-V-vi-IV (Latin pop)",
            "Andalusian cadence: i-bVII-bVI-V",
            "i-iv-V7-i (bolero)"
        ],
        "harmonic_feel": (
            "Latin harmony reflects extreme diversity — from the Andalusian cadence of flamenco and son cubano "
            "to the jazz-sophisticated harmony of bossa nova and the simple diatonic pop of reggaeton. "
            "Minor keys with raised 7th (harmonic minor) are common in Iberian-rooted music. "
            "Jazz extended chords in Latin jazz; simple I-IV-V in dance-oriented cumbia and salsa."
        ),
        "modes": ["Aeolian", "Harmonic minor (flamenco/bolero)", "Phrygian (flamenco)", "Ionian", "Dorian (bossa nova)"],

        # ── RHYTHMUS & TEMPO ──
        "bpm_ranges": {
            "slow": "60-80",
            "mid":  "90-120",
            "fast": "130-200"
        },
        "time_signatures": ["4/4", "3/4 (waltz — danzón)", "6/8 (son, cumbia)", "12/8 (Afro-Cuban 6/8)"],
        "rhythm_feel": (
            "The clave rhythm is the rhythmic soul of Afro-Cuban music — all other instruments phrase in "
            "relationship to it. Brazilian samba and bossa nova have their own distinct patterns. "
            "Reggaeton's dembow is a contemporary simplification of the Afro-Caribbean polyrhythm."
        ),
        "groove_type": "clave-driven (Afro-Cuban), bossa nova samba-jazz, dembow (reggaeton), flamenco compás",

        # ── INSTRUMENTE & SOUND ──
        "core_instruments": [
            "clave (rhythm foundation)", "congas and bongos", "bass guitar or upright bass",
            "piano or keyboards", "lead vocals"
        ],
        "optional_instruments": [
            "trumpet and trombone (salsa/mambo)", "guitar (bossa nova, bolero, flamenco)",
            "violin (mariachi)", "accordion (cumbia, tango)", "cajon (flamenco, Afro-Peruvian)",
            "maracas and güiro"
        ],
        "signature_sounds": [
            "clave rhythm pattern (3-2 or 2-3)", "congas montuno pattern",
            "piano montuno (salsa)", "trumpet fanfare (salsa/mambo)",
            "nylon-string guitar rasgueado (flamenco)", "accordion melody (cumbia)",
            "reggaeton dembow kick-snare"
        ],
        "production_style": (
            "Latin production ranges from raw live salsa recordings to hyper-polished Latin pop (Universal Latin). "
            "Reggaeton and trap Latino are full digital productions with 808s and glossy mixing. "
            "Bossa nova and bolero prioritize intimate vocal-guitar recording. "
            "The rhythmic section must be mixed with precise placement — clave and congas must speak clearly."
        ),
        "mix_character": "rhythm section forward, percussion detailed and present, warm low-end, vocals passionate",

        # ── LYRIK & TEXTE ──
        "lyric_themes": [
            "passionate romantic love", "jealousy and betrayal", "nostalgia and homeland",
            "dancing and the body", "resistance and defiance", "poverty and survival",
            "the sea and travel", "political revolution", "sensuality and desire",
            "cultural pride", "loss and grief (ballad tradition)", "party and celebration"
        ],
        "lyric_style": (
            "Latin lyrics are emotionally expressive and physically oriented — the body and movement are present. "
            "Spanish poetic tradition values metaphor and emotional directness simultaneously. "
            "The piropo (compliment) tradition shapes romantic lyrics. "
            "Improvisation (decima, sonero improvisation in salsa) is valued as much as composed lyrics."
        ),
        "language_register": "Spanish (regional variants), Portuguese (bossa nova/samba), passionate, poetic, vernacular",
        "pov_typical": "first person passionate declaration; direct address to lover; collective cultural pride",
        "rhyme_schemes": ["ABAB", "ABCB", "consonance-heavy Spanish rhyme (assonance acceptable)"],
        "line_length": "medium, syllabically regular for dance-music clarity; poetic line in bolero/bossa nova",

        # ── SONG-STRUKTUR ──
        "typical_structure": "Verse – Chorus – Verse – Chorus – Montuno/Coro (call-and-response jam) – Mambo",
        "intro_style": "Percussion breakdown or piano/guitar intro establishing the groove and feel",
        "chorus_character": "Coro (choir call-and-response) or commercial hook; energetically peaked, full band",
        "bridge_role": "Mambo section (instrumental solo) or instrumental breakdown; rhythmic intensification",
        "outro_style": "Montuno fade or full stop; often ends in percussion climax",

        # ── FUSION-KOMPATIBILITÄT ──
        "fuses_well_with": ["Pop", "R&B", "Jazz", "Hip-Hop", "EDM", "Reggae"],
        "fusion_tension_with": ["Metal", "Folk (non-Latin)", "Classical (without Latin influence)"],
        "bridge_elements": [
            "clave rhythm pattern (→ Reggae, Afrobeat, World)",
            "Spanish guitar (→ Folk, Classical, Flamenco)",
            "jazz harmony (→ Jazz, Bossa Nova)",
            "danceable groove (→ EDM, R&B, Pop)",
            "romantic vocal style (→ R&B, Pop ballad)"
        ],

        # ── SUNO/UDIO PROMPT TAGS ──
        "suno_tags": [
            "latin", "salsa", "bossa nova", "reggaeton", "conga drums",
            "clave", "latin jazz", "flamenco", "Spanish guitar", "tropical",
            "cumbia", "latin pop", "passionate vocals", "danceable", "vibrant"
        ],
        "negative_tags": ["cold", "metal", "atonal", "folk non-Latin", "Nordic"],

        # ── EMOTIONALE DNA ──
        "emotional_spectrum": {
            "primary": ["passion", "joy", "sensuality"],
            "secondary": ["nostalgia", "pride", "longing"],
            "forbidden": ["coldness", "emotional withdrawal", "ironic distance"]
        },
        "listener_state": "The listener wants to feel bodily alive, romantically inflamed, or culturally proud — dancing, celebrating, or in emotional surrender.",
        "cultural_context": (
            "Latin music is the broadest musical category — encompassing the Iberian, African, and indigenous "
            "traditions of an entire continent. Afro-Cuban rhythms (salsa, mambo, rumba) and Brazilian music "
            "(samba, bossa nova) are globally influential. Reggaeton and trap Latino dominate streaming in the 21st century. "
            "Latin music is the fastest-growing global market in recorded music."
        ),

        # ── SUB-GENRES & VARIANTEN ──
        "sub_genres": {
            "Salsa":          "Afro-Cuban clave, brass, piano montuno; Celia Cruz, Ruben Blades, Marc Anthony",
            "Bossa Nova":     "Brazilian jazz-samba fusion, intimate, guitar+voice; João Gilberto, Stan Getz, Astrud Gilberto",
            "Reggaeton":      "Dembow beat, urban Caribbean, Spanish rap-sung; Daddy Yankee, Bad Bunny, J Balvin",
            "Flamenco":       "Spanish Andalusian, cante jondo, guitar rasgueado, compás; Paco de Lucía, Camarón",
            "Cumbia":         "Colombian percussion, accordion melody, accessible dance; Carlos Vives, Tropicalia",
            "Tango":          "Argentine passion dance, bandoneón, melancholic; Astor Piazzolla, Carlos Gardel",
            "Mariachi":       "Mexican brass and strings, patriotic/romantic; Chavela Vargas, Vicente Fernández",
            "Latin Pop":      "Commercial crossover, pop structure in Spanish; Shakira, Ricky Martin, Maluma",
        },

        # ── REPRÄSENTATIVE KÜNSTLER ──
        "iconic_artists": [
            "Celia Cruz", "Tito Puente", "Carlos Santana", "Astor Piazzolla",
            "João Gilberto", "Selena", "Rubén Blades", "Marc Anthony",
            "Gloria Estefan", "Roberto Carlos"
        ],
        "modern_artists": [
            "Bad Bunny", "J Balvin", "Shakira", "Rosalía", "Maluma"
        ],

        # ── SONG-WRITING TIPPS ──
        "writing_tips": [
            "Understand the clave — write your melody in conversation with it, not against it",
            "The coro (call-and-response hook) must be short, repeatable, and emotionally direct",
            "Let the rhythm section tell the story as much as the lyric — the groove IS the emotion",
            "In salsa, the montuno section is for improvisation — build in space for the sonero",
            "Use the Spanish language's vowel-richness for sustained melodic notes",
            "The body must feel the music — if you can't move to it, the rhythm isn't right yet",
            "Cultural specificity (local place names, vernacular, foods) creates authenticity"
        ],
        "avoid": [
            "Generic pan-Latin sounds that don't commit to a specific tradition",
            "Ignoring the rhythmic precision — the clave cannot be faked or approximated",
            "Lyrics that are culturally inauthentic or appropriative without understanding",
            "Over-producing the acoustic elements (guitar, percussion) to remove their character",
            "Treating Latin music as a monolith — each sub-genre has its own rules"
        ],
    },

    "Reggae": {
        # ── VIBES & ATMOSPHÄRE ──
        "vibes": [
            "conscious", "relaxed", "spiritual", "roots", "rebellious",
            "positive vibration", "tropical", "communal", "hypnotic", "peaceful resistance",
            "mystical (Rastafari)", "groove-deep"
        ],
        "anti_vibes": [
            "frantic", "cold-electronic", "aggressive-mindless", "hollow commercialism",
            "ironic", "disconnected from rhythm", "racist"
        ],

        # ── TONARTEN & HARMONIE ──
        "preferred_keys": ["A major", "D major", "G major", "E major", "C major", "Bb major"],
        "chord_progressions": [
            "I-IV-V-I",
            "I-ii-IV-V",
            "i-VII-VI-VII (minor reggae)",
            "I-V-ii-IV",
            "i-iv-i-V (one-drop rhythm)",
            "I-IV-I-V (classic rocksteady)",
            "ii-V-I (jazz-influenced reggae)"
        ],
        "harmonic_feel": (
            "Reggae harmony is diatonic and uncluttered — the chord change is less important than the rhythmic "
            "placement of the chord stabs (the 'skank' on the off-beat). "
            "Major keys dominate for positive vibration; minor for roots-consciousness. "
            "Dub removes harmony almost entirely, leaving bass and rhythm."
        ),
        "modes": ["Ionian (major)", "Aeolian (roots)", "Mixolydian (occasional)", "Blues scale (Jamaican blues)"],

        # ── RHYTHMUS & TEMPO ──
        "bpm_ranges": {
            "slow": "60-80",
            "mid":  "80-100",
            "fast": "100-160"
        },
        "time_signatures": ["4/4 (universal)"],
        "rhythm_feel": (
            "Reggae's defining rhythmic feel is the ONE DROP — the kick and snare emphasize beat 3 "
            "(dropping beats 1 and 2), creating a floating, hypnotic forward motion. "
            "The off-beat guitar 'skank' and bass melody are the heart of the groove."
        ),
        "groove_type": "one-drop (kick on 3, snare on 3), skank guitar on off-beats, bass melodic lead",

        # ── INSTRUMENTE & SOUND ──
        "core_instruments": [
            "bass guitar (melodic, deep, prominent)", "drums (one-drop pattern)",
            "rhythm guitar ('skank' off-beat chop)", "keyboards (organ, piano)",
            "lead vocals"
        ],
        "optional_instruments": [
            "brass section (trumpet, trombone, sax)", "percussion (shaker, cowbell)",
            "melodica", "DJ/toaster (deejay voiceover)", "nyahbinghi drums (roots reggae)"
        ],
        "signature_sounds": [
            "fat sub-bass melodic line", "off-beat guitar skank chord",
            "deep reverb on snare (echo chamber)", "brass stab fill",
            "organ pulse on off-beats", "echo/dub delay effects",
            "bass drop and re-entry"
        ],
        "production_style": (
            "Classic reggae (Studio One, Channel One) used live room recording with pronounced bass and echo. "
            "Lee 'Scratch' Perry and King Tubby invented dub — removing and re-introducing elements, "
            "drowning the mix in delay and reverb for a sonic dreamscape. "
            "Modern reggae production maintains these principles with digital tools."
        ),
        "mix_character": "bass-dominant, deep reverb on drums, guitar mid-present, vocals with reverb warmth",

        # ── LYRIK & TEXTE ──
        "lyric_themes": [
            "Rastafari spirituality and Jah", "oppression and liberation (Babylon system)",
            "Africa and repatriation (roots)", "love and romance (lovers rock)",
            "political resistance", "marijuana and natural living",
            "community solidarity", "peace and unity",
            "poverty and survival in Jamaica", "African identity and pride",
            "biblical imagery and prophecy", "daily life and struggle"
        ],
        "lyric_style": (
            "Roots reggae lyrics are message-first — the lyric is a conscious statement, testimony, or spiritual text. "
            "Biblical language and Rastafari vocabulary (Babylon, Zion, I and I, Jah) permeate the tradition. "
            "Lovers rock softens the political content for romance. "
            "Patois (Jamaican Creole) is the authentic linguistic register; standard English in crossover."
        ),
        "language_register": "Jamaican Patois (roots/dancehall), English crossover, biblical and Rastafari terminology",
        "pov_typical": "first person 'I and I' (Rastafari collective self); direct message to Babylon or the listener",
        "rhyme_schemes": ["AABB", "ABAB", "ABCB; couplet within chant; toasting (dancehall) uses complex internal rhyme"],
        "line_length": "medium, flowing with the groove; Patois syllabic patterns shaped by Jamaican speech rhythms",

        # ── SONG-STRUKTUR ──
        "typical_structure": "Intro groove – Verse – Chorus – Verse – Chorus – Bridge (dub break) – Chorus",
        "intro_style": "Bass establishes groove alone; drums enter; guitar skank completes rhythm; vocal enters on verse",
        "chorus_character": "Sing-along hook with positive message; full band; emotionally open and joyful or solemn",
        "bridge_role": "Dub section — stripped to bass and drums with echo effects; or instrumental brass break",
        "outro_style": "Fade on groove; dub echo trail; sometimes a cappella vocal last lines",

        # ── FUSION-KOMPATIBILITÄT ──
        "fuses_well_with": ["Hip-Hop", "R&B", "EDM", "Pop", "Folk", "Latin"],
        "fusion_tension_with": ["Metal", "Classical (strict)", "Country (traditional)"],
        "bridge_elements": [
            "off-beat guitar skank (→ Ska, Rocksteady, World)",
            "sub-bass prominence (→ Dub, EDM, Hip-Hop)",
            "echo/delay production (→ Dub, Experimental, EDM)",
            "conscious lyric tradition (→ Hip-Hop, Folk, Protest)",
            "one-drop rhythm (→ Dub, Dancehall, Afrobeats)"
        ],

        # ── SUNO/UDIO PROMPT TAGS ──
        "suno_tags": [
            "reggae", "one-drop", "bass-heavy", "off-beat guitar", "Rastafari",
            "roots reggae", "Jamaica", "dub", "groove", "conscious",
            "echo", "soulful vocals", "brass stabs", "tropical", "relaxed"
        ],
        "negative_tags": ["metal", "fast EDM", "classical orchestral", "cold production", "no bass"],

        # ── EMOTIONALE DNA ──
        "emotional_spectrum": {
            "primary": ["peace", "conscious resistance", "spiritual connection"],
            "secondary": ["joy", "longing (for Africa/Zion)", "love"],
            "forbidden": ["nihilism", "aggressive mindlessness", "cultural inauthenticity"]
        },
        "listener_state": "The listener wants to feel grounded, spiritually connected, or peacefully resistant — at a roots session, by the beach, or in reflective political awareness.",
        "cultural_context": (
            "Reggae evolved from Jamaican ska and rocksteady in the late 1960s, carrying the social and spiritual "
            "consciousness of the Rastafari movement. Bob Marley made it a global force. "
            "Dub (King Tubby, Lee Perry) invented studio remixing as art form. "
            "Dancehall emerged in the 1980s as a faster, more digital, and sexually explicit offshoot. "
            "Reggae's influence on hip-hop, dub techno, and global music is incalculable."
        ),

        # ── SUB-GENRES & VARIANTEN ──
        "sub_genres": {
            "Roots Reggae":    "Conscious, Rastafari, roots sound; Bob Marley, Burning Spear, Culture, Steel Pulse",
            "Dub":             "Instrumental remix, studio as instrument, echo and reverb; King Tubby, Lee Perry, Augustus Pablo",
            "Ska":             "Upbeat, horn-driven precursor; The Skatalites, Prince Buster",
            "Rocksteady":      "Slower than ska, proto-reggae; Alton Ellis, Toots and the Maytals",
            "Lovers Rock":     "Romantic, soft, UK-born reggae; Janet Kay, Carroll Thompson",
            "Dancehall":       "Digital, fast, DJ-toasting; Yellowman, Shabba Ranks, Sean Paul, Vybz Kartel",
            "Reggaeton":       "Latin-Caribbean, dembow rhythm (see Latin genre entry)",
        },

        # ── REPRÄSENTATIVE KÜNSTLER ──
        "iconic_artists": [
            "Bob Marley & The Wailers", "Peter Tosh", "Burning Spear", "Lee 'Scratch' Perry",
            "Toots and the Maytals", "Desmond Dekker", "Jimmy Cliff", "Culture"
        ],
        "modern_artists": [
            "Damian Marley", "Chronixx", "Protoje", "Koffee", "Popcaan"
        ],

        # ── SONG-WRITING TIPPS ──
        "writing_tips": [
            "Feel the one-drop first — write everything else after you've locked into that rhythm",
            "The bass line must sing — it carries the melody of the groove, not just the root",
            "Keep the message singular and powerful — clarity over complexity in conscious reggae",
            "The chorus should be a chant the listener can hold onto — brief and profound",
            "Patois words and phrases add authenticity and rhythmic character",
            "Build natural dub space into the arrangement — leave holes for the echo to fill",
            "The positive vibration must be genuine — forced positivity sounds hollow in reggae"
        ],
        "avoid": [
            "Speeding the tempo past the hypnotic zone — reggae's power is in the pocket",
            "Over-quantizing the rhythm section — the slight human feel is essential",
            "Putting the bass in the background — it is the lead instrument of reggae",
            "Ignoring the off-beat guitar skank — it is 50% of the rhythmic identity",
            "Writing lyrics without engaging with the Rastafari/conscious tradition you're working in"
        ],
    },

    "World": {
        # ── VIBES & ATMOSPHÄRE ──
        "vibes": [
            "diverse", "communal", "earthy", "transcendent", "rhythmic",
            "ancient", "spiritual", "celebratory", "soulful", "hypnotic",
            "storytelling", "culturally grounded"
        ],
        "anti_vibes": [
            "culturally appropriative without depth", "Western-only reference",
            "sterile-electronic", "culturally homogenized", "ironic",
            "disconnected from geography"
        ],

        # ── TONARTEN & HARMONIE ──
        "preferred_keys": [
            "Context-specific (each sub-genre has its own system)",
            "Arabic maqam modes (Middle East)", "Pentatonic (African, East Asian)",
            "Raga scales (Indian)", "Phrygian (flamenco)", "Whole-step/half-step",
            "Microtonal scales (Arabic, Turkish, Indian)"
        ],
        "chord_progressions": [
            "Drone-based harmony (Indian, North African)",
            "Two-chord modal vamp (Afrobeat, Celtic)",
            "Pentatonic movement (African pop)",
            "Arabic maqam progression",
            "Western diatonic adapted (World pop crossover)",
            "Polytonality (West African traditional)"
        ],
        "harmonic_feel": (
            "World music harmony resists Western harmonic generalization. "
            "African music often uses polyrhythm and call-and-response rather than chord-based harmony. "
            "Indian classical uses raga (melodic mode) over a drone. Arabic music uses maqam with microtones. "
            "Celtic folk uses modal harmony; Afrobeats uses funk-influenced diatonic harmony."
        ),
        "modes": [
            "All world modes — raga (Indian), maqam (Arabic/Turkish), pentatonic (global)",
            "Celtic modes (Dorian, Mixolydian)", "African pentatonic", "Phrygian (Flamenco/Middle Eastern)"
        ],

        # ── RHYTHMUS & TEMPO ──
        "bpm_ranges": {
            "slow": "50-80",
            "mid":  "90-130",
            "fast": "140-220"
        },
        "time_signatures": [
            "4/4", "6/8", "7/8 (Balkan)", "9/8 (Turkish/Balkan)",
            "5/4", "12/8 (African)", "complex additive rhythms (Indian tala)"
        ],
        "rhythm_feel": (
            "World rhythms are the most diverse on Earth — from the polyrhythm of West Africa (multiple "
            "simultaneous rhythmic layers) to the complex tala of Indian classical, the flamenco compás, "
            "and the driving straight 8th of Afrobeats. Rhythm is often the primary structural element."
        ),
        "groove_type": "sub-genre specific: polyrhythm (West African), tala cycle (Indian), compás (flamenco), clave (Afro-Cuban)",

        # ── INSTRUMENTE & SOUND ──
        "core_instruments": [
            "Region-specific (kora, oud, sitar, djembe, balafon, steel pan, gamelan, etc.)",
            "Vocal traditions (griots, qawwali, Celtic sean-nós)",
            "Percussion (virtually every culture has its own)"
        ],
        "optional_instruments": [
            "Western instruments in crossover contexts",
            "Electric guitar (Afrobeats, South American fusion)",
            "Bass guitar and drum kit (modern Afrobeats, world pop)"
        ],
        "signature_sounds": [
            "kora's bright harp-like pluck (West African)", "oud's warm nasal resonance (Arabic/Turkish)",
            "sitar's resonating sympathetic strings (Indian)", "djembe's sharp slap and bass tone",
            "steel pan melody (Caribbean)", "balafon's woody xylophone tone",
            "throat singing overtones (Tuvan/Mongolian)"
        ],
        "production_style": (
            "World music production varies enormously by region and era. "
            "Traditional recording captures live acoustic ensemble performance with minimal processing. "
            "Modern Afrobeats is slickly produced with digital drums and 808s. "
            "World fusion (Peter Gabriel, Paul Simon's Graceland) blends Western pop production with "
            "acoustic world instruments."
        ),
        "mix_character": "instrument-specific; acoustic world: natural room resonance; modern Afrobeats: punchy and polished",

        # ── LYRIK & TEXTE ──
        "lyric_themes": [
            "ancestral connection and identity", "community and collective celebration",
            "spiritual practice and ritual", "love in cultural context",
            "resistance and liberation", "nature and geography (specific landscapes)",
            "mythological and epic narratives", "social commentary",
            "grief and mourning rituals", "praise (for leaders, divine, community)",
            "everyday life and specific cultural experiences", "migration and diaspora"
        ],
        "lyric_style": (
            "World lyric traditions are extraordinarily diverse. Griot traditions are epic oral history. "
            "Qawwali is mystical devotional poetry (Sufi). Celtic is narrative ballad. "
            "What unites them is cultural specificity and a connection to community, history, and place. "
            "Many traditions prioritize the sound and rhythm of language over translatable meaning."
        ),
        "language_register": "culturally specific language; vernacular of each tradition; many world languages represented",
        "pov_typical": "communal and narrative — speaking for and to the community; individual story as collective mirror",
        "rhyme_schemes": ["Culturally specific; Arabic poetry uses strict meters; Celtic uses assonance; African often uses tonal patterns"],
        "line_length": "culturally variable; often determined by tonal language patterns or metric poetic traditions",

        # ── SONG-STRUKTUR ──
        "typical_structure": "Sub-genre dependent: cyclic (Indian, West African), verse-refrain (folk traditions), through-composed (qawwali build)",
        "intro_style": "Percussive entry OR solo instrument/voice establishing the tonal and rhythmic world",
        "chorus_character": "Communal response section — whether choir, chorus, or call-and-response crowd engagement",
        "bridge_role": "Instrumental solo or improvisation; rhythmic climax (e.g., tabla solo in Indian music)",
        "outro_style": "Gradual deceleration (Indian), fade (Afrobeats modern), or decisive rhythmic stop",

        # ── FUSION-KOMPATIBILITÄT ──
        "fuses_well_with": ["Jazz", "Folk", "R&B", "EDM", "Pop", "Classical"],
        "fusion_tension_with": ["Metal (without world metal tradition)", "strict Classical formalism"],
        "bridge_elements": [
            "pentatonic melody (universally fusible)",
            "polyrhythm layering (→ Jazz, Funk, R&B)",
            "drone-based harmony (→ Experimental, Ambient, Classical minimalism)",
            "call-and-response vocal (→ Gospel, Blues, R&B)",
            "acoustic plucked string texture (→ Folk, Classical, Acoustic Pop)"
        ],

        # ── SUNO/UDIO PROMPT TAGS ──
        "suno_tags": [
            "world music", "afrobeats", "bossa nova", "flamenco", "Celtic",
            "djembe", "kora", "oud", "sitar", "polyrhythm",
            "folk traditional", "acoustic", "cultural fusion", "global",
            "percussion-forward", "ethnic instruments"
        ],
        "negative_tags": ["heavy metal distortion", "808 trap (without cultural context)", "sterile pop production"],

        # ── EMOTIONALE DNA ──
        "emotional_spectrum": {
            "primary": ["cultural connection", "communal joy", "spiritual resonance"],
            "secondary": ["longing (diaspora)", "pride", "grief (ritual mourning)"],
            "forbidden": ["cultural appropriation without respect", "Western imperialist gaze", "homogenization"]
        },
        "listener_state": "The listener wants to be transported to another place and cultural reality — experiencing the profound specificity of human musical expression across the globe.",
        "cultural_context": (
            "'World music' is a Western marketing term that groups all non-Western and non-mainstream Western music. "
            "Each tradition is a complete, sophisticated system with its own history, theory, and cultural logic. "
            "Peter Gabriel's WOMAD festival (1982) popularized the concept. "
            "The most globally impactful current world music force is Afrobeats (Nigeria's Burna Boy, Wizkid, "
            "Davido), which has merged with global pop and hip-hop streaming dominance."
        ),

        # ── SUB-GENRES & VARIANTEN ──
        "sub_genres": {
            "Afrobeats":         "West African pop, Highlife influence, digital + organic; Burna Boy, Wizkid, Davido, Fela Kuti (Afrobeat root)",
            "Flamenco":          "Andalusian Spanish, cante/baile/toque, Phrygian; Paco de Lucía, Camarón de la Isla",
            "Celtic":            "Irish/Scottish/Breton; fiddle, tin whistle, uilleann pipes; Clannad, Chieftains",
            "Bossa Nova":        "Brazilian; see Latin entry — also a world music form",
            "Qawwali":           "South Asian Sufi devotional; Nusrat Fateh Ali Khan",
            "Gnawa":             "Moroccan trance ritual music; Maalem Mahmoud Guinia",
            "Gamelan":           "Indonesian; metallophones and gongs; tuned to slendro or pélog scales",
            "Balkan Folk":       "Complex meters (7/8, 9/8, 11/8); brass, accordion; Goran Bregović, Balkan Beat Box",
        },

        # ── REPRÄSENTATIVE KÜNSTLER ──
        "iconic_artists": [
            "Fela Kuti", "Miriam Makeba", "Ravi Shankar", "Nusrat Fateh Ali Khan",
            "Youssou N'Dour", "Cesária Évora", "Ali Farka Touré", "Paco de Lucía"
        ],
        "modern_artists": [
            "Burna Boy", "Wizkid", "Fatoumata Diawara", "Balthazar & JohnBoy", "Tinariwen"
        ],

        # ── SONG-WRITING TIPPS ──
        "writing_tips": [
            "Research the specific tradition you're writing in — superficial borrowing is heard immediately",
            "Let the rhythm lead — in most world music traditions, rhythm is the structural foundation",
            "Understand the tuning system of the tradition (microtones, raga, maqam) before writing melody",
            "Use call-and-response as a structural principle — it is universal across world traditions",
            "The specific cultural vocabulary (instrument timbre, language, rhythm pattern) cannot be faked",
            "Collaborate with artists from the tradition — cultural knowledge is embodied, not learned from books",
            "Allow the music to breathe within its own time system — Western 4/4 grid thinking must be suspended"
        ],
        "avoid": [
            "Reducing an entire culture to one stereotypical instrumental sound",
            "Applying Western harmonic logic to traditions that use modal or drone-based harmony",
            "Speeding up or quantizing rhythms that are intentionally loose or swing-based",
            "Using 'exotic' sounds as decoration without understanding their cultural context",
            "Mistaking entertainment crossover for authentic traditional practice"
        ],
    },

    "Experimental": {
        # ── VIBES & ATMOSPHÄRE ──
        "vibes": [
            "avant-garde", "challenging", "intellectually stimulating", "disorienting",
            "transcendent (through difficulty)", "exploratory", "unique", "unsettling",
            "meditative (minimalism)", "futuristic", "alien", "liberating"
        ],
        "anti_vibes": [
            "comfortable", "predictable", "formula-driven", "commercially polished",
            "radio-ready", "derivative", "emotionally shallow"
        ],

        # ── TONARTEN & HARMONIE ──
        "preferred_keys": [
            "No fixed key (atonal)", "freely chosen", "microtonal",
            "serialist (12-tone)", "spectral (based on overtone series)",
            "modal (minimalist: one mode, no chord changes)",
            "noise (no pitching)"
        ],
        "chord_progressions": [
            "None (atonal, free improvisation)",
            "Cluster chords",
            "Single sustained chord (drone minimalism)",
            "12-tone row-based harmony",
            "Spectral harmony (harmonics of fundamental)",
            "Random/aleatoric harmony (chance operations)",
            "Non-Western or non-tempered tuning systems"
        ],
        "harmonic_feel": (
            "Experimental music deliberately escapes or destroys the expectations of tonal harmony. "
            "Atonality (Schoenberg, Webern), minimalist stasis (Glass, Reich), noise (Merzbow), "
            "spectral harmony (Grisey), and improvised free jazz (Coleman) each represent a different "
            "rejection of or departure from conventional harmony. The goal is new sonic experience."
        ),
        "modes": ["Atonal", "Spectral modes", "Non-Western", "Microtonal", "Any mode as conceptual choice"],

        # ── RHYTHMUS & TEMPO ──
        "bpm_ranges": {
            "slow": "any/static",
            "mid":  "any/variable",
            "fast": "any/poly-temporal"
        },
        "time_signatures": ["Any — including no meter, free time, polyrhythm, irrational meters, aleatoric"],
        "rhythm_feel": (
            "Experimental rhythm spans from metronomic grid (minimalism) to complete metric freedom (free jazz, noise). "
            "Polyrhythm, metric modulation, and irrational time signatures are common tools."
        ),
        "groove_type": "no groove (conceptual), polyrhythm, free time, metronomic minimalism, glitchy programmed",

        # ── INSTRUMENTE & SOUND ──
        "core_instruments": [
            "any instrument used unconventionally", "extended technique instruments",
            "electronics (synthesizer, computer, tape)", "voice (extended techniques)",
            "found objects and prepared piano"
        ],
        "optional_instruments": [
            "turntable as melodic instrument", "field recordings",
            "circuit-bent electronics", "modular synthesizer", "acoustic instruments played incorrectly"
        ],
        "signature_sounds": [
            "prepared piano (screws, rubber on strings)", "electronic noise wall",
            "field recording collage", "glitched and stuttered digital audio",
            "extended technique (multiphonics, col legno, sul ponticello)",
            "microtonal quarter-tone melody", "drone with gradual transformation"
        ],
        "production_style": (
            "Experimental production has no rules — the studio is the instrument (musique concrète). "
            "Pierre Schaeffer's tape manipulation, Brian Eno's ambient production, and Aphex Twin's "
            "algorithmic composition are all valid models. "
            "The production concept IS the music — process is compositional."
        ),
        "mix_character": "concept-dependent: dense noise wall, crystalline and wide (ambient), distorted extreme, or deliberately unbalanced",

        # ── LYRIK & TEXTE ──
        "lyric_themes": [
            "the act of perception itself", "conceptual abstraction",
            "language as sound and material", "political disruption",
            "inner consciousness and fragmentation", "technology and the body",
            "science and physics (spectral, quantum conceptualism)",
            "silence and nothingness", "the collapse of meaning",
            "humor and absurdity (Dada)", "environmental and ecological",
            "personal narrative through unconventional form"
        ],
        "lyric_style": (
            "Experimental lyrics range from entirely absent (pure music) to deconstructed language "
            "(phonetic poetry, sound poetry), found text (cut-up technique), and spoken word. "
            "When present, lyrics often foreground the sound and rhythm of words rather than semantic meaning. "
            "Burroughs' cut-up, Cage's chance operations, and Ono's instruction pieces are models."
        ),
        "language_register": "phonetic, found text, deconstructed, multilingual, or absent; rarely conventional narrative",
        "pov_typical": "dissolved — or radically unexpected; the 'voice' itself is questioned as a concept",
        "rhyme_schemes": ["None, or deliberately broken, or phonetic rather than semantic rhyme"],
        "line_length": "irrelevant as concept — or hyper-specific as formal constraint",

        # ── SONG-STRUKTUR ──
        "typical_structure": "Non-standard; process-generated, through-composed, improvised, or chance-determined",
        "intro_style": "Abrupt, gradual process, or conceptually determined entry",
        "chorus_character": "Absent OR a recurring textural state rather than melodic hook; repetition as minimalist device",
        "bridge_role": "Structural disruption or deviation — the unexpected break IS the point",
        "outro_style": "Silence, abrupt stop, fade into field recording, or infinite drone",

        # ── FUSION-KOMPATIBILITÄT ──
        "fuses_well_with": ["Classical (contemporary)", "Jazz (free/fusion)", "EDM (experimental electronics)", "Folk (freak folk)", "Pop (art pop)"],
        "fusion_tension_with": ["Schlager", "Country (commercial)", "Pop (commercial)"],
        "bridge_elements": [
            "extended instrumental technique (→ Classical contemporary, Jazz)",
            "electronic processing (→ EDM, ambient)",
            "conceptual framework (→ Art Pop, Avant-Rock)",
            "field recording texture (→ Ambient, World)",
            "free improvisation (→ Jazz, Free Improv)"
        ],

        # ── SUNO/UDIO PROMPT TAGS ──
        "suno_tags": [
            "experimental", "avant-garde", "noise", "ambient", "electronic",
            "atonal", "abstract", "soundscape", "glitch", "drone",
            "minimalist", "unconventional", "textural", "processed", "boundary-pushing"
        ],
        "negative_tags": ["radio-ready", "commercial pop", "verse-chorus structure", "predictable", "formulaic"],

        # ── EMOTIONALE DNA ──
        "emotional_spectrum": {
            "primary": ["intellectual curiosity", "disorientation", "transcendence"],
            "secondary": ["awe", "unease", "liberation"],
            "forbidden": ["comfortable familiarity", "emotional predictability", "passive consumption"]
        },
        "listener_state": "The listener wants to be actively challenged, have their perceptions of sound altered, or experience music as a genuinely new event — in a gallery, headphones in darkness, or at a concert hall.",
        "cultural_context": (
            "Experimental music is the avant-garde history of music — from Cage's 4'33'' to Schoenberg's "
            "twelve-tone rows, Stockhausen's electronic compositions, and Merzbow's noise walls. "
            "It is the R&D department of all music — genres that were once experimental (jazz, rock, electronic) "
            "became mainstream. The experimental tradition questions what music is and can be."
        ),

        # ── SUB-GENRES & VARIANTEN ──
        "sub_genres": {
            "Noise":              "Extreme sonic density, feedback, distortion as medium; Merzbow, Whitehouse, Wolf Eyes",
            "Ambient":            "Texture over melody, environmental, non-intrusive; Brian Eno, Stars of the Lid, Grouper",
            "Musique Concrète":   "Tape manipulation of recorded sounds; Pierre Schaeffer, Pierre Henry",
            "Free Improvisation": "No fixed structure, total spontaneity; AMM, Derek Bailey, Peter Brötzmann",
            "Minimalism":         "Gradual process, repetition; Steve Reich, Philip Glass, Terry Riley",
            "Glitch":             "Digital errors as aesthetic; Oval, Autechre, Tim Hecker",
            "Drone":              "Sustained tones, hypnotic; La Monte Young, Sunn O))), Earth",
            "Acousmatic":         "Loudspeaker-only performance, spatially composed; Jonty Harrison, Denis Smalley",
        },

        # ── REPRÄSENTATIVE KÜNSTLER ──
        "iconic_artists": [
            "John Cage", "Karlheinz Stockhausen", "Brian Eno", "Arnold Schoenberg",
            "Ornette Coleman", "Iannis Xenakis", "Merzbow", "Pierre Schaeffer"
        ],
        "modern_artists": [
            "Arca", "Holly Herndon", "Matmos", "Tim Hecker", "Jlin"
        ],

        # ── SONG-WRITING TIPPS ──
        "writing_tips": [
            "Define your concept first — what system or process generates the music",
            "Constraints can be liberating — set arbitrary rules and follow them strictly",
            "Learn the tradition you're reacting against — transgression requires knowledge",
            "The listener's perception is your instrument — manipulate expectation deliberately",
            "Silence is as compositional as sound — use it structurally",
            "Extended techniques transform familiar instruments into unfamiliar sound sources",
            "Process and improvisation can be scored — notate the instructions, not the result"
        ],
        "avoid": [
            "Random weirdness without conceptual justification — experimental ≠ arbitrary",
            "Ignoring the performance/presentation context — where and how it's heard matters",
            "Confusing technical complexity with artistic depth",
            "Alienating the audience without a meaningful payoff",
            "Avant-garde posturing — the concept must generate genuine sonic experience"
        ],
    },

    "Classics": {
        # ── VIBES & ATMOSPHÄRE ──
        "vibes": [
            "timeless elegance", "nostalgic warmth", "romantic charm", "sophisticated",
            "cinematic", "bittersweet", "wistful", "joyful (swing era)", "innocent romance",
            "ballroom grandeur", "intimate torch song", "supper-club refinement"
        ],
        "anti_vibes": [
            "aggressive", "lo-fi raw", "modern cynicism", "digitally sterile",
            "post-modern irony", "vulgar", "rhythmically primitive"
        ],

        # ── TONARTEN & HARMONIE ──
        "preferred_keys": ["C major", "F major", "Bb major", "Eb major", "G major", "D major", "A minor"],
        "chord_progressions": [
            "I-vi-ii-V (1950s 'do-wop' turnaround)",
            "I-IV-V-I (Tin Pan Alley diatonic)",
            "iii-VI7-ii-V7-I (circle of fifths descent)",
            "I-bVII7-IV-I (jazz-pop bridge)",
            "ii-V-I (bebop-influenced standards)",
            "I-I7-IV-iv-I (blues-pop hybrid)",
            "Chromatic descending bass: I-I/7-vi-vi/5-IV-IVm-I (sophisticated ballad)"
        ],
        "harmonic_feel": (
            "Pre-1960 popular music inhabits the space between simple diatonic songwriting and jazz sophistication. "
            "Extended chords (7ths, 9ths) appear naturally without being academic. "
            "The Great American Songbook (Gershwin, Berlin, Porter, Kern) set the harmonic template: "
            "diatonic with jazz-inflected passages, unexpected but immediately satisfying progressions. "
            "Modulation is used for emotional climax (key change into final chorus)."
        ),
        "modes": ["Ionian (major)", "Aeolian (ballads)", "Mixolydian (blues-pop)", "Dorian (occasional jazz influence)"],

        # ── RHYTHMUS & TEMPO ──
        "bpm_ranges": {
            "slow": "55-75",
            "mid":  "80-140",
            "fast": "140-220"
        },
        "time_signatures": ["4/4", "3/4 (waltz — very common)", "2/4 (march, quickstep)", "6/8"],
        "rhythm_feel": (
            "Pre-1960 music spans the swing of the Big Band era to the half-time ballad, the boogie-woogie, "
            "the waltz, and the shuffle. Swing feel (long-short triplet) is foundational. "
            "Rock and roll (1955–1959) brought the straight 8th backbeat into popular music."
        ),
        "groove_type": "swing (big band), half-time ballad, waltz, boogie-woogie, early rock-and-roll shuffle",

        # ── INSTRUMENTE & SOUND ──
        "core_instruments": [
            "piano", "upright bass", "drums (jazz kit or brushes)", "brass section (big band)",
            "lead vocalist with microphone (period-accurate reverb)"
        ],
        "optional_instruments": [
            "string orchestra", "clarinet (swing era)", "guitar (acoustic or hollow-body electric)",
            "accordion (European pop)", "banjo (1920s Dixieland)"
        ],
        "signature_sounds": [
            "period-accurate plate reverb on vocals", "warm mono recording texture",
            "big band brass hit", "swinging piano boogie-woogie left hand",
            "brushed snare drum", "vocal vibrato of the crooner tradition",
            "warm string pad (Hollywood orchestration)"
        ],
        "production_style": (
            "Pre-1960 recordings were mono, often recorded live with orchestra. "
            "Warm microphone tone (ribbon mics), natural room acoustics, and minimal editing define the era. "
            "Modern recreations use period-accurate compression, plate reverb simulation, "
            "and mono or near-mono panning to capture the vintage quality. "
            "The imperfections of analog tape and early recording are part of the aesthetic."
        ),
        "mix_character": "warm mono or narrow stereo, vintage tape saturation, vocal-forward, natural room reverb, period-authentic",

        # ── LYRIK & TEXTE ──
        "lyric_themes": [
            "romantic love (courtly, restrained)", "longing and heartbreak",
            "the big city and its romance", "dancing and glamour",
            "hope and optimism (post-war)", "nostalgia and memory",
            "humor and wit (Cole Porter tradition)", "patriotism (wartime)",
            "nature and seasons as metaphor", "standard imagery: moon, stars, rain, love's pain",
            "social class and aspiration", "innocence of youth"
        ],
        "lyric_style": (
            "The Great American Songbook tradition elevated popular lyric to literary art. "
            "Wit, elegance, and emotional precision coexist. Cole Porter's sophistication, "
            "Lorenz Hart's melancholy, and Ira Gershwin's playfulness define the range. "
            "Lyrics are meant to be understood immediately but reward closer reading. "
            "Imagery is conventional but used with craft and freshness."
        ),
        "language_register": "formal-elegant, 1920s–1950s American English, witty, emotionally restrained but felt",
        "pov_typical": "first person romantic confession or observer; direct address to beloved",
        "rhyme_schemes": ["AABA (standard song form)", "ABAB", "AABB", "sophisticated internal rhyme (Porter)"],
        "line_length": "medium, iambic tendency, fits the melodic phrase precisely — lyrics and melody written together",

        # ── SONG-STRUKTUR ──
        "typical_structure": "Verse (ad lib intro) – AABA chorus (32 bars) — or Verse–Chorus in popular song form",
        "intro_style": "Orchestra intro or piano intro establishing key and character; 4–8 bars before vocal verse",
        "chorus_character": "The 32-bar AABA form IS the song — memorable, melodically peaked at the B section (bridge)",
        "bridge_role": "The B section of AABA — harmonic adventure, often to a distant key or emotional peak",
        "outro_style": "Final A section, ritardando, instrumental tag; or 'button' (rhythmic final chord)",

        # ── FUSION-KOMPATIBILITÄT ──
        "fuses_well_with": ["Jazz", "Classical", "Pop (retro)", "Blues", "Gospel", "R&B (early)"],
        "fusion_tension_with": ["Metal", "Hip-Hop", "EDM (pure electronic)"],
        "bridge_elements": [
            "AABA song form (→ Jazz, Pop sophisticated)",
            "big band orchestration (→ Jazz, Swing)",
            "romantic lyric tradition (→ R&B ballad, Pop)",
            "32-bar harmonic cycle (→ Jazz improvisation)",
            "crooner vocal style (→ Pop vocal tradition)"
        ],

        # ── SUNO/UDIO PROMPT TAGS ──
        "suno_tags": [
            "vintage", "jazz standard", "big band", "1940s", "1950s",
            "swing", "crooner", "retro", "piano", "orchestral pop",
            "romantic ballad", "torch song", "tin pan alley", "old Hollywood",
            "warm mono recording"
        ],
        "negative_tags": ["modern production", "808 bass", "autotune", "EDM synth", "trap beat"],

        # ── EMOTIONALE DNA ──
        "emotional_spectrum": {
            "primary": ["romantic longing", "nostalgia", "elegant joy"],
            "secondary": ["wistfulness", "charm", "bittersweet hope"],
            "forbidden": ["modern cynicism", "aggression", "emotional rawness without grace"]
        },
        "listener_state": "The listener wants to feel transported to an era of elegance, romance, and graceful emotional expression — in a supper club, at a classic cinema, or in warm nostalgia.",
        "cultural_context": (
            "Pre-1960 popular music is anchored in the Great American Songbook (1920s–1950s) — "
            "the songs of Gershwin, Berlin, Porter, Kern, and Rodgers that defined American popular culture. "
            "Big band swing, the crooner era (Sinatra, Bing Crosby), and early rock and roll (Chuck Berry, "
            "Little Richard, Buddy Holly) all belong here. "
            "This music carries the aesthetic of Hollywood's golden age, the optimism of post-war America, "
            "and the formal elegance of an era before the counterculture broke every convention."
        ),

        # ── SUB-GENRES & VARIANTEN ──
        "sub_genres": {
            "Tin Pan Alley":      "1920s–40s songwriting tradition; Gershwin, Berlin, Porter, Kern; formal elegance",
            "Big Band Swing":     "1930s–40s; large ensemble, danceable; Ellington, Goodman, Glenn Miller",
            "Crooner Ballad":     "1940s–50s vocal romanticism; Frank Sinatra, Bing Crosby, Nat King Cole",
            "Jump Blues":         "High-energy boogie blues-pop; Louis Jordan, Wynonie Harris",
            "Doo-Wop":            "Vocal group harmony, 1950s pop; The Platters, Drifters, Coasters",
            "Early Rock & Roll":  "1954–1959 synthesis of blues, country, R&B; Chuck Berry, Little Richard, Buddy Holly",
            "Cabaret/Chanson":    "European tradition; Édith Piaf, Marlene Dietrich, Kurt Weill; theatrical intimacy",
            "Torch Song":         "Intimate, heartbreak ballad; Billie Holiday, Helen Morgan; stripped-down pain",
        },

        # ── REPRÄSENTATIVE KÜNSTLER ──
        "iconic_artists": [
            "Frank Sinatra", "Ella Fitzgerald", "Nat King Cole", "Billie Holiday",
            "Bing Crosby", "Louis Armstrong", "Duke Ellington", "Glenn Miller",
            "Chuck Berry", "Édith Piaf"
        ],
        "modern_artists": [
            "Michael Bublé", "Diana Krall", "Norah Jones", "Tony Bennett (late era)", "Gregory Porter"
        ],

        # ── SONG-WRITING TIPPS ──
        "writing_tips": [
            "Master the AABA form — 32 bars of A-A-B-A is the architecture of hundreds of standards",
            "The B section (bridge) must go somewhere harmonically unexpected before returning home",
            "Write melody and lyric simultaneously — they are inseparable in this tradition",
            "Wit and elegance over raw emotion — the craft of restraint is the emotional technique",
            "The title should appear in the final A section — it is the emotional payoff",
            "Study Cole Porter's inner rhymes and Lorenz Hart's unexpected rhyme solutions",
            "The orchestration should illustrate the lyric — string swells, brass stabs should be text-painted"
        ],
        "avoid": [
            "Modern slang and contemporary cultural references that break the period illusion",
            "Harmonic choices that sound too modern (trap, pop production)",
            "Abandoning the formal elegance for self-indulgent excess",
            "Ignoring the singer's breath — this music is written for the human voice",
            "Unresolved dissonance without the harmonic grace that the idiom demands"
        ],
    },
}


# ═══════════════════════════════════════════════════════════════════════════
# HELPER FUNCTIONS
# ═══════════════════════════════════════════════════════════════════════════

def get_genre_style(genre: str) -> dict:
    """Gibt das vollständige Stilprofil eines Genres zurück."""
    return GENRE_STYLE_LIBRARY.get(genre, {})


def get_vibes(genre: str) -> list:
    """Gibt die Vibes/Atmosphären eines Genres zurück."""
    return GENRE_STYLE_LIBRARY.get(genre, {}).get("vibes", [])


def get_suno_tags(genre1: str, genre2: str = None) -> list:
    """
    Gibt Suno/Udio Prompt Tags zurück.
    Bei zwei Genres: kombiniert die Tags beider Genres für Fusion-Prompts.
    """
    tags1 = set(GENRE_STYLE_LIBRARY.get(genre1, {}).get("suno_tags", []))
    if genre2:
        tags2 = set(GENRE_STYLE_LIBRARY.get(genre2, {}).get("suno_tags", []))
        return list(tags1.union(tags2))
    return list(tags1)


def get_fusion_compatibility(genre1: str, genre2: str) -> dict:
    """
    Analysiert die Fusion-Kompatibilität zweier Genres.

    Returns:
        dict mit:
            - compatibility: 'high', 'tension', oder 'neutral'
            - bridge_elements: gemeinsame Brücken-Elemente
            - shared_vibes: geteilte Atmosphären
            - shared_themes: geteilte lyrische Themen
            - recommended_tags: Suno/Udio Tags für den Fusion-Prompt
    """
    g1 = GENRE_STYLE_LIBRARY.get(genre1, {})
    g2 = GENRE_STYLE_LIBRARY.get(genre2, {})

    fuses_well = (
        genre2 in g1.get("fuses_well_with", []) or
        genre1 in g2.get("fuses_well_with", [])
    )
    tension = (
        genre2 in g1.get("fusion_tension_with", []) or
        genre1 in g2.get("fusion_tension_with", [])
    )
    bridges = list(set(g1.get("bridge_elements", []) + g2.get("bridge_elements", [])))
    shared_vibes = [v for v in g1.get("vibes", []) if v in g2.get("vibes", [])]
    shared_themes = [t for t in g1.get("lyric_themes", []) if t in g2.get("lyric_themes", [])]

    # Build recommended tags (deduplicated union minus negatives)
    tags1 = set(g1.get("suno_tags", []))
    tags2 = set(g2.get("suno_tags", []))
    neg1 = set(g1.get("negative_tags", []))
    neg2 = set(g2.get("negative_tags", []))
    combined_tags = (tags1.union(tags2)) - neg1 - neg2

    return {
        "compatibility": "high" if fuses_well else ("tension" if tension else "neutral"),
        "bridge_elements": bridges,
        "shared_vibes": shared_vibes,
        "shared_themes": shared_themes,
        "recommended_suno_tags": list(combined_tags),
    }


def get_bpm_for_mood(genre: str, mood: str = "mid") -> str:
    """
    Gibt den BPM-Bereich eines Genres für eine Stimmung zurück.

    Args:
        genre: Genre-Name
        mood: 'slow', 'mid', oder 'fast'
    """
    ranges = GENRE_STYLE_LIBRARY.get(genre, {}).get("bpm_ranges", {})
    return ranges.get(mood, "unbekannt")


def get_writing_tips(genre: str) -> list:
    """Gibt die Songwriting-Tipps für ein Genre zurück."""
    return GENRE_STYLE_LIBRARY.get(genre, {}).get("writing_tips", [])


def get_sub_genres(genre: str) -> dict:
    """Gibt alle Sub-Genres eines Genres mit Beschreibung zurück."""
    return GENRE_STYLE_LIBRARY.get(genre, {}).get("sub_genres", {})


def get_iconic_artists(genre: str) -> list:
    """Gibt die ikonischen Künstler eines Genres zurück."""
    return GENRE_STYLE_LIBRARY.get(genre, {}).get("iconic_artists", [])


def get_chord_progressions(genre: str) -> list:
    """Gibt die typischen Akkordfolgen eines Genres zurück."""
    return GENRE_STYLE_LIBRARY.get(genre, {}).get("chord_progressions", [])


def get_lyric_themes(genre: str) -> list:
    """Gibt die lyrischen Themen eines Genres zurück."""
    return GENRE_STYLE_LIBRARY.get(genre, {}).get("lyric_themes", [])


def get_emotional_dna(genre: str) -> dict:
    """Gibt die emotionale DNA eines Genres zurück."""
    return GENRE_STYLE_LIBRARY.get(genre, {}).get("emotional_spectrum", {})


def list_all_genres() -> list:
    """Gibt alle verfügbaren Genres zurück."""
    return list(GENRE_STYLE_LIBRARY.keys())


def search_genres_by_vibe(vibe: str) -> list:
    """
    Sucht alle Genres, die eine bestimmte Vibe enthalten.

    Args:
        vibe: Stimmungs-/Atmosphäre-Begriff (case-insensitive)
    Returns:
        Liste der passenden Genre-Namen
    """
    vibe_lower = vibe.lower()
    return [
        genre for genre, data in GENRE_STYLE_LIBRARY.items()
        if any(vibe_lower in v.lower() for v in data.get("vibes", []))
    ]


def build_prompt_for_ai(
    genre: str,
    sub_genre: str = None,
    mood: str = "mid",
    fusion_genre: str = None
) -> str:
    """
    Generiert einen strukturierten KI-Prompt für Suno/Udio.

    Args:
        genre: Haupt-Genre
        sub_genre: Optionales Sub-Genre
        mood: 'slow', 'mid', oder 'fast'
        fusion_genre: Optionales zweites Genre für Fusion
    Returns:
        Fertiger Prompt-String
    """
    g = GENRE_STYLE_LIBRARY.get(genre, {})
    if not g:
        return f"Genre '{genre}' not found."

    tags = g.get("suno_tags", [])[:8]
    bpm = g.get("bpm_ranges", {}).get(mood, "120")
    vibe = ", ".join(g.get("vibes", [])[:3])
    feel = g.get("rhythm_feel", "")
    prod = g.get("production_style", "")

    prompt_parts = [f"{genre}"]
    if sub_genre:
        prompt_parts.append(sub_genre)
    if fusion_genre:
        g2 = GENRE_STYLE_LIBRARY.get(fusion_genre, {})
        extra_tags = g2.get("suno_tags", [])[:4]
        tags = list(set(tags + extra_tags))
        prompt_parts.append(f"{fusion_genre} fusion")

    prompt_parts.append(f"BPM {bpm}")
    prompt_parts.extend(tags[:10])
    prompt_parts.append(f"vibe: {vibe}")

    return ", ".join(prompt_parts)


# ═══════════════════════════════════════════════════════════════════════════
# QUICK REFERENCE: ALLE GENRES MIT KERN-ATTRIBUTEN
# ═══════════════════════════════════════════════════════════════════════════

GENRE_QUICK_REFERENCE = {
    genre: {
        "vibes":       data.get("vibes", [])[:3],
        "bpm_mid":     data.get("bpm_ranges", {}).get("mid", "?"),
        "key_tags":    data.get("suno_tags", [])[:5],
        "top_artists": data.get("iconic_artists", [])[:3],
        "structure":   data.get("typical_structure", "?"),
    }
    for genre, data in GENRE_STYLE_LIBRARY.items()
}


if __name__ == "__main__":
    # ── Demo-Ausgabe ──
    print("=" * 65)
    print("HIRSCH MUSIC HIT MAKER — Genre Style Library v1.0")
    print("=" * 65)
    print(f"\nVerfügbare Genres ({len(GENRE_STYLE_LIBRARY)}):")
    for i, genre in enumerate(list_all_genres(), 1):
        g = GENRE_STYLE_LIBRARY[genre]
        bpm = g.get("bpm_ranges", {}).get("mid", "?")
        vibes = ", ".join(g.get("vibes", [])[:2])
        print(f"  {i:2}. {genre:<20} BPM {bpm:<12} [{vibes}]")

    print("\n" + "─" * 65)
    print("FUSION BEISPIEL: Rock + Blues")
    print("─" * 65)
    result = get_fusion_compatibility("Rock", "Blues")
    print(f"  Kompatibilität:  {result['compatibility'].upper()}")
    print(f"  Shared Vibes:    {result['shared_vibes']}")
    print(f"  Bridge Elements: {result['bridge_elements'][:3]}")
    print(f"  Suno Tags ({len(result['recommended_suno_tags'])}): "
          f"{result['recommended_suno_tags'][:8]}")

    print("\n" + "─" * 65)
    print("PROMPT BUILDER BEISPIEL: Jazz, slow mood")
    print("─" * 65)
    prompt = build_prompt_for_ai("Jazz", mood="slow", fusion_genre="Blues")
    print(f"  {prompt}")

    print("\n" + "─" * 65)
    print("VIBE SEARCH: 'nostalgic'")
    print("─" * 65)
    nostalgic_genres = search_genres_by_vibe("nostalgic")
    print(f"  Genres mit 'nostalgic': {nostalgic_genres}")

    print("\n✓ Genre Style Library erfolgreich geladen.")
