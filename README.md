<h1>SQLite with Python</h1>

<h2>Getting started with SQLite in Python</h2>

This repository contains what I learned with respect to SQLite in Python. Also, a few units of energy was expended on integrating SQLite with Jupyter notebook.

Below have I offered in broad strokes the concepts learned in the long run...

Table of Contents

- [Installation and Setup](#setup)
- [Defining Database Schema](#schema)
- [Basic SQL](#basic)
- [Joins](#joins)

<br>

<a id='setup'></a>

<h3>Installation and Setup</h3>

Python 3.10.6 was used at the time of documenting this whole thing. SQLite by default comes with Python. Hence unlike MySQL there won't be much of a installation.

<br>

<a id='schema'></a>

<h3>Defining Database Schema</h3>

At the moment there isn't a database readily available to connect to. So a new one named, `database.db` was created, and will be used throughout this scope.

Tables. Three tables were created inside the same database and for the sake of reference, below are the first four rows of each table

`student_profile`

| id  |   student_name   | current_level |       faculty       | department |        last_updated |
| :-: | :--------------: | :-----------: | :-----------------: | :--------: | ------------------: |
|  1  |    Rose Vang     |      100      |       Science       |  Physics   | 2022-10-04 16:15:04 |
|  2  |    Jimmy Wang    |      500      | College of Medicine |  Nursing   | 2022-10-04 16:15:04 |
|  3  | Kailani Browning |      100      |   Social Sciences   | Psychology | 2022-10-04 16:15:04 |
|  4  |   Rohan Hogan    |      100      |   Social Sciences   | Psychology | 2022-10-04 16:15:04 |

`courses`

| id  | course_code |            course_description            |
| :-: | :---------: | :--------------------------------------: |
|  1  |   CLA100    |    Introduction to Speech Composition    |
|  2  |   CLA105    |             Public Speaking              |
|  3  |   CLA155    | Introduction to Digital Media Production |
|  4  |   CLA181    |     Elements of Speech-Honors Course     |

`students_profile`

| profile_id | course_id | score |    last_updated     |
| :--------: | :-------: | :---: | :-----------------: |
|     1      |     5     |  96   | 2022-10-04 16:15:06 |
|     1      |    139    |  77   | 2022-10-04 16:15:06 |
|     1      |    140    |  95   | 2022-10-04 16:15:06 |
|     1      |    141    |  58   | 2022-10-04 16:15:06 |


1. **Student Profiles**: This table stores basic profile information such as name, faculty, department and current_level. To keep things simple, this table does not necessarily need to store information such as date of birth, gender, nationality and so on.
2. **Courses**: This table stores course codes and their corresponding description.
3. **Results** : Student respective scores.

_database schema definition queries can be found in [define_schema.py](https://github.com/Oyebamiji-Micheal/SQLite-with-Python/blob/main/define_schema.py)._

<br>

<a id='basic'></a>

<h3>Basic SQL</h3>

The questions below are for the sake of getting acquainted with SQLite syntax and how they might differ from other relational databases such as MySQL and Oracle. The questions span different topics such as

- Clauses
- Aggregate Functions: Group By, Sum, Min, Max etc.
- Condition: Case Statements
- Data Manipulation Statements

_NB: Since there are hundreds of records in the database, large query result will be limited to 5 rows._

**Exercises** 

Write SQL queries to perform the following tasks:

A. Count the number of student from each department. Sample output below...
| department | no_of_student |
|:----------:|:-------------:|
| Physics    |            26 |
| Nursing    |            55 |
| Psychology |            52 |
| Geology    |            55 |
| Economics  |            59 |

B. Which faculty has the highest number of student?

C. Count the number of students across each level in the faculty of science. Sort result by student level in ascending order.

D. Write sql query to assign a grade to each student's result. Use the format below as a guide.
|    score  |   grade   |
|:---------:|:----------|
| 100 - 70  |   A       |
| 69 - 60   |   B       |
| 59 - 45   |   C       |
| 44 - 0    |   F       |

Sample result below...
| profile_id | course_id | score | grade |
|:----------:|:---------:|:-----:|:-----:|
|          1 |         5 |    96 | A     |
|          1 |       139 |    77 | A     |
|          1 |       140 |    95 | A     |
|          1 |       141 |    58 | C     |
|          1 |       177 |    51 | C     |

E. Count the number of students across each grade. Sample result below...
| grade | number_of_students  |
|:-----:|:-------------------:|
| A     |                2056 |
| B     |                 696 |
| C     |                1037 |
| F     |                 357 |


F. Show all levels with one or more student across each department. Your result should follow the format below...
| department                      | available_levels        |
|:-------------------------------:|------------------------:|
| Adult Education                 | 100, 200, 300, 400, 500 |
| Biochemistry                    | 100, 200, 300, 400, 500 |
| Civil Engineering               | 100, 200, 300, 400, 500 |
| Communication and Language Arts | 100, 200, 300, 400, 500 |
| Computer Science                | 100, 200, 300, 400, 500 |

_NB: `available_levels need not be sorted`._

Solution can be found [here](https://github.com/Oyebamiji-Micheal/SQLite-with-Python/blob/main/basic_crud.py).

<br>

<a id='joins'></a>

<h3>Joins</h3>

In the last section, I was able to use common SQL functions, clauses and statements. This section however focuses primarily on joins and this include

- Inner Join
- Left Join
- Right Join


_NB: The data is generated in such a way that all students who wrote an exam have a corresponding score._ 

_Large query result will be limited to 5 rows._

**Exercises**

Write SQL queries to perform the following tasks:

A. How many students wrote 'GES101' exam? Sample result below...


| course_code | course_description | no_of_students |
|:-----------:|:------------------:|---------------:|
| GES101      | Use of English I   |            197 |


B. Show all students from the faculty of science who wrote 'GES101' exam? Sample result below...

| course_code | course_description | faculty | department   | student_name    | current_level | score |
|:-----------:|:------------------:|--------:|-------------:|:---------------:|--------------:|:-----:|
| GES101      | Use of English I   | Science | Physics      | Rose Vang       |           100 |    96 |
| GES101      | Use of English I   | Science | Mathematics  | Orlando Barker  |           100 |    76 |
| GES101      | Use of English I   | Science | Mathematics  | Amira Pitts     |           100 |    85 |
| GES101      | Use of English I   | Science | Microbiology | Alivia Travis   |           100 |    64 |
| GES101      | Use of English I   | Science | Mathematics  | Gideon Arellano |           100 |    63 |


C. Show all students from the faculty of Technology who wrote 'GES201' exam? Sample result below...

| course_code | course_description | faculty | department   | student_name    | current_level | score |
|:-----------:|:------------------:|--------:|-------------:|:---------------:|--------------:|:-----:|
| GES201| Use of English II  | Technology | Mechanical Engineering | Jimena Conway     |200 |    78 |
| GES201| Use of English II  | Technology | Civil Engineering      | Lola Weber        |200 |    83 |
| GES201| Use of English II  | Technology | Civil Engineering      | Alijah Washington |200 |    86 |
| GES201| Use of English II  | Technology | Mechanical Engineering | Avianna Avery     |200 |    54 |
| GES201| Use of English II  | Technology | Civil Engineering      | Lina Shannon      |200 |    94 |


D. Display the total number of courses offered by all departments in the faculty of arts across all levels. Note that students wrote corresponding exam for each course they offer. Sample result below...

| department                      | current_level | number_of_courses  |
|:-------------------------------:|:-------------:|-------------------:|
| Communication and Language Arts |           100 |                  5 |
| Communication and Language Arts |           200 |                  5 |
| Communication and Language Arts |           300 |                  4 |
| Communication and Language Arts |           400 |                  4 |
| History                         |           100 |                  5 |


E. Display the highest score in each course relative to statistics department, 100 level. Sample result below 

| department | course_code | course_description                   | maximum_score |
|:----------:|:-----------:|:------------------------------------:|:-------------:|
| Statistics |         100 | Use of English I                     |            78 |
| Statistics |         100 | Introduction to Programming          |            82 |
| Statistics |         100 | Algebra                              |            80 |
| Statistics |         100 | Introduction to Probability Theory I |            87 |
| Statistics |         100 | Introductory Heat and Thermodynamics |            77 |


F. Perhaps some students' exam records have not been updated i.e. not present in the table. Display students with no results. Sample result below...

| student_name      | faculty | department                             | course_id | score |
|:----------:|:-----------:|:------------------------------------:|:-------------:|:------:|
| Jimmy Wang        |     500 | Nursing                                |      NULL |  NULL |
| Kennedi Cooper    |     500 | Mathematics                            |      NULL |  NULL |
| Jonathan Lim      |     500 | Electrical and Electronics Engineering |      NULL |  NULL |
| Remington Wiggins |     500 | Civil Engineering                      |      NULL |  NULL |
| Livia Blackwell   |     500 | Communication and Language Arts        |      NULL |  NULL |

Solution can be found [here](https://github.com/Oyebamiji-Micheal/SQLite-with-Python/blob/main/joins.py).