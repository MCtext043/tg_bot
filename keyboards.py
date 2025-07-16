from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_main_inline_keyboard(lang: str = 'ru'):
    if lang == 'en':
        return InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Add/Change wallet", callback_data="wallet")],
                [InlineKeyboardButton(text="Create deal", callback_data="deal")],
                [InlineKeyboardButton(text="Referral link", callback_data="referral")],
                [InlineKeyboardButton(text="Change language", callback_data="language")],
                [InlineKeyboardButton(text="Support", url="https://forms.gle/4kN2r57SJiPrxBjf9")],
            ]
        )
    return InlineKeyboardMarkup(
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