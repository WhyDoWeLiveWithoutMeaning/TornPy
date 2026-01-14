from enum import Enum
from typing import List, Optional
from pydantic import BaseModel

class Crimes(int, Enum):
    SEARCH_FOR_CASH = 1
    BOOTLEGGING = 2
    GRAFFITI = 3
    SHOPLIFTING = 4
    PICKPOCKETING = 5
    CARD_SKIMMING = 6
    BURGLARY = 7
    HUSTLING = 8
    DISPOSAL = 9
    CRACKING = 10
    FORGERY = 11
    SCAMMING = 12
    ARSON = 13

class RaceClassEnum(str, Enum):
    A = "A"
    B = "B"
    C = "C"
    D = "D"
    E = "E"

class MissionDifficultyEnum(str, Enum):
    VERY_EASY = "Very easy"
    EASY = "Easy"
    MEDIUM = "Medium"
    HARD = "Hard"
    VERY_HARD = "Very hard"
    EXPERT = "Expert"

class UserGenderEnum(str, Enum):
    MALE = "Male"
    FEMALE = "Female"
    ENBY = "Enby"

class UserStatusStateEnum(str, Enum):
    ABROAD = "Abroad"
    AWOKEN = "Awoken"
    DORMANT = "Dormant"
    FALLEN = "Fallen"
    FEDERAL = "Federal"
    HOSPITAL = "Hospital"
    JAIL = "Jail"
    OKAY = "Okay"
    TRAVELING = "Traveling"

class ItemRarity(str, Enum):
    YELLOW = "Yellow"
    ORANGE = "Orange"
    RED = "Red"

class UserPlaneImageTypeEnum(str, Enum):
    PRIVATE_JET = "private_jet"
    LIGHT_AIRCRAFT = "light_aircraft"
    AIRLINER = "airliner"

class TornItemAmmoTypeEnum(str, Enum):
    STANDARD = "Standard"
    HOLLOWPOINT = "Hollow Point"
    PIERCING = "Piercing"
    TRACER = "Tracer"
    INCENDIARY = "Incendiary"

class ApiFiltersAttacksRevivesEnum(str, Enum):
    INCOMING = "incoming"
    OUTGOING = "outgoing"
    IDFILTER = "idFilter"

class FactionAttackResult(str, Enum):
    NONE = "None"
    ATTACKED = "Attacked"
    MUGGED = "Mugged"
    HOSPITALIZED = "Hospitalized"
    ARRESTED = "Arrested"
    LOOTED = "Looted"
    LOST = "Lost"
    STALEMATE = "Stalemate"
    ASSIST = "Assist"
    ESCAPE = "Escape"
    TIMEOUT = "Timeout"
    SPECIAL = "Special"
    BOUNTY = "Bounty"
    INTERRUPTED = "Interrupted"

class RPSEnum(str, Enum):
    ROCK = "rock"
    PAPER = "paper"
    SCISSORS = "scissors"

class UserCrimeUniquesRewardAmmoEnum(str, Enum):
    STANDARD = "standard"
    SPECIAL = "special"

class TornItemTypeEnum(str, Enum):
    ALCOHOL = "Alcohol"
    ARMOR = "Armor"
    ARTIFACT = "Artifact"
    BOOK = "Book"
    BOOSTER = "Booster"
    CANDY = "Candy"
    CAR = "Car"
    CLOTHING = "Clothing"
    COLLECTIBLE = "Collectible"
    DRUG = "Drug"
    ENERGY_DRINK = "Energy Drink"
    ENHANCER = "Enhancer"
    FLOWER = "Flower"
    JEWELRY = "Jewelry"
    MATERIAL = "Material"
    MEDICAL = "Medical"
    OTHER = "Other"
    PLUSHIE = "Plushie"
    SPECIAL = "Special"
    SUPPLY_PACK = "Supply Pack"
    TOOL = "Tool"
    UNUSED = "Unused"
    WEAPON = "Weapon"

class TornItemWeaponTypeEnum(str, Enum):
    HEAVY_ARTILLERY = "Heavy artillery"
    MACHINE_GUN = "Machine gun"
    PISTOL = "Pistol"
    RIFLE = "Rifle"
    SHOTGUN = "Shotgun"
    SMG = "SMG"
    TEMPORARY = "Temporary"
    CLUBBING = "Clubbing"
    PIERCING = "Piercing"
    SLASHING = "Slashing"
    MECHANICAL = "Mechanical"

class TornItemWeaponCategoryEnum(str, Enum):
    MELEE = "Melee"
    SECONDARY = "Secondary"
    PRIMARY = "Primary"
    TEMPORARY = "Temporary"

class TornItemAmmoTypeEnum(str, Enum):
    STANDARD = "Standard"
    HOLLOW_POINT = "Hollow Point"
    PIERCING = "Piercing"
    TRACER = "Tracer"
    INCENDIARY = "Incendiary"

class ApiKeyAccessTypeEnum(str, Enum):
    CUSTOM = "Custom"
    PUBLIC_ONLY = "Public Only"
    MINIMAL_ACCESS = "Minimal Access"
    LIMITED_ACCESS = "Limited Access"
    FULL_ACCESS = "Full Access"

class PersonalStatsCategoryEnum(str, Enum):
    ALL = "all"
    POPULAR = "popular"
    ATTACKING = "attacking"
    BATTLE_STATS = "battle_stats"
    JOBS = "jobs"
    TRADING = "trading"
    JAIL = "jail"
    HOSPITAL = "hospital"
    FINISHING_HITS = "finishing_hits"
    COMMUNICATION = "communication"
    CRIMES = "crimes"
    BOUNTIES = "bounties"
    INVESTMENTS = "investments"
    ITEMS = "items"
    TRAVEL = "travel"
    DRUGS = "drugs"
    MISSIONS = "missions"
    RACING = "racing"
    NETWORTH = "networth"
    OTHER = "other"
    ITEM_MARKET_CUSTOMERS = "itemmarketcustomers"
    ITEM_MARKET_SALES = "itemmarketsales"
    ITEM_MARKET_REVENUE = "itemmarketrevenue"
    ITEM_MARKET_FEES = "itemmarketfees"

class PersonalStatsStatName(str, Enum):
    # --- Combat & Attacks ---
    ATTACKS_WON = "attackswon"
    ATTACKS_LOST = "attackslost"
    ATTACKS_DRAW = "attacksdraw"
    ATTACKS_ASSISTED = "attacksassisted"
    DEFENDS_WON = "defendswon"
    DEFENDS_LOST = "defendslost"
    DEFENDS_STALEMATED = "defendsstalemated"
    ELO = "elo"
    YOU_RUNAWAY = "yourunaway"
    THEY_RUNAWAY = "theyrunaway"
    UNARMORED_WIN = "unarmoredwon"
    BEST_KILL_STREAK = "bestkillstreak"
    ATTACK_HITS = "attackhits"
    ATTACK_MISSES = "attackmisses"
    ATTACK_DAMAGE = "attackdamage"
    BEST_DAMAGE = "bestdamage"
    ONE_HIT_KILLS = "onehitkills"
    ATTACK_CRITICAL_HITS = "attackcriticalhits"
    ROUNDS_FIRED = "roundsfired"
    SPECIAL_AMMO_USED = "specialammoused"
    HOLLOW_AMMO_USED = "hollowammoused"
    TRACER_AMMO_USED = "tracerammoused"
    PIERCING_AMMO_USED = "piercingammoused"
    INCENDIARY_AMMO_USED = "incendiaryammoused"
    ATTACKS_STEALTHED = "attacksstealthed"
    RETALS = "retals"
    MONEY_MUGGED = "moneymugged"
    LARGEST_MUG = "largestmug"
    ITEMS_LOOTED = "itemslooted"
    HIGHEST_BEATEN = "highestbeaten"
    RESPECT_FOR_FACTION = "respectforfaction"
    RANKED_WAR_HITS = "rankedwarhits"
    RAID_HITS = "raidhits"

    # --- Interaction & Trade ---
    AUCTIONS_WON = "auctionswon"
    AUCTION_SELLS = "auctionsells"
    ITEMS_SENT = "itemssent"
    TRADES = "trades"
    CITY_ITEMS_BOUGHT = "cityitemsbought"
    POINTS_BOUGHT = "pointsbought"
    POINTS_SOLD = "pointssold"
    BAZAAR_CUSTOMERS = "bazaarcustomers"
    BAZAAR_SALES = "bazaarsales"
    BAZAAR_PROFIT = "bazaarprofit"

    # --- Legal & Medical ---
    JAILED = "jailed"
    PEOPLE_BUSTED = "peoplebusted"
    FAILED_BUSTS = "failedbusts"
    PEOPLE_BOUGHT = "peoplebought"
    PEOPLE_BOUGHT_SPENT = "peopleboughtspent"
    HOSPITAL = "hospital"
    MEDICAL_ITEMS_USED = "medicalitemsused"
    BLOOD_WITHDRAWN = "bloodwithdrawn"
    REVIVE_SKILL = "reviveskill"
    REVIVES = "revives"
    REVIVES_RECEIVED = "revivesreceived"

    # --- Weapon Specific ---
    HEAVY_HITS = "heavyhits"
    MACHINE_HITS = "machinehits"
    RIFLE_HITS = "riflehits"
    SMG_HITS = "smghits"
    SHOTGUN_HITS = "shotgunhits"
    PISTOL_HITS = "pistolhits"
    TEMP_HITS = "temphits"
    PIERCING_HITS = "piercinghits"
    SLASHING_HITS = "slashinghits"
    CLUBBING_HITS = "clubbinghits"
    MECHANICAL_HITS = "mechanicalhits"
    H2H_HITS = "h2hhits"

    # --- Communication ---
    MAILS_SENT = "mailssent"
    FRIEND_MAILS_SENT = "friendmailssent"
    FACTION_MAILS_SENT = "factionmailssent"
    COMPANY_MAILS_SENT = "companymailssent"
    SPOUSE_MAILS_SENT = "spousemailssent"
    CLASSIFIED_ADS_PLACED = "classifiedadsplaced"
    PERSONALS_PLACED = "personalsplaced"

    # --- Crimes 1.0 (Legacy) ---
    CRIMINAL_OFFENSES_OLD = "criminaloffensesold"
    SELL_ILLEGAL_GOODS = "sellillegalgoods"
    THEFT_OLD = "theftold"
    AUTO_THEFT_CRIME = "autotheftcrime"
    DRUG_DEALS_CRIME = "drugdealscrime"
    COMPUTER_CRIME = "computercrime"
    FRAUD_OLD = "fraudold"
    MURDER_CRIME = "murdercrime"
    OTHER_CRIME = "othercrime"
    ORGANIZED_CRIMES = "organizedcrimes"

    # --- Bounties & Finds ---
    BOUNTIES_PLACED = "bountiesplaced"
    TOTAL_BOUNTY_SPENT = "totalbountyspent"
    BOUNTIES_COLLECTED = "bountiescollected"
    TOTAL_BOUNTY_REWARD = "totalbountyreward"
    BOUNTIES_RECEIVED = "bountiesreceived"
    RECEIVED_BOUNTY_VALUE = "receivedbountyvalue"
    CITY_FINDS = "cityfinds"
    DUMP_FINDS = "dumpfinds"
    ITEMS_DUMPED = "itemsdumped"

    # --- Consumables & Boosters ---
    BOOKS_READ = "booksread"
    BOOSTERS_USED = "boostersused"
    CONSUMABLES_USED = "consumablesused"
    CANDY_USED = "candyused"
    ALCOHOL_USED = "alcoholused"
    ENERGY_DRINK_USED = "energydrinkused"
    STAT_ENHANCERS_USED = "statenhancersused"
    EASTER_EGGS_FOUND = "eastereggsfound"
    EASTER_EGGS_USED = "eastereggsused"
    VIRUSES_CODED = "virusescoded"

    # --- Travel ---
    TRAVEL_TIMES = "traveltimes"
    TIME_SPENT_TRAVELING = "timespenttraveling"
    ITEMS_BOUGHT_ABROAD = "itemsboughtabroad"
    ATTACKS_WON_ABROAD = "attackswonabroad"
    DEFENDS_LOST_ABROAD = "defendslostabroad"
    ARG_TRAVEL = "argtravel"
    MEX_TRAVEL = "mextravel"
    UAE_TRAVEL = "uaetravel"
    HAW_TRAVEL = "hawtravel"
    JAP_TRAVEL = "japtravel"
    UK_TRAVEL = "uktravel"
    SA_TRAVEL = "satravel"
    SWI_TRAVEL = "switravel"
    CHI_TRAVEL = "chitravel"
    CAN_TRAVEL = "cantravel"
    CAY_TRAVEL = "caytravel"

    # --- Drugs & Rehab ---
    DRUGS_USED = "drugsused"
    OVERDOSED = "overdosed"
    REHABS = "rehabs"
    REHAB_COST = "rehabcost"
    CAN_TAKEN = "cantaken"
    EXT_TAKEN = "exttaken"
    KET_TAKEN = "kettaken"
    LSD_TAKEN = "lsdtaken"
    OPI_TAKEN = "opitaken"
    PCP_TAKEN = "pcptaken"
    SHR_TAKEN = "shrtaken"
    SPE_TAKEN = "spetaken"
    VIC_TAKEN = "victaken"
    XAN_TAKEN = "xantaken"

    # --- Racing & Missions ---
    MISSIONS_COMPLETED = "missionscompleted"
    CONTRACTS_COMPLETED = "contractscompleted"
    DUKE_CONTRACTS_COMPLETED = "dukecontractscompleted"
    MISSION_CREDITS_EARNED = "missioncreditsearned"
    RACING_SKILL = "racingskill"
    RACING_POINTS_EARNED = "racingpointsearned"
    RACES_ENTERED = "racesentered"
    RACES_WON = "raceswon"

    # --- General & Stats ---
    NETWORTH = "networth"
    TIME_PLAYED = "timeplayed"
    ACTIVE_STREAK = "activestreak"
    BEST_ACTIVE_STREAK = "bestactivestreak"
    AWARDS = "awards"
    REFILLS = "refills"
    NERVE_REFILLS = "nerverefills"
    TOKEN_REFILLS = "tokenrefills"
    MERITS_BOUGHT = "meritsbought"
    DAYS_BEEN_DONATOR = "daysbeendonator"
    
    # --- Crimes 2.0 Stats ---
    CRIMINAL_OFFENSES = "criminaloffenses"
    VANDALISM = "vandalism"
    THEFT = "theft"
    COUNTERFEITING = "counterfeiting"
    FRAUD = "fraud"
    ILLICIT_SERVICES = "illicitservices"
    CYBERCRIME = "cybercrime"
    EXTORTION = "extortion"
    ILLEGAL_PRODUCTION = "illegalproduction"

    # --- Battle Stats ---
    CURRENT_KILLSTREAK = "currentkillstreak"
    STRENGTH = "strength"
    DEFENSE = "defense"
    SPEED = "speed"
    DEXTERITY = "dexterity"
    TOTAL_STATS = "totalstats"
    MANUAL_LABOR = "manuallabor"
    INTELLIGENCE = "intelligence"
    ENDURANCE = "endurance"
    TOTAL_WORKING_STATS = "totalworkingstats"

    # --- Finance & Stocks ---
    MONEY_INVESTED = "moneyinvested"
    INVESTED_PROFIT = "investedprofit"
    INVEST_AMOUNT = "investamount"
    BANK_TIME_LEFT = "banktimeleft"
    STOCK_PROFITS = "stockprofits"
    STOCK_LOSSES = "stocklosses"
    STOCK_FEES = "stockfees"
    STOCK_NET_PROFITS = "stocknetprofits"
    STOCK_PAYOUTS = "stockpayouts"

    # --- Networth Breakdown ---
    NETWORTH_WALLET = "networthwallet"
    NETWORTH_VAULT = "networthvault"
    NETWORTH_BANK = "networthbank"
    NETWORTH_CAYMAN = "networthcayman"
    NETWORTH_POINTS = "networthpoints"
    NETWORTH_ITEMS = "networthitems"
    NETWORTH_DISPLAY_CASE = "networthdisplaycase"
    NETWORTH_BAZAAR = "networthbazaar"
    NETWORTH_ITEM_MARKET = "networthitemmarket"
    NETWORTH_PROPERTIES = "networthproperties"
    NETWORTH_STOCKMARKET = "networthstockmarket"
    NETWORTH_AUCTIONHOUSE = "networthauctionhouse"
    NETWORTH_BOOKIE = "networthbookie"
    NETWORTH_COMPANY = "networthcompany"
    NETWORTH_ENLISTED_CARS = "networthenlistedcars"
    NETWORTH_PIGGYBANK = "networthpiggybank"
    NETWORTH_PENDING = "networthpending"
    NETWORTH_LOAN = "networthloan"
    NETWORTH_UNPAID_FEES = "networthunpaidfees"

    # --- Skills ---
    HUNTING_SKILL = "huntingskill"
    SEARCH_FOR_CASH_SKILL = "searchforcashskill"
    BOOTLEGGING_SKILL = "bootleggingskill"
    GRAFFITI_SKILL = "graffitiskill"
    SHOPLIFTING_SKILL = "shopliftingskill"
    PICKPOCKETING_SKILL = "pickpocketingskill"
    CAR_SKIMMING_SKILL = "cardskimmingskill"
    BURGLARY_SKILL = "burglaryskill"
    HUSTLING_SKILL = "hustlingskill"
    DISPOSAL_SKILL = "disposalskill"
    CRACKING_SKILL = "crackingskill"
    FORGERY_SKILL = "forgeryskill"
    SCAMMING_SKILL = "scammingskill"
    ARSON_SKILL = "arsonskill"

class ForumFeedTypeEnum(int, Enum):
    X_POSTED_A_THREAD = 1
    X_CREATED_A_THREAD = 2
    X_LIKED_YOUR_THREAD = 3
    X_DISLIKED_YOUR_THREAD = 4
    X_LIKED_YOUR_POST = 5
    X_DISLIKED_YOUR_POST = 6
    X_QUOTED_YOUR_POST = 7

class FactionApplicationStatusEnum(str, Enum):
    ACCEPTED = "accepted"
    DECLINED = "declined"
    WITHDRAWN = "withdrawn"
    ACTIVE = "active"
