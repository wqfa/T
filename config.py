from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import os
app_id = 20399469
app_hash = "154dbb8114573c13387d0c7fb9d0fde6"
session = os.environ.get("teleson")
StrPython = TelegramClient(StringSession(session), app_id, app_hash)
StrPython.start()
