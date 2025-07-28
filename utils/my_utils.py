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

def split_mssg(text):
     splmsg = text.split(",")
     return splmsg  
 
def split_date(text):
     splmssg = text.split(".")
     return splmssg   

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
    #mecanicus = 'Сатлыганов И.Р.'
    async with aiosqlite.connect('D:/SQLStudio/database1') as connection:
        async with connection.cursor() as cur:
            data_to_pdf = split_mssg(mssg)
            number = data_to_pdf[3]
            surname = data_to_pdf[2]
            date_rl = data_to_pdf[0]
            date_to_split = split_date(date_rl)
            day = date_to_split[0]
            mouth = date_to_split[1]
            await cur.execute("SELECT Марка FROM Автомобили WHERE Номер = ?", (number,))
            row = await cur.fetchone()
            if row is not None:
                 result = row[0]
            auto = str(result)
            await cur.execute("SELECT Гос_номер FROM Автомобили WHERE Номер = ?", (number,))
            row = await cur.fetchone()
            if row is not None:
                 result = row[0]
            auto_num = str(result)
            await cur.execute("SELECT Номер FROM Автомобили WHERE Номер = ?", (number,))
            row = await cur.fetchone()
            if row is not None:
                 result = row[0]
            num = str(result)
            await cur.execute("SELECT Механик FROM Автомобили WHERE Номер = ?", (number,))
            row = await cur.fetchone()
            if row is not None:
                 result = row[0]
            mecanicus = str(result)
            #print(auto_num)
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
            await cur.execute("SELECT ВУ FROM Сотрудники WHERE Фамилия = ?", (surname,))
            row = await cur.fetchone()
            if row is not None:
                 result = row[0]
            dl_num = str(result)
            await cur.execute("SELECT Дата_ВУ FROM Сотрудники WHERE Фамилия = ?", (surname,))
            row = await cur.fetchone()
            if row is not None:
                 result = row[0]
            dl_date = str(result)
            await cur.execute("SELECT СНИЛС FROM Сотрудники WHERE Фамилия = ?", (surname,))
            row = await cur.fetchone()
            if row is not None:
                 result = row[0]
            snils = str(result)
            await cur.execute("SELECT Класс FROM Сотрудники WHERE Фамилия = ?", (surname,))
            row = await cur.fetchone()
            if row is not None:
                 result = row[0]
            dl_class = str(result)
            await cur.execute("SELECT Местоположение FROM Автомобили WHERE Номер = ?", (number,))
            row = await cur.fetchone()
            if row is not None:
                 result = row[0]
            location = str(result)
            
            with open(r'D:/last.html', 'r', encoding='utf-8') as f:
                    file = f.read()
                    template = templ.from_string(file)
                    #print(date_rl)
                    pdf_template = template.render({'first_date':day, 'mouth':mouth, 'end_date':day, 'num':num, 'num_auto':auto_num, 'dl_date':dl_date, 'dl_num':dl_num, 'dl_class':dl_class, 'location':location, 'mecanicus':mecanicus, 'last_name': last_name, 'first_name': first_name, 'snils': snils, })
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
