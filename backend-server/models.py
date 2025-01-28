from datetime import datetime

from typing import Optional


from pydantic import BaseModel, Field

class Track(BaseModel):
    id: int
    title: str
    artist: str
    duration: float
    last_play: datetime

