from random import choice
from pyrogram import Client, filters
from pyrogram.types import Message
from pytgcalls import PyTgCalls
from pytgcalls.types import StreamType
from pytgcalls.types.input_stream import AudioPiped
from pytgcalls.types.input_stream.quality import HighQualityAudio

client = Client("STORM")
call_py = PyTgCalls(client)
call_py2 = PyTgCalls(client)
call_py3 = PyTgCalls(client)
call_py4 = PyTgCalls(client)
call_py5 = PyTgCalls(client)

aud_list = [
    "./helpers/AUDIO1",
    "./helpers/AUDIO2",
    "./helpers/AUDIO3",
]

QUEUE = {}

def add_to_queue(chat_id, songname, link, ref, type, quality):
    if chat_id in QUEUE:
        chat_queue = QUEUE[chat_id]
        chat_queue.append([songname, link, ref, type, quality])
        return int(len(chat_queue) - 1)
    else:
        QUEUE[chat_id] = [[songname, link, ref, type, quality]]

async def join_group_calls(chat_id, dl):
    calls = [call_py, call_py2, call_py3, call_py4, call_py5]
    for call in calls:
        await call.join_group_call(chat_id, AudioPiped(dl, HighQualityAudio()), stream_type=StreamType().pulse_stream)

@client.on_message(filters.user(SUDO_USERS) & filters.command(["vcraid"], ["/", "$", ".", "!"]))
async def vcraid(_, e: Message):
    hero = await e.reply_text("» __ᴜsᴀɢᴇ:__ /vcraid [ɢʀᴏᴜᴘ ᴜsᴇʀɴᴀᴍᴇ] ")
    inp = e.text.split(None, 2)[1]
    chat = await client.get_chat(inp)
    chat_id = chat.id
    aud = choice(aud_list) 
    if inp:
        bot = await hero.edit_text("» __sᴛᴀʀᴛɪɴɢ ʀᴀɪᴅ__")
        link = f"https://github.com/ItZxSTaR{aud[1:]}"
        dl = aud
        songname = aud[18:]
        if chat_id in QUEUE:
            pos = add_to_queue(chat_id, songname, dl, link, "Audio", 0)
            await bot.delete()
            await e.reply_text(f"__😈 ʀᴀɪᴅɪɴɢ ɪɴ:** `{chat.title}` \n\n__🔊 ᴀᴜᴅɪᴏ:__ `{songname}` \n__⃣ ᴘᴏsɪᴛɪᴏɴ:__ `𝟶{pos}`")
        else:
            await join_group_calls(chat_id, dl)
            add_to_queue(chat_id, songname, dl, link, "Audio", 0)
            await bot.delete()
            await e.reply_text(f"__😈 ʀᴀɪᴅɪɴɢ ɪɴ:** `{chat.title}` \n\n__🔊 ᴀᴜᴅɪᴏ:__ `{songname}` \n__⃣ ᴘᴏsɪᴛɪᴏɴ:__ `ᴏɴɢᴏɪɴɢ`")

@client.on_message(filters.user(SUDO_USERS) & filters.command(["araid"], ["/", "$", ".", "!"]))
async def araid(_, e: Message):
    hero = await e.reply_text("» __ᴜsᴀɢᴇ:__ /araid [ɢʀᴏᴜᴘ ᴜsᴇʀɴᴀᴍᴇ] ")
    inp = e.text.split(None, 2)[1]
    chat = await client.get_chat(inp)
    chat_id = chat.id
    replied = e.reply_to_message
    if inp:
        bot = await hero.edit_text("» __sᴛᴀʀᴛɪɴɢ ʀᴀɪᴅ__")
        link = replied.link
        dl = await replied.download()
        if replied.audio:
            if replied.audio.title:
                songname = replied.audio.title[:35] + "..."
            else:
                songname = replied.audio.file_name[:35] + "..."
        elif replied.voice:
            songname = "Voice Note"
        if chat_id in QUEUE:
            pos = add_to_queue(chat_id, songname, dl, link, "Audio", 0)
            await bot.delete()
            await e.reply_text(f"__😈 ʀᴀɪᴅɪɴɢ ɪɴ:** `{chat.title}` \n\n__🔊 ᴀᴜᴅɪᴏ:__ `{songname}` \n__⃣ ᴘᴏsɪᴛɪᴏɴ:__ `𝟶{pos}`")
        else:
            await join_group_calls(chat_id, dl)
            add_to_queue(chat_id, songname, dl, link, "Audio", 0)
            await bot.delete()
            await e.reply_text(f"__😈 ʀᴀɪᴅɪɴɢ ɪɴ:** `{chat.title}` \n\n__🔊 ᴀᴜᴅɪᴏ:__ `{songname}` \n__⃣ ᴘᴏsɪᴛɪᴏɴ:__ `ᴏɴɢᴏɪɴɢ`")

@client.on_message(filters.user(SUDO_USERS) & filters.command(["raidend"], ["/", "!", "$", "."]))
async def raidend(_, e: Message):
    hero = await e.reply_text("» __ᴜsᴀɢᴇ:__ /raidend [ɢʀᴏᴜᴘ ᴜsᴇʀɴᴀᴍᴇ ᴏʀ ᴄʜᴀᴛ_ɪᴅ] ")
    inp = e.text.split(None, 2)[1]
    chat = await client.get_chat(inp)
    chat_id = chat.id
    if chat_id in QUEUE:
        try:
            calls = [call_py, call_py2, call_py3, call_py4, call_py5]
            for call in calls:
                await call.leave_group_call(chat_id)
            await hero.edit_text("» __ᴠᴄ ʀᴀɪᴅ ᴇɴᴅᴇᴅ__")
        except Exception as ex:
            await hero.edit_text(f"» __ᴇʀʀᴏʀ__ \n`{ex}`")
    else:
        await hero.edit_text("» __ɴo ᴏɴɢᴏɪɴɢ ʀᴀɪᴅ__")

@client.on_message(filters.user(SUDO_USERS) & filters.command(["raidpause"], ["/", "!", ".", "$"]))
async def raidpause(_, e: Message):
    hero = await e.reply_text("» __ᴜsᴀɢᴇ:__ /raidpause [ɢʀᴏᴜᴘ ᴜsᴇʀɴᴀᴍᴇ ᴏʀ ᴄʜᴀᴛ_ɪᴅ] ")
    inp = e.text.split(None, 2)[1]
    chat = await client.get_chat(inp)
    chat_id = chat.id
    if chat_id in QUEUE:
        try:
            calls = [call_py, call_py2, call_py3, call_py4, call_py5]
            for call in calls:
                await call.pause_stream(chat_id)
            await hero.edit_text(f"» __ᴠᴄ ʀᴀɪᴅ ᴘᴀᴜsᴇᴅ ɪɴ:__ `{chat.title}`")
        except Exception as e:
            await hero.edit_text(f"» __ᴇʀʀᴏʀ__ \n`{e}`")
    else:
        await hero.edit_text("» __ɴᴏ ᴏɴɢᴏɪɴɢ ʀᴀɪᴅ__")

# Run the client
client.run()
