import sqlite3
con = sqlite3.connect('quizbowlDB2.db')
cur = con.cursor()


print("Please select an option. 1: adds a course, question and answer to the quizbowl game,",
          "2: lets you see all of the data within the database")
userinput0 = input()
if userinput0 == "1":
        userinputDB = input("Enter the course you would like to add.")

        userinputDB2 = input("Enter the question you would like to add.")

        userinputDB3 = input("Enter the answer you would like to add.")
        print("Added to the quiz")
if userinput0 == "2":
        cur.execute('''SELECT * FROM math''')
        printdata = cur.fetchall()
        print(printdata)
        

quizbowl_questions = [
userinputDB, userinputDB2, userinputDB3
]

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




cur.executemany('''
               INSERT INTO <tablename> (course, question, answer)
               VALUES (?, ?, ?)
               ''', quizbowl_questions)
cur.execute('''DELETE FROM <tablename>''')

con.commit()
