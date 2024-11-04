import sqlite3
con = sqlite3.connect('quizbowlDB2.db')
cur = con.cursor()

#DATABASE TABLES WITH THEIR RESPECTIVE ROWS

# cur.execute('''
#                 CREATE TABLE IF NOT EXISTS Math 
#                 (id INTEGER PRIMARY KEY AUTOINCREMENT
#                ,
# #                course TEXT
# #                ,
# #                question TEXT
# #                ,
# #                answer TEXT
# #                )
# #                 ''')

# # quizbowl_questions = [
# #     ("math", "What is 5 + 3?", "8"),
# #     ("math", "What is 10 - 4?", "6"),
# #     ("math", "What is 2 x 6?", "12"),
# #     ("math", "What is 12 ÷ 3?", "4"),
# #     ("math", "What is the value of the square root of 9?", "3"),
# #     ("math", "What is 100 + 0?", "100"),
# #     ("math", "If you have 5 apples and give away 2, how many do you have left?", "3"),
# #     ("math", "What number comes after 9?", "10"),
# #     ("math", "What is the value of 7 - 7?", "0"),
# #     ("math", "What is half of 8?", "4")
# # ]




cur.execute('''
                CREATE TABLE IF NOT EXISTS IT 
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
    ("IT" , "What does CPU stand for?", "Central Processing Unit"),
    ("IT" , "What is the main function of the operating system?", "Manage hardware and software resources"),
    ("IT" , "What does HTML stand for?", "HyperText Markup Language"),
    ("IT" , "What is the primary purpose of a firewall?", "To protect a network from unauthorized access"),
    ("IT" , "What does the term 'cloud computing' refer to?", "Storing and accessing data over the internet"),
    ("IT" , "What is the most common language used for web development?", "JavaScript"),
    ("IT" , "What does VPN stand for?", "Virtual Private Network"),
    ("IT" , "What is a database?", "An organized collection of data"),
    ("IT" , "What is the function of an IP address?", "Identify a device on a network"),
    ("IT" , "What does 'phishing' mean?", "A fraudulent attempt to obtain sensitive information")
]





cur.executemany('''
               INSERT INTO IT (course, question, answer)
               VALUES (?, ?, ?)
               ''', quizbowl_questions)
# cur.execute('''DELETE FROM IT''')

con.commit()