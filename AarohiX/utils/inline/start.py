from typing import Union

from pyrogram.types import InlineKeyboardButton

import config
from AarohiX import app


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="⛩️𝐀ᴅᴅ ᴍᴜsɪᴄ 𝐁σт⛩️",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="🍧ʜᴇʟᴩ🍧",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="❤‍🔥sᴇᴛᴛɪɴɢs❤‍🔥", callback_data="settings_helper"
            ),
        ],
        [
            InlineKeyboardButton(
                text="💌𝗦ԩ𝐚ʏя𝗼༌🪽", url=f"https://t.me/SHAYRI_CHANNEL1"),
            InlineKeyboardButton(
                text="🍒‌⃰‌˶‌֟፝ᴄʜᴀɴɴᴇʟ⏎‌🝛꯭🧸", url=f"https://t.me/MUSICBOT_OWNER"
            ),
        ],
        [
            InlineKeyboardButton(
                text="👑 ᴍᴀɪɴᴛᴀɪɴᴇʀ 👑", user_id=OWNER),
            InlineKeyboardButton(
                text="💒ʙωғ sᴜᴩᴩᴏʀᴛ💒", url=f"https://t.me/BWF_MUSIC1"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="⛩️𝐀ᴅᴅ ᴍᴜsɪᴄ 𝐁σт⛩️",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text="🍧ʜᴇʟᴩ🍧", callback_data="settings_back_helper"
            ),
        ],
        [
            InlineKeyboardButton(
                text="💌𝗦ԩ𝐚ʏя𝗼༌🪽", url=f"https://t.me/SHAYRI_CHANNEL1"),
            InlineKeyboardButton(
                text="🍒‌⃰‌˶‌֟፝ᴄʜᴀɴɴᴇʟ⏎‌🝛꯭🧸", url=f"https://t.me/MUSICBOT_OWNER"
            ),
        ],
        [
            InlineKeyboardButton(text="👑 ᴍᴀɪɴᴛᴀɪɴᴇʀ 👑", user_id=OWNER),
            InlineKeyboardButton(
                text="💒ʙωғ sᴜᴩᴩᴏʀᴛ💒", url=f"https://t.me/BWF_MUSIC1"
            ),
        ],
        [
            InlineKeyboardButton(
                    text="[🥀✨➪ 𝐎ωиєя ⏎】", url=f"https://t.me/L2R_KING0"
                )
        ],
     ]
    return buttons
