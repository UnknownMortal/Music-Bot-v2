#
# Copyright (C) by M8N@Github, < https://github.com/UnknownMortal >.
#
# This file is part of < https://github.com/UnknownMortal/Music-Bot-v2 > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/UnknownMortal/Music-Bot-v2/blob/main/LICENSE >
#
# All rights reserved !!


from typing import Dict, List, Union

from robot.core import db


pytgdb = db.pytg
admindb = db.admin


async def get_active_chats() -> list:
    chats = pytgdb.find({"chat_id": {"$lt": 0}})
    if not chats:
        return []
    chats_list = []
    for chat in await chats.to_list(length=1000000000):
        chats_list.append(chat)
    return chats_list

async def is_active_chat(chat_id: int) -> bool:
    chat = await pytgdb.find_one({"chat_id": chat_id})
    if not chat:
        return False
    return True

async def add_active_chat(chat_id: int):
    is_served = await is_active_chat(chat_id)
    if is_served:
        return
    return await pytgdb.insert_one({"chat_id": chat_id})

async def remove_active_chat(chat_id: int):
    is_served = await is_active_chat(chat_id)
    if not is_served:
        return
    return await pytgdb.delete_one({"chat_id": chat_id})


async def is_music_playing(chat_id: int) -> bool:
    chat = await admindb.find_one({"chat_id_toggle": chat_id})
    if not chat:
        return True
    return False

async def music_on(chat_id: int):
    is_karma = await is_music_playing(chat_id)
    if is_karma:
        return
    return await admindb.delete_one({"chat_id_toggle": chat_id})

async def music_off(chat_id: int):
    is_karma = await is_music_playing(chat_id)
    if not is_karma:
        return
    return await admindb.insert_one({"chat_id_toggle": chat_id})
