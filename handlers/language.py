from aiogram import types
from keyboards import language_keyboard
from handlers.start import send_start_screen
from user_data import user_languages

async def language_callback(callback: types.CallbackQuery):
    if callback.data == "language":
        text = "🌍 Choose your language:\n\nВыберите язык:"
        await callback.message.answer(text, reply_markup=language_keyboard)
        await callback.answer()
    elif callback.data == "lang_en":
        user_languages[callback.from_user.id] = 'en'
        await callback.message.delete()
        await send_start_screen(callback.message, lang='en')
        await callback.answer()
    elif callback.data == "lang_ru":
        user_languages[callback.from_user.id] = 'ru'
        await callback.message.delete()
        await send_start_screen(callback.message, lang='ru')
        await callback.answer() 