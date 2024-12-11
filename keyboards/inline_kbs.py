from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from aiogram.utils.keyboard import InlineKeyboardBuilder
from all_keyboards import main_kb
def ease_link_kb():
    inline_kb_list = [
        [InlineKeyboardButton(text="Мой хабр", url='https://habr.com/ru/users/yakvenalex/')],
        [InlineKeyboardButton(text="Мой Telegram", url='tg://resolve?domain=yakvenalexx')],
        [InlineKeyboardButton(text="Веб приложение", web_app=WebAppInfo(url="https://tg-promo-bot.ru/questions"))]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list)

def back_to_menu():
    inline_kb_list2 = [
        [InlineKeyboardButton(text="Назад", callback_data='back_home')]
    ]
    return InlineKeyboardMarkup(inline_keyboard=main_kb)
