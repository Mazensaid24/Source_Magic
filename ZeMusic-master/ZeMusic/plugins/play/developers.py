import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from ZeMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from ZeMusic import app
from random import  choice, randint

#          
                
@app.on_message(filters.command(["مازن","المبرمج مازن","مبرمج السورس","مبرمج"],"")
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/96857cb597b588139fdd5.jpg",
        caption=f"""◉ 𝙽𝙰𝙼𝙴 : ❪[𐇮 𝗠𝗮𝗭𝗲𝗡 𖠮🚸𖠮 آلـۘهہؚيـٰـ‌ُـُ໋۠بـ໋ۘ۠ه 𐇮](https://t.me/Fv_av)❫
◉ 𝚄𝚂𝙴𝚁 : ❪ @Ve_G4 ❫
◉ 𝙸𝙳      : ❪ `5951674553` ❫
◉ 𝙱𝙸𝙾    : ❪ for me (@Fv_av) my world (@Fv_av - @d_aa_m) my bro (@Fv_av) ❫""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "᳒𐇮 𝗠𝗮𝗭𝗲𝗡 𖠮🚸𖠮 آلـۘهہؚيـٰـ‌ُـُ໋۠بـ໋ۘ۠ه 𐇮", url=f"https://t.me/Ve_G4"), 
                 ],[
                   InlineKeyboardButton(
                        "🔱 𝚜𝚘𝚞𝚛𝚌𝚎 𝚖𝚊𝚐𝚒𝚌 🔱", url=f"https://t.me/Fv_av"),
                ],

            ]

        ),

    )
