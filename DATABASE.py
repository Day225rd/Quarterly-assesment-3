import sqlite3
con = sqlite3.connect('quizbowlDB2.db')
cur = con.cursor()

#UN COMMENT TO MAKE CHANGES
#// Represents the areas bwtween different functions
        
#list to add questions (course, question, answer)
# quizbowl_questions = [

# ]

#//////////////////////////////////////////////////////////////////

#Creating the database tables
# cur.execute('''
#                 CREATE TABLE IF NOT EXISTS DatabaseM 
#                 (id INTEGER PRIMARY KEY AUTOINCREMENT
#                ,
#                course TEXT
#                ,
#                question TEXT
#                ,
#                answer TEXT
#                )
#                 ''')


#//////////////////////////////////////////////////////////////////

#function for inserting data into tables
# cur.executemany('''
#                INSERT INTO DatabaseM (course, question, answer)
#                VALUES (?, ?, ?)
#                ''', quizbowl_questions)

#//////////////////////////////////////////////////////////////////

#for viewing data within the database
# cur.execute('''SELECT * FROM Informationsystems''')
# printdata = cur.fetchall()
# print(printdata)

#//////////////////////////////////////////////////////////////////

#to delete tables, dangerous will nuke tables
# cur.execute('''DROP TABLE <tablename> ''')

#//////////////////////////////////////////////////////////////////

#deletes data from table, much safer than the above option
# cur.execute('''DELETE FROM <tablename> ''')

#commits changes to database
con.commit()
