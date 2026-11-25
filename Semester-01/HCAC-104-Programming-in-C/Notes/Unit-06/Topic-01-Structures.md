# Topic 1: Structures

**Unit VI | HCAC-104 Programming in C**

## 1. Introduction

### 1.1 Definition
A **structure** is a user-defined data type that groups variables of **different data types** under one name. Each variable inside is a **member** (or field).

### 1.2 Why Structures?
A student has a roll number (`int`), a name (`char` array) and marks (`float`). Keeping them in three separate variables is untidy; a structure keeps one student's data together.

## 2. Defining a Structure

```c
struct Student {
    int   roll;
    char  name[50];
    float marks;
};                      /* the semicolon is required */
```

This defines a **new type** `struct Student`; it reserves no memory yet.

## 3. Declaring Variables

```c
struct Student s1, s2;                 /* after the definition */

struct Point { int x, y; } p1, p2;     /* together with the definition */
```

With `typedef` the keyword `struct` can be dropped:

```c
typedef struct {
    int roll;
    float marks;
} Student;

Student s3;
```

## 4. Initialization

```c
struct Student s1 = {1, "Sita", 78.5f};          /* in member order */
struct Student s2 = {.roll = 2, .marks = 60.0f}; /* designated (C99); name becomes empty */
```

## 5. Accessing Members: The Dot Operator

```c
s1.roll = 5;
s1.marks += 5;
strcpy(s1.name, "Hari");          /* strings need strcpy, not = */
printf("%s %d\n", s1.name, s1.roll);
```

Important: a `char` array member cannot be assigned with `=`; use `strcpy` or `scanf`/`fgets`.

Whole structures **can** be copied: `s2 = s1;` copies every member.

Tested: [Program 39: Student Structure](../../Programs/Program-39-Student-Structure/README.md).

## 6. Memory of a Structure

Members are stored one after another, but the compiler may insert **padding** bytes for alignment, so `sizeof(struct)` can be larger than the sum of the member sizes. Always use `sizeof`.

## 7. Nested Structures

A structure may contain another structure.

```c
struct Date { int day, month, year; };
struct Person {
    char name[30];
    struct Date dob;            /* nested structure */
};

struct Person p;
p.dob.year = 2005;
```

## 8. Array vs Structure

| Basis | Array | Structure |
|---|---|---|
| Element types | All the same | Can differ |
| Access | By index `a[i]` | By member name `s.roll` |
| Keyword | None | `struct` |
| Memory | Contiguous, same size items | Members possibly padded |

## 9. Exam-Oriented Answers

### 5-mark: What is a structure? How is it defined and accessed?
Definition, syntax with the `Student` example, declaring variables, the dot operator, and an example program (Program 39).

### 5-mark: Differentiate between an array and a structure.
Use the table in section 8.

## 10. Summary

A structure groups related data of different types. Define it with `struct`, create variables from it, and access members with the dot operator.

---

[Back to Unit Introduction](Introduction.md) | [Next: Arrays of Structures, Functions and Pointers](Topic-02-Structures-Arrays-Functions-and-Pointers.md)
