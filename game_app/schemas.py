from pydantic import BaseModel
from datetime import datetime


class UserBase(BaseModel):
    display_name: str
    points: int
    rank: int


class UserCreate(UserBase):
    country: str


class UserOut(UserBase):
    user_id: int
    class Config:
        orm_mode = True


class LeaderBoard(BaseModel):
    rank: int
    points: int
    display_name: str
    country: str

    class Config:
        orm_mode = True


class SubmitScore(BaseModel):
    score_worth: float
    user_id: int
    timestamp: datetime
