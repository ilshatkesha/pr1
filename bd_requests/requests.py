import asyncio
import aiosqlite
import sqlite3
from utils.my_utils import split_mssg

conn = sqlite3.connect('D:/SQLStudio/database1')
cur = conn.cursor()

def add_empl(empl_cort):
    empl_list = split_mssg(empl_cort)
    print(empl_list)
    cur.executemany('INSERT INTO Сотрудники (Фамилия, Имя_Отчество, СНИЛС, ВУ, Дата_ВУ, Табельный_номер, Класс) VALUES (?,?,?,?,?,?,?)', (empl_list,))
    conn.commit()
    #conn.close()

def add_auto(auto_cort):
    auto_list = split_mssg(auto_cort)
    print(auto_list)
    cur.executemany('INSERT INTO Автомобили (Марка, Гос_номер, Местоположение, Номер) VALUES (?,?,?,?)', (auto_list,))
    conn.commit()



    
