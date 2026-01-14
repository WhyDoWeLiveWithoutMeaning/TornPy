from enum import Enum
from typing import List, Optional
from pydantic import BaseModel

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