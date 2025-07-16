from aiogram import types
from aiogram.types import FSInputFile
from keyboards import menu_keyboard, main_inline_keyboard
from handlers.start import WELCOME_TEXT

async def menu_callback(callback: types.CallbackQuery):
    if callback.data == "menu":
        await callback.message.answer("Open menu\n\n/start", reply_markup=menu_keyboard)
        await callback.answer()
    elif callback.data == "back_to_main":
        photo = FSInputFile("start.jpg")
        await callback.message.answer_photo(photo, caption=WELCOME_TEXT, reply_markup=main_inline_keyboard)
        await callback.answer() 