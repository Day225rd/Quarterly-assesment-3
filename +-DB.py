#DATABASE CONNECTION
import sqlite3
connection = sqlite3.connect('newDB.db')
cursor = connection.cursor()

#ADDING TABLES
cursor.execute('''
               CREATE TABLE IF NOT EXISTS quizbowl
               
               (course TEXT PRIMARY KEY
               , 
               questions TEXT
               , 
               feedback TEXT)
               ''')


#ADDING ROWS
cursor.execute('''
               INSERT INTO <table> (course1,course2....)
               VALUES(1,2,....)
               ''')

#DELETING DATA
#USE CAUTION, CAN BE DANGEROUS. DATA WILL BE LOST
import sqlite3
connection = sqlite3.connect('newDB.db')
cursor = connection.cursor()

cursor.execute("DELETE FROM (TABLE) WHERE (ROW) = ''")

#COMMITS CHANGES TO DATABASE
connection.commit()