from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, KeyboardButtonPollType, CallbackQuery
from create_bot import admins


def main_kb(user_telegram_id: int):
    kb_list = [
        [KeyboardButton(text="Запросить")],
        [KeyboardButton(text="Добавить сотр"), KeyboardButton(text="добавить авто")],
        [KeyboardButton(text="Отправить")]
    ]
    if user_telegram_id in admins:
        kb_list.append([KeyboardButton(text="⚙️ Админ панель")])
    keyboard = ReplyKeyboardMarkup(keyboard=kb_list,
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder="Воспользуйтесь меню:")
    return keyboard

def create_spec_kb():
    kb_list = [
        [KeyboardButton(text="Отправить гео", request_location=True)],
        [KeyboardButton(text="Поделиться номером", request_contact=True)],
        [KeyboardButton(text="Отправить викторину/опрос", request_poll=KeyboardButtonPollType())]
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb_list,
                                   resize_keyboard=True,
                                   one_time_keyboard=True,
                                   input_field_placeholder="Воспользуйтесь специальной клавиатурой:")
    return keyboard