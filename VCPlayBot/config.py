import os
from os import getenv

from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("SESSION_NAME", "BQHBq6EAa6bGEEbYVEycuJPOH9WddDaNcRK95OGfC5jpvbu6V2jUGsJ7Jww0D4ej8EsbNIs9n-5Mqbha5TXjpp_8R3Pw9GJyfVyVpjZLqIoxY_rWMMq7rlftwKlogj_nw4QPzuDfWoORrjMBhK0JpitlqMLaY05b_6zgiRLye0C2tpEQaMAuPbEIcl1_uU81T_kGD1j7Jlol0xA-N6_drccimZNR1Er9fAAAtkcjbvfdhCMOQe3YTFsKGbHyahaQx3dM0krdR_ee_i4rAvB2kP8qeetZBcfYU87XQkjYaQ2C4AIE-U6P0rCws9AL46CXXZTOPZhyLdREriz63s0g7nCsaWSX9QAAAAGjr5bsAA")
BOT_TOKEN = getenv("BOT_TOKEN", "7319569765:AAGhZCLgKKWVEv4-1S4rt4AwGYDZkAs5F-s")
BOT_NAME = getenv("BOT_NAME", "˹sᴀᴛᴀɴ  ꭙ ʀᴏʙᴏᴛ™ ♡゙")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "Satan_Network")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/9b13ea3ce046a1a5c8098.png")
admins = {}
API_ID = int(getenv("API_ID", "29469601"))
API_HASH = getenv("API_HASH". "c5773359dc095f51b3d57f2f7969c5dc")
BOT_USERNAME = getenv("BOT_USERNAME", "SatanXrobo_bot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Baki_X_Hanma")
OWNER_NAME = getenv("OWNER_NAME", "Baki_X_Hanma")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "Satan_Fucker")
PROJECT_NAME = getenv("PROJECT_NAME", "VCPlayBot1.0")
SOURCE_CODE = getenv("SOURCE_CODE", "github.com/BakiHanma0001/VCPlayBot")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "7"))
ARQ_API_KEY = getenv("ARQ_API_KEY", None)
PMPERMIT = getenv("PMPERMIT", None)
LOG_GRP = getenv("LOG_GRP", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5096741943").split()))
