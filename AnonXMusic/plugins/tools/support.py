from pyrogram import Client, filters
import requests
import random
import os
import re
import asyncio
import time
from AnonXMusic import app
from AnonXMusic.utils.database import add_served_chat, delete_served_chat
from AnonXMusic.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


app.on_message(
    filters.command("support")
    & filters.group)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/1cb02101c98b30fd3bf22.jpg",
        caption=f"""ᴄʟɪᴄᴋ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘs""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="ᴄʜᴀɴɴᴇʟ", url="https://t.me/STATUSDAIRY2"
                    ),

                    InlineKeyboardButton(
                        text="ᴍᴜsɪᴄ ɢʀᴏᴜᴘ", url="https://t.me/vohmusic"
                    ),
                    
                ],
                [

                    InlineKeyboardButton(
                        text="sᴜᴘᴘᴏʀᴛ", url="https://t.me/VOICEOFHEART0"
                    )
                    
                ],
                [
                    InlineKeyboardButton(
                        text="ᴄʟᴏsᴇ", callback_data=f"close"
                    )
                ],
            ]
        ),
    )

@app.on_message(
    filters.command("support")
    & filters.group)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/1cb02101c98b30fd3bf22.jpg",
        caption=f"""ᴄʟɪᴄᴋ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘs""",
        reply_markup=InlineKeyboardMarkup(
              [
                    InlineKeyboardButton(
                        text="ᴄʜᴀɴɴᴇʟ", url="https://t.me/STATUSDAIRY2"
                    ),

                    InlineKeyboardButton(
                        text="ᴍᴜsɪᴄ ɢʀᴏᴜᴘ", url="https://t.me/vohmusic"
                    ),
                    
                ],
                [

                    InlineKeyboardButton(
                        text="sᴜᴘᴘᴏʀᴛ", url="https://t.me/VOICEOFHEART0"
                    )
                    
                ],
                [
                    InlineKeyboardButton(
                        text="ᴄʟᴏsᴇ", callback_data=f"close"
                    )
                ],
            ]
        ),
    )

@app.on_message(
    filters.command("support")
    & filters.group)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/1cb02101c98b30fd3bf22.jpg",
        caption=f"""ᴄʟɪᴄᴋ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘs""",
        reply_markup=InlineKeyboardMarkup(
               [
                    InlineKeyboardButton(
                        text="ᴄʜᴀɴɴᴇʟ", url="https://t.me/STATUSDAIRY2"
                    ),

                    InlineKeyboardButton(
                        text="ᴍᴜsɪᴄ ɢʀᴏᴜᴘ", url="https://t.me/vohmusic"
                    ),
                    
                ],
                [

                    InlineKeyboardButton(
                        text="sᴜᴘᴘᴏʀᴛ", url="https://t.me/VOICEOFHEART0"
                    )
                    
                ],
                [
                    InlineKeyboardButton(
                        text="ᴄʟᴏsᴇ", callback_data=f"close"
                    )
                ],
            ]
        ),
    )
