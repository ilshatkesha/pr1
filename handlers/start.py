from aiogram import Router, F, types
import io
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.types import InputMediaDocument
from utils.my_utils import create_pdf
from keyboards.all_keyboards import main_kb
import time
from create_bot import bot
from aiogram.types.input_file import FSInputFile
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State
from aiogram.fsm.state import StatesGroup
#rom utils.my_utils import split_empl
from bd_requests.requests import add_empl, add_auto
#from concurrent.futures import ThreadPoolExecuto

start_router = Router()

class Form(StatesGroup):  # Наследуем от StatesGroup
    waiting_for_text = State()
    waiting_empl = State()
    waiting_auto = State()

@start_router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Запуск сообщения по команде /start используя фильтр CommandStart()',
                         reply_markup=main_kb(message.from_user.id))

@start_router.message(Command('start_2'))
async def cmd_start_2(message: Message):
    await message.answer('Запуск сообщения по команде /start_2 используя фильтр Command()')

@start_router.message(F.text == 'Запросить')
async def req_list(message: Message, state:FSMContext):
    await message.answer('Введите текст (дата, место, фамилия, номер авто)')
    await state.set_state(Form.waiting_for_text)

@start_router.message(F.text, Form.waiting_for_text)
async def capture_mssg(message: Message, state:FSMContext):
    await state.update_data(mssg=message.text)
    mssg = message.text
    #time.sleep(10)
    print(mssg)
    await create_pdf(mssg)
    doc=FSInputFile('D:/out.pdf')
    #with open('D:/out.pdf', 'rb') as file:
    await bot.send_document(chat_id=message.chat.id, document=doc)    
    #pdf_template = await create_pdf(mssg)
    
    #await bot.send_document(io.BytesIO(output), caption='Ваш PDF файл')

@start_router.message(F.text == 'Добавить сотр')
async def add_car(message: Message, state:FSMContext):
    await message.answer('Введите текст БЕЗ ПРОБЕЛОВ И ЧЕРЕЗ ЗАПЯТЫЕ!! Фамилия, Имя Отчество, СНИЛС, Серия и номер в.у., Дата в.у. Категории в.у., Табельный номер(?))')
    await state.set_state(Form.waiting_empl)

@start_router.message(F.text, Form.waiting_empl)
async def capture_mssg(message: Message, state:FSMContext):
    await state.update_data(mssg=message.text)
    mssg = message.text
    add_empl(mssg)
    await message.answer('Успешный успех, больше так не делайте')

@start_router.message(F.text == 'добавить авто')
async def add_employer(message: Message, state:FSMContext):
    await message.answer('Введите текст БЕЗ ПРОБЕЛОВ И ЧЕРЕЗ ЗАПЯТЫЕ!! Марка,Гос.номер,Местоположение,номер без букв')
    await state.set_state(Form.waiting_auto)

@start_router.message(F.text, Form.waiting_auto)
async def capture_mssg(message: Message, state:FSMContext):
    await state.update_data(mssg=message.text)
    mssg = message.text
    add_auto(mssg)
    await message.answer('Успешный успех, больше так не делайте')
    #time.sleep(10)

    #print(split_empl(mssg))
    # #await create_pdf(mssg)
    # doc=FSInputFile('D:/out.pdf')
    # #with open('D:/out.pdf', 'rb') as file:
    # await bot.send_document(chat_id=message.chat.id, document=doc)
