# Practical Project: Student Record Manager

**Subject:** HCAC-104 Programming in C | **Official lab item:** "Project: a simple C application with input, processing, output and storage in an external file"

## What It Does

A menu-driven program that stores student records (roll number, name, marks) in a binary file, lists them, and searches by roll number. Records stay in `students.dat` after the program ends.

## Concepts Used

| Concept | Where | Notes |
|---|---|---|
| Structures | `struct Student` | [Unit VI](../../Notes/Unit-06/Topic-01-Structures.md) |
| Functions | `add_student`, `list_students`, `search_student`, `find_student` | [Unit IV](../../Notes/Unit-04/Topic-01-Function-Concept.md) |
| Loops and `switch` | Menu in `main` | [Unit III](../../Notes/Unit-03/Topic-02-Looping-Statements.md) |
| Binary file I/O | `fopen("ab"/"rb")`, `fwrite`, `fread` | [Unit VII](../../Notes/Unit-07/Topic-03-Formatted-Character-and-Direct-IO.md) |

## Logic

1. The menu repeats with a `do-while` loop until the user chooses 0.
2. Adding first checks the file for a duplicate roll number, then appends one record with `fwrite`.
3. Listing reads records one by one with `fread` until it returns something other than 1.
4. Searching reuses `find_student`, which scans the file.
5. Every `scanf` result and every `fopen` result is checked.

## Source Code

[student_records.c](student_records.c)

## Compile and Run

```bash
gcc -Wall -Wextra -std=c11 -o student_records student_records.c
./student_records
```

## Sample Runs

The sample input was supplied from a file, so it is not echoed in the captured output.

### Run 1: add two students, try a duplicate roll, then list

Typed by the user:

```text
1
1 Ram 70.5
1
2 Sita 88
1
1
2
0
```

Program output:

```text

1. Add student
2. List students
3. Search by roll
0. Exit
Choice: Roll: Name (one word): Marks: Saved.

1. Add student
2. List students
3. Search by roll
0. Exit
Choice: Roll: Name (one word): Marks: Saved.

1. Add student
2. List students
3. Search by roll
0. Exit
Choice: Roll: Roll 1 already exists.

1. Add student
2. List students
3. Search by roll
0. Exit
Choice: Roll   Name                 Marks
1      Ram                  70.5
2      Sita                 88.0
Total records: 2

1. Add student
2. List students
3. Search by roll
0. Exit
Choice: Goodbye.
```

Exit status: 0

### Run 2: start again in the same folder (data was saved), search and list

Typed by the user:

```text
3
2
3
9
2
0
```

Program output:

```text

1. Add student
2. List students
3. Search by roll
0. Exit
Choice: Roll to search: Found: 2 Sita 88.0

1. Add student
2. List students
3. Search by roll
0. Exit
Choice: Roll to search: Roll 9 not found.

1. Add student
2. List students
3. Search by roll
0. Exit
Choice: Roll   Name                 Marks
1      Ram                  70.5
2      Sita                 88.0
Total records: 2

1. Add student
2. List students
3. Search by roll
0. Exit
Choice: Goodbye.
```

Exit status: 0

## Testing Note

Compiled with `gcc (Ubuntu 13.3.0-6ubuntu2~24.04.1) 13.3.0` using `-Wall -Wextra -std=c11 -pedantic` with no warnings. Both runs above were executed in one folder, so Run 2 really read the file created by Run 1.

## Limitations

- Names are one word only; there is no edit or delete option.
- The binary file depends on the system's structure layout, so it is not portable between machines.

---

[Back to subject](../../README.md)
