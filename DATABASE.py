import sqlite3
con = sqlite3.connect('quizbowlDB2.db')
cur = con.cursor()


        
#list to add questions (course, question, answer)

quizbowl_questions = [

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



#function for inserting data into tables
cur.executemany('''
               INSERT INTO DatabaseM (course, question, answer)
               VALUES (?, ?, ?)
               ''', quizbowl_questions)

#to delete tables, dangerous will nuke tables
# cur.execute('''DROP TABLE <tablename> ''')

#deletes data from table, much safer than the above option
# cur.execute('''DELETE FROM <tablename> ''')

con.commit()
