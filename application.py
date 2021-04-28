from sqlalchemy.orm import Session
from game_app import crud, models, schemas
from game_app.database import SessionLocal, engine
from fastapi import Depends, FastAPI, HTTPException
from typing import List
import uvicorn

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/user/create")
def create_user(request: schemas.UserCreate, db: Session = Depends(get_db)):
    created_user = crud.create_user(request=request, db=db)
    return get_user(created_user.user_id, db=db)


@app.get("/users/profile/{user_id}", response_model=schemas.UserOut)
def get_user(user_id: int, db: Session = Depends(get_db)):
    db_users = crud.get_users_by_points_descending(db)
    for i in range(len(db_users)):
        user = db_users[i]
        new_user = models.User(user_id=user.user_id, display_name=user.display_name,
                               points=user.points, rank=i + 1, country=user.country)
        if new_user.user_id == user_id:
            return new_user
    raise HTTPException(status_code=404, detail="User not found")


@app.get('/leaderboard', response_model=List[schemas.LeaderBoard])
def get_leaderboard(db: Session = Depends(get_db)):
    db_users = crud.get_users_by_points_descending(db)
    if not db_users:
        raise HTTPException(status_code=204)
    sorted_list = []
    for i in range(len(db_users)):
        user = db_users[i]
        new_user = models.User(user_id=user.user_id, display_name=user.display_name,
                               points=user.points, rank=i + 1, country=user.country)
        sorted_list.append(new_user)
    return sorted_list


@app.get('/leaderboard/{country_code}', response_model=List[schemas.LeaderBoard])
def get_leaderboard_with_sorted_by_country(country_code: str, db: Session = Depends(get_db)):
    db_users = crud.get_users_by_country_code_and_ordered_by_point(
        country_code, db)
    if not db_users:
        raise HTTPException(status_code=204)
    sorted_list = []
    for i in range(len(db_users)):
        user = db_users[i]
        new_user = models.User(user_id=user.user_id, display_name=user.display_name,
                               points=user.points, rank=i + 1, country=user.country)
        sorted_list.append(new_user)
    return sorted_list


@app.post('/submit/score')
def submit_score(request: schemas.SubmitScore, db: Session = Depends(get_db)):
    crud.update_user_point(request=request, db=db)
    return request

@app.get('/')
def index():
    return {'message':'Hello, please proceed to /docs :)'}


if __name__=='__main__':
    uvicorn.run(app,host="0.0.0.0",port=8000)