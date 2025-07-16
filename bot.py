import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, FSInputFile, BotCommand

API_TOKEN = '7707235660:AAHnhWeQvtc-wCArnL_lVlvMCbOng82TEQI'

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

main_inline_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Добавить/изменить кошелек", callback_data="wallet")],
        [InlineKeyboardButton(text="Создать сделку", callback_data="deal")],
        [InlineKeyboardButton(text="Реферальная ссылка", callback_data="referral")],
        [InlineKeyboardButton(text="Change language", callback_data="language")],
        [InlineKeyboardButton(text="Поддержка", url="https://forms.gle/4kN2r57SJiPrxBjf9")],
    ]
)

menu_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Назад", callback_data="back_to_main")],
    ]
)

language_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="English", callback_data="lang_en")],
        [InlineKeyboardButton(text="Русский", callback_data="lang_ru")],
    ]
)


async def start_handler(message: types.Message):
    photo = FSInputFile("start.jpg")
    await message.answer_photo(photo, caption=WELCOME_TEXT, reply_markup=main_inline_keyboard)


async def callback_handler(callback: types.CallbackQuery):
    if callback.data == "language":
        text = "🌍 Choose your language:\n\nВыберите язык:"
        await callback.message.answer(text, reply_markup=language_keyboard)
        await callback.answer()
    elif callback.data == "lang_en":
        await callback.message.answer("Language set to English.")
        await callback.answer()
    elif callback.data == "lang_ru":
        await callback.message.answer("Язык установлен: Русский.")
        await callback.answer()
    elif callback.data == "menu":
        await callback.message.answer("Open menu\n\n/start", reply_markup=menu_keyboard)
        await callback.answer()
    elif callback.data == "back_to_main":
        photo = FSInputFile("start.jpg")
        await callback.message.answer_photo(photo, caption=WELCOME_TEXT, reply_markup=main_inline_keyboard)
        await callback.answer()
    else:
        await callback.answer()


async def set_commands(bot: Bot):
    commands = [
        BotCommand(command="start", description="Open menu"),
    ]
    await bot.set_my_commands(commands)


async def main():
    bot = Bot(token=API_TOKEN)
    dp = Dispatcher()
    dp.message.register(start_handler, Command("start"))
    dp.callback_query.register(callback_handler)
    await set_commands(bot)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
