Ultimate QuizBowl Application
Overview
The Ultimate QuizBowl is a quiz application built with Python's tkinter library for the graphical user interface (GUI) and sqlite3 for database management. The application allows users to select a topic (e.g., Programming Logic, Data Analytics, etc.), answer questions, and track their score. The questions are fetched dynamically from an SQLite database.

Features
User-friendly GUI to select a quiz topic and answer questions.
Questions are dynamically loaded from the database based on the selected topic.
Keeps track of the score and displays it at the end of the quiz.
Displays correct/incorrect feedback after each question.
Prerequisites
Python 3.x installed on your machine.
Tkinter: Tkinter comes pre-installed with Python, so no additional installation is necessary.
SQLite3: This is also included in Python's standard library, so no additional installation is required.

Getting Started
1. Install Python
If you haven't already, install Python 3.x from the official website: https://www.python.org/downloads/.

2. Prepare the Database
The application assumes that there is an SQLite database (quizBowlDB2.db) that contains tables for different quiz topics. Each table should have columns for question and answer.

For example, a table for Programming Logic might look like:

sql
Copy code
CREATE TABLE ProgrammingLogic (
    question TEXT,
    answer TEXT
);
Make sure to add questions and answers for each topic. The application will fetch questions from the selected table in the database.

3. Running the Application
Clone the repository or save the Python script (quizbowl_app.py).

Ensure the database (quizBowlDB2.db) is in the same directory as the script.

Run the application using the command:

bash
Copy code
python quizbowl_app.py
This will launch the GUI where you can select a topic and begin the quiz.

Code Explanation
1. Database Connection
The application connects to the SQLite database quizBowlDB2.db using the sqlite3 module.

python
Copy code
con = sqlite3.connect('quizBowlDB2.db')
cur = con.cursor()
The database contains multiple tables, each corresponding to a quiz topic. The questions and answers are stored in these tables.

2. QuizBowlApp Class
This class initializes the main window, which contains:

A welcome message.
A set of radio buttons for selecting a quiz topic (e.g., Programming Logic, Data Analytics, etc.).
A button to start the quiz once a topic is selected.
3. New_window Class
This class handles the quiz interface:

Displays a question.
Accepts user input for the answer.
Validates the answer and provides feedback (correct/incorrect).
Loads the next question upon clicking "Next question".
Tracks the score and shows the final result when the quiz is finished.
4. SQLite Queries
The load_questions() method retrieves the questions and answers for the selected topic from the database using the SQL query:

python
Copy code
cur.execute(f'''SELECT question, answer FROM {self.course}''')
The course variable is dynamically set based on the topic selected by the user.

Troubleshooting
Issue: Application doesn’t load questions from the database.

Solution: Ensure that the database (quizBowlDB2.db) contains valid data (questions and answers) for the selected quiz topic. Check the database schema to ensure it matches the expected format.
Issue: Incorrect or missing database connection.

Solution: Make sure that the SQLite database file is located in the same directory as the Python script, or provide the correct file path to the sqlite3.connect() function
