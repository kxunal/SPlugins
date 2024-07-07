from random import choice
from pyrogram import Client, filters
from pyrogram.types import Message
from pytgcalls import PyTgCalls
from pytgcalls.types.input_stream import AudioPiped
from pytgcalls.types.input_stream.quality import HighQualityAudio

# Initialize Pyrogram client
client = Client("my_bot_session")  # Replace "my_bot_session" with your desired session name

# Initialize PyTgCalls
call_py = PyTgCalls(client)
call_py2 = PyTgCalls(client)
call_py3 = PyTgCalls(client)
call_py4 = PyTgCalls(client)
call_py5 = PyTgCalls(client)

# Define your aud_list and QUEUE here
aud_list = [
    "./helpers/AUDIO1",
    "./helpers/AUDIO2",
    "./helpers/AUDIO3",
]

QUEUE = {}

# Function to add to queue
def add_to_queue(chat_id, songname, link, ref, type, quality):
    if chat_id in QUEUE:
        chat_queue = QUEUE[chat_id]
        chat_queue.append([songname, link, ref, type, quality])
        return int(len(chat_queue) - 1)
    else:
        QUEUE[chat_id] = [[songname, link, ref, type, quality]]

# Command to start audio raid
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
            if call_py:
                await call_py.join_group_call(chat_id, AudioPiped(dl, HighQualityAudio()), stream_type=3)
            if call_py2:
                await call_py2.join_group_call(chat_id, AudioPiped(dl, HighQualityAudio()), stream_type=3)
            if call_py3:
                await call_py3.join_group_call(chat_id, AudioPiped(dl, HighQualityAudio()), stream_type=3)
            if call_py4:
                await call_py4.join_group_call(chat_id, AudioPiped(dl, HighQualityAudio()), stream_type=3)
            if call_py5:
                await call_py5.join_group_call(chat_id, AudioPiped(dl, HighQualityAudio()), stream_type=3)
            add_to_queue(chat_id, songname, dl, link, "Audio", 0)
            await bot.delete()
            await e.reply_text(f"__😈 ʀᴀɪᴅɪɴɢ ɪɴ:** `{chat.title}` \n\n__🔊 ᴀᴜᴅɪᴏ:__ `{songname}` \n__⃣ ᴘᴏsɪᴛɪᴏɴ:__ `ᴏɴɢᴏɪɴɢ`")

# Command to start audio raid with replied message
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
            if call_py:
                await call_py.join_group_call(chat_id, AudioPiped(dl, HighQualityAudio()), stream_type=3)
            if call_py2:
                await call_py2.join_group_call(chat_id, AudioPiped(dl, HighQualityAudio()), stream_type=3)
            if call_py3:
                await call_py3.join_group_call(chat_id, AudioPiped(dl, HighQualityAudio()), stream_type=3)
            if call_py4:
                await call_py4.join_group_call(chat_id, AudioPiped(dl, HighQualityAudio()), stream_type=3)
            if call_py5:
                await call_py5.join_group_call(chat_id, AudioPiped(dl, HighQualityAudio()), stream_type=3)
            add_to_queue(chat_id, songname, dl, link, "Audio", 0)
            await bot.delete()
            await e.reply_text(f"__😈 ʀᴀɪᴅɪɴɢ ɪɴ:** `{chat.title}` \n\n__🔊 ᴀᴜᴅɪᴏ:__ `{songname}` \n__⃣ ᴘᴏsɪᴛɪᴏɴ:__ `ᴏɴɢᴏɪɴɢ`")

# Command to end raid
@client.on_message(filters.user(SUDO_USERS) & filters.command(["raidend"], ["/", "!", "$", "."]))
async def raidend(_, e: Message):
    hero = await e.reply_text("» __ᴜsᴀɢᴇ:__ /raidend [ɢʀᴏᴜᴘ ᴜsᴇʀɴᴀᴍᴇ ᴏʀ ᴄʜᴀᴛ_ɪᴅ] ")
    inp = e.text.split(None, 2)[1]
    chat = await client.get_chat(inp)
    chat_id = chat.id
    if chat_id in QUEUE:
        try:
            if call_py:
                await call_py.leave_group_call(chat_id)
            if call_py2:
                await call_py2.leave_group_call(chat_id)
            if call_py3:
                await call_py3.leave_group_call(chat_id)
            if call_py4:
                await call_py4.leave_group_call(chat_id)
            if call_py5:
                await call_py5.leave_group_call(chat_id)
            await hero.edit_text("» __ᴠᴄ ʀᴀɪᴅ ᴇɴᴅᴇᴅ__")
        except Exception as ex:
            await hero.edit_text(f"» __ᴇʀʀᴏʀ__ \n`{ex}`")
    else:
        await hero.edit_text("» __ɴo ᴏɴɢᴏɪɴɢ ʀᴀɪᴅ__")

# Command to pause raid
@client.on_message(filters.user(SUDO_USERS) & filters.command(["raidpause"], ["/", "!", ".", "$"]))
async def raidpause(_, e: Message):
    hero = await e.reply_text("» __ᴜsᴀɢᴇ:__ /raidpause [ɢʀᴏᴜᴘ ᴜsᴇʀɴᴀᴍᴇ ᴏʀ ᴄʜᴀᴛ_ɪᴅ] ")
    inp = e.text.split(None, 2)[1]
    chat = await client.get_chat(inp)
    chat_id = chat.id
    if chat_id in QUEUE:
        try:
            if call_py:
                await call_py.pause_stream(chat_id)
            if call_py2:
                await call_py2.pause_stream(chat_id)
            if call_py3:
                await call_py3.pause_stream(chat_id)
            if call_py4:
                await call_py4.pause_stream(chat_id)
            if call_py5:
                await call_py5.pause_stream(chat_id)
            await hero.edit_text(f"» __ᴠᴄ ʀᴀɪᴅ ᴘᴀᴜsᴇᴅ ɪɴ:__ `{chat.title}`")
        except Exception as e:
            await hero.edit_text(f"» __ᴇʀʀᴏʀ__ \n`{e}`")
    else:
        await hero.edit_text("» __ɴᴏ ᴏɴɢᴏɪɴɢ ʀᴀɪᴅ__")

# Command to resume raid
@client.on_message(filters.user(SUDO_USERS) & filters.command(["raidresume"], ["/", "!", ".", "$"]))
async def raidresume(_, e: Message):
    hero = await e.reply_text("» __ᴜsᴀɢᴇ:__ /raidpause [ɢʀᴏᴜᴘ ᴜsᴇʀɴᴀᴍᴇ ᴏʀ ᴄʜᴀᴛ_ɪᴅ] ")
    inp = e.text.split(None, 2)[1]
    chat = await client.get_chat(inp)
    chat_id = chat.id
    if chat_id in QUEUE:
        try:
            if call_py:
                await call_py.resume_stream(chat_id)
            if call_py2:
                await call_py2.resume_stream(chat_id)
            if call_py3:
                await call_py3.resume_stream(chat_id)
            if call_py4:
                await call_py4.resume_stream(chat_id)
            if call_py5:
                await call_py5.resume_stream(chat_id)
            await hero.edit_text(f"__» ᴠᴄ ʀᴀɪᴅ ʀᴇsᴜᴍᴇᴅ ɪɴ:__ `{chat.title}`")
        except Exception as e:
            await hero.edit_text(f"» __ᴇʀʀᴏʀ__ \n`{e}`")
    else:
        await hero.edit_text("» __ɴᴏ ʀᴀɪᴅ ɪs ᴄᴜʀʀᴇɴᴛʟʏ ᴘᴀᴜsᴇᴅ__")
