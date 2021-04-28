from sqlalchemy import Boolean, Column, Integer, String
from game_app.database import Base


class User(Base):
    __tablename__ = "users"

    def __init__(self, display_name, points, rank, country, user_id=None):
        self.user_id = user_id
        self.display_name = display_name
        self.points = points
        self.rank = rank
        self.country = country

    user_id = Column(Integer, primary_key=True,
                     index=True)
    display_name = Column(String, index=True)
    points = Column(Integer, index=True, default=0)
    rank = Column(Integer, index=True)
    country = Column(String, index=True)
