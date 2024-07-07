from pyrogram import Client, filters
from pyrogram.types import Message
import asyncio
from config import SUDO_USERS

@Client.on_message(
    filters.command(["lovestory"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def hearts(client: Client, message: Message):
    await message.edit("**ᴛʜɪꜱ ᴘʟᴜɢɪɴ ɪꜱ ɴᴏᴛ ᴀᴠᴀɪʟᴀʙʟᴇ ʀɪɢʜᴛ ɴᴏᴡ. ɪᴛ ᴡᴀꜱ ᴅᴇᴅᴜᴄᴛᴇᴅ ɪɴ ᴛʜᴇ ꜱᴛᴏʀᴍ ᴜꜱᴇʀʙᴏᴛ ᴜᴘᴅᴀᴛᴇ [ᴠ-2.1.1].**")
    #await asyncio.sleep(0.5)
    #await message.edit("1 ❤️ ʟᴏᴠᴇ ꜱᴛᴏʀʏ")
    #await asyncio.sleep(0.5)
    #await message.edit("😐             😕 \n/👕\         <👗\ \n 👖               /|")
    #await asyncio.sleep(0.5)
    #await message.edit("😉          😳 \n/👕\       /👗\ \n  👖            /|")
    #await asyncio.sleep(0.5)
    #await message.edit("😚            😒 \n/👕\         <👗> \n  👖             /|")
    #await asyncio.sleep(0.5)
    #await message.edit("😍         ☺️ \n/👕\      /👗\ \n  👖          /|")
    #await asyncio.sleep(0.5)
    #await message.edit("😍          😍 \n/👕\       /👗\ \n  👖           /|")
    #await asyncio.sleep(0.5)
    #await message.edit("😘   😊 \n /👕\/👗\ \n   👖   /|")
    #await asyncio.sleep(0.5)
    #await message.edit("😳  😁 \n /|\ /👙\ \n /     / |")
    #await asyncio.sleep(0.5)
    #await message.edit("😈    /😰\ \n<|\      👙 \n /🍆    / |")
    #await asyncio.sleep(0.5)
    #await message.edit("😅 \n/(),✊😮 \n /\         _/\\/|")
    #await asyncio.sleep(0.5)
    #await message.edit("😎 \n/\\_,__😫 \n  //    //       \\")
    #await asyncio.sleep(0.5)
    #await message.edit("😖 \n/\\_,💦_😋  \n  //         //        \\")
    #await asyncio.sleep(0.5)
    #await message.edit("😭      ☺️ \n  /|\   /(👶)\ \n  /!\   / \ ")
    #await asyncio.sleep(0.5)
    #await message.edit("ᴛʜᴇ ᴇɴᴅ 😂.......")
