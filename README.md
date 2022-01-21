### Game Localization
Frontend Repo 👉 https://github.com/victorjambo/game-localization-web

## Dev setup (Docker)
__requirements__ Ensure you have docker installed
- Build docker images
    ```bash
      make build
    ```
- Before starting the up, create the database volume. __(run once)__
    ```bash
      make volume
    ```
- Start flask app with.
    ```bash
      make start
    ```
- On a separate command line, you need to run migrations. __(run once)__
    ```bash
      make migrate
    ```
- To run test via docker. Run this command
    ```bash
      make test
    ```
- Woohoo!!! You are done, you can now get something to eat 😀🍽

## Dev setup (locally)
__requirements__ Ensure you're running on Python 3.8 and postgres is installed
- Create virtual env `python3 -m venv venv`
- Activate venv `. venv/bin/activate`
- Create `.env` file and copy contents from `.env.sample` file, then run `source .env` __(you can skip this)__
- install packages `pip install -r requirements.txt`
- run the app `flask run`
- Woohoo!!!
