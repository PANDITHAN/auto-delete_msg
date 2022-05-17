# AutoDelete-V2

p align="center">
  <img src="PANDITHAN/9D4C6ECD-D04D-409D-B711-B10EAB40BC9F.jpeg" alt="DELET-BOT Logo">
</p>
<h1 align="center">
  <b>DELET-BOT</b>
</h1>

Delete group messages after a specific time

## Variables
1. `API_ID` : Get from [my.telegram.org](https://my.telegram.org/)
2. `API_HASH` : Get from [my.telegram.org](https://my.telegram.org)
3. `BOT_TOKEN` : Your telegram bot token from [@BotFather](https://t.me/BotFather)
4. `SESSION` : Generate from here [GenerateStringName](https://replit.com/@PANDITHAN/getStringName)
5. `GROUPS` : ID of Groups (seperate by spaces)
6. `ADMINS` : ID of Admins, messages from admins will not delete (seperate by spaces)
7. `TIME` : Time in seconds

### Make sure:
- Bot is admin in Groups with delete permission
- Account used to create SESSION is a member in Groups

# 𝐃𝐞𝐩𝐥𝐨𝐲a 𝐓𝐨 𝐇𝐞𝐫𝐨𝐤𝐮
<a href="https://heroku.com/deploy?template= https://github.com/PANDITHAN/auto-delete_msg"><img src="https://github.com/PANDITHAN/auto-delete_msg/blob/main/Logo/565048BC-5F3D-4430-A05A-BC03E96729D4.png" alt="PANDITHAN" border="0" height="50" width="200" align="center" /></a>

# Railway - use at own risk
 [![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new/template/FtddV8)

## Deploy in your VPS

```sh
git clone https://github.com/Arun-TG/AutoDelete-V2
cd AutoDelete-V2
pip3 install -r requirements.txt
# <Create Variables appropriately>
python3 bot.py
```

### Credits
- [Pyrogram](https://github.com/pyrogram/pyrogram)
- [PANDITHAN](https://t.me/PANDITHAN_SIR)
