# Gamer-Rank
https://burakhan-game-ranker.herokuapp.com/docs

In this small project, I used FastAPI to implement a backend service for gaming platform. :octocat:

Exposed endpoints can be seen and tested with the beautiful documentation of FastAPI

<img width="1425" alt="Swagger" src="https://user-images.githubusercontent.com/31994778/116240280-4f14c580-a76c-11eb-8843-2a9d4e69d6a9.png">

-> I followed FastAPI website to implement this project, [click here](https://fastapi.tiangolo.com/)

Implemented operations:

### POST, GET, PATCH

##### Create User (POST)
<img width="1366" alt="CreateUser" src="https://user-images.githubusercontent.com/31994778/116241242-5a1c2580-a76d-11eb-96d1-67fd2de6a270.png">

##### Get leaderboard (GET)
<img width="1355" alt="Leaderboard" src="https://user-images.githubusercontent.com/31994778/116241493-9ea7c100-a76d-11eb-99f5-e926e8cdb0cd.png">

##### Patch (Post request on /submit/score endpoint patches user's points)
<img width="1361" alt="Submit" src="https://user-images.githubusercontent.com/31994778/116241885-0cec8380-a76e-11eb-8cf8-e30bd59a9d6e.png">

# How to run
Clone the project and create a virtual environment. Having done that, activate virtual environment and run "pip install -r requirements.txt".

After running, go to [localhost](http://127.0.0.1:8000/docs) :tada:

## Unit Test
<img width="1029" alt="Screen Shot 2021-04-27 at 7 55 45 PM" src="https://user-images.githubusercontent.com/31994778/116316010-04219f00-a7ba-11eb-83c3-20e20565042f.png">
<img width="784" alt="Screen Shot 2021-04-28 at 12 39 00 AM" src="https://user-images.githubusercontent.com/31994778/116316140-2adfd580-a7ba-11eb-8006-1788c2392ab0.png">
