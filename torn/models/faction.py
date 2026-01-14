from pydantic import BaseModel, Field
from typing import List, Optional, Union, Annotated, Literal
from .common import *
from .enums import *




class FactionApplicationUserBattleStats(BaseModel):
    strength: int
    speed: int
    dexterity: int
    defense: int

class FactionApplicationUser(BaseModel):
    id: int
    name: str
    level: int
    stats: Optional[FactionApplicationUserBattleStats] = None

# Sub Model

class FactionApplication(BaseModel):
    id: int
    user: FactionApplicationUser
    message: Optional[str] = None
    valid_until: int
    status: FactionApplicationStatusEnum

# Models

class FactionApplicationsResponse(BaseModel):
    applications: List[FactionApplication]