from aiogram import types
from keyboards import menu_keyboard
from handlers.start import send_start_screen
from user_data import user_languages

async def menu_callback(callback: types.CallbackQuery):
    if callback.data == "menu":
        await callback.message.answer("Open menu\n\n/start", reply_markup=menu_keyboard)
        await callback.answer()
    elif callback.data == "back_to_main":
        lang = user_languages.get(callback.from_user.id, 'ru')
        await send_start_screen(callback.message, lang=lang)
        await callback.answer() 