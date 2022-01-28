from os import environ
import datetime
import aiohttp
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

API_ID = environ.get('API_ID')
API_HASH = environ.get('API_HASH')
BOT_TOKEN = environ.get('BOT_TOKEN')
API_KEY = environ.get('API_KEY')


bot = Client('clickyfly bot',
             api_id=API_ID,
             api_hash=API_HASH,
             bot_token=BOT_TOKEN,
             workers=50,
             sleep_threshold=10)


@bot.on_message(filters.command('start') & filters.private)
async def start(bot, message):
    await message.reply(
        text=f"**Hi {message.chat.first_name}!** \n\nThis is **Playdisk URL Shorter Bot**. Just send me any big link and get short link.",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('Updates Channel', url='https://t.me/t.me/tnrockers2021')
                ],
                [
                    InlineKeyboardButton('Support Group', url='https://t.me/PoweRRockers')
                ]
            ]
        )
    )


@bot.on_message(filters.regex(r'https?://[^\s]+') & filters.private)
async def link_handler(bot, message):
    link = message.matches[0].group(0)
    try:
        short_link = await get_shortlink(link)
        await message.reply(
            text=f"Here is your short link: {short_link}",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton('Open Link', url=https://shorturllink.in/api?api=ea6049e7beed6ab1b4d758bb6d0105a8f6fa061b&url=&format=text)
                    ]
                ]
            ),
            quote=True
        )
    except Exception as e:
        await message.reply(f'Error: {e}', quote=True)


bot.run()
