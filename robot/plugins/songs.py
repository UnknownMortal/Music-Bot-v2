#
# Copyright (C) by M8N@Github, < https://github.com/UnknownMortal >.
#
# This file is part of < https://github.com/UnknownMortal/Music-Bot-v2 > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/UnknownMortal/Music-Bot-v2/blob/main/LICENSE >
#
# All rights reserved !!

import os
import requests
import aiohttp
import yt_dlp

from pyrogram import Client, filters
from youtube_search import YoutubeSearch

from robot import app
from robot.config import BOT_USERNAME
from robot.setup.filters import command


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


@app.on_message(command(["song"]))
def song(client, message):

    user_id = message.from_user.id
    user_name = message.from_user.first_name
    rpk = "[" + user_name + "](tg://user?id=" + str(user_id) + ")"

    query = "".join(" " + str(i) for i in message.command[1:])
    print(query)
    m = message.reply("🔎 ғɪɴᴅɪɴɢ..... ʏᴏᴜʀ sᴏɴɢ !!")
    ydl_opts = {"format": "bestaudio[ext=m4a]"}
    try:
        results = YoutubeSearch(query, max_results=5).to_dict()
        link = f"https://youtube.com{results[0]['url_suffix']}"
        # print(results)
        title = results[0]["title"][:40]
        thumbnail = results[0]["thumbnails"][0]
        thumb_name = f"thumb{title}.jpg"
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(thumb_name, "wb").write(thumb.content)

        duration = results[0]["duration"]
        url_suffix = results[0]["url_suffix"]
        views = results[0]["views"]

    except Exception as e:
        m.edit(
            "❌ ғᴏᴜɴᴅ ɴᴏᴛʜɪɴɢ !!"
        )
        print(str(e))
        return
    m.edit("ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ 📥 sᴏɴɢ....")
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
        rep = f"🎙 **sᴏɴɢ**: [{title[:35]}]({link})\n🎬 **sᴏᴜʀᴄᴇ**: YouTube\n⏱️ **ᴅᴜʀᴀᴛɪᴏɴ**: `{duration}`\n👁‍🗨 **ᴠɪᴇᴡs**: `{views}`\n📤 **ᴜᴘʟᴏᴀᴅᴇʀ**: @{BOT_USERNAME}"
        secmul, dur, dur_arr = 1, 0, duration.split(":")
        for i in range(len(dur_arr) - 1, -1, -1):
            dur += int(dur_arr[i]) * secmul
            secmul *= 60
        message.reply_audio(
            audio_file,
            caption=rep,
            thumb=thumb_name,
            parse_mode="md",
            title=title,
            duration=dur,
        )
        m.delete()
    except Exception as e:
        m.edit("❌ ᴇʀʀᴏʀ 404 !!")
        print(e)

    try:
        os.remove(audio_file)
        os.remove(thumb_name)
    except Exception as e:
        print(e)
