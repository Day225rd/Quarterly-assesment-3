import sqlite3
con = sqlite3.connect('quizbowlDB2.db')
cur = con.cursor()


# print("Please select an option. 1: adds a course, question and answer to the quizbowl game,",
#           "2: lets you see all of the data within the database")
# userinput0 = input()
# if userinput0 == "1":
#         userinputDB = input("Enter the course you would like to add.")

#         userinputDB2 = input("Enter the question you would like to add.")

#         userinputDB3 = input("Enter the answer you would like to add.")
#         print("Added to the quiz")
# if userinput0 == "2":
#         cur.execute('''SELECT * FROM math''')
#         printdata = cur.fetchall()
#         print(printdata)
        

quizbowl_questions = [
("Database Management", "What is a table", "Structure"),
("Database Management", "What is a primary key", "Identifier"),
("Database Management", "What is SQL", "Query Language"),
("Database Management", "What is a foreign key", "Relationship"),
("Database Management", "What is a view", "Virtual Table"),
("Database Management", "What is a schema", "Blueprint"),
("Database Management", "What is normalization", "Organization"),
("Database Management", "What is a join", "Combination"),
("Database Management", "What is an index", "Optimization"),
("Database Management", "What is a transaction", "Operation")
]

#DATABASE TABLES WITH THEIR RESPECTIVE ROWS

cur.execute('''
                CREATE TABLE IF NOT EXISTS DatabaseM 
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
               INSERT INTO DatabaseM (course, question, answer)
               VALUES (?, ?, ?)
               ''', quizbowl_questions)
# cur.execute('''DROP TABLE IT ''')

con.commit()
