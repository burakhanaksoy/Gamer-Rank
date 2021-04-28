from sqlalchemy.orm import Session
from sqlalchemy.orm import Query
from game_app import models, schemas


def get_users(db: Session):
    return db.query(models.User).all()


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.user_id == user_id).first()


def create_user(request: schemas.UserCreate, db: Session):
    new_user = models.User(display_name=request.display_name, points=request.points, rank=request.rank, country=request.country)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_users_by_points_descending(db: Session):
    return db.query(models.User).order_by(models.User.points.desc()).all()


def get_users_by_country_code_and_ordered_by_point(country_code: str, db: Session):
    return db.query(models.User).filter(models.User.country == country_code).order_by(models.User.points.desc()).all()


def update_user_point(request: schemas.SubmitScore, db: Session):
    user = db.query(models.User).filter(models.User.user_id ==
                                        request.user_id).update({"points": models.User.points+request.score_worth})
    db.commit()
    return user
