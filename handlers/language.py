from aiogram import types
from keyboards import language_keyboard

async def language_callback(callback: types.CallbackQuery):
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