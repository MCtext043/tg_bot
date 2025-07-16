from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

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