from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("29828941"))
API_HASH = getenv("adac20199eb0294db727da4259360ab0")

BOT_TOKEN = getenv("7297611324:AAGTU7O6vcdsapztvVrxPzTH_SGh9TwAXns", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("1220257387"))

PING_IMG = getenv("PING_IMG", "https://graph.org/file/6e5004198c3bdbba84bdc.jpg")
START_IMG = getenv("START_IMG", "https://graph.org/file/6e5004198c3bdbba84bdc.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/Music_Mrko")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/Files_php3")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1220257387").split()))


FAILED = "https://graph.org/file/6e5004198c3bdbba84bdc.jpg"
