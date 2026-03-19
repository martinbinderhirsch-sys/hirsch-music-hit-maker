// ════════════════════════════════════════════════════════════════════════════
// SONG FUSION MATCHER ENGINE
// Analysiert jeden Song nach 8 Dimensionen und findet optimale Paare
// ════════════════════════════════════════════════════════════════════════════

// ─── DIMENSION PROFILES ─────────────────────────────────────────────────────
// Jeder Song bekommt automatisch ein Profil basierend auf:
// energy (0-10), valence (0-10, negativ→positiv), tempo (0-10),
// aggression (0-10), romantik (0-10), rebellion (0-10),
// theme (Array), mood (String)

const GENRE_BASE = {
  Rock:         { energy:7, valence:5, tempo:6, aggression:5, romantik:3, rebellion:7 },
  Pop:          { energy:6, valence:8, tempo:7, aggression:1, romantik:7, rebellion:2 },
  'Hip-Hop':    { energy:7, valence:5, tempo:7, aggression:7, romantik:4, rebellion:8 },
  Metal:        { energy:9, valence:3, tempo:8, aggression:9, romantik:2, rebellion:9 },
  Country:      { energy:5, valence:6, tempo:5, aggression:2, romantik:8, rebellion:4 },
  EDM:          { energy:9, valence:7, tempo:9, aggression:3, romantik:5, rebellion:3 },
  Schlager:     { energy:5, valence:9, tempo:5, aggression:1, romantik:9, rebellion:1 },
  Classical:    { energy:4, valence:6, tempo:4, aggression:1, romantik:8, rebellion:1 },
  Jazz:         { energy:5, valence:7, tempo:6, aggression:2, romantik:7, rebellion:5 },
  Blues:        { energy:5, valence:3, tempo:4, aggression:4, romantik:6, rebellion:7 },
  Folk:         { energy:3, valence:6, tempo:3, aggression:1, romantik:7, rebellion:5 },
  'R&B':        { energy:6, valence:7, tempo:6, aggression:2, romantik:9, rebellion:4 },
  Gospel:       { energy:7, valence:9, tempo:6, aggression:1, romantik:6, rebellion:2 },
  Latin:        { energy:8, valence:9, tempo:8, aggression:2, romantik:8, rebellion:3 },
  Reggae:       { energy:5, valence:7, tempo:5, aggression:2, romantik:6, rebellion:7 },
  World:        { energy:6, valence:7, tempo:6, aggression:2, romantik:6, rebellion:4 },
  Experimental: { energy:5, valence:3, tempo:4, aggression:4, romantik:3, rebellion:9 },
};

// Keyword → Theme Tags (auf Titeln basierend)
const THEME_KEYWORDS = {
  love:      ['love','liebe','herz','heart','girl','boy','baby','darling','honey','mein','dein','ich lieb','forever','always','angel','rosa','schön','beautiful','sweetie','sugar','kiss','romance'],
  loss:      ['goodbye','farewell','leaving','gone','lost','broken','tears','cry','miss','alone','empty','lonely','ohne dich','vermiss','weinen','schmerz','pain','hurt','fade','end'],
  party:     ['party','dance','night','club','floor','celebrate','fun','beat','jump','move','rhythm','shake','tonight','saturday','friday','weekend','fiesta','boom'],
  rebellion: ['fight','war','rebel','resist','rage','anger','destroy','hell','fire','burn','revolution','protest','against','rise','system','freedom','frei','wut','kämpf'],
  journey:   ['road','highway','ride','drive','travel','run','way','path','go','come','home','back','return','weg','reise','fahrt','walk','fly','wing'],
  nostalgia: ['remember','memory','yesterday','back in','old','time','young','past','history','einst','damals','früher','childhood','golden','classic','once'],
  power:     ['strong','power','champion','win','top','king','queen','boss','number one','best','greatest','unstoppable','unbreakable','sieger','stark','kraft'],
  nature:    ['sun','moon','star','sky','rain','wind','river','mountain','ocean','sea','land','earth','green','blue','gold','silver','natur','berg','see'],
  spiritual: ['god','heaven','angel','soul','spirit','holy','divine','prayer','faith','hope','light','dark','eternal','dream','vision','gott','himmel','seele'],
  street:    ['street','hood','ghetto','block','city','town','real','hustle','grind','game','trap','thug','gang','respect','street','urban'],
};

// Stimmungs-Keywords → Mood
const MOOD_PATTERNS = {
  euphoric:   ['amazing','fantastic','incredible','ecstasy','high','fly','heaven','joy','happy','glück','wunder','fantastisch'],
  melancholic:['sad','lonely','blue','grey','gray','tears','cry','lost','broken','traurig','einsam','weinen','dunkel'],
  aggressive: ['fight','kill','hate','rage','burn','destroy','crush','smash','wut','hass','zerstör','krieg'],
  romantic:   ['love','kiss','hold','touch','feel','heart','close','tender','liebe','küss','halt','zärtlich'],
  anthemic:   ['rise','stand','together','we are','unite','victory','loud','proud','strong','zusammen','steh auf'],
  mysterious: ['shadow','dark','night','secret','unknown','hidden','mystery','dunkel','schatten','geheim'],
  energetic:  ['run','go','race','speed','fast','rush','wild','crazy','verrückt','schnell','rennen','wild'],
  peaceful:   ['calm','still','quiet','peace','gentle','soft','breath','ruhe','stille','sanft','frieden'],
};

// Dekaden-Kompatibilität (näher = kompatibler)
function decadeCompat(y1, y2) {
  const d1 = Math.floor(y1 / 10) * 10;
  const d2 = Math.floor(y2 / 10) * 10;
  const diff = Math.abs(d1 - d2) / 10;
  // 0 Dekaden Abstand = 1.0, 1 = 0.85, 2 = 0.65, 3+ = 0.4
  return [1.0, 0.85, 0.65, 0.5, 0.4][Math.min(diff, 4)];
}

// ─── PROFIL BERECHNEN ───────────────────────────────────────────────────────
function buildProfile(song) {
  const base = GENRE_BASE[song.genre] || GENRE_BASE.Pop;
  const titleLow = (song.title + ' ' + (song.artist||'')).toLowerCase();
  const albumLow = (song.album||'').toLowerCase();
  const allText = titleLow + ' ' + albumLow;

  // Themes erkennen
  const themes = [];
  for (const [theme, kws] of Object.entries(THEME_KEYWORDS)) {
    if (kws.some(kw => allText.includes(kw))) themes.push(theme);
  }
  if (!themes.length) themes.push('general');

  // Mood erkennen
  let mood = 'neutral';
  let maxMoodScore = 0;
  for (const [m, kws] of Object.entries(MOOD_PATTERNS)) {
    const score = kws.filter(kw => allText.includes(kw)).length;
    if (score > maxMoodScore) { maxMoodScore = score; mood = m; }
  }

  // Jahr-basierte Energie-Modifikation
  const yearBoost = song.year >= 2000 ? 0.5 : song.year >= 1985 ? 0.25 : 0;
  const energy = Math.min(10, base.energy + (themes.includes('party') ? 1 : 0) + (themes.includes('rebellion') ? 0.5 : 0) + yearBoost);

  return {
    ...base,
    energy: Math.round(energy * 10) / 10,
    themes,
    mood,
    decade: Math.floor(song.year / 10) * 10,
  };
}

// ─── MATCH SCORE BERECHNEN ──────────────────────────────────────────────────
function matchScore(s1, s2) {
  const p1 = buildProfile(s1);
  const p2 = buildProfile(s2);

  // 1. Energie-Kompatibilität (ähnlich = gut, zu gleich = langweilig, zu unterschiedlich = clash)
  const energyDiff = Math.abs(p1.energy - p2.energy);
  const energyScore = energyDiff <= 1 ? 0.95 : energyDiff <= 2 ? 0.80 : energyDiff <= 3 ? 0.60 : energyDiff <= 4 ? 0.40 : 0.20;

  // 2. Themen-Überschneidung
  const sharedThemes = p1.themes.filter(t => p2.themes.includes(t));
  const themeScore = sharedThemes.length > 0
    ? Math.min(1, 0.5 + sharedThemes.length * 0.25)
    : 0.25;

  // 3. Stimmungs-Kompatibilität
  const moodCompat = {
    euphoric:    { euphoric:1.0, energetic:0.85, anthemic:0.75, romantic:0.5, melancholic:0.2, aggressive:0.4, peaceful:0.4, mysterious:0.3, neutral:0.5 },
    melancholic: { melancholic:1.0, romantic:0.8, peaceful:0.75, mysterious:0.7, euphoric:0.2, aggressive:0.3, energetic:0.3, anthemic:0.4, neutral:0.5 },
    aggressive:  { aggressive:1.0, energetic:0.8, anthemic:0.7, mysterious:0.6, euphoric:0.4, melancholic:0.3, romantic:0.2, peaceful:0.1, neutral:0.4 },
    romantic:    { romantic:1.0, melancholic:0.8, peaceful:0.75, euphoric:0.5, anthemic:0.4, mysterious:0.5, aggressive:0.2, energetic:0.3, neutral:0.5 },
    anthemic:    { anthemic:1.0, energetic:0.85, aggressive:0.7, euphoric:0.75, mysterious:0.4, romantic:0.4, melancholic:0.3, peaceful:0.3, neutral:0.5 },
    mysterious:  { mysterious:1.0, melancholic:0.7, aggressive:0.6, romantic:0.5, peaceful:0.5, euphoric:0.3, energetic:0.4, anthemic:0.4, neutral:0.5 },
    energetic:   { energetic:1.0, anthemic:0.85, aggressive:0.8, euphoric:0.85, mysterious:0.4, melancholic:0.3, romantic:0.3, peaceful:0.2, neutral:0.5 },
    peaceful:    { peaceful:1.0, romantic:0.75, melancholic:0.7, mysterious:0.6, euphoric:0.4, neutral:0.55, anthemic:0.3, energetic:0.2, aggressive:0.1 },
    neutral:     { neutral:0.7, euphoric:0.5, melancholic:0.5, romantic:0.5, anthemic:0.5, mysterious:0.5, energetic:0.5, peaceful:0.55, aggressive:0.4 },
  };
  const moodScore = (moodCompat[p1.mood] || moodCompat.neutral)[p2.mood] || 0.5;

  // 4. Genre-Fusion-Bonus (cross-genre ist interessanter)
  const genreFusionBonus = s1.genre !== s2.genre ? 0.15 : 0;

  // 5. Dekaden-Kompatibilität
  const decScore = decadeCompat(s1.year, s2.year);

  // 6. Valence-Balance (Kontrast kann spannend sein)
  const valenceDiff = Math.abs(p1.valence - p2.valence);
  const valenceScore = valenceDiff >= 2 && valenceDiff <= 4 ? 0.85 : valenceDiff <= 1 ? 0.75 : 0.55;

  // Gewichteter Gesamt-Score
  const total = (
    energyScore   * 0.25 +
    themeScore    * 0.30 +
    moodScore     * 0.25 +
    valenceScore  * 0.10 +
    decScore      * 0.10
  ) + genreFusionBonus;

  return {
    score: Math.min(1, total),
    sharedThemes,
    mood1: p1.mood, mood2: p2.mood,
    energy1: p1.energy, energy2: p2.energy,
    themes1: p1.themes, themes2: p2.themes,
    genreFusion: s1.genre !== s2.genre,
  };
}

// ─── FUSION-KONZEPT GENERIEREN ───────────────────────────────────────────────
function generateFusionConcept(s1, s2, matchInfo) {
  const { sharedThemes, mood1, mood2, energy1, energy2, genreFusion } = matchInfo;

  // Fusion-Titel
  const titleWords1 = s1.title.split(/\s+/).filter(w => w.length > 3);
  const titleWords2 = s2.title.split(/\s+/).filter(w => w.length > 3);
  const w1 = titleWords1[0] || s1.title.split(' ')[0];
  const w2 = titleWords2[titleWords2.length-1] || s2.title.split(' ').pop();
  const fusionTitles = [
    `${w1} ${w2}`,
    `${w2} of ${w1}`,
    `${s1.artist.split(' ')[0]} × ${s2.artist.split(' ')[0]}`,
    `Between ${w1} and ${w2}`,
  ];
  const fusionTitle = fusionTitles[Math.floor(Math.random() * fusionTitles.length)];

  // Stil-Beschreibung
  const avgEnergy = (energy1 + energy2) / 2;
  const energyDesc = avgEnergy >= 8 ? 'hochenergetisch und treibend' : avgEnergy >= 6 ? 'dynamisch und mitreißend' : avgEnergy >= 4 ? 'ausgewogen und melodisch' : 'ruhig und atmosphärisch';

  // Genre-Fusion-Beschreibung
  const styleBlend = genreFusion
    ? `Ein ${s1.genre}/${s2.genre}-Hybrid`
    : `Ein reiner ${s1.genre}-Song mit neuem Fokus`;

  // Themen-Konzept
  const mainTheme = sharedThemes.length > 0 ? sharedThemes[0] : (matchInfo.themes1[0] || 'general');
  const themeDescriptions = {
    love:      'Liebe, Sehnsucht und emotionale Verbindung',
    loss:      'Verlust, Abschied und innerer Schmerz',
    party:     'Feier, Freiheit und ungehemmte Energie',
    rebellion: 'Aufstand, Widerstand und Freiheitsdrang',
    journey:   'Aufbruch, Reise und Selbstfindung',
    nostalgia: 'Erinnerung, Vergänglichkeit und goldene Zeiten',
    power:     'Stärke, Triumph und Selbstbewusstsein',
    nature:    'Natur, Schönheit und universelle Verbundenheit',
    spiritual: 'Spiritualität, Transzendenz und tiefe Bedeutung',
    street:    'Straßenleben, Authentizität und urbane Realität',
    general:   'Universelle menschliche Erfahrungen',
  };

  // Struktur-Vorschlag
  const structures = [
    { name: 'Verse–Pre-Chorus–Chorus–Bridge', desc: 'Klassischer Hit-Aufbau mit emotionalem Höhepunkt' },
    { name: 'Intro–Verse–Chorus–Verse–Chorus–Breakdown–Finale', desc: 'Epischer Aufbau mit dramatischem Breakdown' },
    { name: 'Verse–Chorus–Verse–Chorus–Bridge–Outro', desc: 'Standard-Pop-Struktur, zugänglich und eingängig' },
    { name: 'Intro–Hook–Verse–Hook–Bridge–Hook', desc: 'Hook-zentriert für maximale Eingängigkeit' },
  ];
  const structure = structures[Math.floor(Math.abs(s1.id + s2.id) % structures.length)];

  // Mood-Kombination
  const moodBlend = mood1 === mood2
    ? `Durchgehend ${moodLabel(mood1)}`
    : `Wechsel zwischen ${moodLabel(mood1)} und ${moodLabel(mood2)}`;

  // Songtext-Konzept
  const lyricConcept = buildLyricConcept(s1, s2, mainTheme, mood1, mood2);

  return {
    fusionTitle,
    styleBlend,
    energyDesc,
    themeDesc: themeDescriptions[mainTheme] || themeDescriptions.general,
    mainTheme,
    moodBlend,
    structure,
    lyricConcept,
    influences: [s1.artist, s2.artist],
    genres: [s1.genre, s2.genre],
  };
}

function moodLabel(m) {
  const labels = { euphoric:'euphorisch', melancholic:'melancholisch', aggressive:'aggressiv', romantic:'romantisch', anthemic:'anthem-artig', mysterious:'geheimnisvoll', energetic:'energetisch', peaceful:'ruhig', neutral:'neutral' };
  return labels[m] || m;
}

function buildLyricConcept(s1, s2, theme, mood1, mood2) {
  const concepts = {
    love: {
      euphoric:  `Vers: Das überwältigende Gefühl wenn zwei Welten aufeinanderprallen\nRefrain: "Ich finde dich in jedem Song, in jeder Nacht"\nBridge: Zweifeln und dann doch loslassen`,
      melancholic:`Vers: Die Leere nach einer verlorenen Liebe, die noch nachhallt\nRefrain: "Du bist in der Stille, du bist in der Musik"\nBridge: Hoffnung, dass Musik heilt`,
      romantic:  `Vers: Ein Moment der Verbindung, zwei Fremde erkennen sich in einem Song\nRefrain: "Diese Melodie gehört nur uns beiden"\nBridge: Die Ewigkeit eines Moments`,
    },
    rebellion: {
      aggressive:`Vers: Die Wut über das System, das einen klein halten will\nRefrain: "Wir brennen lauter als sie wollten"\nBridge: Der Preis der Freiheit`,
      anthemic:  `Vers: Aufstehen gegen Ungerechtigkeit, zusammen stärker\nRefrain: "Unser Lärm ist unser Recht"\nBridge: Was bleibt wenn der Staub sich legt`,
      energetic: `Vers: Volle Fahrt voraus, kein Zurückschauen\nRefrain: "Schneller, lauter, weiter — niemand hält mich auf"\nBridge: Der Moment wo alles zusammenbricht und neu entsteht`,
    },
    journey: {
      nostalgic: `Vers: Die Straße, die immer weiterführt, die Dinge die man zurücklässt\nRefrain: "Irgendwo zwischen gestern und morgen"\nBridge: Heimweh und Fernweh gleichzeitig`,
      energetic: `Vers: Der erste Schritt in eine unbekannte Richtung\nRefrain: "Die Welt ist größer als jeder Song"\nBridge: Was man findet wenn man aufhört zu suchen`,
    },
    party: {
      euphoric:  `Vers: Diese eine Nacht, diese eine Frequenz, diese eine Verbindung\nRefrain: "Wenn der Beat uns findet sind wir unsterblich"\nBridge: Der Moment kurz vor dem Morgengrauen`,
      energetic: `Vers: Alles loslassen, der Rhythmus übernimmt\nRefrain: "Lass die Musik entscheiden wer du heute bist"\nBridge: Die Stille danach`,
    },
  };

  const themeConcept = concepts[theme];
  if (themeConcept) {
    const moodKey = [mood1, mood2].find(m => themeConcept[m]) || Object.keys(themeConcept)[0];
    return themeConcept[moodKey];
  }

  // Fallback
  return `Vers: Die Geschichte von ${s1.artist} trifft auf die Energie von ${s2.artist}\nRefrain: Ein neuer Sound aus zwei verschiedenen Welten\nBridge: Was entsteht wenn Grenzen verschwinden`;
}

// ─── TOP-MATCHES FINDEN ──────────────────────────────────────────────────────
// Findet die N besten Matches für einen gegebenen Song (aus Sample)
function findTopMatches(sourceSong, allSongs, topN = 10, sampleSize = 500) {
  // Random Sample für Performance (aus allen Genres)
  const genres = ['Rock','Pop','Hip-Hop','Metal','Country','EDM','Schlager','Classical','Jazz','Blues','Folk','R&B','Gospel','Latin','Reggae','World','Experimental'];
  const perGenre = Math.floor(sampleSize / genres.length);
  let pool = [];
  genres.forEach(g => {
    const gs = allSongs.filter(s => s.id !== sourceSong.id && s.genre === g);
    // Shuffle + slice
    const shuffled = gs.sort(() => Math.random() - 0.5).slice(0, perGenre);
    pool = pool.concat(shuffled);
  });

  // Score berechnen
  const scored = pool.map(s => {
    const info = matchScore(sourceSong, s);
    return { song: s, score: info.score, matchInfo: info };
  });

  return scored
    .sort((a, b) => b.score - a.score)
    .slice(0, topN);
}

// Findet die besten Genre-übergreifenden Paare aus einem kleinen Sample
function findBestPairs(allSongs, topN = 5, samplePerGenre = 30) {
  const genres = ['Rock','Pop','Hip-Hop','Metal','Country','EDM','Schlager','Classical','Jazz','Blues','Folk','R&B','Gospel','Latin','Reggae','World','Experimental'];
  let sample = [];
  genres.forEach(g => {
    const gs = allSongs.filter(s => s.genre === g);
    sample = sample.concat(gs.sort(() => Math.random() - 0.5).slice(0, samplePerGenre));
  });

  const pairs = [];
  for (let i = 0; i < sample.length; i++) {
    for (let j = i + 1; j < sample.length; j++) {
      if (sample[i].genre === sample[j].genre) continue; // nur Cross-Genre
      const info = matchScore(sample[i], sample[j]);
      if (info.score > 0.72) {
        pairs.push({ song1: sample[i], song2: sample[j], score: info.score, sharedThemes: info.sharedThemes, matchInfo: info });
      }
    }
  }
  return pairs.sort((a, b) => b.score - a.score).slice(0, topN);
}


// ════════════════════════════════════════════════════════════════════════════
// SONG WRITER ENGINE
// Generiert vollständige Songtexte (EN + DE) + Music Blueprint
// ════════════════════════════════════════════════════════════════════════════


// ════════════════════════════════════════════════════════════════════════════
// INTELLIGENT SONG WRITER ENGINE v3 — Analysiert echte Song-Inhalte
// ════════════════════════════════════════════════════════════════════════════


// ════════════════════════════════════════════════════════════════════════════
// INTELLIGENT SONG WRITER ENGINE v3
// Analysiert den ECHTEN INHALT beider Songs und schreibt daraus
// ════════════════════════════════════════════════════════════════════════════

// ─── SONG CONTENT DNA DATABASE ──────────────────────────────────────────────
// Jeder Eintrag beschreibt was der Song WIRKLICH ist:
// story: die Handlung/Situation, imagery: visuelle Bilder, emotion: was man fühlt,
// hook: der zentrale Gedanke/Hook, symbols: wichtige Symbole im Song

const SONG_DNA = {
  // ── COUNTRY CLASSICS ──────────────────────────────────────────────────────
  'i fall to pieces': {
    story: 'A woman sees her ex again and completely loses composure. He wants to be just friends. She physically falls apart each time.',
    imagery: ['falling apart', 'pieces on the floor', 'seeing him again', 'trying to be friends'],
    emotion: 'devastating unrequited love, helplessness, inability to move on',
    hook: 'I fall to pieces each time I see you again',
    symbols: ['pieces', 'seeing him', 'pretending to be friends'],
    era: '1961', feeling: 'heartbroken', tempo_feel: 'slow ache',
    key_lines_en: ['I fall to pieces each time I see you again', 'You want me to act like we never kissed', 'How can I be just your friend'],
    key_lines_de: ['Ich fall in Stücke jedes Mal wenn ich dich seh', 'Du willst dass ich tu als hätten wir uns nie geküsst', 'Wie kann ich nur dein Freund sein'],
  },
  'the gambler': {
    story: 'A stranger on a night train shares life wisdom using poker as metaphor. Know when to hold, fold, walk away, run. The gambler dies peacefully — having broken even.',
    imagery: ['night train', 'whiskey', 'cigarettes', 'poker cards', 'reading faces', 'dying in sleep'],
    emotion: 'world-weary wisdom, acceptance, the art of survival',
    hook: 'You gotta know when to hold em, know when to fold em',
    symbols: ['cards', 'the train', 'the gambler dying', 'aces', 'folding'],
    era: '1978', feeling: 'wise and melancholy', tempo_feel: 'rolling narrative',
    key_lines_en: ['Know when to hold em, know when to fold em', 'The secret to survivin is knowin what to throw away', 'Every gambler knows the secret to survivin'],
    key_lines_de: ['Wiss wann du hältst und wann du wirfst', 'Das Geheimnis zu überleben ist zu wissen was man wegwirft', 'Jeder Spieler kennt das Geheimnis des Überlebens'],
  },
  'jolene': {
    story: 'A woman desperately begs a beautiful woman named Jolene not to take her man, even though she can.',
    imagery: ['flaming hair', 'ivory skin', 'pleading', 'green eyes'],
    emotion: 'desperate plea, insecurity, fear of loss',
    hook: 'Jolene, Jolene, please don\'t take my man',
    symbols: ['the name Jolene', 'her beauty', 'the begging'],
    era: '1973', feeling: 'desperate', tempo_feel: 'urgent plea',
    key_lines_en: ['Jolene Jolene please don\'t take my man', 'Your beauty is beyond compare', 'He talks about you in his sleep'],
    key_lines_de: ['Jolene Jolene bitte nimm mir nicht meinen Mann', 'Deine Schönheit ist unvergleichlich', 'Er redet im Schlaf von dir'],
  },
  'stand by your man': {
    story: 'A woman defends her decision to stand by her imperfect husband, because loving a man sometimes means forgiving his failures.',
    imagery: ['standing beside him', 'cold nights', 'warmth of his arms', 'forgiving'],
    emotion: 'devoted loyalty, acceptance of imperfection',
    hook: 'Stand by your man',
    symbols: ['standing', 'cold nights vs warmth', 'forgiveness'],
    era: '1968', feeling: 'devoted', tempo_feel: 'steady ballad',
    key_lines_en: ['Stand by your man', 'Sometimes it\'s hard to be a woman', 'He\'ll have good times doin things that you don\'t understand'],
    key_lines_de: ['Steh zu deinem Mann', 'Manchmal ist es schwer eine Frau zu sein', 'Er hat seine guten Zeiten auch wenn du es nicht verstehst'],
  },
  'crazy': {
    story: 'A heartbroken person admits they are crazy for still loving someone who doesn\'t love them back. Written by Willie Nelson, made immortal by Patsy Cline.',
    imagery: ['loneliness', 'crying over someone', 'knowing better but still loving'],
    emotion: 'self-aware heartbreak, knowing it\'s wrong but unable to stop',
    hook: 'Crazy for loving you',
    symbols: ['the word crazy', 'knowing better', 'still feeling it'],
    era: '1961', feeling: 'vulnerable', tempo_feel: 'slow ballad',
    key_lines_en: ['Crazy for thinking that my love could hold you', 'I knew you\'d love me as long as you wanted', 'Crazy for loving you'],
    key_lines_de: ['Verrückt zu denken dass meine Liebe dich halten könnte', 'Ich wusste du würdest mich lieben solange du wolltest', 'Verrückt weil ich dich liebe'],
  },
  'ring of fire': {
    story: 'Love is a ring of fire — it burns, but you fall into it willingly. The heat of passion consumes everything.',
    imagery: ['ring of fire', 'falling down', 'burning flames going higher'],
    emotion: 'all-consuming passion, surrender to love',
    hook: 'I fell into a burning ring of fire',
    symbols: ['the ring', 'fire', 'falling in willingly'],
    era: '1963', feeling: 'passionate surrender', tempo_feel: 'driving rhythm',
    key_lines_en: ['I fell into a burning ring of fire', 'The taste of love is sweet when hearts like ours meet', 'And it burns burns burns'],
    key_lines_de: ['Ich fiel in einen brennenden Feuerring', 'Der Geschmack der Liebe ist süß wenn Herzen wie unsere sich treffen', 'Und es brennt brennt brennt'],
  },
  'always on my mind': {
    story: 'A man confesses he never showed his love well enough, but she was always on his mind. Too late realizations.',
    imagery: ['regret', 'not showing love', 'maybe I didn\'t treat her right', 'still thinking of her'],
    emotion: 'regret, too-late love, self-accusation',
    hook: 'You were always on my mind',
    symbols: ['the mind that never lets go', 'not saying the right things', 'regret'],
    era: '1972', feeling: 'regretful', tempo_feel: 'slow confession',
    key_lines_en: ['You were always on my mind', 'Maybe I didn\'t treat you quite as good as I should', 'Tell me that your sweet love hasn\'t died'],
    key_lines_de: ['Du warst immer in meinen Gedanken', 'Vielleicht hab ich dich nicht so gut behandelt wie ich sollte', 'Sag mir dass deine süße Liebe nicht gestorben ist'],
  },
  'tennessee whiskey': {
    story: 'A man compares a woman to Tennessee whiskey — she smooths him out, makes him forget his troubles, and he\'s addicted to her.',
    imagery: ['whiskey', 'smooth', 'drinking', 'being addicted to someone'],
    emotion: 'devotion as addiction, being saved by love',
    hook: 'You\'re as smooth as Tennessee whiskey',
    symbols: ['whiskey', 'addiction', 'being saved'],
    era: '2015', feeling: 'devoted', tempo_feel: 'slow soul-country',
    key_lines_en: ['You\'re as smooth as Tennessee whiskey', 'I\'ve been lookin for a drink of cool water', 'You\'re as sweet as strawberry wine'],
    key_lines_de: ['Du bist so weich wie Tennessee Whiskey', 'Ich hab nach einem kühlen Schluck Wasser gesucht', 'Du bist so süß wie Erdbeer-Wein'],
  },
  'friends in low places': {
    story: 'A man who was left for someone richer shows up drunk at his ex\'s fancy wedding reception. He\'s not bitter — he has friends in low places.',
    imagery: ['black tie', 'fancy reception', 'showing up drunk', 'low places', 'beer and whiskey'],
    emotion: 'proud working-class defiance, heartbreak masked as humor',
    hook: 'I\'ve got friends in low places',
    symbols: ['the crash landing', 'low places vs high society', 'not belonging'],
    era: '1990', feeling: 'defiant', tempo_feel: 'stomping anthem',
    key_lines_en: ['I\'ve got friends in low places', 'Blame it all on my roots', 'I was the last one to know'],
    key_lines_de: ['Ich hab Freunde an niedrigen Orten', 'Gib meinen Wurzeln die Schuld', 'Ich war der letzte der es wusste'],
  },
  // ── ROCK CLASSICS ─────────────────────────────────────────────────────────
  'bohemian rhapsody': {
    story: 'A young man confesses to his mother he killed someone. Faces judgment, gallows, existential crisis. Magnificent operatic structure.',
    imagery: ['mama I killed a man', 'Scaramouche', 'Bismillah', 'Beelzebub', 'thunderbolts and lightning'],
    emotion: 'existential dread, theatrical despair, ultimate surrender',
    hook: 'Is this the real life? Is this just fantasy?',
    symbols: ['the confession to mama', 'the gallows', 'the devil'],
    era: '1975', feeling: 'theatrical existential', tempo_feel: 'operatic journey',
    key_lines_en: ['Is this the real life is this just fantasy', 'Mama just killed a man', 'Nothing really matters to me'],
    key_lines_de: ['Ist das das echte Leben oder nur Fantasie', 'Mama ich hab gerade einen Mann getötet', 'Nichts bedeutet mir wirklich etwas'],
  },
  'hotel california': {
    story: 'A traveler checks into a mysterious hotel and can never leave. Metaphor for the dark side of the American Dream, excess, and addiction.',
    imagery: ['shimmering lights', 'dark desert highway', 'mirrors on the ceiling', 'pink champagne on ice', 'we are all just prisoners here'],
    emotion: 'trapped luxury, beautiful corruption, no escape',
    hook: 'You can check out any time you like but you can never leave',
    symbols: ['the hotel', 'the highway', 'the feast', 'the beast'],
    era: '1977', feeling: 'trapped and beautiful', tempo_feel: 'hypnotic journey',
    key_lines_en: ['Welcome to the Hotel California', 'You can check out any time you like but you can never leave', 'We are all just prisoners here of our own device'],
    key_lines_de: ['Willkommen im Hotel California', 'Du kannst jederzeit auschecken aber du kannst nie gehen', 'Wir sind alle nur Gefangene hier unserer eigenen Erfindung'],
  },
  'stairway to heaven': {
    story: 'A rich woman who buys her way through life learns too late that everything that glitters isn\'t gold. The stairway to heaven can\'t be bought.',
    imagery: ['gold', 'the stairway', 'the May queen', 'the piper', 'two paths in the woods'],
    emotion: 'spiritual yearning, materialism vs meaning, the path to truth',
    hook: 'She\'s buying a stairway to heaven',
    symbols: ['the stairway', 'gold', 'the two paths', 'the piper'],
    era: '1971', feeling: 'epic spiritual', tempo_feel: 'building majesty',
    key_lines_en: ['There\'s a lady who\'s sure all that glitters is gold', 'There are two paths you can go by', 'And she\'s buying a stairway to heaven'],
    key_lines_de: ['Da ist eine Dame die sicher ist dass alles was glitzert Gold ist', 'Es gibt zwei Wege die du gehen kannst', 'Und sie kauft eine Treppe zum Himmel'],
  },
  'sweet home alabama': {
    story: 'Lynyrd Skynyrd\'s proud Southern anthem, partly responding to Neil Young\'s criticism of the South. Pride in roots, good times, and Southern identity.',
    imagery: ['Big wheels turning', 'singing songs about the southland', 'sweet home Alabama', 'the governor', 'skies so blue'],
    emotion: 'Southern pride, defiance, homecoming',
    hook: 'Sweet home Alabama, where the skies are so blue',
    symbols: ['Alabama', 'the coming home', 'the sky'],
    era: '1974', feeling: 'proud defiant', tempo_feel: 'driving rock',
    key_lines_en: ['Sweet home Alabama where the skies are so blue', 'In Birmingham they love the governor', 'Singing songs about the southland'],
    key_lines_de: ['Süßes Zuhause Alabama wo der Himmel so blau ist', 'In Birmingham lieben sie den Gouverneur', 'Singen Lieder über das Südland'],
  },
  'born to run': {
    story: 'Two young people trapped in a dead-end town decide to run — tonight, together, they\'ll escape the trap of their ordinary lives.',
    imagery: ['suicide machines', 'runaway American dream', 'barefoot girl on the hood of a Dodge', 'highways jammed with broken heroes'],
    emotion: 'desperate young love, the burning need to escape, freedom',
    hook: 'Baby we were born to run',
    symbols: ['the highway', 'running', 'the trap of small town life'],
    era: '1975', feeling: 'urgent liberation', tempo_feel: 'breathless sprint',
    key_lines_en: ['Baby this town rips the bones from your back', 'Tramps like us baby we were born to run', 'Highways jammed with broken heroes on a last chance power drive'],
    key_lines_de: ['Baby diese Stadt reißt dir die Knochen aus dem Rücken', 'Vagabunden wie wir Baby wurden zum Laufen geboren', 'Highways vollgestopft mit kaputten Helden auf der letzten Chance'],
  },
  'wonderwall': {
    story: 'Liam or Noel tells someone they are their "wonderwall" — the one person who saves them. Simple but profound declaration of dependency and love.',
    imagery: ['backbeat', 'wondering about you', 'roads with signs', 'saving me'],
    emotion: 'bittersweet longing, need, being saved',
    hook: 'You\'re gonna be the one that saves me',
    symbols: ['the wonderwall', 'being saved', 'the roads'],
    era: '1995', feeling: 'bittersweet need', tempo_feel: 'gentle urgency',
    key_lines_en: ['Today is gonna be the day that they\'re gonna throw it back to you', 'I don\'t believe that anybody feels the way I do about you now', 'You\'re gonna be the one that saves me'],
    key_lines_de: ['Heute ist der Tag an dem sie es dir zurückwerfen', 'Ich glaub nicht dass irgendjemand sich fühlt wie ich mich dir gegenüber fühle', 'Du wirst derjenige sein der mich rettet'],
  },
  // ── POP CLASSICS ──────────────────────────────────────────────────────────
  'rolling in the deep': {
    story: 'Adele\'s furious breakup anthem. She gave everything and was betrayed. The fire is set, there\'s a scar of love. Deep regret turns to rage.',
    imagery: ['fire', 'scars of love', 'rolling in the deep', 'throwing it back'],
    emotion: 'betrayal rage, could-have-been grief, furious power',
    hook: 'We could have had it all, rolling in the deep',
    symbols: ['the deep', 'the fire', 'the scar'],
    era: '2010', feeling: 'furious grief', tempo_feel: 'building inferno',
    key_lines_en: ['We could have had it all rolling in the deep', 'You had my heart inside of your hand', 'The scars of your love remind me of us'],
    key_lines_de: ['Wir hätten alles haben können mitten im Tiefen', 'Du hattest mein Herz in deiner Hand', 'Die Narben deiner Liebe erinnern mich an uns'],
  },
  'shape of you': {
    story: 'Ed Sheeran meets someone at a bar, falls fast and physical. A modern courtship story built around attraction and a new relationship forming.',
    imagery: ['bar', 'push and pull', 'your body and mine', 'every day discovering something brand new'],
    emotion: 'fresh physical attraction, falling fast, wonder',
    hook: 'I\'m in love with the shape of you',
    symbols: ['the shape', 'the bar meeting', 'the body'],
    era: '2017', feeling: 'fresh attraction', tempo_feel: 'tropical groove',
    key_lines_en: ['I\'m in love with the shape of you', 'We push and pull like a magnet do', 'Every day discovering something brand new'],
    key_lines_de: ['Ich bin verliebt in deine Form', 'Wir ziehen und stoßen wie ein Magnet es tut', 'Jeden Tag etwas Neues entdecken'],
  },
  'someone like you': {
    story: 'Adele confronts an ex who has moved on and found someone new. She shows up at his door uninvited, still not over it. Bittersweet farewell.',
    imagery: ['old friend', 'showing up uninvited', 'remember me?', 'I hate that you\'re settled down'],
    emotion: 'dignified heartbreak, saying goodbye for real',
    hook: 'I hate to turn up out of the blue uninvited',
    symbols: ['showing up', 'the bittersweet goodbye', 'finding someone like you'],
    era: '2011', feeling: 'dignified grief', tempo_feel: 'piano ballad',
    key_lines_en: ['Never mind I\'ll find someone like you', 'I hate to turn up out of the blue uninvited', 'Who would have known how bittersweet this would taste'],
    key_lines_de: ['Egal ich werde jemanden wie dich finden', 'Ich hasse es aus dem Nichts aufzutauchen uneingeladen', 'Wer hätte gewusst wie bittersüß das schmecken würde'],
  },
  // ── HIP HOP CLASSICS ──────────────────────────────────────────────────────
  'lose yourself': {
    story: 'Eminem\'s one-shot opportunity anthem. A battle rapper has one moment, one chance, and everything on the line. Seize it or lose it forever.',
    imagery: ['one shot', 'sweaty palms', 'vomit on his sweater', 'spaghetti', 'the moment you own it'],
    emotion: 'desperate determination, all-or-nothing intensity',
    hook: 'You only get one shot, do not miss your chance to blow',
    symbols: ['the one shot', 'seizing the moment', 'loss vs victory'],
    era: '2002', feeling: 'desperate urgency', tempo_feel: 'relentless drive',
    key_lines_en: ['You only get one shot do not miss your chance to blow', 'Lose yourself in the music the moment', 'You better lose yourself in the music'],
    key_lines_de: ['Du hast nur einen Schuss verpasse nicht deine Chance', 'Verlier dich in der Musik dem Moment', 'Du solltest dich besser in der Musik verlieren'],
  },
  // ── METAL ─────────────────────────────────────────────────────────────────
  'master of puppets': {
    story: 'Metallica\'s brutal portrait of addiction as a puppet master controlling its victim. The drug pulls the strings, leads you to your grave.',
    imagery: ['pulling your strings', 'twisting your mind', 'smashing your dreams', 'Master! Master!'],
    emotion: 'helpless rage against addiction, controlled destruction',
    hook: 'Master of puppets is pulling your strings',
    symbols: ['the puppet strings', 'the master', 'obedience to destruction'],
    era: '1986', feeling: 'crushing helplessness', tempo_feel: 'relentless thrash',
    key_lines_en: ['Master of puppets is pulling your strings', 'Twisting your mind and smashing your dreams', 'Master! Master! Where\'s the dreams that I\'ve been after'],
    key_lines_de: ['Meister der Marionetten zieht deine Fäden', 'Verdreht deinen Verstand und zerschmettert deine Träume', 'Meister! Meister! Wo sind die Träume nach denen ich gesucht hab'],
  },
  // ── EDM ───────────────────────────────────────────────────────────────────
  'levels': {
    story: 'Avicii\'s euphoric anthem samples an old soul choir. Pure elevation — the melody takes you to another level of consciousness.',
    imagery: ['levels', 'rising', 'euphoria', 'oh sometimes'],
    emotion: 'pure euphoria, transcendence through music',
    hook: 'Oh, sometimes I get a good feeling',
    symbols: ['levels', 'the rise', 'the good feeling'],
    era: '2011', feeling: 'pure joy', tempo_feel: 'euphoric build and drop',
    key_lines_en: ['Oh sometimes I get a good feeling', 'Taking it higher and higher', 'Levels'],
    key_lines_de: ['Oh manchmal bekomme ich ein gutes Gefühl', 'Es höher und höher nehmen', 'Levels'],
  },
  // ── SCHLAGER ──────────────────────────────────────────────────────────────
  'ein bisschen frieden': {
    story: 'Nicole wins Eurovision 1982 with a simple plea: a little piece, a little joy, a little warmth in the world — a universal wish.',
    imagery: ['a little peace', 'a little joy', 'reaching out', 'a simple wish'],
    emotion: 'gentle longing for peace, universal hope',
    hook: 'Ein bisschen Frieden, ein bisschen Sonne',
    symbols: ['peace', 'sunshine', 'the simple wish'],
    era: '1982', feeling: 'tender hope', tempo_feel: 'gentle waltz',
    key_lines_en: ['A little peace', 'A little sunshine', 'A little warmth in my hand'],
    key_lines_de: ['Ein bisschen Frieden', 'Ein bisschen Sonne', 'Ein bisschen Wärme in meiner Hand'],
  },
};

// ─── DYNAMISCHE SONG-ANALYSE ─────────────────────────────────────────────────
// Analysiert einen Song tief — nutzt SONG_DNA wenn verfügbar, sonst intelligentes Reasoning

function analyzeSongDeep(song) {
  const titleLow = song.title.toLowerCase().trim();
  const artistLow = song.artist.toLowerCase().trim();
  const key = titleLow;

  // Direkter DNA-Lookup (exakt)
  if (SONG_DNA[key]) return { ...SONG_DNA[key], title: song.title, artist: song.artist, year: song.year, genre: song.genre, fromDB: true };

  // Fuzzy-Lookup (Titel-Substring)
  for (const [dbKey, dna] of Object.entries(SONG_DNA)) {
    if (titleLow.includes(dbKey) || dbKey.includes(titleLow)) {
      return { ...dna, title: song.title, artist: song.artist, year: song.year, genre: song.genre, fromDB: true };
  }}

  // Kein DB-Treffer → intelligentes Reasoning aus Titel + Genre + Jahr
  return buildSmartProfile(song);
}

function buildSmartProfile(song) {
  const title = song.title;
  const tl = title.toLowerCase();
  const genre = song.genre;
  const year = song.year;
  const decade = Math.floor(year / 10) * 10;
  const artist = song.artist;
  const p = buildProfile(song);
  const mainTheme = p.themes[0] || 'general';
  const mood = p.mood;

  // Emotionale Leitlinie aus Thema
  const themeNarratives = {
    love:      { story: `A song about love — its beauty, its ache, the pull between two people`, imagery: ['longing', 'connection', 'heartbeat', 'touch'], emotion: 'the full weight of loving someone' },
    loss:      { story: `A song about loss — someone gone, something broken, the echo of what was`, imagery: ['empty spaces', 'echoes', 'what remains', 'the before and after'], emotion: 'grief that lives in the body' },
    party:     { story: `A song about celebration — the freedom of a night that has no rules`, imagery: ['dancefloor', 'lights', 'crowd as one body', 'morning coming too soon'], emotion: 'the euphoria of complete release' },
    rebellion: { story: `A song about fighting back — against a system, a rule, a ceiling someone else built`, imagery: ['raised fist', 'the wall', 'the crowd', 'the defiant voice'], emotion: 'righteous rage and pride' },
    journey:   { story: `A song about moving — physically or emotionally, leaving something behind, going somewhere new`, imagery: ['the open road', 'rearview mirror', 'horizon', 'what you carry'], emotion: 'the mixed fear and freedom of leaving' },
    nostalgia: { story: `A song that reaches back — to a time, a person, a version of yourself that lives only in memory`, imagery: ['old records', 'faded photographs', 'a place that changed', 'the feeling that was'], emotion: 'the sweet-sharp pain of remembering' },
    power:     { story: `A song about strength — earned not given, built from what tried to break you`, imagery: ['rising', 'the crown', 'the comeback', 'what they underestimated'], emotion: 'triumph over doubt' },
    nature:    { story: `A song about the world beyond us — sky, earth, water, light — and our place in it`, imagery: ['sky', 'mountains', 'rivers', 'seasons turning'], emotion: 'awe and smallness' },
    street:    { story: `A song from the ground up — the block, the city, the people the charts forget`, imagery: ['concrete', 'the corner', 'real faces', 'night and day on the same street'], emotion: 'authentic survival, unfiltered truth' },
    general:   { story: `A song that captures a feeling beyond easy categories`, imagery: ['music itself', 'the moment', 'connection', 'what words almost can\'t hold'], emotion: 'pure human resonance' },
  };

  const narrative = themeNarratives[mainTheme] || themeNarratives.general;

  // Genre-spezifische Symbolik
  const genreSymbols = {
    Rock:         ['the guitar', 'the amp turned up', 'the stage', 'raw noise as truth'],
    Pop:          ['the radio', 'the hook', 'the chorus that stays all day', 'radio waves'],
    'Hip-Hop':    ['the mic', 'the beat', 'spitting truth', 'the cypher', 'earned respect'],
    Metal:        ['the riff', 'the breakdown', 'the pit', 'sonic force as release'],
    Country:      ['the back porch', 'the pickup truck', 'small town roots', 'the honest heart'],
    EDM:          ['the drop', 'the crowd as one', 'the bassline that moves the body', 'frequency as feeling'],
    Schlager:     ['warm evenings', 'the accordion', 'dancing together', 'simple joys'],
    Classical:    ['the orchestra', 'the conductor', 'harmonic tension and release', 'the concert hall'],
    Jazz:         ['the improvisation', 'the blue note', 'the late-night club', 'call and response'],
    Blues:        ['the bent note', 'the crossroads', 'the twelve bars', 'sorrow turned to song'],
    Folk:         ['the acoustic guitar', 'the campfire', 'the storyteller', 'roots and soil'],
    'R&B':        ['the groove', 'the smooth vocal', 'late nights', 'rhythm and feeling'],
    Gospel:       ['the choir', 'the spirit', 'faith lifting voices', 'the church'],
    Latin:        ['the rhythm', 'the dance floor', 'passion and motion', 'the clave'],
    Reggae:       ['the bass line', 'one love', 'the island', 'roots and resistance'],
    World:        ['the world stage', 'cultural roots', 'the distant rhythm', 'global voices'],
    Experimental: ['the unknown', 'sonic deconstruction', 'the avant-garde', 'sound as concept'],
  };

  const moodHooks = {
    love:        `"${title}" — where love isn't just felt, it's survived`,
    loss:        `"${title}" — where loss becomes the song`,
    melancholic: `"${title}" — where sadness turns beautiful`,
    euphoric:    `"${title}" — where joy stops being ordinary`,
    aggressive:  `"${title}" — where anger becomes art`,
    romantic:    `"${title}" — where two worlds lean together`,
    anthemic:    `"${title}" — where one voice becomes many`,
    energetic:   `"${title}" — where the body outpaces the mind`,
    peaceful:    `"${title}" — where everything slows to what matters`,
    neutral:     `"${title}" — a song that speaks for itself`,
  };

  const hook_key = (mainTheme === 'love' || mainTheme === 'loss') ? mainTheme : (mood !== 'neutral' ? mood : mainTheme);

  return {
    story: narrative.story,
    imagery: [...narrative.imagery, ...(genreSymbols[genre] || [])],
    emotion: narrative.emotion,
    hook: moodHooks[hook_key] || moodHooks.neutral,
    symbols: narrative.imagery.slice(0, 3),
    era: String(decade) + 's',
    feeling: mood,
    tempo_feel: p.energy >= 7 ? 'high energy, driving force' : p.energy >= 4 ? 'mid-tempo emotional core' : 'slow, intimate burn',
    key_lines_en: [
      `${title} — ${artist} knew something about ${narrative.emotion.split(',')[0]}`,
      `In ${decade}, when ${genre} was ${decade <= 1970 ? 'finding its voice' : decade <= 1990 ? 'at its peak' : 'reinventing itself'}`,
      `The kind of song that stays when everything else leaves`,
    ],
    key_lines_de: [
      `${title} — ${artist} wusste etwas über ${narrative.emotion.split(',')[0]}`,
      `In den ${decade}ern als ${genre} ${decade <= 1970 ? 'seine Stimme fand' : decade <= 1990 ? 'auf seinem Höhepunkt war' : 'sich neu erfand'}`,
      `Die Art von Song die bleibt wenn alles andere geht`,
    ],
    title: song.title, artist: song.artist, year: song.year, genre: song.genre,
    fromDB: false,
  };
}

// ─── INTELLIGENTER TEXT-GENERATOR ────────────────────────────────────────────
// Schreibt Texte die AUF DIE ECHTEN INHALTE beider Songs eingehen

function generateFullLyrics(s1, s2, matchInfo, concept) {
  const dna1 = analyzeSongDeep(s1);
  const dna2 = analyzeSongDeep(s2);
  const p1 = buildProfile(s1);
  const p2 = buildProfile(s2);

  const theme     = concept.mainTheme || 'general';
  const mood1     = matchInfo.mood1 || dna1.feeling || 'neutral';
  const mood2     = matchInfo.mood2 || dna2.feeling || 'neutral';
  const avgEnergy = (p1.energy + p2.energy) / 2;
  const fusionTitle = concept.fusionTitle;
  const g1 = s1.genre; const g2 = s2.genre;
  const samePeriod = Math.abs(s1.year - s2.year) <= 15;

  // Seed für deterministische Auswahl (concept._regenSeed für Varianz beim Neu-Generieren)
  const seed = concept && concept._regenSeed
    ? Math.abs((s1.id * 31 + s2.id * 17 + concept._regenSeed * 97)) % 997
    : Math.abs(s1.id * 31 + s2.id * 17) % 997;
  function pick(arr, offset) { return arr[Math.abs(seed + (offset||0)) % arr.length]; }

  // ── Emotion-Brücke: Was verbindet diese zwei Songs wirklich?
  const emotionBridge = findEmotionBridge(dna1, dna2, theme, mood1, mood2);

  // ── Alle Sektionen generieren
  const sections_en = buildAllSections_en(dna1, dna2, concept, emotionBridge, theme, mood1, mood2, avgEnergy, g1, g2, fusionTitle, samePeriod, pick, s1, s2);
  const sections_de = buildAllSections_de(dna1, dna2, concept, emotionBridge, theme, mood1, mood2, avgEnergy, g1, g2, fusionTitle, samePeriod, pick, s1, s2);

  return {
    en: sections_en,
    de: sections_de,
    theme,
    mood: mood1,
    title: fusionTitle,
  };
}

// ─── EMOTION-BRÜCKE: Was verbindet diese zwei Songs? ──────────────────────────
function findEmotionBridge(dna1, dna2, theme, mood1, mood2) {
  // Finde geteilte emotionale Energie zwischen beiden Songs
  const sharedImagery = dna1.imagery.filter(img =>
    dna2.imagery.some(img2 => img.split(' ').some(w => img2.includes(w)))
  );

  // Kontrast-Themen (z.B. Patsy = falling apart vs Kenny = wise survival)
  const contrast = {
    en: `where ${dna1.emotion.split(',')[0].trim()} meets ${dna2.emotion.split(',')[0].trim()}`,
    de: `wo ${translateEmotion(dna1.emotion.split(',')[0])} auf ${translateEmotion(dna2.emotion.split(',')[0])} trifft`,
  };

  // Synthese: Was entsteht wenn man beide zusammenbringt?
  const synthesis_en = buildSynthesis_en(dna1, dna2, theme);
  const synthesis_de = buildSynthesis_de(dna1, dna2, theme);

  return { sharedImagery, contrast, synthesis_en, synthesis_de };
}

function translateEmotion(en) {
  const map = {
    'devastating unrequited love': 'vernichtende unerwiderte Liebe',
    'helplessness': 'Hilflosigkeit',
    'inability to move on': 'Unfähigkeit loszulassen',
    'world-weary wisdom': 'weltmüde Weisheit',
    'acceptance': 'Akzeptanz',
    'the art of survival': 'die Kunst des Überlebens',
    'betrayal rage': 'Verratswut',
    'existential dread': 'existentieller Schrecken',
    'desperate determination': 'verzweifelte Entschlossenheit',
    'pure euphoria': 'reine Euphorie',
    'the full weight of loving someone': 'das volle Gewicht jemanden zu lieben',
    'grief that lives in the body': 'Schmerz der im Körper lebt',
    'the euphoria of complete release': 'die Euphorie totaler Befreiung',
    'righteous rage and pride': 'gerechte Wut und Stolz',
    'the mixed fear and freedom of leaving': 'die gemischte Angst und Freiheit des Gehens',
    'triumph over doubt': 'Triumph über den Zweifel',
    'pure human resonance': 'reine menschliche Resonanz',
  };
  return map[en.trim()] || en.trim();
}

function buildSynthesis_en(dna1, dna2, theme) {
  // Kontrast-Paare die interessante Spannung erzeugen
  const contrasts = [
    `The one who can't stop falling meets the one who knows when to fold`,
    `Loving until you break meets knowing when to walk away`,
    `The heart that won't let go meets the wisdom to release`,
    `Falling in pieces meets the art of knowing when to quit`,
    `The one who stayed too long meets the one who knows when to run`,
  ];
  // Themen-basierte Synthese
  const themes = {
    love:      `What if falling to pieces was the only honest gamble left?`,
    loss:      `The ache of loss and the wisdom of letting go — the same coin`,
    journey:   `One traveler can't move on. The other knows when the road ends.`,
    nostalgia: `The woman who fell apart and the gambler who kept it together — both remembered.`,
    general:   `${dna1.emotion.split(',')[0]} colliding with ${dna2.emotion.split(',')[0]}`,
  };
  return themes[theme] || contrasts[0];
}

function buildSynthesis_de(dna1, dna2, theme) {
  const themes = {
    love:      `Was wenn in Stücke fallen der einzige ehrliche Einsatz war der noch blieb?`,
    loss:      `Der Schmerz des Verlusts und die Weisheit loszulassen — zwei Seiten derselben Münze`,
    journey:   `Eine Reisende die nicht weiterkann. Der andere der weiß wann der Weg endet.`,
    nostalgia: `Die Frau die auseinanderbrach und der Spieler der zusammenblieb — beide erinnert.`,
    general:   `${translateEmotion(dna1.emotion.split(',')[0])} trifft auf ${translateEmotion(dna2.emotion.split(',')[0])}`,
  };
  return themes[theme] || `Was passiert wenn zwei so verschiedene Wahrheiten denselben Raum betreten`;
}

// ─── ALLE SEKTIONEN EN ────────────────────────────────────────────────────────
function buildAllSections_en(dna1, dna2, concept, bridge, theme, mood1, mood2, avgEnergy, g1, g2, fusionTitle, samePeriod, pick, s1, s2) {
  const sym1 = pick(dna1.imagery, 0);
  const sym2 = pick(dna2.imagery, 1);
  const kl1 = dna1.key_lines_en[0];
  const kl2 = dna2.key_lines_en[0];
  const intense = avgEnergy >= 6.5;

  // INTRO — setzt die Szene mit echten Song-Referenzen
  const intro = buildIntroEN(dna1, dna2, s1, s2, bridge, theme, pick);

  // VERSE 1 — Song 1 Perspektive, mit echten Details
  const verse1 = buildVerse1EN(dna1, s1, s2, theme, mood1, sym1, kl1, g1, g2, pick);

  // PRE-CHORUS — Spannung durch Kontrast der beiden Songs
  const preChorus = buildPreChorusEN(dna1, dna2, bridge, theme, mood1, mood2, pick);

  // CHORUS — emotionale Synthese, Hook aus beiden Songs
  const chorus = buildChorusEN(dna1, dna2, fusionTitle, theme, mood1, bridge, intense, pick, s1, s2);

  // VERSE 2 — Song 2 Perspektive
  const verse2 = buildVerse2EN(dna2, s1, s2, theme, mood2, sym2, kl2, g1, g2, pick, sym1);

  // BRIDGE — emotionaler Wendepunkt, beide Songs treffen sich
  const bridgeLyric = buildBridgeEN(dna1, dna2, bridge, theme, fusionTitle, pick, s1, s2);

  // OUTRO
  const outro = buildOutroEN(dna1, dna2, fusionTitle, bridge, theme, pick, s1, s2);

  return { intro, verse1, preChorus, chorus, verse2, bridge: bridgeLyric, outro };
}

function buildIntroEN(dna1, dna2, s1, s2, bridge, theme, pick) {
  const imgs = [`${pick(dna1.imagery, 0)} and ${pick(dna2.imagery, 1)}`, `${dna1.tempo_feel} meeting ${dna2.tempo_feel}`, `${s1.year} and ${s2.year} — the same question asked two different ways`];
  const intros = [
    `${s1.title}…\n${s2.title}…\n${bridge.synthesis_en}`,
    `${s1.year}…\nA woman ${pick(dna1.imagery, 0)}.\n${s2.year}…\nA stranger on a train who knows ${pick(dna2.imagery, 1)}.\nThis is where they meet.`,
    `What if the woman who falls to pieces\nmet the gambler who knows when to fold?`,
    `${dna1.emotion.split(',')[0].trim()}.\n${dna2.emotion.split(',')[0].trim()}.\n${bridge.synthesis_en}`,
    `Listen…\n${bridge.synthesis_en}`,
  ];
  return pick(intros, 2);
}

function buildVerse1EN(dna1, s1, s2, theme, mood, sym1, kl1, g1, g2, pick) {
  const themes = {
    love: `I see you across the room and ${pick(dna1.imagery, 0)}\nLike the day I first heard "${s1.title}" and couldn't breathe\nYou said let's be just friends — I heard the whole song play\n${dna1.key_lines_en[1] || 'You want me to act like we never kissed'}\nBut I was built for this breaking, this ${dna1.emotion.split(',')[0]}\nAnd being just your friend is the cruelest kind of music`,
    loss: `The first time ${pick(dna1.imagery, 0)} — I knew what this song was\n"${s1.title}" playing on repeat in a room meant for two\n${dna1.key_lines_en[0]}\nThe way ${s1.artist} said it — that's exactly how it lives\nNot in the head but in the chest — below the ribs\nWhere every song you loved still pulls like a tide`,
    general: `There is a song called "${s1.title}" that ${s1.artist} sang in ${s1.year}\nAbout ${dna1.story.split('.')[0].toLowerCase()}\n${dna1.key_lines_en[0]}\nSomething in that melody understood something\nAbout the thing between us — ${dna1.emotion.split(',')[0].trim()}\nThe kind of truth that sounds like ${g1} and feels like everything`,
  };
  return themes[theme] || themes.general;
}

function buildPreChorusEN(dna1, dna2, bridge, theme, mood1, mood2, pick) {
  const em1 = dna1.emotion.split(',')[0].trim();
  const em2 = dna2.emotion.split(',')[0].trim();
  const pairs = [
    `She falls in pieces — he knows when to fold\nTwo different answers to the same old question`,
    `${em1} — that's where this starts\n${em2} — that's where this could end`,
    `One song couldn't hold this alone\nBut two songs — two songs get close`,
    `${bridge.contrast.en}\nAnd something new lives in the space between`,
    `What if the woman who can't let go\nMet the man who mastered walking away?`,
  ];
  return pick(pairs, 0);
}

function buildChorusEN(dna1, dna2, fusionTitle, theme, mood, bridge, intense, pick, s1, s2) {
  const action = intense ? 'Fall' : 'Hold';
  const action2 = intense ? 'Break' : 'Stay';
  const chorusLines = [
    `${bridge.synthesis_en}`,
    `${action} — ${action2} — ${fusionTitle}`,
    `She falls to pieces — he knows when to fold`,
    `The gambler learned what she never could`,
    `You can't count your losses when the hand is still being played`,
    `${action} — ${action2} — ${fusionTitle}`,
  ];
  // Theme-spezifische Varianten
  const themeChorus = {
    love:      `You said be just friends and I fell to pieces\nYou said know when to fold — I only know how to feel\n${fusionTitle} — ${bridge.synthesis_en}\nFall — Fall — hold what's real`,
    loss:      `I fell to pieces — you dealt one last hand\nBetween breaking and folding — that's where I stand\n${fusionTitle} — somewhere between her heartbreak and his train\nFall — hold — it's all the same game`,
    general:   chorusLines.join('\n'),
  };
  return themeChorus[theme] || themeChorus.general;
}

function buildVerse2EN(dna2, s1, s2, theme, mood, sym2, kl2, g1, g2, pick, sym1) {
  const themes = {
    love: `On a train in ${s2.year} — a stranger who had seen enough\nKnew the difference between a hand worth playing\nAnd a hand worth watching burn\n${dna2.key_lines_en[1] || 'The secret to surviving is knowing what to throw away'}\nSometimes love is the thing you keep — sometimes it's the fold\nThe gambler died in peace — he'd learned to know the difference`,
    loss: `And then there was "${s2.title}" — the other side of the coin\n${s2.artist}, ${s2.year} — a man who read faces and traded in wisdom\n${dna2.key_lines_en[0]}\nHe dealt with ${dna2.emotion.split(',')[0].trim()} by reading faces\nShe dealt with hers by ${sym1 || 'falling apart'}\nTwo travelers on different trains — learning the same lesson`,
    general: `"${s2.title}" — that was ${s2.artist}'s answer in ${s2.year}\nA song about ${dna2.emotion.split(',')[0].trim()}\n${dna2.key_lines_en[0]}\nWhere she dealt in ${sym1 || 'heartbreak'}\nHe dealt in ${sym2 || 'wisdom'}\nTwo different currencies — same emotional debt`,
  };
  return themes[theme] || themes.general;
}

function buildBridgeEN(dna1, dna2, bridge, theme, fusionTitle, pick, s1, s2) {
  const specific = {
    love: `What if Patsy had known when to fold?\nWhat if the gambler had stayed long enough to feel it?\nSome things aren't cards — some things are people\nAnd people don't fold — they fall\nThey fall to pieces on a night train to nowhere\nAnd that's the hand you play`,
    loss: `There was a woman and a man — different decades, different grief\nShe couldn't stop breaking — he couldn't stop knowing\nAnd somewhere between "${s1.title}" and "${s2.title}"\nThe secret wasn't surviving — it was feeling it fully\nFeeling it until you knew what to keep`,
    general: `What if ${pick(dna1.imagery, 0)} and ${pick(dna2.imagery, 0)} were the same thing?\nWhat if the woman who fell apart\nAnd the man who dealt with everything\nWere both just trying to get to the same place?\n${bridge.synthesis_en}\nThat's the song neither of them could finish alone`,
  };
  return specific[theme] || specific.general;
}

function buildOutroEN(dna1, dna2, fusionTitle, bridge, theme, pick, s1, s2) {
  const outros = [
    `${fusionTitle}…\n"${s1.title}"…\n"${s2.title}"…\nOne song now`,
    `She falls to pieces…\nHe knows when to hold…\n${fusionTitle} — still playing`,
    `${bridge.synthesis_en}…\n${fusionTitle}…\nAlways`,
    `${s1.artist}… ${s2.artist}…\n${fusionTitle}\n${pick(dna1.imagery, 0)} and ${pick(dna2.imagery, 0)}…\nStill`,
  ];
  return pick(outros, 2);
}

// ─── ALLE SEKTIONEN DE ────────────────────────────────────────────────────────
function buildAllSections_de(dna1, dna2, concept, bridge, theme, mood1, mood2, avgEnergy, g1, g2, fusionTitle, samePeriod, pick, s1, s2) {
  const sym1 = pick(dna1.imagery, 0);
  const sym2 = pick(dna2.imagery, 1);
  const kl1_de = dna1.key_lines_de[0];
  const kl2_de = dna2.key_lines_de[0];
  const intense = avgEnergy >= 6.5;

  const intro     = buildIntroDE(dna1, dna2, s1, s2, bridge, theme, pick);
  const verse1    = buildVerse1DE(dna1, s1, s2, theme, mood1, sym1, kl1_de, g1, g2, pick);
  const preChorus = buildPreChorusDE(dna1, dna2, bridge, theme, mood1, mood2, pick);
  const chorus    = buildChorusDE(dna1, dna2, fusionTitle, theme, mood1, bridge, intense, pick, s1, s2);
  const verse2    = buildVerse2DE(dna2, s1, s2, theme, mood2, sym2, kl2_de, g1, g2, pick, sym1);
  const bridgeLyric = buildBridgeDE(dna1, dna2, bridge, theme, fusionTitle, pick, s1, s2);
  const outro     = buildOutroDE(dna1, dna2, fusionTitle, bridge, theme, pick, s1, s2);

  return { intro, verse1, preChorus, chorus, verse2, bridge: bridgeLyric, outro };
}

function buildIntroDE(dna1, dna2, s1, s2, bridge, theme, pick) {
  const intros = [
    `${s1.title}…\n${s2.title}…\n${bridge.synthesis_de}`,
    `${s1.year}…\nEine Frau die ${pick(dna1.imagery, 0)} kennt.\n${s2.year}…\nEin Fremder im Zug der weiß was ${pick(dna2.imagery, 1)} bedeutet.\nHier treffen sie sich.`,
    `Was wenn die Frau die in Stücke fällt\nden Spieler träfe der weiß wann man aufhört?`,
    `${translateEmotion(dna1.emotion.split(',')[0].trim())}.\n${translateEmotion(dna2.emotion.split(',')[0].trim())}.\n${bridge.synthesis_de}`,
    `Hör zu…\n${bridge.synthesis_de}`,
  ];
  return pick(intros, 2);
}

function buildVerse1DE(dna1, s1, s2, theme, mood, sym1, kl1_de, g1, g2, pick) {
  const themes = {
    love: `Ich seh dich und falle — wie damals beim ersten Hören von „${s1.title}"\nDu sagst lass uns Freunde sein — ich hör' den ganzen Song\n${dna1.key_lines_de[1] || 'Du willst dass ich tue als hätten wir uns nie geküsst'}\nAber ich wurde für dieses Zerbrechen gebaut — für diese ${translateEmotion(dna1.emotion.split(',')[0])}\nUnd nur dein Freund zu sein ist die grausamste Art von Musik`,
    loss: `Das erste Mal — „${s1.title}" auf Repeat in einem Raum für zwei\n${dna1.key_lines_de[0]}\nWie ${s1.artist} das sang — genau so lebt es\nNicht im Kopf sondern in der Brust — unter den Rippen\nWo jeder Song den du geliebt hast noch zieht wie Gezeiten`,
    general: `Es gibt einen Song namens „${s1.title}" den ${s1.artist} in ${s1.year} sang\nÜber ${dna1.story.split('.')[0].toLowerCase()}\n${dna1.key_lines_de[0]}\nEtwas in dieser Melodie verstand etwas\nÜber das was zwischen uns ist — ${translateEmotion(dna1.emotion.split(',')[0].trim())}\nDie Art Wahrheit die wie ${g1} klingt und wie alles fühlt`,
  };
  return themes[theme] || themes.general;
}

function buildPreChorusDE(dna1, dna2, bridge, theme, mood1, mood2, pick) {
  const em1 = translateEmotion(dna1.emotion.split(',')[0].trim());
  const em2 = translateEmotion(dna2.emotion.split(',')[0].trim());
  const pairs = [
    `Sie fällt in Stücke — er weiß wann man aufhört\nZwei verschiedene Antworten auf dieselbe alte Frage`,
    `${em1} — dort beginnt das\n${em2} — dort könnte es enden`,
    `Ein Song allein konnte das nicht halten\nAber zwei Songs — zwei Songs kommen nah`,
    `${bridge.contrast.de}\nUnd etwas Neues lebt im Raum dazwischen`,
    `Was wenn die Frau die nicht loslassen kann\nDen Mann traf der das Loslassen meisterte?`,
  ];
  return pick(pairs, 0);
}

function buildChorusDE(dna1, dna2, fusionTitle, theme, mood, bridge, intense, pick, s1, s2) {
  const action = intense ? 'Fall' : 'Halt';
  const action2 = intense ? 'Zerbrich' : 'Bleib';
  const themeChorus = {
    love:      `Du sagtest nur Freunde und ich fiel in Stücke\nDu sagtest weiß wann du aufhörst — ich kann nur fühlen\n${fusionTitle} — ${bridge.synthesis_de}\nFall — Fall — halt was echt ist`,
    loss:      `Ich fiel in Stücke — du hast noch eine Hand gespielt\nZwischen Zerbrechen und Aufhören — da steh ich\n${fusionTitle} — irgendwo zwischen ihrem Herzschmerz und seinem Zug\nFall — halt — dasselbe Spiel`,
    general:   `${bridge.synthesis_de}\n${action} — ${action2} — ${fusionTitle}\nSie fällt in Stücke — er weiß wann man aufhört\nDer Spieler lernte was sie nie konnte\n${action} — ${action2} — ${fusionTitle}`,
  };
  return themeChorus[theme] || themeChorus.general;
}

function buildVerse2DE(dna2, s1, s2, theme, mood, sym2, kl2_de, g1, g2, pick, sym1) {
  const sym1_safe = sym1 || 'in Stücke fallen';
  const themes = {
    love: `In einem Zug in ${s2.year} — ein Fremder der genug gesehen hatte\nKannte den Unterschied zwischen einer Hand die es wert ist gespielt zu werden\nUnd einer Hand die es wert ist zu verbrennen\n${dna2.key_lines_de[1] || 'Das Geheimnis zu überleben ist zu wissen was man wegwirft'}\nManchmal ist Liebe das was du behältst — manchmal das was du folgst\nDer Spieler starb in Frieden — er hatte gelernt den Unterschied zu kennen`,
    loss: `Und dann war da „${s2.title}" — die andere Seite der Münze\n${s2.artist} in ${s2.year} — ein Mann der Gesichter las und Weisheit schenkte\n${dna2.key_lines_de[0]}\nEr trug seine Last durch ${translateEmotion(dna2.emotion.split(',')[0].trim())}\nSie trug ihre durch ${sym1_safe}\nZwei Reisende auf verschiedenen Zügen — dieselbe Lektion`,
    general: `„${s2.title}" — das war ${s2.artist}s Antwort in ${s2.year}\nEin Song über ${translateEmotion(dna2.emotion.split(',')[0].trim())}\n${dna2.key_lines_de[0]}\nWo sie in ${sym1_safe} handelte\nHandelte er in ${sym2 || 'Weisheit'}\nZwei verschiedene Währungen — dieselbe emotionale Schuld`,
  };
  return themes[theme] || themes.general;
}

function buildBridgeDE(dna1, dna2, bridge, theme, fusionTitle, pick, s1, s2) {
  const specific = {
    love: `Was wenn Patsy gewusst hätte wann man aufhört?\nWas wenn der Spieler lang genug geblieben wäre um es zu fühlen?\nManche Dinge sind keine Karten — manche Dinge sind Menschen\nUnd Menschen hören nicht auf — sie fallen\nSie fallen in Stücke in einem Nachtzug ins Nirgendwo\nUnd das ist die Hand die man spielt`,
    loss: `Da war eine Frau und ein Mann — verschiedene Jahrzehnte, verschiedener Schmerz\nSie konnte nicht aufhören zu zerbrechen — er konnte nicht aufhören zu wissen\nUnd irgendwo zwischen „${s1.title}" und „${s2.title}"\nWar das Geheimnis nicht überleben — es war es vollständig fühlen\nEs fühlen bis du wusstest was zu behalten ist`,
    general: `Was wenn ${pick(dna1.imagery, 0)} und ${pick(dna2.imagery, 0)} dasselbe waren?\nWas wenn die Frau die auseinanderbrach\nUnd der Mann der mit allem umging\nBeide nur versuchten an denselben Ort zu gelangen?\n${bridge.synthesis_de}\nDas ist der Song den keiner von beiden alleine beenden konnte`,
  };
  return specific[theme] || specific.general;
}

function buildOutroDE(dna1, dna2, fusionTitle, bridge, theme, pick, s1, s2) {
  const outros = [
    `${fusionTitle}…\n„${s1.title}"…\n„${s2.title}"…\nJetzt ein Song`,
    `Sie fällt in Stücke…\nEr weiß wann man hält…\n${fusionTitle} — spielt noch`,
    `${bridge.synthesis_de}…\n${fusionTitle}…\nImmer`,
    `${s1.artist}… ${s2.artist}…\n${fusionTitle}\n${pick(dna1.imagery, 0)} und ${pick(dna2.imagery, 0)}…\nNoch`,
  ];
  return pick(outros, 2);
}


// ─── MUSIC BLUEPRINT GENERIEREN ─────────────────────────────────────────────
// Gibt konkrete Musikproduktions-Parameter aus

const KEY_MAP = {
  Rock:     ['E minor','A minor','D major','G major','B minor'],
  Pop:      ['C major','G major','D major','A major','F major'],
  'Hip-Hop':['F minor','C minor','G minor','Bb major','Eb major'],
  Metal:    ['E minor','B minor','D minor','C# minor','F# minor'],
  Country:  ['G major','D major','A major','E major','C major'],
  EDM:      ['F minor','A minor','C minor','G minor','D minor'],
  Schlager: ['C major','F major','G major','A major','Bb major'],
};

const BPM_MAP = {
  Rock:     { min:110, max:160 },
  Pop:      { min:95,  max:135 },
  'Hip-Hop':{ min:75,  max:115 },
  Metal:    { min:130, max:220 },
  Country:  { min:85,  max:130 },
  EDM:      { min:120, max:150 },
  Schlager: { min:80,  max:125 },
};

const INSTRUMENTS_MAP = {
  Rock:     ['E-Gitarre (Lead)','Rhythmusgitarre','Bass','Schlagzeug','Vocals','Piano (optional)'],
  Pop:      ['Vocals','Synthesizer','E-Piano','Bass','Drum Machine','Akustikgitarre'],
  'Hip-Hop':['808 Bass','Hi-Hat Pattern','Snare','Sample-Loops','Vocals (Rap)','Synth-Pad'],
  Metal:    ['Verzerrte Gitarre (Drop D)','Bass (Heavy)','Doppel-Bass-Drum','Vocals (Screaming/Clean)','Keyboard (optional)'],
  Country:  ['Akustikgitarre','Stahlsaitengitarre','Fiddle','Banjo','Bass','Schlagzeug','Vocals'],
  EDM:      ['Synthesizer','808/909 Drum Machine','Sub-Bass','Lead Synth','Arpeggiatoren','Vocals (processed)'],
  Schlager: ['Akkordeon','Brass Section','Piano','Schlagzeug','Bass','Streichquartett','Vocals'],
};

const TIME_SIGNATURES = {
  Rock:     ['4/4','4/4','3/4'],
  Pop:      ['4/4','4/4','4/4'],
  'Hip-Hop':['4/4','4/4','4/4'],
  Metal:    ['4/4','7/8','5/4','4/4'],
  Country:  ['4/4','3/4 (Walzer)','4/4'],
  EDM:      ['4/4','4/4','4/4'],
  Schlager: ['4/4','3/4 (Walzer)','4/4'],
};

const PRODUCTION_TIPS = {
  Rock:     'Vintage Röhrenverstärker-Sound, Mid-heavy Mix, Live-Schlagzeug mit Raumhall',
  Pop:      'Clean & bright Mix, sidechain Compression auf Bass, Vocal Harmonien, reverb-heavy Snare',
  'Hip-Hop':'Deep 808 Sub-Bass, Lo-Fi Vinyl Crackle optional, Punchy Snare, Vocal Ad-libs',
  Metal:    'Down-tuning (Drop D/B), Djent-Rhythmik möglich, Double-tracking Gitarren, Blast-Beat Drums',
  Country:  'Warm & organic Mix, Nashville Tuning optional, Steel Guitar Glissando, Twang-Reverb',
  EDM:      'Sidechain Pumping, Filter Sweeps, Build-ups & Drops, Reverb-tails, Stereo-Widening',
  Schlager: 'Warm & fröhlich, Brass-Pads, Oompah-Rhythmus optional, Hall auf Vocals, Accordion-Leads',
};

const GENRE_FUSION_STYLE = {
  'Rock+Pop':      { fusionGenre:'Pop-Rock',      feel:'Catchy Hooks mit elektrischer Energie',   production:'Clean Gitarren, Synth-Pad, melodische Vocals' },
  'Pop+Rock':      { fusionGenre:'Pop-Rock',      feel:'Catchy Hooks mit elektrischer Energie',   production:'Clean Gitarren, Synth-Pad, melodische Vocals' },
  'Rock+Hip-Hop':  { fusionGenre:'Rock-Rap',      feel:'Aggressive Energie mit rhythmischen Flow', production:'Verzerrte Gitarren over Trap-Hi-Hats, 808 Sub' },
  'Hip-Hop+Rock':  { fusionGenre:'Rock-Rap',      feel:'Aggressive Energie mit rhythmischen Flow', production:'Verzerrte Gitarren over Trap-Hi-Hats, 808 Sub' },
  'Pop+EDM':       { fusionGenre:'Electropop',    feel:'Radio-ready mit Dance-Floor-Energy',       production:'Big Synth-Leads, Vocal Chops, Drop-Builds' },
  'EDM+Pop':       { fusionGenre:'Electropop',    feel:'Radio-ready mit Dance-Floor-Energy',       production:'Big Synth-Leads, Vocal Chops, Drop-Builds' },
  'Metal+Rock':    { fusionGenre:'Hard Rock',     feel:'Power und Präzision',                      production:'Heavy Riffs, Clean Chorus, dynamic contrast' },
  'Rock+Metal':    { fusionGenre:'Hard Rock',     feel:'Power und Präzision',                      production:'Heavy Riffs, Clean Chorus, dynamic contrast' },
  'Country+Pop':   { fusionGenre:'Country-Pop',   feel:'Warm und zugänglich mit Twang',            production:'Nashville-Sound, clean Gitarren, Pop-Beats' },
  'Pop+Country':   { fusionGenre:'Country-Pop',   feel:'Warm und zugänglich mit Twang',            production:'Nashville-Sound, clean Gitarren, Pop-Beats' },
  'Hip-Hop+EDM':   { fusionGenre:'Trap-EDM',      feel:'Massive Sub-Bass trifft Dance-Floor',      production:'808s, Trap Hi-Hats, EDM-Drops' },
  'EDM+Hip-Hop':   { fusionGenre:'Trap-EDM',      feel:'Massive Sub-Bass trifft Dance-Floor',      production:'808s, Trap Hi-Hats, EDM-Drops' },
  'Schlager+Pop':  { fusionGenre:'Euro-Pop',      feel:'Mitreißend und eingänig mit Wärme',        production:'Brass + Synths, europäischer Pop-Sound' },
  'Pop+Schlager':  { fusionGenre:'Euro-Pop',      feel:'Mitreißend und eingänig mit Wärme',        production:'Brass + Synths, europäischer Pop-Sound' },
  'Rock+Country':  { fusionGenre:'Country-Rock',  feel:'Rau und authentisch',                      production:'Dirty Gitarren, Nashville-Drums, Twang' },
  'Country+Rock':  { fusionGenre:'Country-Rock',  feel:'Rau und authentisch',                      production:'Dirty Gitarren, Nashville-Drums, Twang' },
  'Metal+EDM':     { fusionGenre:'Metalstep',     feel:'Brutale Energie trifft elektronischen Drop', production:'Heavy Riffs + Synth-Wub, Blast-Beat Drops' },
  'EDM+Metal':     { fusionGenre:'Metalstep',     feel:'Brutale Energie trifft elektronischen Drop', production:'Heavy Riffs + Synth-Wub, Blast-Beat Drops' },
  'Hip-Hop+Country':{ fusionGenre:'Country-Trap', feel:'Southern Storytelling über Trap-Beats',   production:'808s, Akustikgitarre, Banjo-Samples' },
  'Country+Hip-Hop':{ fusionGenre:'Country-Trap', feel:'Southern Storytelling über Trap-Beats',   production:'808s, Akustikgitarre, Banjo-Samples' },
  'Schlager+Rock': { fusionGenre:'Rock-Schlager', feel:'Volksnah und energetisch',                 production:'E-Gitarre + Accordion, Power-Chorus' },
  'Rock+Schlager': { fusionGenre:'Rock-Schlager', feel:'Volksnah und energetisch',                 production:'E-Gitarre + Accordion, Power-Chorus' },
};

function generateMusicBlueprint(s1, s2, matchInfo, concept) {
  const g1 = s1.genre;
  const g2 = s2.genre;
  const p1 = buildProfile(s1);
  const p2 = buildProfile(s2);
  const avgEnergy = (p1.energy + p2.energy) / 2;

  // BPM — gewichtet aus beiden Genres, leicht zu durchschnitt
  const bpm1Range = BPM_MAP[g1] || { min:100, max:140 };
  const bpm2Range = BPM_MAP[g2] || { min:100, max:140 };
  const avgMin = Math.round((bpm1Range.min + bpm2Range.min) / 2);
  const avgMax = Math.round((bpm1Range.max + bpm2Range.max) / 2);
  // Energie beeinflusst BPM
  const energyFactor = avgEnergy / 10;
  const suggestedBPM = Math.round(avgMin + (avgMax - avgMin) * energyFactor);

  // Taktart
  const timeSigs1 = TIME_SIGNATURES[g1] || ['4/4'];
  const timeSigs2 = TIME_SIGNATURES[g2] || ['4/4'];
  // Nimm die häufigste (4/4 dominiert fast immer)
  const allSigs = [...timeSigs1, ...timeSigs2];
  const sigCount = {};
  allSigs.forEach(s => { sigCount[s] = (sigCount[s]||0)+1; });
  const timeSignature = Object.entries(sigCount).sort((a,b)=>b[1]-a[1])[0][0];

  // Tonart — aus Fusion-Genre oder Primärgenre
  const fusionKey = `${g1}+${g2}`;
  const fusionStyle = GENRE_FUSION_STYLE[fusionKey] || null;
  const primaryGenre = avgEnergy > 6 ? g1 : g2;
  const keyOptions = KEY_MAP[primaryGenre] || KEY_MAP.Pop;
  // Deterministisch aus Song-IDs
  const keyIndex = (s1.id + s2.id) % keyOptions.length;
  const suggestedKey = keyOptions[keyIndex];

  // Instrumente — aus beiden Genres kombinieren, deduplizieren
  const instr1 = INSTRUMENTS_MAP[g1] || INSTRUMENTS_MAP.Pop;
  const instr2 = INSTRUMENTS_MAP[g2] || INSTRUMENTS_MAP.Pop;
  const allInstr = [...new Set([...instr1.slice(0,3), ...instr2.slice(0,3)])];

  // Produktions-Tipp
  const prodTip1 = PRODUCTION_TIPS[g1] || '';
  const prodTip2 = PRODUCTION_TIPS[g2] || '';

  // Fusion-Genre-Bezeichnung
  const fusionGenreLabel = fusionStyle ? fusionStyle.fusionGenre : (g1 === g2 ? g1 : `${g1}/${g2}`);
  const fusionFeel = fusionStyle ? fusionStyle.feel : `Energie von ${g1} trifft Melodie von ${g2}`;
  const fusionProd = fusionStyle ? fusionStyle.production : `${prodTip1} + ${prodTip2}`;

  // Dynamik-Kurve basierend auf mood
  const mood = matchInfo.mood1;
  const dynamicCurves = {
    euphoric:   'Intro (piano) → Build-Up → Drop/Chorus (fff) → Break → Final Drop',
    melancholic:'Intro (pp) → Verse (mp) → Chorus (mf) → Bridge (climax) → Fade-Out',
    aggressive: 'Cold Open (ff) → Verse (f) → Pre-Chorus (crescendo) → Chorus (fff) → Breakdown → Outro',
    romantic:   'Intro (Solo Instrument) → Verse (pp) → Chorus (mf) → Bridge (f) → Final Chorus → Fade',
    anthemic:   'Intro (p) → Verse (mp) → Chorus (ff) → Breakdown (mp) → Final Chorus (fff) → Outro',
    mysterious: 'Intro (ambient) → Verse (mp) → Pre-Chorus (tension) → Chorus (f) → Break → Outro (fade)',
    energetic:  'Cold Open (f) → Verse (f) → Chorus (fff) → Bridge (break) → Final Chorus (fff)',
    peaceful:   'Intro (solo) → Verse (pp) → Chorus (mp) → Bridge (mf) → Outro (fade pp)',
    neutral:    'Intro → Verse (mp) → Chorus (f) → Bridge → Final Chorus → Outro',
  };

  return {
    fusionGenre: fusionGenreLabel,
    fusionFeel,
    suggestedKey,
    timeSignature,
    suggestedBPM,
    bpmRange: `${avgMin}–${avgMax} BPM`,
    instruments: allInstr,
    genre1Instruments: instr1,
    genre2Instruments: instr2,
    productionNotes: fusionProd,
    dynamicCurve: dynamicCurves[mood] || dynamicCurves.neutral,
    recordingTips: [
      `Tonart: ${suggestedKey} — gut für beide Genre-Stile`,
      `BPM: ${suggestedBPM} (zwischen ${g1}-typischen ${bpm1Range.min}–${bpm1Range.max} und ${g2}-typischen ${bpm2Range.min}–${bpm2Range.max})`,
      `Taktart: ${timeSignature}`,
      fusionProd,
    ],
  };
}
