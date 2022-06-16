import asyncio

from pyrogram import Client, filters, __version__ as pyrover
from pyrogram.errors import FloodWait, UserNotParticipant
from pytgcalls import (__version__ as pytover)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, ChatJoinRequest

from robot.setup.filters import command
from robot.config import BOT_NAME, OWNER_USERNAME, UPDATE, SUPPORT


@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f""" """,
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🏳‍🌈 About", callback_data="cbabout"),
                    InlineKeyboardButton(
                        "☁️ Others", callback_data="others")
                ],
                [
                    InlineKeyboardButton(
                        "🗂 Commands", callback_data="cbevery")
                ],
                [
                    InlineKeyboardButton(
                        "✚ Click here to Summon Me", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                ]
           ]
        ),
    )

