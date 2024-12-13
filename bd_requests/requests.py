import asyncio
import aiosqlite
import sqlite3
from utils.my_utils import split_empl

conn = sqlite3.connect('D:/SQLStudio/database1')
cur = conn.cursor()

def add_empl(empl_cort):
    empl_list = split_empl(empl_cort)
    print(empl_list)
    cur.executemany('INSERT INTO Сотрудники (Фамилия, Имя_Отчество, СНИЛС, ВУ, Дата_ВУ, Табельный_номер, Класс) VALUES (?,?,?,?,?,?,?)', [empl_list])
    conn.commit
    conn.close



    
