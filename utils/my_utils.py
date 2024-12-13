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

def split_empl(text):
     empl = text.split(",")
     return empl    

#def create_pdf_sync(pdf_template):
#    return pdfkit.from_string(pdf_template, False)  # Возвращаем байты PDFdef processing_file(file, last_name, first_name, snils):
#connection = aiosqlite.connect('D:/SQLStudio/database1')
#cur = connection.cursor()
#async def add_pdf_to_db(file_path):
    #async with aiosqlite.connect('D:/SQLStudio/database1') as connection:
        #async with connection.cursor() as cur:
            #with open(file_path, 'rb') as file:
                #pdf_data = file.read()
                #await cur.execute('INSERT INTO Путевые (Путевой) VALUES (?)', (pdf_data))
                #await connection.commit()


async def create_pdf (mssg):
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
            row = await cur.fetchone()
            if row is not None:
                 result = row[0]
            last_name = str(result)
            await cur.execute("SELECT Имя_Отчество FROM Сотрудники WHERE Фамилия = ?", (surname,))
            row = await cur.fetchone()
            if row is not None:
                 result = row[0]
            first_name = str(result)
            await cur.execute("SELECT СНИЛС FROM Сотрудники WHERE Фамилия = ?", (surname,))
            row = await cur.fetchone()
            if row is not None:
                 result = row[0]
            snils = str(result)
            
            with open(r'D:/new 1.html', 'r', encoding='utf-8') as f:
                    file = f.read()
                    template = templ.from_string(file)
                    pdf_template = template.render({'last_name': last_name, 'first_name': first_name, 'snils': snils, })
                    await pdfkit.from_string(pdf_template, "D:/out.pdf")
                    #with open('D:/out.pdf', 'w', encoding='utf-8') as f2:
                     #   f2.write(out_file)
                        #f = open('D:/new.html', 'w')
                        #f.write(f2)
                        #f.close()
            
            #await add_pdf_to_db('D:/out.pdf')
            #return('out.pdf')

            #with open(r'qwezxc123.html', 'r', encoding='utf-8') as f:
             #       t = f.read()
            #template = templ.from_string(t)        
            #pdf_template = template.render({'last_name': last_name, 'first_name': first_name, 'snils': snils, })
            #print(pdf_template)
            
            
            
            #return ('')y
            #ThreadPoolExecutor
            #output = await asyncio.get_event_loop().run_in_executor(pdf_executor, create_pdf_sync, pdf_template)
            #output = pdfkit.from_string(pdf_template, False)
            #bot.send_document(io.BytesIO(pdf_template), caption='Ваш PDF файл')

            #pdf_template = await template.render({'auto_num': auto_num,'num': num, 'first_date': first_date, 'sec_date': sec_date, 'auto_mark': auto_mark, 'last_name': last_name, 'first_name': first_name,
                                #'snils': snils, 'tab_num': tab_num, 'dl_num': dl_num, 'dl_date': dl_date, 'dl_class': dl_class, 'location': location, 'engineer': engineer})
