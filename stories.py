# news-image-20261123 — story slate, Monday 23 November 2026.
# 44 stories, 7 regions. Every item verified Mon 23 Nov 2026 ~12:00 WIB
# against a named wire/primary source (see the research note).
# Rules baked into the decks: Democrats 258 (AP/Reuters, never CNN's 259);
# Dymer "at least 14" missing (wires split 14 vs 15); Cikande "3 confirmed
# dead, dozens missing; 24 body bags recovered" (body bags != deaths);
# Syria landmine "4-5 children killed" (wires split 4 vs 5); IRGC Patriot
# claim and the Khartoum drone-origin claim are attributed, never stated;
# Gauteng "agreed in principle; signing pending"; UK-EU "deal agreed",
# never "signed". Events dated Fri 19 / Sat 21 / Sun 22 Nov carry that
# date INSIDE their deck; nothing is decked as Monday news unless it is.
# The 7 developing stories (India Test, Nepal-Modi, NATO council, IG
# Metall strike, Dymer toll, Cikande toll, Monday markets) are decked at
# their research-time status; the ~20:00 WIB freeze pass updates them.
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
     "AT LEAST 14 MISSING IN KYIV DRONE HIT",
     "At least 14 missing in Dymer; 9 evacuated, 2 bodies found. Sun.",
     "Reuters", "flats"),
    (5, "Asia", "Disasters", "DISASTER",
     "CIKANDE FACTORY FIRE KILLS 3",
     "3 confirmed dead, dozens missing; 24 body bags recovered. Sat.",
     "Reuters", "fire"),
    (6, "Americas", "Sport", "SPORT",
     "VERSTAPPEN WINS LAS VEGAS GP",
     "Beats Norris by 0.639s; 35 lead changes, 352 overtakes. Sat.",
     "formula1.com", "race"),
    (7, "Oceania", "Sport", "CRICKET",
     "INDIA DECLARE 720/9 IN WELLINGTON",
     "Highest Test total in NZ; Rahul 136, Pant 128. NZ 227/5, day 5.",
     "ESPNcricinfo", "cricket"),
    (8, "Asia", "Politics", "DIPLOMACY",
     "NEPAL PM SHAH MEETS MODI TODAY",
     "First bilateral trip since Mar; talks in Delhi Mon.",
     "IANS", "flags"),
    (9, "Asia", "Politics", "EDUCATION",
     "S KOREA EDUCATION MINISTER QUITS",
     "Choi Kyo-jin resigns over CSAT cheating scandal; 111 cases. Sun.",
     "Reuters", "exam"),
    (10, "Europe", "Politics", "NATO",
     "NATO EMERGENCY MEETING TODAY",
     "3 Russian objects entered Polish airspace Fri; council meets Mon.",
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
     "WORST WEEK FOR STOCKS SINCE 2020",
     "S&P -3.7%, Nasdaq -5.28% Fri; Anthropic debuts $111.50 Thu; -9% Fri.",
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
    (25, "Europe", "Labour", "IG Metall strike today: 23,000 workers out (Reuters)"),
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
                "Investopedia, EC, QNC, MEM, PIB, FT, EIN, Okinawa Direct.")
