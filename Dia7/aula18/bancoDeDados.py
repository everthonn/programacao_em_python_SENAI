import sqlite3

import tkinter as tk 
from tkinter import messagebox

def create_db():
    conn = sqlite3.connect("meu_ banco.db")
    cursor = conn.cursor()
    cursor.execute(''' CREATE TABLE IF NOT EXISTS pessoas (
                        id AUTOINCREMENT NOT NULL,
                        nome TEXT NOT NULL,
                        idade INTEGER NOT NULL,
                        peso REAL NOT NULL,
                        altura REAL NOT NULL,
                        imc REAL NOT NULL
                   )''')
    
    conn.commit()
    conn.close()

create_db()