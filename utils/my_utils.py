from jinja2 import Environment, FileSystemLoader
import asyncio
import pdfkit
import aiosqlite
import io
from create_bot import bot
from concurrent.futures import ThreadPoolExecutor
from aiogram import Bot, Dispatcher, types
from aiogram import F
from aiogram.filters import Command
#from aiogram import Application
path_wkhtmltopdf = 'D:/wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
templ = Environment(loader=FileSystemLoader("D:/"))

pdf_executor = ThreadPoolExecutor()

#def create_pdf_sync(pdf_template):
#    return pdfkit.from_string(pdf_template, False)  # Возвращаем байты PDF

#connection = aiosqlite.connect('D:/SQLStudio/database1')
#cur = connection.cursor()

async def create_pdf (mssg: str):
    num_auto = '326'
    num = '228'
    first_date = '123'
    sec_date = '321'
    surname = mssg
    async with aiosqlite.connect('D:/SQLStudio/database1') as connection:
        async with connection.cursor() as cur:
            #auto_mark = str(await cur.execute("SELECT Марка FROM Автомобили WHERE Гос_номер = ?", (num_auto,)).fetchone()[0])
            #auto_num = str(await cur.execute("SELECT Гос_номер FROM Автомобили WHERE Гос_номер = ?", (num_auto,)).fetchone()[0])
            await cur.execute("SELECT Фамилия FROM Сотрудники WHERE Фамилия = ?", (surname,))
            result = await cur.fetchone()
            last_name = str(result)
            await cur.execute("SELECT Имя_Отчество FROM Сотрудники WHERE Фамилия = ?", (surname,))
            result = await cur.fetchone()
            first_name = str(result)
            await cur.execute("SELECT СНИЛС FROM Сотрудники WHERE Фамилия = ?", (surname,))
            result = await cur.fetchone()
            snils = str(result)
            
            template = templ.get_template('Book1.html')

            pdf_template = template.render({'last_name': last_name, 'first_name': first_name, 'snils': snils, })
            pdfkit.from_string(pdf_template, 'D:/out.pdf')
            return('out.pdf')
            #return ('')
            #ThreadPoolExecutor
            #output = await asyncio.get_event_loop().run_in_executor(pdf_executor, create_pdf_sync, pdf_template)
            #output = pdfkit.from_string(pdf_template, False)
            #bot.send_document(io.BytesIO(pdf_template), caption='Ваш PDF файл')

            #pdf_template = await template.render({'auto_num': auto_num,'num': num, 'first_date': first_date, 'sec_date': sec_date, 'auto_mark': auto_mark, 'last_name': last_name, 'first_name': first_name,
                                #'snils': snils, 'tab_num': tab_num, 'dl_num': dl_num, 'dl_date': dl_date, 'dl_class': dl_class, 'location': location, 'engineer': engineer})
