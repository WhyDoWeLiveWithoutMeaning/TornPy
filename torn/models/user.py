from pydantic import BaseModel, Field, RootModel
from typing import List, Optional, Union, Annotated, Literal, Dict, Any, TypeAlias
from .common import *
from .enums import *

# Sub Sub Sub Models

class UserCrimeRewardItem(BaseModel):
    id: int
    amount: int

class UserCrimeUniquesRewardMoney(BaseModel):
    min: int
    max: int

class UserCrimeUniquesRewardAmmo(BaseModel):
    amount: int
    type: UserCrimeUniquesRewardAmmoEnum

class UserMissionGiverContractsRewards(BaseModel):
    money: int
    credits: int

class MissionRewardDetailsAmmo(BasicTornModel):
    type: TornItemAmmoTypeEnum

class MissionRewardDetailsItem(BasicTornModel):
    type: TornItemTypeEnum
    sub_type: Optional[TornItemWeaponTypeEnum] = None

class PersonalStatsAttackingFactionTerritory(BaseModel):
    wall_joins: int
    wall_clears: int
    wall_time: int

class PersonalStatsTradingItemsBought(BaseModel):
    market: int
    shops: int

class PersonalStatsTradingItemsAuctions(BaseModel):
    won: int
    sold: int

class PersonalStatsOtherActivityStreak(BaseModel):
    current: int
    best: int

# SubSub models

class AttackModifiers(BaseModel):
    fair_fight: float
    war: float
    retaliation: float
    group: float
    overseas: float
    chain: float
    warlord: float

class UserStatus(BaseModel):
    description: str
    details: Optional[str] = None
    state: Optional[UserStatusStateEnum] = None
    color: str
    until: Optional[int] = None
    plane_image_type: Optional[UserPlaneImageTypeEnum] = None

class UserAmmoType(BaseModel):
    name: TornItemAmmoTypeEnum
    quantity: int
    equipped: bool

class AttackingFinishingHitEffects(BaseModel):
    name: str
    value: int

class AttackPlayerSimplified(BaseModel):
    id: int
    faction_id: Optional[int] = None

class AttackSimplified(BaseModel):
    id: int
    code: str
    started: int
    ended: int
    attacker: Optional[AttackPlayerSimplified] = None
    defender: AttackPlayerSimplified
    result: FactionAttackResult
    respect_gain: float
    respect_loss: float

class AttackPlayer(BasicUser):
    level: int
    faction: Optional[AttackPlayerFaction] = None

class Attack(BaseModel):
    id: int
    code: str
    started: int
    ended: int
    attacker: Optional[AttackPlayer] = None
    defender: AttackPlayer
    result: FactionAttackResult
    respect_gain: float
    respect_loss: float
    chain: int
    is_interrupted: bool
    is_stealthed: bool
    is_raid: bool
    is_ranked_war: bool
    finishing_hit_effects: List[AttackingFinishingHitEffects]
    modifiers: AttackModifiers

class UserBarBasic(BaseModel):
    current: int
    maximum: int

class UserBar(UserBarBasic):
    increment: int
    interval: int
    tick_time: int
    full_time: int

class UserBattleStatModifierDetail(BaseModel):
    effect: str
    value: int
    type: str

class UserCrimeDetailsBootleggingOnlineStore(BaseModel):
    earnings: int
    visits: int
    customers: int
    sales: int

class UserCrimeDetailsBootleggingDVDSales(BaseModel):
    action: int
    comedy: int
    drama: int
    fantasy: int
    horror: int
    romance: int
    thriller: int
    sci_fi: int
    total: int
    earnings: int

class UserCrimeDetailsCardSkimmingCardDetails(BaseModel):
    recoverable: int
    recovered: int
    sold: int
    lost: int
    areas: List[UserCrimeRewardItem]

class UserCrimeDetailsCardSkimmingSkimmerDetails(BaseModel):
    active: int
    most_lucrative: int
    oldest_recovered: int
    lost: int

class UserCrimeDetailsScammingZones(BaseModel):
    red: int
    neutral: int
    concern: int
    sensitivity: int
    temptation: int
    hesitation: int
    low_reward: int
    medium_reward: int
    high_reward: int

class UserCrimeDetailsScammingConcerns(BaseModel):
    attempts: int
    resolved: int

class UserCrimeDetailsScammingPayouts(BaseModel):
    low: int
    medium: int
    high: int

class UserCrimeDetailsScammingEmails(BaseModel):
    scraper: int
    phisher: int

class UserCrimeRewardItem(BaseModel):
    id: int
    amount: int

class UserCrimeRewardAmmo(BaseModel):
    standard: int
    special: int

class UserSubCrime(BaseModel):
    id: int
    total: int
    success: int
    fail: int

class UserCrimeUniquesReward(BaseModel):
    items: List[UserCrimeRewardItem]
    money: Optional[UserCrimeUniquesRewardMoney] = None
    ammo: Optional[UserCrimeUniquesRewardAmmo] = None

class ForumPollVote(BaseModel):
    answer: str
    votes: int

class UserMissionGiverContracts(BaseModel):
    title: str
    difficulty: MissionDifficultyEnum
    status: MissionStatusEnum
    created_at: int
    started_at: Optional[int] = None
    expires_at: Optional[int] = None
    completed_at: Optional[int] = None
    rewards: Optional[UserMissionGiverContractsRewards] = None

class PersonalStatsCrimesV2Offenses(BaseModel):
    vandalism: int
    fraud: int
    theft: int
    counterfeiting: int
    illicit_services: int
    cybercrime: int
    extortion: int
    illegal_production: int
    organized_crimes: int
    total: int

class PersonalStatsCrimesV2Skills(BaseModel):
    search_for_cash: int
    bootlegging: int
    graffiti: int
    shoplifting: int
    pickpocketing: int
    card_skimming: int
    burglary: int
    hustling: int
    disposal: int
    cracking: int
    forgery: int
    scamming: int
    arson: int

class PersonalStatsAttackingAttacks(BaseModel):
    won: int
    lost: int
    stalemate: int
    assist: int
    stealth: int

class PersonalStatsAttackingDefends(BaseModel):
    won: int
    lost: int
    stalemate: int
    total: int

class PersonalStatsAttackingEscapes(BaseModel):
    player: int
    foes: int

class PersonalStatsAttackingKillstreak(BaseModel):
    best: int
    current: int

class PersonalStatsAttackingHits(BaseModel):
    success: int
    miss: int
    critical: int
    one_hit_kills: int

class PersonalStatsAttackingDamage(BaseModel):
    total: int
    best: int

class PersonalStatsAttackingNetworth(BaseModel):
    money_mugged: int
    largest_mug: int
    items_looted: int

class PersonalStatsAttackingAmmunition(BaseModel):
    total: int
    special: int
    hollow_point: int
    tracer: int
    piercing: int
    incendiary: int

class PersonalStatsAttackingFaction(BaseModel):
    respect: int
    retaliations: int
    ranked_war_hits: int
    raid_hits: int
    territory: PersonalStatsAttackingFactionTerritory

class PersonalStatsJobsStats(BaseModel):
    manual: int
    intelligence: int
    endurance: int
    total: int

class PersonalStatsTradingItems(BaseModel):
    bought: PersonalStatsTradingItemsBought
    auctions: PersonalStatsTradingItemsAuctions
    sent: int

class PersonalStatsTradingPoints(BaseModel):
    bought: int
    sold: int

class PersonalStatsTradingBazaar(BaseModel):
    customers: int
    sales: int
    profit: int

class PersonalStatsTradingItemMarket(BaseModel):
    customers: int
    sales: int
    revenue: int
    fees: int

class PersonalStatsJailBusts(BaseModel):
    success: int
    fails: int

class PersonalStatsJailBails(BaseModel):
    amount: int
    fees: int

class PersonalStatsHospitalReviving(BaseModel):
    skill: int
    revives: int
    revives_received: int

class PersonalStatsCommunicationMailsSent(BaseModel):
    total: int
    friends: int
    faction: int
    colleagues: int
    spouse: int

class PersonalStatsBountiesGeneric(BaseModel):
    amount: int
    value: int

class PersonalStatsInvestmentsBank(BaseModel):
    total: int
    profit: int
    current: int
    time_remaining: int

class PersonalStatsInvestmentsStocks(BaseModel):
    profits: int
    losses: int
    fees: int
    net_profits: int
    payouts: int

class PersonalStatsItemsFound(BaseModel):
    city: int
    dump: int
    easter_eggs: int

class PersonalStatsItemsUsed(BaseModel):
    books: int
    boosters: int
    consumables: int
    candy: int
    alcohol: int
    energy_drinks: int
    stat_enhancers: int
    easter_eggs: int

class PersonalStatsTravelHunting(BaseModel): skill: int

class PersonalStatsDrugsRehabilitation(BaseModel):
    amount: int
    fees: int

class PersonalStatsMissionsContracts(BaseModel):
    total: int
    duke: int

class PersonalStatsRacingRaces(BaseModel):
    entered: int
    won: int

class PersonalStatsOtherActivity(BaseModel):
    time: int
    streak: PersonalStatsOtherActivityStreak

class PersonalStatsOtherRefills(BaseModel):
    energy: int
    nerve: int
    token: int

# Mid Sub Models

class UserBattleStatDetail(BaseModel):
    value: int
    modifier: int
    modifiers: List[UserBattleStatModifierDetail]

class UserCrimeDetailsBootlegging(BaseModel):
    online_store: UserCrimeDetailsBootleggingOnlineStore
    dvd_sales: UserCrimeDetailsBootleggingDVDSales
    dvds_copied: int

class UserCrimeDetailsGraffiti(BaseModel):
    cans_used: int
    most_graffiti_in_one_area: int
    most_graffiti_simultaneously: int
    graffiti_removed: int
    cost_to_city: int

class UserCrimeDetailsShoplifting(BaseModel):
    average_notoriety: float

class UserCrimeDetailsCardSkimming(BaseModel):
    card_details: UserCrimeDetailsCardSkimmingCardDetails
    skimmers: UserCrimeDetailsCardSkimmingSkimmerDetails

class UserCrimeDetailsHustling(BaseModel):
    total_audience_gathered: int
    biggest_money_won: int
    shill_money_collected: int
    pickpocket_money_collected: int

class UserCrimeDetailsCracking(BaseModel):
    brute_force_cycles: int
    encryption_layers_broken: int
    highest_mips: int
    chars_guessed: int
    chars_guessed_total: int

class UserCrimeDetailsScamming(BaseModel):
    most_responses: int
    zones: UserCrimeDetailsScammingZones
    concerns: UserCrimeDetailsScammingConcerns
    payouts: UserCrimeDetailsScammingPayouts
    emails: UserCrimeDetailsScammingEmails

class UserCrimeRewards(BaseModel):
    money: int
    ammo: UserCrimeRewardAmmo
    items: List[UserCrimeRewardItem]

class UserCrimeAttempts(BaseModel):
    total: int
    success: int
    fail: int
    critical_fail: int
    subcrimes: List[UserSubCrime]

class UserCrimeUniques(BaseModel):
    id: int
    rewards: UserCrimeUniquesReward

class UserCurrentEducation(BaseModel):
    id: int
    until: int

class TornItemEquipmentStats(TornItemBaseStats):
    quality: float

class ForumThreadAuthor(BaseModel):
    id: int
    username: str
    karma: int

class ForumSubscribedThreadPostsCount(BaseModel):
    new: int
    total: int

class ForumPoll(BaseModel):
    question: str
    answers_count: int
    answers: List[ForumPollVote]

class HofValue(BaseModel):
    value: int
    rank: int

class HofValueFloat(BaseModel):
    value: float
    rank: int

class HofValueString(BaseModel):
    value: str
    rank: Optional[int] = None

class UserJobPoints(BaseModel):
    army: int
    casino: int
    education: int
    grocer: int
    law: int
    medical: int

class UserCompanyPoints(BaseModel):
    company: BasicTornModel
    points: int

class UserLastAction(BaseModel):
    status: UserLastActionStatusEnum
    timestamp: int
    relative: str

class UserStatus(BaseModel):
    description: str
    details: Optional[str] = None
    state: Union[UserStatusStateEnum, str]
    color: str
    until: Optional[int] = None
    plane_image_type: Optional[UserPlaneImageTypeEnum] = None

class UserLogDetails(BaseModel):
    id: int
    title: str
    category: str

class UserMeritUpgrade(BaseModel):
    id: int
    level: int

class UserMissionGiver(BaseModel):
    id: int
    name: str
    contracts: List[UserMissionGiverContracts]

class UserMissionReward(BaseModel):
    type: MissionRewardUpgrade
    details: Union[MissionRewardDetailsItem, MissionRewardDetailsAmmo, BasicTornModel]
    amount: int
    cost: int
    expires_at: int

class UserMoneyCityBank(BaseModel):
    amount: int
    profit: int
    duration: int
    interest_rate: float
    until: int
    invested_at: int

class UserMoneyFactionBank(BaseModel):
    money: int
    points: int

class PersonalStatsCrimesV1(BaseModel):
    total: int
    sell_illgal_goods: int
    theft: int
    auto_theft: int
    drug_deals: int
    computer: int
    fraud: int
    murder: int
    other: int
    organized_crimes: int
    version: str

class PersonalStatsCrimesV2(BaseModel):
    offenses: PersonalStatsCrimesV2Offenses
    skills: PersonalStatsCrimesV2Skills
    version: str

class PersonalStatsAttacking(BaseModel):
    attacks: PersonalStatsAttackingAttacks
    defends: PersonalStatsAttackingDefends
    elo: int
    unarmored_wins: int
    highest_level_beaten: int
    escapes: PersonalStatsAttackingEscapes
    killstreak: PersonalStatsAttackingKillstreak
    hits: PersonalStatsAttackingHits
    damage: PersonalStatsAttackingDamage
    networth: PersonalStatsAttackingNetworth
    faction: PersonalStatsAttackingFaction

class PersonalStatsBattleStats(BaseModel):
    strength: int
    defense: int
    speed: int
    dexterity: int
    total: int

class PersonalStatsJobs(BaseModel):
    job_points_used: int
    trains_received: int
    stats: Optional[PersonalStatsJobsStats] = None

class PersonalStatsTrading(BaseModel):
    items: PersonalStatsTradingItems
    trades: int
    points: PersonalStatsTradingPoints
    bazaar: PersonalStatsTradingBazaar
    item_market: PersonalStatsTradingItemMarket

class PersonalStatsJail(BaseModel):
    times_jailed: int
    busts: PersonalStatsJailBusts
    bails: PersonalStatsJailBails

class PersonalStatsHospital(BaseModel):
    times_hospitalized: int
    medical_items_used: int
    blood_withdrawn: int
    reviving: PersonalStatsHospitalReviving

class PersonalStatsFinishingHits(BaseModel):
    heavy_artillery: int
    machine_guns: int
    rifles: int
    sub_machine_guns: int
    shotguns: int
    pistols: int
    temporary: int
    piercing: int
    slashing: int
    clubbing: int
    mechanical: int
    hand_to_hand: int

class PersonalStatsCommunication(BaseModel):
    mails_sent: PersonalStatsCommunicationMailsSent
    classified_ads: int
    personals: int

class PersonalStatsBounties(BaseModel):
    placed: PersonalStatsBountiesGeneric
    collected: PersonalStatsBountiesGeneric
    received: PersonalStatsBountiesGeneric

class PersonalStatsInvestments(BaseModel):
    bank: PersonalStatsInvestmentsBank
    stocks: PersonalStatsInvestmentsStocks

class PersonalStatsItems(BaseModel):
    found: PersonalStatsItemsFound
    trashed: int
    used: PersonalStatsItemsUsed
    viruses_coded: int

class PersonalStatsTravel(BaseModel):
    total: int
    time_spent: int
    hunting: PersonalStatsTravelHunting
    attacks_won: int
    defends_lost: int
    argentina: int
    canada: int
    cayman_islands: int
    china: int
    hawaii: int
    japan: int
    mexico: int
    united_arab_emirates: int
    united_kingdom: int
    south_africa: int
    switzerland: int

class PersonalStatsDrugs(BaseModel):
    cannabis: int
    ecstasy: int
    ketamine: int
    lsd: int
    opium: int
    pcp: int
    shrooms: int
    speed: int
    vicodin: int
    xanax: int
    total: int
    overdoses: int
    rehabilitations: PersonalStatsDrugsRehabilitation

class PersonalStatsMissions(BaseModel):
    missions: int
    contracts: PersonalStatsMissionsContracts
    credits: int 

class PersonalStatsRacing(BaseModel):
    skill: int
    points: int
    races: PersonalStatsRacingRaces

class PersonalStatsNetworth(BaseModel): total: int

class PersonalStatsOther(BaseModel):
    activity: PersonalStatsOtherActivity
    awards: int
    merits_bought: int
    refills: PersonalStatsOtherRefills
    donator_days: int
    ranked_war_wins: int

# Sub Models

class UserBasic(BasicUser):
    level: int
    gender: UserGenderEnum
    status: UserStatus

class UserAmmo(BaseModel):
    id: int
    name: str
    types: List[UserAmmoType]

class UserDiscord(BaseModel):
    discord_id: str
    user_id: int

class UserBars(BaseModel):
    energy: UserBar
    nerve: UserBar
    happy: UserBar
    life: UserBar
    chain: FactionOngoingChain

class UserBattleStats(BaseModel):
    strength: UserBattleStatDetail
    defense: UserBattleStatDetail
    speed: UserBattleStatDetail
    dexterity: UserBattleStatDetail
    total: int

class Bounty(BaseModel):
    target_id: int
    target_name: str
    target_level: int
    lister_id: Optional[int] = None
    lister_name: Optional[str] = None
    reward: int
    reason: Optional[str] = None
    quantity: int
    is_anonymous: bool
    valid_until: int

class UserCalendar(BaseModel):
    start_time: str

class UserCompetitonHalloween(BaseModel):
    name: Literal["Halloween"]
    treats_collected: int
    basket: BasicTornModel

class UserCompetitionEasterEggs(BaseModel):
    name: Literal["Easter Egg Hunt"]
    score: int
    total: int

class UserCompetitionElimination(BaseModel):
    name: Literal["Elimination"]
    score: int
    team: str
    attacks: int

class UserCompetitionRps(BaseModel):
    name: Literal["Rock, Paper, Scissors"]
    status: RPSEnum
    hp: UserBarBasic

class UserCooldowns(BaseModel):
    drug: int
    medical: int
    booster: int

class UserCrime(BaseModel):
    nerve_spent: int
    skill: int
    progression_bonus: int
    rewards: UserCrimeRewards
    attempts: UserCrimeAttempts
    uniques: List[UserCrimeUniques]
    miscellaneous: Optional[Union[
        UserCrimeDetailsBootlegging,
        UserCrimeDetailsGraffiti,
        UserCrimeDetailsShoplifting,
        UserCrimeDetailsCardSkimming,
        UserCrimeDetailsHustling,
        UserCrimeDetailsCracking,
        UserCrimeDetailsScamming
    ]] = None

class UserEducation(BaseModel):
    complete: List[int]
    current: Optional[UserCurrentEducation] = None

class UserRaceCarDetails(BaseModel):
    car_item_id: int
    car_item_name: str
    top_speed: int
    acceleration: int
    braking: int
    dirt: int
    handling: int
    safety: int
    tarmac: int
    car_class: RaceClassEnum = Field(alias="class")
    id: int
    name: Optional[str] = None
    worth: int
    points_spent: int
    races_entered: int
    races_won: int
    is_removed: bool
    parts: List[int]

class UserEquipment(BaseModel):
    uid: int
    stats: Optional[TornItemEquipmentStats] = None # Fucked Cause API says this is GONNA BE THERE
    bonuses: List[ItemMarketListingItemBonus]
    rarity: Optional[ItemRarity] = None
    id: int
    name: str
    type: TornItemTypeEnum
    sub_type: Optional[TornItemWeaponTypeEnum] = None
    slot: int

class UserClothing(BaseModel):
    id: int
    name: str
    uid: int
    type: TornItemTypeEnum

class UserEvent(BaseModel):
    id: str
    timestamp: int
    event: str

class UserFaction(BaseModel):
    id: int
    name: str
    tag: str
    tag_image: str
    position: str
    days_in_faction: int

class ForumFeed(BaseModel):
    thread_id: int
    post_id: int
    user: ForumThreadAuthor
    title: str
    text: str
    timestamp: int
    is_seen: bool
    type: ForumFeedTypeEnum

class ForumPost(BaseModel):
    id: int
    thread_id: int
    author: ForumThreadAuthor
    is_legacy: bool
    is_topic: bool
    is_edited: bool
    is_pinned: bool
    created_time: int
    edited_by: Optional[int] = None
    has_quote: bool
    quoted_post_id: Optional[int] = None
    content: str
    likes: int
    dislikes: int

class ForumSubscribedThread(BaseModel):
    id: int
    forum_id: int
    author: ForumThreadAuthor
    title: str
    posts: ForumSubscribedThreadPostsCount

class ForumThreadBase(BaseModel):
    id: int
    title: str
    forum_id: int
    posts: int
    rating: int
    views: int
    author: ForumThreadAuthor
    last_poster: Optional[ForumThreadAuthor] = None
    first_post_time: Optional[int] = None
    last_post_time: Optional[int] = None
    has_poll: bool
    is_locked: bool
    is_sticky: bool
    
class ForumThreadExtended(ForumThreadBase):
    content: str
    content_raw: str
    poll: Optional[ForumPoll] = None

class UserHofStats(BaseModel):
    attacks: HofValue
    busts: HofValue
    defends: HofValue
    networth: HofValue
    offences: HofValue
    revives: HofValue
    level: HofValue
    rank: HofValue
    awards: HofValue
    racing_skill: HofValueFloat
    racing_points: HofValue
    racing_wins: HofValue
    travel_time: HofValue
    working_stats: HofValue
    battle_stats: Optional[HofValue] = None

class UserHonor(BaseModel):
    id: int
    timestamp: int

class UserIconPublic(BaseModel):
    id: int
    title: str
    description: str

class UserIconPrivate(UserIconPublic):
    until: Optional[int] = None

class UserJobPointsWrap(BaseModel):
    jobs: UserJobPoints
    companies: List[UserCompanyPoints]

class UserJobRanks(BaseModel):
    army: JobPositionArmyEnum
    grocer: JobPositionGrocerEnum
    casino: JobPositionCasinoEnum
    medical: JobPositionMedicalEnum
    law: JobPositionLawEnum
    education: JobPositionEducationEnum

class UserList(BaseModel):
    id: int
    name: str
    level: int
    faction_id: Optional[int] = None
    last_action: UserLastAction
    status: UserStatus

class UserLog(BaseModel):
    id: str
    timestamp: int
    details: UserLogDetails
    data: Dict[str, Any]
    params: Dict[str, Any]

class UserMedal(BaseModel):
    id: int
    timestamp: int

class UserMerits(BaseModel):
    upgrades: List[UserMeritUpgrade]
    available: int
    used: int
    medals: int
    honors: int

class UserMessage(BaseModel):
    id: int
    sender: BasicUser
    timestamp: int
    topic: str
    type: UserMessageTypeEnum
    seen: bool
    read: bool

class UserMissions(BaseModel):
    credits: int
    givers: List[UserMissionGiver]
    rewards: List[UserMissionReward]

class UserMoney(BaseModel):
    points: int
    wallet: int
    company: int
    vault: int
    cayman_bank: int
    city_bank: Optional[UserMoneyCityBank] = None
    faction: Optional[UserMoneyFactionBank] = None
    daily_networth: int

class UserNotifications(BaseModel):
    messages: int
    events: int
    awards: int
    competition: int

class UserOrganizedCrimeError(BaseModel):
    code: Literal[27]
    error: str

class UserOranizedCrime(BaseModel):
    id: int
    previous_crime_id: int

class PersonalStatsCrimes(BaseModel):
    crimes: Union[
        PersonalStatsCrimesV1,
        PersonalStatsCrimesV2
    ]

class PersonalStatsBasic(BaseModel):
    name: str
    value: int
    timestamp: int

class PersonalStats(BaseModel):
    attacking: Optional[PersonalStatsAttacking] = None
    battle_stats: Optional[PersonalStatsBattleStats] = None
    jobs: Optional[PersonalStatsJobs] = None
    trading: Optional[PersonalStatsTrading] = None
    jail: Optional[PersonalStatsJail] = None
    hospital: Optional[PersonalStatsHospital] = None
    finishing_hits: Optional[PersonalStatsFinishingHits] = None
    communication: Optional[PersonalStatsCommunication] = None
    crimes: Optional[Union[PersonalStatsCrimesV1, PersonalStatsCrimesV2]] = None
    bounties: Optional[PersonalStatsBounties] = None
    investments: Optional[PersonalStatsInvestments] = None
    items: Optional[PersonalStatsItems] = None
    travel: Optional[PersonalStatsTravel] = None
    drugs: Optional[PersonalStatsDrugs] = None
    missions: Optional[PersonalStatsMissions] = None
    racing: Optional[PersonalStatsRacing] = None
    networth: Optional[PersonalStatsNetworth] = None
    other: Optional[PersonalStatsOther] = None


# Models

class UserBasicResponse(BaseModel): profile: UserBasic
class UserAmmoResponse(BaseModel): ammo: List[UserAmmo]
class UserDiscordResponse(BaseModel): discord: UserDiscord
class UserBarsResponse(BaseModel): bars: UserBars
class AttacksResponse(BaseModel): attacks: List[Attack]
class AttacksFullResponse(BaseModel): attacks: List[AttackSimplified]
class UserBattleStatsResponse(BaseModel): battlestats: UserBattleStats
class UserBountiesResponse(BaseModel): bounties: List[Bounty]
class UserCalendarResponse(BaseModel): calendar: UserCalendar

class UserCompetitionResponse(BaseModel):
    competition: Annotated[
        Union[
            UserCompetitonHalloween,
            UserCompetitionEasterEggs,
            UserCompetitionElimination,
            UserCompetitionRps
            ],
        Field(discriminator="name")
    ]

class UserCooldownsResponse(BaseModel): cooldowns: UserCooldowns
class UserCrimesResponse(BaseModel): crimes: UserCrime
class UserEducationResponse(BaseModel): education: UserEducation
class UserEnlistedCarsResponse(BaseModel): enlistedcars: List[UserRaceCarDetails]

class UserEquipmentResponse(BaseModel):
    equipment: List[UserEquipment]
    clothing: List[UserClothing]

class UserEventsResponse(BaseModel): events: List[UserEvent]
class UserFactionResponse(BaseModel): faction: Optional[UserFaction]
class UserForumFeedResponse(BaseModel): forumFeed: List[ForumFeed]
class UserForumFriendsResponse(BaseModel): forumFriends: List[ForumFeed]
class UserForumPostsResponse(BaseModel): forumPosts: List[ForumPost]
class UserForumSubscribedThreadsResponse(BaseModel): forumSubscribedThreads: List[ForumSubscribedThread]
class UserHofResponse(BaseModel): hof: UserHofStats
class UserHonorsResponse(BaseModel): honors: List[UserHonor]
class UserIconsResponse(BaseModel): icons: List[Union[UserIconPrivate, UserIconPublic]]
class UserJobPointsResponse(BaseModel): jobpoints: UserJobPointsWrap
class UserJobRanksResponse(BaseModel): jobranks: UserJobRanks
class UserListResponse(BaseModel): list: List[UserList]
class UserLogsResponse(BaseModel): log: List[UserLog]
class UserMedalsResponse(BaseModel): medals: List[UserMedal]
class UserMeritsResponse(BaseModel): merits: UserMerits
class UserMessagesResponse(BaseModel): messages: List[UserMessage]
class UserMissionsResponse(BaseModel): missions: UserMissions
class UserMoneyResponse(BaseModel): money: UserMoney
class UserNewEventsResponse(BaseModel): events: List[UserEvent]
class UserNewMessagesResponse(BaseModel): messages: List[UserMessage]
class UserNotificationsResponse(BaseModel): notifications: UserNotifications
class UserOrganizedCrimeResponse(BaseModel): organizedCrime: Optional[Union[FactionCrime, UserOrganizedCrimeError]] = None

class UserPersonalStatsResponse(BaseModel):
    personalstats: Union[
        PersonalStats,
        List[PersonalStatsBasic]
    ]

