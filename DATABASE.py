import sqlite3
con = sqlite3.connect('quizbowlDB2.db')
cur = con.cursor()

#DATABASE TABLES WITH THEIR RESPECTIVE ROWS

cur.execute('''
                CREATE TABLE IF NOT EXISTS Course 
                (id INTEGER PRIMARY KEY AUTOINCREMENT
               ,
               course TEXT
               ,
               question TEXT
               ,
               answer TEXT
               )
                ''')

quizbowl_questions = [
    ("math", "What is 5 + 3?", "8"),
    ("math", "What is 10 - 4?", "6"),
    ("math", "What is 2 x 6?", "12"),
    ("math", "What is 12 ÷ 3?", "4"),
    ("math", "What is the value of the square root of 9?", "3"),
    ("math", "What is 100 + 0?", "100"),
    ("math", "If you have 5 apples and give away 2, how many do you have left?", "3"),
    ("math", "What number comes after 9?", "10"),
    ("math", "What is the value of 7 - 7?", "0"),
    ("math", "What is half of 8?", "4")
]

cur.executemany('''
               INSERT INTO Course (course, question, answer)
               VALUES (?, ?, ?)
               ''', quizbowl_questions)
con.commit()