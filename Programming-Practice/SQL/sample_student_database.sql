-- SQLite-compatible standalone SQL practice script.
PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS Student (
    student_id INTEGER PRIMARY KEY,
    full_name TEXT NOT NULL,
    semester INTEGER NOT NULL CHECK (semester BETWEEN 1 AND 8)
);

CREATE TABLE IF NOT EXISTS Course (
    course_id INTEGER PRIMARY KEY,
    course_name TEXT NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS Enrollment (
    student_id INTEGER NOT NULL,
    course_id INTEGER NOT NULL,
    enrolled_on TEXT NOT NULL DEFAULT CURRENT_DATE,
    PRIMARY KEY (student_id, course_id),
    FOREIGN KEY (student_id) REFERENCES Student(student_id),
    FOREIGN KEY (course_id) REFERENCES Course(course_id)
);

INSERT INTO Student (student_id, full_name, semester)
VALUES (1, 'Example Student', 1);

INSERT INTO Course (course_id, course_name)
VALUES (101, 'Database Practice');

INSERT INTO Enrollment (student_id, course_id)
VALUES (1, 101);

SELECT s.full_name, c.course_name, e.enrolled_on
FROM Enrollment AS e
JOIN Student AS s ON s.student_id = e.student_id
JOIN Course AS c ON c.course_id = e.course_id;
