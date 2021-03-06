import os
from os import getenv
from pyrogram import Client
from pytgcalls import PyTgCalls, idle

Bot = Client(
    "Pyrogram Bot",
    bot_token=os.environ.get("BOT_TOKEN"),
    api_id=int(os.environ.get("API_ID")),
    api_hash=os.environ.get("API_HASH")
)


abhi = Client(
    api_id=int(os.environ.get("API_ID")),
    api_hash=os.environ.get("API_HASH"),
    session_name=getenv("SESSION_NAME"),
    
    )

calls = PyTgCalls(abhi,
    cache_duration=100,
    overload_quiet_mode=True,)

with Client("Pyrogram Bot", API_ID, API_HASH, bot_token=BOT_TOKEN) as app:
    me_bot = app.get_me()
with abbi as app:
    me_abhi = app.get_me()
