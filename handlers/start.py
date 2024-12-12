from aiogram import Router, F
import io
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from utils.my_utils import create_pdf
from keyboards.all_keyboards import main_kb
import time
from create_bot import bot
#from concurrent.futures import ThreadPoolExecuto

start_router = Router()

@start_router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Запуск сообщения по команде /start используя фильтр CommandStart()',
                         reply_markup=main_kb(message.from_user.id))

@start_router.message(Command('start_2'))
async def cmd_start_2(message: Message):
    await message.answer('Запуск сообщения по команде /start_2 используя фильтр Command()')

@start_router.message(F.text == 'Запросить')
async def req_list(message: Message):
    await message.answer('Введите текст (дата, место, фамилия, номер авто)')
    mssg=message.text
    #time.sleep(10)
    await create_pdf(mssg)
    #pdf_template = await create_pdf(mssg)
    await bot.send_document(chat_id=message.chat.id, document=open('D:/out.pdf', 'rb'), caption='Ваш PDF файл')    
    #await bot.send_document(io.BytesIO(output), caption='Ваш PDF файл')