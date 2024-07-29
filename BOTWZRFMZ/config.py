from os import getenv

from dotenv import load_dotenv

load_dotenv(".env")

DEVS = [
    7184813521
    #id_owner_disini
]
API_ID = int(getenv("API_ID", "22253882"))

API_HASH = getenv("API_HASH", "899e723dbd98494999ebd5bca3e51caf")

BOT_TOKEN = getenv("BOT_TOKEN", "7374148710:AAETEM4_fM8DXthmUeh9IN1tLjO77MxI7nY")

OWNER = int(getenv("OWNER", "7184813521"))

MAX_BOT = int(getenv("MAX_BOT", "2")) #TergantungPanel

RESI = getenv("RESI", "26646379b9945347b1fc403cb40bcbc6407f1f8106ba8d4b02a9b399999d100c") #BentarLupa

LOGS = int(getenv("LOGS", "-1002159915598")) #id_gc

COMMAND = getenv("COMMAND", ". , ? ;")
cmd = COMMAND.split()

DB_URL = getenv("DATABASE_URL", "url")

BLACKLIST_CHAT = list(
    map(
        int,
        getenv(
            "BLACKLIST_CHAT",
            "-1002159915598"
        )
    )
) #idblgrup

MONGO_URL = getenv(
    "MONGO_URL",
    "mongodb+srv://VegetaMusic:Vegeta@cluster0.dohyl.mongodb.net/myFirstDatabase?retryWrites=true&w=majority",
)

SESSIONS_STRING = getenv(
    "SESSION", "",
)


