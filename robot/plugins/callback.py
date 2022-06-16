from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

from robot.config import BOT_NAME, OWNER_USERNAME, UPDATE, SUPPORT, BOT_USERNAME


@Client.on_callback_query(filters.regex("start"))
async def cbhome(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""ᴡᴇʟᴄᴏᴍᴇ : [{query.message.chat.first_name}](tg://user?id={query.message.chat.id})

ɪ ᴀᴍ ᴩᴏᴡᴇʀғᴜʟ ᴍᴜsɪᴄ ᴩʟᴀʏᴇʀ ʙᴏᴛ ᴡɪᴛʜ sᴏᴍᴇ ᴀᴡᴇsᴏᴍᴇ ᴀɴᴅ ᴜsᴇғᴜʟ ғᴇᴀᴛᴜʀᴇs.

ᴜsᴇ ɪɴʟɪɴᴇ ʙᴜᴛᴛᴏɴs ɢɪᴠᴇɴ ʙᴇʟᴏᴡ ᴛᴏ ᴋɴᴏᴡ ᴍᴏʀᴇ ᴀʙᴏᴜᴛ ᴍᴇ !!""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🗂 ᴄᴏᴍᴍᴀɴᴅs", callback_data="cmds"),
                    InlineKeyboardButton(
                        "🆘 ʜᴇʟᴘ", url=f"https://t.me/{SUPPORT}")
                ],
                [
                    InlineKeyboardButton(
                        "✚ ᴄʟɪᴄᴋ ʜᴇʀᴇ ᴛᴏ ᴀᴅᴅ ᴍᴇ", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                ],
                [
                    InlineKeyboardButton(
                        "📡 ᴄʜᴀɴɴᴇʟ", url=f"https://t.me/{UPDATE}"),
                    InlineKeyboardButton(
                        "☁️ ᴏᴛʜᴇʀs", callback_data="others")
                ]
           ]
        ),
    )
