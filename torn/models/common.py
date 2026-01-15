from enum import Enum
from typing import List, Optional
from pydantic import BaseModel
from .enums import *


#Sub Sub Models

class FactionCrimeRequirementItem(BaseModel):
    id: int
    is_reusable: bool
    is_available: bool

class FactionCrimeUser(BaseModel):
    id: int
    outcome: Optional[str] = None
    outcome_duration: Optional[int] = None
    item_outcome: Optional[FactionCrimeUserItemOutcomeEnum] = None
    joined_at: int
    progress: float

class FactionCrimeRewardItem(BaseModel):
    id: int
    quantity: int

class FactionCrimeRewardPayout(BaseModel):
    type: str
    percentage: int
    paid_py: int
    paid_at: int

## Sub Models

class FactionOngoingChain(BaseModel):
    id: int
    current: int
    max: int
    timeout: int
    modifier: float
    cooldown: int
    start: int
    end: int

class FactionCrimeSlot(BaseModel):
    position: str
    position_id: str
    position_number: int
    item_requirement: Optional[FactionCrimeRequirementItem] = None
    user: Optional[FactionCrimeUser] = None
    checkpoint_pass_rate: int

class FactionCrimeReward(BaseModel):
    money: int
    items: List[FactionCrimeRewardItem]
    respect: int
    scope: int
    payout: Optional[FactionCrimeRewardPayout] = None

## Models
class BasicTornModel(BaseModel):
    id: int
    name: str

class BasicUser(BasicTornModel):
    pass

class AttackPlayerFaction(BasicTornModel):
    pass

class TornItemBaseStats(BaseModel):
    damage: Optional[float] = None
    accuracy: Optional[float] = None
    armor: Optional[float] = None

class ItemMarketListingItemBonus(BaseModel):
    id: int
    title: str
    description: str
    value: int

class FactionCrime(BaseModel):
    id: int
    previous_crime_id: Optional[int] = None
    name: str
    difficulty: int
    status: FactionCrimeStatusEnum
    created_at: int
    planning_at: Optional[int] = None
    ready_at: Optional[int] = None
    expired_at: int
    executed_at: Optional[int] = None
    slots: List[FactionCrimeSlot]
    rewards: Optional[FactionCrimeReward] = None