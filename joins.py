import sqlite3


def main():
    db = sqlite3.connect('database.db')
    mycursor = db.cursor()
    solutions(mycursor)


def solutions(mycursor):
    # 1. Number of students who wrote 'GES101' exam
    mycursor.execute(
        '''
        SELECT
            course_code,
            course_description,
            COUNT( profile_id) AS 'no_of_students'
        FROM courses
        INNER JOIN scores
            ON courses.id = scores.course_id
        WHERE course_code = 'GES101'
        '''
    )
    print(mycursor.fetchall(), end='\n\n')

    # 2. Show students from the faculty of science who wrote 'GES101' exam
    mycursor.execute(
        '''
        SELECT
            course_code, course_description,
            faculty, department,
            student_name, current_level,
            score
        FROM courses
        INNER JOIN scores
            ON courses.id = scores.course_id
        INNER JOIN students_profile
            ON scores.profile_id = students_profile.id
        WHERE
            course_code = 'GES101' AND
            faculty = 'Science'
        LIMIT 5
        '''
    )
    print(mycursor.fetchall(), end='\n\n')

    # 3. Show students from the faculty of technology who wrote 'GES201' exam
    mycursor.execute(
        '''
        SELECT
            course_code, course_description,
            faculty, department,
            student_name, current_level,
            score
        FROM courses
        INNER JOIN scores
            ON courses.id = scores.course_id
        INNER JOIN students_profile
            ON scores.profile_id = students_profile.id
        WHERE
            course_code = 'GES201' AND
            faculty = 'Technology'
        LIMIT 5;
        '''
    )
    print(mycursor.fetchall(), end='\n\n')

    # 4. Number of courses offered by all departments in
    # the faculty of arts across all levels
    mycursor.execute(
        '''
        SELECT
            department, current_level,
            COUNT(DISTINCT course_code) AS 'number_of_courses'
        FROM courses
        INNER JOIN scores
            ON courses.id = scores.course_id
        INNER JOIN students_profile
            ON scores.profile_id = students_profile.id
        WHERE
            faculty = 'Arts'
        GROUP BY department, current_level
        LIMIT 5
        '''
    )
    print(mycursor.fetchall(), end='\n\n')

    # 5. Display the highest score in each course
    # relative to statistics department, 100 level
    mycursor.execute(
        '''
        SELECT
            department, current_level
            course_code, course_description,
            max(score) AS 'maximum_score'
        FROM courses
        INNER JOIN scores
            ON courses.id = scores.course_id
        INNER JOIN students_profile
            ON scores.profile_id = students_profile.id
        WHERE
            department = 'Statistics' AND
            current_level = 100
        GROUP BY course_code;
        '''
    )
    print(mycursor.fetchall(), end='\n\n')

    # 6. Students with no exam record
    mycursor.execute(
        '''
        SELECT
            student_name, current_level
            faculty, department,
            course_id, score
        FROM students_profile
        LEFT JOIN scores
            ON students_profile.id = scores.profile_id
        WHERE course_id IS NULL
        LIMIT 5;
        '''
    )
    print(mycursor.fetchall(), end='\n\n')


if __name__ == '__main__':
    main()
