from asyncio import sleep
from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart
from wikipediaapi import Wikipedia
from data.config import welcome_text, welcome_photo, no_group, f, n

router = Router()
wiki = Wikipedia(language="ru", user_agent="Your_User_Agent_String")

@router.message(CommandStart())
async def send_welcome(message: Message):
    await message.answer_photo(photo=welcome_photo, caption=welcome_text)

@router.message(F.text)
async def wiki_search(message: Message):
    if message.chat.type != "private":
        await message.reply(no_group)
        return

    query = message.text
    page = wiki.page(query)
    msg = await message.answer(f)

    await sleep(0.5)

    if page.exists():
        text = (
            f"<b>🌐 {page.title}:</b>\n"
            f"{page.summary}\n\n"
            f"<b>Вся информация:</b> -> <a href='{page.fullurl}'>тык</a>"
        )
        await message.answer(text)
    else:
        await message.reply(n)

    await msg.delete()
