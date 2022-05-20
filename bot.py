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

BOUT ="""**👋Hi ᴅᴇᴀʀ**
I do not have much to say on help - I just delete telegram group messages
 MADE BY [M-STer](https://t.me/PANDITHAN_SIR)"""

TEN = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('CREDIT', url='https://t.me/PANDITHAN_SIR'),
        InlineKeyboardButton('Home', callback_data='home')
        ]]
    )

MALIK = """╔════❰ ABOUT ❱═❍⊱❁۪۪
║╭━━━━━━━━━━━━━━━➣ 
║┣⪼ 𝙼𝚈 𝙽𝙰𝙼𝙴 : MESSAGE DELETE BOT
║┣⪼ 𝙲𝚁𝙴𝙰𝚃𝙾𝚁 : [⸙ꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋM-STER](https://t.me/FLIQ_YT)
║┣⪼ 𝙻𝙸𝙱𝚁𝙰𝚁𝚈 : PYROGRAM
║┣⪼ 𝙻𝙰𝙽𝙶𝚄𝙰𝙶𝙴 : PYTHON 3
║┣⪼ 𝙱𝙾𝚃 𝚂𝙴𝚁𝚅𝙴𝚁 : ZeeT
║┣⪼ 𝙱𝚄𝙸𝙻𝙳 𝚂𝚃𝙰𝚃𝚄𝚂 : v1.0.1 [ 𝙱𝙴𝚃𝙰 ]
║┣⪼ 𝙲𝚁𝙴𝙳𝙸𝚃𝚂 : [PANDITHAN](https://t.me/PANDITHAN_SIR)
║╰━━━━━━━━━━━━━━━➣ ╚══════════════════❍⊱❁۪۪۪۪ """
MALIK2 = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Source code', url='https://github.com/PANDITHAN/auto-delete_msg'),
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

@PANDITHAN.on_message(filters.private & filters.command(["help"]))
async def start_handler(c: Client, m: Message): await m.reply_text(
 text=BOUT.format(m.from_user.mention),
        disable_web_page_preview=True,
 reply_markup=TEN
    )

@PANDITHAN.on_message(filters.private & filters.command(["about"]))
async def start_handler(c: Client, m: Message): await m.reply_text(
 text=MALIK.format(m.from_user.mention),
        disable_web_page_preview=True,
 reply_markup=MALIK2
    )

@Bot.on_callback_query()
async def cb_handler(bot, update):
    if update.data == "home":
        await m.message.edit_text(
            text=START_TEXT.format(m.from_user.mention),
            reply_markup=START_BUTTONS,
            disable_web_page_preview=True
        )
    else:
        await update.message.delete()

@User.on_message(filters.chat(GROUPS))
async def delete(user, message):
    try:
       if message.from_user.id in ADMINS:
          return
       else:
          await asyncio.sleep(TIME)
          await PANDITHAN.delete_messages(message.chat.id, message.id)
    except Exception as e:
       print(e)
       
User.start()
print("User Started!")
PANDITHAN.start()
print("Bot Started!")

idle()

User.stop()
print("User Stopped!")
PANDITHAN.stop()
print("Bot Stopped!")
