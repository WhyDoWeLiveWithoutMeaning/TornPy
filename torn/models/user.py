from pydantic import BaseModel, Field
from typing import List, Optional, Union, Annotated, Literal
from .common import (
    BasicTornModel,
    BasicUser,
    ItemRarity,
    TornItemBaseStats,
    ItemMarketListingItemBonus,
    TornItemAmmoTypeEnum,
    UserStatusStateEnum,
    UserPlaneImageTypeEnum,
    UserGenderEnum,
    ApiFiltersAttacksRevivesEnum,
    AttackPlayerFaction,
    FactionAttackResult,
    FactionOngoingChain,
    RPSEnum,
    UserCrimeUniquesRewardAmmoEnum,
    RaceClassEnum,
    TornItemTypeEnum,
    TornItemWeaponTypeEnum
)

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

# Models

class UserBasicResponse(BaseModel):
    profile: UserBasic

class UserAmmoResponse(BaseModel):
    ammo: List[UserAmmo]

class UserDiscordResponse(BaseModel):
    discord: UserDiscord

class UserBarsResponse(BaseModel):
    bars: UserBars

class AttacksResponse(BaseModel):
    attacks: List[Attack]

class AttacksFullResponse(BaseModel):
    attacks: List[AttackSimplified]

class UserBattleStatsResponse(BaseModel):
    battlestats: UserBattleStats

class UserBountiesResponse(BaseModel):
    bounties: List[Bounty]

class UserCalendarResponse(BaseModel):
    calendar: UserCalendar

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

class UserCooldownsResponse(BaseModel):
    cooldowns: UserCooldowns

class UserCrimesResponse(BaseModel):
    crimes: UserCrime

class UserEducationResponse(BaseModel):
    education: UserEducation

class UserEnlistedCarsResponse(BaseModel):
    enlistedcars: List[UserRaceCarDetails]

class UserEquipmentResponse(BaseModel):
    equipment: List[UserEquipment]
    clothing: List[UserClothing]