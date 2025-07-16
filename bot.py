import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import BotCommand
from config import API_TOKEN
from handlers.start import start_handler
from handlers.language import language_callback
from handlers.menu import menu_callback

async def set_commands(bot: Bot):
    commands = [
        BotCommand(command="start", description="Open menu"),
    ]
    await bot.set_my_commands(commands)

async def main():
    bot = Bot(token=API_TOKEN)
    dp = Dispatcher()
    dp.message.register(start_handler, Command("start"))
    dp.callback_query.register(language_callback)
    dp.callback_query.register(menu_callback)
    await set_commands(bot)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
