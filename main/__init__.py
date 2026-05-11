#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config("14698983", default=None, cast=int)
API_HASH = config("3a680114122dac2cba978097dfb6bc2e", default=None)
BOT_TOKEN = config("8669447275:AAGPkyDLa1-Yes-Z4pXtnAT86xENJULwEhg", default=None)
SESSION = config("1BVtsOK4BuxPkU8S0AELyZvr4np_FXdLzshVIbTe1sCzfoO5akAihV2d3EXfiuza-3UWQowr-a5muJsWXXuGQE5ViXepea20y-CkipsTBLlKUkDBSBB19scQkiAA-VnD0AbZNBeJCO6mJauTs7dJoQtPpAGY2KnXxK73GXWD2YK3tXmjHp0Et1_pj3ipMZlj66-4IBCFnQcFe1yp7JmXEuPH9v3lfw2BJr8f103s3SdvJhAoWt9brohCU5ycPzBe8Y4NnZvqtJPp9NB5s7-jioJ89QL1W8ijmCBiCYSIfDOnbeTaYve-ygc2yN2zAZHyUFWgYPmOGleDxk-pI3rqzikKbqXix-i0=", default=None)
FORCESUB = config("Nexa_Flow_Official", default=None)
AUTH = config("7899586166", default=None, cast=int)

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
