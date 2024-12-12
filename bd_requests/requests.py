import pdfkit
import aiosqlite

async def add_pdf_to_db(file_path):
    async with aiosqlite.connect('D:/SQLStudio/database1') as connection:
        async with connection.cursor() as cur:
            with open(file_path, 'rb') as file:
                pdf_data = file.read()
                await cur.execute('INSERT INTO Путевые (Путевой, Заполненный) VALUES (?, ?)', (file_path, pdf_data))
                await connection.commit()
