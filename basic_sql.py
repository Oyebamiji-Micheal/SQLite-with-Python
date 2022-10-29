import sqlite3


def main():
    con = sqlite3.connect('database.db')
    mycursor = con.cursor()
    solutions(mycursor)


def solutions(mycursor):
    # 1. Number of students from each department
    mycursor.execute(
        '''
        SELECT department, COUNT(department) AS 'no_of_student'
        FROM students_profile
        GROUP BY department
        LIMIT 5
        '''
    )
    print(mycursor.fetchall(), end='\n\n')

    # 2. Number of students across each level in the faculty of science
    mycursor.execute(
        '''
        SELECT faculty, COUNT(faculty) AS 'no_of_student'
        FROM students_profile
        GROUP BY faculty
        ORDER BY no_of_student DESC
        LIMIT 1
        '''
    )
    print(mycursor.fetchall(), end='\n\n')

    # 3. Assign a grade to each student's result
    mycursor.execute(
        '''
        SELECT
            profile_id, course_id, score,
            CASE
                WHEN score < 45 THEN 'F'
                WHEN score < 60 THEN 'C'
                WHEN score < 70 THEN 'B'
                ELSE 'A'
            END AS 'grade'
        FROM scores
        LIMIT 5
        '''
    )
    print(mycursor.fetchall(), end='\n\n')

    # 4. Count the number of students across each grade
    mycursor.execute(
        '''
        SELECT
            CASE
                WHEN score < 45 THEN 'F'
                WHEN score < 60 THEN 'C'
                WHEN score < 70 THEN 'B'
                ELSE 'A'
            END AS 'grade',
            count(*) AS 'number_of_students'
        FROM scores
        GROUP BY grade
        ORDER BY grade
        '''
    )
    print(mycursor.fetchall(), end='\n\n')

    # 5. All levels with one or more student across each department
    mycursor.execute(
        '''
        SELECT
            department,
            GROUP_CONCAT(
                DISTINCT current_level
            ) AS 'available_levels'
        FROM students_profile
        GROUP BY department
        LIMIT 5
        '''
    )
    print(mycursor.fetchall())


if __name__ == '__main__':
    main()
