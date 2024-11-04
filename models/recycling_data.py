from pydantic import BaseModel
from typing import List, Optional

class RecyclingFacility(BaseModel):
    name: str
    address: str
    contact: Optional[str]
    materials_accepted: List[str]
    operating_hours: Optional[str]
    requirements: Optional[str]
    website: Optional[str]

class RecyclingData(BaseModel):
    location: str
    facilities: List[RecyclingFacility]
    last_updated: str 