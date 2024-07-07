from pyrogram import Client, filters
from pyrogram.types import Message
import asyncio
from config import SUDO_USERS

@Client.on_message(
    filters.command(["lovestory"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def hearts(client: Client, message: Message):
    animation_interval = 0.5
    animation_ttl = range(0, 14)
    await message.edit("ʟᴇᴛ ᴍᴇ ᴛᴇʟʟ ʏᴏᴜ ᴀ ʟᴏᴠᴇ ꜱᴛᴏʀʏ...")
    
    animation_chars = [
        "1 ❤️ ʟᴏᴠᴇ ꜱᴛᴏʀʏ",
        r"  😐             😕 \n/👕\         <👗\ \n 👖               /|",
        r"  😉          😳 \n/👕\       /👗\ \n  👖            /|",
        r"  😚            😒 \n/👕\         <👗> \n  👖             /|",
        r"  😍         ☺️ \n/👕\      /👗\ \n  👖          /|",
        r"  😍          😍 \n/👕\       /👗\ \n  👖           /|",
        r"  😘   😊 \n /👕\/👗\ \n   👖   /|",
        r" 😳  😁 \n /|\ /👙\ \n /     / |",
        r"😈    /😰\ \n<|\      👙 \n /🍆    / |",
        r"😅 \n/(),✊😮 \n /\         _/\\/|",
        r"😎 \n/\\_,__😫 \n  //    //       \\",
        r"😖 \n/\\_,💦_😋  \n  //         //        \\",
        r"  😭      ☺️ \n  /|\   /(👶)\ \n  /!\   / \ ",
        "ᴛʜᴇ ᴇɴᴅ 😂...",
    ]
    
    for i in animation_ttl:
        await message.edit(animation_chars[i % len(animation_chars)])
        await asyncio.sleep(animation_interval)
