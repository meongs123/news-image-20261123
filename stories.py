# news-image-20261123 — story slate, Monday 23 November 2026.
# 44 stories, 7 regions. Every item verified Mon 23 Nov 2026 ~12:00 WIB
# against a named wire/primary source (see the research note).
# Rules baked into the decks: Democrats 258 (AP/Reuters, never CNN's 259);
# Dymer "11 killed" and Cikande "24 confirmed dead" are the freeze-pass
# final tolls (Kyiv Post 23 Nov; Kapolres Serang / Reuters 23 Nov);
# Syria landmine "4-5 children killed" (wires split 4 vs 5); IRGC Patriot
# claim and the Khartoum drone-origin claim are attributed, never stated;
# Gauteng "agreed in principle; signing pending"; UK-EU "deal agreed",
# never "signed". Events dated Fri 19 / Sat 21 / Sun 22 Nov carry that
# date INSIDE their deck; nothing is decked as Monday news unless it is.
# The 7 developing stories (India Test, Nepal-Modi, NATO council, IG
# Metall strike, Dymer toll, Cikande toll, Monday markets) were decked at
# their research-time status; the ~20:00 WIB freeze pass updated them
# (see git log) to their final Monday values.
# Peru quake (6.7) is NOT in this slate at all.

LEADS = [
    # (num, region, field, tag, headline, deck, source, art)
    (1, "World/Global", "Climate", "CLIMATE",
     "COP31 COLLAPSES: NO DEAL IN ANTALYA",
     "COP ends with no pact; EU rejects text without fossil fuels. "
     "First deal-less COP since 2009. Sun.",
     "Reuters", "cop"),
    (2, "Americas", "Politics", "POLITICS",
     "DEMOCRATS WIN 258 HOUSE SEATS",
     "Biggest House majority since 1992; Hubbard beats Foxx by ~330 "
     "votes after recount. 4 races uncalled. Sun.",
     "AP", "capitol"),
    (3, "Europe", "War", "BENGHAZI",
     "RUSSIAN CORVETTE SUNK AT BENGHAZI",
     "Suspected Ukrainian sea drones hit the Steregushchiy-class ship "
     "at anchor; 10 lightly hurt. Sun.",
     "Reuters", "sunk"),
    (4, "Europe", "War", "UKRAINE",
     "11 KILLED IN DYMER DRONE HIT",
     "11 dead incl. 11-yr-old girl; search over, 5 in hospital. Mon.",
     "Kyiv Post", "flats"),
    (5, "Asia", "Disasters", "DISASTER",
     "CIKANDE TOLL CONFIRMED AT 24",
     "24 confirmed dead Mon; ~30 still missing. DNA ID under way.",
     "Reuters", "fire"),
    (6, "Americas", "Sport", "SPORT",
     "VERSTAPPEN WINS LAS VEGAS GP",
     "Beats Norris by 0.639s; 35 lead changes, 352 overtakes. Sat.",
     "formula1.com", "race"),
    (7, "Oceania", "Sport", "CRICKET",
     "NZ SAVE DRAW IN WELLINGTON",
     "India 720/9 dec; NZ 368 & 239/5 hold on day 5. Mitchell 49*.",
     "ESPNcricinfo", "cricket"),
    (8, "Asia", "Politics", "DIPLOMACY",
     "NEPAL, INDIA SIGN 8 PACTS",
     "8 MoUs signed in Delhi; India pledges $1.63bn package. Mon.",
     "Hindu BusinessLine", "flags"),
    (9, "Asia", "Politics", "EDUCATION",
     "S KOREA EDUCATION MINISTER QUITS",
     "Choi Kyo-jin resigns over CSAT cheating scandal; 111 cases. Sun.",
     "Reuters", "exam"),
    (10, "Europe", "Politics", "NATO",
     "NATO TO SEND AWACS TO POLAND",
     "AWACS to deploy after missile incident; no Article 4 invoked. Mon.",
     "Reuters", "shield"),
    (11, "Middle East", "War", "GULF",
     "IRGC HITS US BASES IN BAHRAIN",
     "Iran claims 2 Patriot radars destroyed - unverified. 2 hurt in Sitra. Sat-Sun.",
     "Al Jazeera", "gulf"),
    (12, "Europe", "War", "BALTIC",
     "SPARTA II TOWED OUT AFTER HIT",
     "Hit Sat off Finland; 16 crew evacuated, 1 lightly hurt.",
     "Reuters", "tow"),
    (13, "Americas", "Economy", "MARKETS",
     "STOCKS SOAR IN MONDAY REBOUND",
     "S&P +4.73%, Nasdaq +6.51% Mon; Nvidia +31.5%.",
     "Investopedia", "chart"),
]

# (num, region, field, one-line text incl. source in parens).
# One line at 8px in a ~232px column holds ~52 chars; the renderer fails
# loudly if any brief exceeds it, so these are kept short on purpose.
BRIEFS = [
    (14, "Europe", "Sport", "Alcaraz wins first ATP Finals title"),
    (15, "Africa", "Health", "DR Congo Ebola: 11,376 cases, 5,568 deaths (16 Nov)"),
    (16, "Asia", "Economy", "EU-Indonesia trade deal CEPA signed Sat (EC)"),
    (17, "Europe", "Politics", "Thousands march in Lisbon on living costs (Reuters)"),
    (18, "Africa", "War", "24 civilians killed in South Sudan camp attack (AFP)"),
    (19, "Middle East", "War", "Gaza: 3 killed in strike on aid vehicle for WCK (EIN)"),
    (20, "Europe", "Sport", "Liverpool 4-0 Man Utd in Pochettino debut (Reuters)"),
    (21, "Africa", "Politics", "Gauteng coalition agreed; signing still pending (ANC)"),
    (22, "Africa", "Disasters", "Nigeria funeral boat capsizes; at least 24 dead (AP)"),
    (23, "World/Global", "War", "UN killer-robot talks end with no binding rules (AP)"),
    (24, "Asia", "Politics", "India-China hold 2nd round of LAC talks"),
    (25, "Europe", "Labour", "IG Metall strike: 23,000+ workers called out (Reuters)"),
    (26, "Americas", "Politics", "Bolsonaro in ICU after abdomen blockage (Reuters)"),
    (27, "Americas", "Tech", "FBI probes suspected hack of crime database (AP)"),
    (28, "Africa", "War", "Khartoum drone strikes kill 4, hit UN building (AP)"),
    (29, "Americas", "Transport", "Delta Atlanta delays over automation fault (Reuters)"),
    (30, "Asia", "Disasters", "Kota crash: 9 pilgrims killed in Rajasthan (ANI)"),
    (31, "Asia", "Health", "India launches first home-made H5N1 vaccine (PIB)"),
    (32, "Europe", "Politics", "UK-EU reset deal agreed, not signed (Reuters)"),
    (33, "Asia", "Politics", "Myanmar rejects ICJ genocide verdict (Reuters)"),
    (34, "Middle East", "War", "Houthi missile hits PIF Tower, Riyadh, Thu (Reuters)"),
    (35, "Americas", "Politics", "Senate blocks Iran war-powers curb 51-48 Thu (Reuters)"),
    (36, "Asia", "Culture", "Shuri Castle main hall reopens today (Okinawa)"),
    (37, "Americas", "Society", "Miley Cyrus marries Maxx Morando Sat (People)"),
    (38, "Middle East", "War", "Syria landmine kills 4-5 children in Idlib (MEM)"),
    (39, "Asia", "Politics", "Bangladesh: Yunus home torched; at least 4 dead"),
    (40, "Americas", "Tech", "US ports face surge in cyberattack attempts (FT)"),
    (41, "Asia", "Sport", "Cricketer Chahal joins BJP's OBC Morcha (ANI)"),
    (42, "World/Global", "Space", "BepiColombo enters Mercury orbit Sat (ESA)"),
    (43, "Americas", "Justice", "Mexico captures 'El Chapo Isidro' Fri (Reuters)"),
    (44, "Africa", "Politics", "Somalia-UAE row: rallies as deadline runs out (QNC)"),
]

REGION_ORDER = ["Americas", "Asia", "Europe", "Africa", "Middle East",
                "World/Global", "Oceania"]

# Short label used inside the region bar (the full name is in the footer).
REGION_SHORT = {"World/Global": "World"}

DATE_CHECK = [
    ("Shenzhen Trump-Xi-Putin summit", "Thu 19 Nov"),
    ("ICJ Rohingya genocide verdict", "Thu 19 Nov"),
    ("PIF Tower, Riyadh, hit", "Thu 19 Nov"),
    ("Senate Iran war-powers vote 51-48", "Thu 19 Nov"),
    ("BepiColombo Mercury arrival", "Sat 21 Nov 18:24 UTC"),
]

SOURCES_LINE = ("Sources: Reuters, AP, Al Jazeera, AFP, ANI, IANS, ESA, "
                "CNN, Fox, People, ESPNcricinfo, formula1.com, "
                "Investopedia, EC, QNC, MEM, PIB, FT, EIN, Okinawa Direct, "
                "Kyiv Post, Hindu BusinessLine.")
