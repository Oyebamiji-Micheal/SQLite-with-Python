import sqlite3

from details import students_data, courses_data, scores_data


def main():
    # Create and connect to a database
    con = sqlite3.connect('database.db')
    mycursor = con.cursor()
    create_tables(con, mycursor)


def create_tables(con, mycursor):
    # Create tables
    mycursor.execute('''
        CREATE TABLE students_profile(
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            student_name TEXT NOT NULL,
            current_level INT NOT NULL,
            faculty TEXT NOT NULL,
            department TEXT NOT NULL,
            last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    mycursor.execute('''
        CREATE TABLE courses(
            id INTEGER,
            course_code TEXT NOT NULL UNIQUE,
            course_description TEXT NOT NULL UNIQUE
        )
    ''')

    mycursor.execute('''
        CREATE TABLE scores(
            profile_id INTEGER NOT NULL,
            course_id INTEGER NOT NULL,
            score INTEGER NOT NULL,
            last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(profile_id) REFERENCES students_profile(id),
            FOREIGN KEY(course_id) REFERENCES courses(id),
            PRIMARY KEY(profile_id, course_id)
        )
    ''')
    insert_data(con, mycursor)


def insert_data(con, mycursor):
    # insert values into students profile table
    data = students_data()
    mycursor.executemany(
        '''INSERT INTO students_profile(
            student_name, current_level, faculty, department
        )
        VALUES(?, ?, ?, ?)''', data
    )
    con.commit()

    # insert values into courses table
    data = courses_data()
    mycursor.executemany(
        '''INSERT INTO courses(
            id, course_code, course_description
        )
        VALUES(?, ?, ?)''', data
    )
    con.commit()

    # insert values into scores table
    data = scores_data()
    mycursor.executemany(
        '''INSERT INTO scores(
            profile_id, course_id, score
        )
        VALUES(?, ?, ?)''', data
    )
    con.commit()


if __name__ == "__main__":
    main()
