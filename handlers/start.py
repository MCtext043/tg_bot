from aiogram import types
from aiogram.types import FSInputFile
from keyboards import main_inline_keyboard

WELCOME_TEXT = (
    "Добро пожаловать в ELF OTC – надежный P2P-гарант\n\n"
    "💼 Покупайте и продавайте всё, что угодно – безопасно!\n"
    "От Telegram-подарков и NFT до токенов и фиата – сделки проходят легко и без риска.\n\n"
    "🔹 Удобное управление кошельками\n"
    "🔹 Реферальная система\n\n"
    "📖 Как пользоваться?\n"
    "Ознакомьтесь с инструкцией — https://telegra.ph/Podrobnyj-gajd-po-ispolzovaniyu-GiftElfRobot-04-25\n\n"
    "Выберите нужный раздел ниже:"
)

async def start_handler(message: types.Message):
    photo = FSInputFile("start.jpg")
    await message.answer_photo(photo, caption=WELCOME_TEXT, reply_markup=main_inline_keyboard) 