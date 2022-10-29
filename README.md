<h1>SQLite with Python</h1>

<h2>Getting started with SQLite in Python</h2>

This repository contains what I learned with respect to SQLite in Python. However, a few units of energy was expended on integrating SQLite with Jupyter notebook.

Below have I offered in broad strokes the concepts learned in the long run...

Table of Contents

- [Installation and Setup](#setup)
- [Defining Database Schema](#schema)

<a id='setup'></a>

<h3>Installation and Setup</h3>

Python 3.10.6 was used at the time of documenting this whole thing. SQLite by default comes with Python. Hence unlike MySQL there won't be much of a installation.

<a id='schema'></a>

<h3>Defining Database Schema<h3>

At the moment there isn't a database readily available to connect to. So a new one named, `result.db` was created, and will be used throughout this scope.

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

_database schema definition queries can be found in [define_schema.py]()_
