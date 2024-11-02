import sqlite3
connection = sqlite3.connect('newDB.db')
cursor = connection.cursor()

#DATABASE TABLES WITH THEIR RESPECTIVE ROWS

cursor.execute('''
               CREATE TABLE IF NOT EXISTS Course1
               
               (
               questions1 TEXT PRIMARY KEY
               , 
               questions2 TEXT
               ,
               questions3 TEXT
               ,
               questions4 TEXT
               ,
               questions5 TEXT
               ,
               questions6 TEXT
               , 
               questions7 TEXT
               ,
               questions8 TEXT
               ,
               questions9 TEXT
               ,
               questions10 TEXT
                              )
               ''')
cursor.execute('''
               CREATE TABLE IF NOT EXISTS Course2
               
               (
               questions1 TEXT PRIMARY KEY
               , 
               questions2 TEXT
               ,
               questions3 TEXT
               ,
               questions4 TEXT
               ,
               questions5 TEXT
               ,
               questions6 TEXT
               , 
               questions7 TEXT
               ,
               questions8 TEXT
               ,
               questions9 TEXT
               ,
               questions10 TEXT
                              )
               ''')
cursor.execute('''
               CREATE TABLE IF NOT EXISTS Course3
               
               (
               questions1 TEXT PRIMARY KEY
               , 
               questions2 TEXT
               ,
               questions3 TEXT
               ,
               questions4 TEXT
               ,
               questions5 TEXT
               ,
               questions6 TEXT
               , 
               questions7 TEXT
               ,
               questions8 TEXT
               ,
               questions9 TEXT
               ,
               questions10 TEXT
                              )
               ''')
cursor.execute('''
               CREATE TABLE IF NOT EXISTS Course4
               
               (
               questions1 TEXT PRIMARY KEY
               , 
               questions2 TEXT
               ,
               questions3 TEXT
               ,
               questions4 TEXT
               ,
               questions5 TEXT
               ,
               questions6 TEXT
               , 
               questions7 TEXT
               ,
               questions8 TEXT
               ,
               questions9 TEXT
               ,
               questions10 TEXT
                              )
               ''')
cursor.execute('''
               CREATE TABLE IF NOT EXISTS Course5
               
               (
               questions1 TEXT PRIMARY KEY
               , 
               questions2 TEXT
               ,
               questions3 TEXT
               ,
               questions4 TEXT
               ,
               questions5 TEXT
               ,
               questions6 TEXT
               , 
               questions7 TEXT
               ,
               questions8 TEXT
               ,
               questions9 TEXT
               ,
               questions10 TEXT
                              )
               ''')

