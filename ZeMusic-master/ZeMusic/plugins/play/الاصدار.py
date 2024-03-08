import asyncio
import os
import time
import requests
import aiohttp
import config
from pyrogram import filters
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from ZeMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from ZeMusic import app

import re
import sys
from os import getenv

from dotenv import load_dotenv



@app.on_message(
    command(["الاصدار"])
  
)
async def bkouqw(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph//file/a92c0bf56bbf2c4ffff25.jpg",
        caption=f"""**اهلا بك عزيزي {message.from_user.mention} في اصدار سورس ماجيك
★᚜ اسم سورس : ماجيك 

★᚜ نوع : ميوزك

★᚜ اللغه : اللغه العربيه ويدعم الانجليزيه 

★᚜ مجال العمل : بوتات تشغيل الموسيقى في الاتصال
★᚜ نظام التشغيل : كارولين بوت ميوزك
★᚜ الاصدار 2.0.14
★᚜ تاريخ التأسيس : 2024/2/2

★᚜ مؤسس ماجيك : [ 𐇮 𝗠𝗮𝗭𝗲𝗡 𖠮🚸𖠮 آلـۘهہؚيـٰـ‌ُـُ໋۠بـ໋ۘ۠ه 𐇮](https://t.me/Ve_G4)""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝚂𝙾𝚄𝚁𝙲𝙴 𝙼𝙰𝙶𝙸𝙲", url=f"https://t.me/Fv_av"), 
                 ],[
                 InlineKeyboardButton(
                        "", callback_data="hpdtsnju"),
               ],
          ]
        ),
    )

