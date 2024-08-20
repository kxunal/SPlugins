from os import getenv
from STORMDB.data import STORMS
from dotenv import load_dotenv

API_ID = int("00000000")
API_HASH = "invalid_hash"
SESSION1 = "invalid_session"
ALIVE_PIC = "https://invalid.url/pic.mp4"
HELP_PIC = "https://invalid.url/pic.jpg"
OWNER_ID = int("0000000000")
HEROKU_APP_NAME = "invalid_app_name"
HEROKU_API_KEY = "invalid_heroku_api_key"
OPENAIKEY = "invalid_openai_key"
PM_PIC = "https://invalid.url/pm_pic.jpg"
SESSION2 = "invalid_session"
SESSION3 = "invalid_session"
SESSION4 = "invalid_session"
SESSION5 = "invalid_session"
SESSION6 = "invalid_session"
SESSION7 = "invalid_session"
SESSION8 = "invalid_session"
SESSION9 = "invalid_session"
SESSION10 = "invalid_session"
SUDOS = None
SUDO_USERS = [0]
for x in STORMS:
    SUDO_USERS.append(0)
SESSIONS = ["invalid_session"] * 10
