from pydantic import BaseModel
from typing import List, Optional
from .common import (
    BasicUser,
    TornItemAmmoTypeEnum,
    UserStatusStateEnum,
    UserPlaneImageTypeEnum,
    UserGenderEnum,
    ApiFiltersAttacksRevivesEnum,
    AttackPlayerFaction,
    FactionAttackResult
)

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

# Models

class UserBasicResponse(BaseModel):
    profile: UserBasic

class UserAmmoResponse(BaseModel):
    ammo: List[UserAmmo]

class UserDiscordResponse(BaseModel):
    discord: UserDiscord

class AttacksResponse(BaseModel):
    attacks: List[Attack]