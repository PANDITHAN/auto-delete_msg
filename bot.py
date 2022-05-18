import asyncio
from os import environ
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import Client, filters, idle
from pyrogram.types import Message
from pyrogram import Client as Bot

API_ID = int(environ.get("API_ID"))
API_HASH = environ.get("API_HASH")
BOT_TOKEN = environ.get("BOT_TOKEN")
SESSION = environ.get("SESSION")
TIME = int(environ.get("TIME"))
GROUPS = []
for grp in environ.get("GROUPS").split():
    GROUPS.append(int(grp))
ADMINS = []
for usr in environ.get("ADMINS").split():
    ADMINS.append(int(usr))

START_TEXT = "<b>Hai {},\nI'm a simple bot\ndelete group messages after a specific time</b>"

START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Credits', url='https://t.me/PANDITHAN_SIR'),
        ]]
    )

User = Client(name="user-account",
              session_string=SESSION,
              api_id=API_ID,
              api_hash=API_HASH,
              workers=300
              )


PANDITHAN = Client(name="auto-delete",
             api_id=API_ID,
             api_hash=API_HASH,
             bot_token=BOT_TOKEN,
             workers=300
             )


@PANDITHAN.on_message(filters.private & filters.command(["start"]))
async def start_handler(c: Client, m: Message): await m.reply_text(
 text=START_TEXT.format(m.from_user.mention),
        disable_web_page_preview=True,
 reply_markup=START_BUTTONS

    )

@User.on_message(filters.chat(GROUPS))
async def delete(user, message):
    try:
       if message.from_user.id in ADMINS:
          return
       else:
          await asyncio.sleep(TIME)
          await Bot.delete_messages(message.chat.id, message.id)
    except Exception as e:
       print(e)
       
User.start()
print("User Started!")
Bot.start()
print("Bot Started!")

idle()

User.stop()
print("User Stopped!")
Bot.stop()
print("Bot Stopped!")
