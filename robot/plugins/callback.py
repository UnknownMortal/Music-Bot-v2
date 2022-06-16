from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_callback_query(filters.regex("start"))
async def cbhome(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""
