# Topic 4: Programming Techniques (Procedural, Modular, Object-Oriented)

**Unit I | HCAC-104 Programming in C**

## 1. Introduction

A **programming technique** (or paradigm) is a style of organising a program. The syllabus names three: procedural, modular and object-oriented programming. C supports the first two directly. Object-oriented programming is studied properly in C++ (HCAC-154) and Java.

## 2. Procedural Programming

### 2.1 Definition
A program is written as a sequence of instructions executed from top to bottom, using procedures (functions), loops and decisions. The focus is on **what steps to perform**.

### 2.2 Characteristics
1. Follows a top-down approach.
2. Data and the functions that work on it are separate.
3. Uses variables, conditions, loops and function calls.

### 2.3 Example (C)

```c
#include <stdio.h>

int main(void)
{
    int a = 4, b = 5;
    printf("Sum = %d\n", a + b);   /* Sum = 9 */
    return 0;
}
```

### 2.4 Advantages and Disadvantages

| Advantages | Disadvantages |
|---|---|
| Simple and easy to learn | Hard to manage as programs grow |
| Fast execution | Global data can be changed by any function |
| Good for small, direct tasks | Limited code reuse |

## 3. Modular Programming

### 3.1 Definition
A large program is divided into smaller, independent **modules** (functions or files). Each module does one specific job and can be developed and tested separately.

### 3.2 Characteristics
1. Divide and conquer: break a big problem into small ones.
2. Each module has a clear input and output.
3. Modules can be reused in other programs.

### 3.3 Example (C)

```c
#include <stdio.h>

int add(int x, int y)        /* module 1 */
{
    return x + y;
}

int multiply(int x, int y)   /* module 2 */
{
    return x * y;
}

int main(void)
{
    printf("%d %d\n", add(2, 3), multiply(2, 3));   /* 5 6 */
    return 0;
}
```

### 3.4 Advantages and Disadvantages

| Advantages | Disadvantages |
|---|---|
| Easier to test and debug | Needs careful planning of module interfaces |
| Reusable code | Too many tiny modules can add overhead |
| Team members can work in parallel | |

## 4. Object-Oriented Programming (OOP)

### 4.1 Definition
A program is built from **objects** that combine **data** (attributes) and the **functions** (methods) that operate on it. Objects are created from **classes**.

### 4.2 Main Ideas (introduction only)
- **Encapsulation:** data and methods bundled together.
- **Abstraction:** showing only essential details.
- **Inheritance:** a class reuses features of another class.
- **Polymorphism:** one name, many forms.

These are covered in detail in the C++ course.

### 4.3 Advantages and Disadvantages

| Advantages | Disadvantages |
|---|---|
| Models real-world things naturally | More concepts to learn |
| Strong reuse through inheritance | Can be slower and heavier for tiny tasks |
| Data is protected inside objects | Needs good design |

## 5. Comparison

| Basis | Procedural | Modular | Object-Oriented |
|---|---|---|---|
| Main focus | Sequence of steps | Splitting into modules | Objects (data + methods) |
| Data and functions | Separate | Separate, grouped by module | Bound together |
| Data security | Low | Moderate | High |
| Reuse | Low | Medium | High |
| Example languages | C, Pascal | C (with functions/files) | C++, Java |

## 6. Summary

Procedural programming focuses on steps, modular programming divides work into reusable parts, and object-oriented programming organises code around objects. Large real-world programs usually combine these ideas.

## 7. Exam-Oriented Answers

### 5-mark: Explain procedural, modular and object-oriented programming.
Give a definition, characteristics and a small advantage/disadvantage line for each, then the comparison table.

### 5-mark: Differentiate between procedural and object-oriented programming.
Use the rows "main focus", "data and functions", "data security" and "reuse" from the comparison table.

### 10-mark: Explain the programming techniques in detail with examples.
Cover all three techniques with the C examples (`Sum = 9` for procedural, the `add` and `multiply` modules for modular), the four OOP ideas, advantages and disadvantages tables, the comparison table and a conclusion that real programs combine techniques.

---

[Previous: Features of a Good Program](Topic-03-Features-of-a-Good-Program.md) | [Back to Unit Introduction](Introduction.md)
