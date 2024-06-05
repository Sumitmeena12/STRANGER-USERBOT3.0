from SpamX.config import *
from SpamX.core.version import __version__
from SpamX import sudoser, RiZoeL 
from RiZoeLX import __version__ as pip_vr
from pyrogram import __version__ as pyro_vr
import platform

__version__ = __version__


ping_msg = PING_MSG if PING_MSG else "⚡️𝗗𝗥𝗔𝗚𝗢𝗡𓆩⚡️"
pic = ALIVE_PIC if ALIVE_PIC else "https://telegra.ph/file/19a19a82d791ee5f8abcb.jpg"
amsg = ALIVE_MSG if ALIVE_MSG else"⚡️𝗗𝗥𝗔𝗚𝗢𝗡𓆩 𝗦𝗣𝗔𝗠⚡️"

try:
   sah = RiZoeL.get_users(OWNER_ID)
   owner_mention = sah.mention
except:
   owner_mention = f"[{OWNER_ID}](tg://user?id={OWNER_ID})"

class Alive:
     Pic = pic
     
     msg = f"""
      **[⚡️𝗗𝗥𝗔𝗚𝗢𝗡𓆩⚡️](https://t.me/dragondpworld)
◈ •━━━━━★✦♡✦★━━━━━• ◈ 

➪ **𝗠ᴀsᴛᴇʀ:** [⚡️𝗗𝗥𝗔𝗚𝗢𝗡𓆩⚡️](https://t.me/Farzicoderxd)

➪ **𝗣ʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ:**`{platform.python_version()}`

➪ **𝗧ᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ:** `{__version__}`

➪ **𝗣ʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ:** `{pyro_vr}`
◈ •━━━━━★✦♡✦★━━━━━• ◈
     """

handler = HNDLR
Owner = int(OWNER_ID)
DATABASE_URL = DATABASE_URL
LOGS_CHANNEL = LOGS_CHANNEL

if DATABASE_URL:
   from SpamX.database import users_db
   Sudos = []
   All = users_db.get_all_sudos()
   for x in All:
     Sudos.append(x.user_id)
else:
   Sudos = sudoser
