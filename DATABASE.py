import sqlite3
con = sqlite3.connect('quizbowlDB2.db')
cur = con.cursor()

#DATABASE TABLES WITH THEIR RESPECTIVE ROWS

cur.execute('''
                CREATE TABLE IF NOT EXISTS <tablename> 
                (id INTEGER PRIMARY KEY AUTOINCREMENT
               ,
               course TEXT
               ,
               question TEXT
               ,
               answer TEXT
               )
                ''')

userinputDB = input("Enter the course you would like to add.")
userinputDB2 = input("Enter the question you would like to add.")
userinputDB3 = input("Enter the answer you would like to add.")

quizbowl_questions = [
 userinputDB, userinputDB2, userinputDB3
]

print(quizbowl_questions)
print("Added to the databae!")




cur.executemany('''
               INSERT INTO <tablename> (course, question, answer)
               VALUES (?, ?, ?)
               ''', quizbowl_questions)
cur.execute('''DELETE FROM <tablename>''')

con.commit()