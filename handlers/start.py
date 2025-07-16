from aiogram import types
from aiogram.types import FSInputFile
from keyboards import get_main_inline_keyboard
from user_data import user_languages

def get_welcome_text(lang: str = 'ru'):
    if lang == 'en':
        return (
            "Welcome to ELF OTC – your trusted P2P-guarantor\n\n"
            "💼 Buy and sell anything safely!\n"
            "From Telegram gifts and NFTs to tokens and fiat – deals are easy and risk-free.\n\n"
            "🔹 Convenient wallet management\n"
            "🔹 Referral system\n\n"
            "📖 How to use?\n"
            "Read the guide — https://telegra.ph/Podrobnyj-gajd-po-ispolzovaniyu-GiftElfRobot-04-25\n\n"
            "Choose a section below:"
        )
    return (
        "Добро пожаловать в ELF OTC – надежный P2P-гарант\n\n"
        "💼 Покупайте и продавайте всё, что угодно – безопасно!\n"
        "От Telegram-подарков и NFT до токенов и фиата – сделки проходят легко и без риска.\n\n"
        "🔹 Удобное управление кошельками\n"
        "🔹 Реферальная система\n\n"
        "📖 Как пользоваться?\n"
        "Ознакомьтесь с инструкцией — https://telegra.ph/Podrobnyj-gajd-po-ispolzovaniyu-GiftElfRobot-04-25\n\n"
        "Выберите нужный раздел ниже:"
    )

async def send_start_screen(message: types.Message, lang: str = None):
    if lang is None:
        lang = user_languages.get(message.from_user.id, 'ru')
    photo = FSInputFile("start.jpg")
    await message.answer_photo(photo, caption=get_welcome_text(lang), reply_markup=get_main_inline_keyboard(lang))

async def start_handler(message: types.Message):
    await send_start_screen(message) 