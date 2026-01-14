from enum import Enum
from typing import List, Optional
from pydantic import BaseModel

## Enums
class RaceClassEnum(str, Enum):
    A = "A"
    B = "B"
    C = "C"
    D = "D"
    E = "E"

class MissionDifficultyEnum(str, Enum):
    VERYEASY = "Very easy"
    EASY = "Easy"
    MEDIUM = "Medium"
    HARD = "Hard"
    VERYHARD = "Very hard"
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

## Models

class BasicTornModel(BaseModel):
    id: int
    name: str

class BasicUser(BasicTornModel):
    pass

class AttackPlayerFaction(BasicTornModel):
    pass