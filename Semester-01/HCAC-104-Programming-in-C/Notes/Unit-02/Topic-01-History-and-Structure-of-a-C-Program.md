# Topic 1: History of C and Structure of a C Program

**Unit II | HCAC-104 Programming in C**

## 1. Introduction

C is a general-purpose, procedural programming language. It is used for operating systems, compilers, embedded systems and many other programs where speed and control over hardware matter. It is also the foundation for C++, Java and many other languages, which is why it is taught first.

## 2. History of C

| Year (approx.) | Event |
|---|---|
| 1960s | **BCPL** is designed by Martin Richards. |
| 1969-70 | **B** is created by Ken Thompson at Bell Laboratories, based on BCPL. |
| 1972 | **C** is developed by **Dennis Ritchie** at Bell Laboratories, mainly to write the UNIX operating system. |
| 1978 | Kernighan and Ritchie publish *The C Programming Language*; this version is called **K&R C**. |
| 1989 | The American National Standards Institute standardises the language: **ANSI C** (C89). |
| 1990 | Adopted by ISO as **C90**. |
| 1999 | **C99** adds `//` comments, `long long`, declarations anywhere in a block and more. |
| 2011 and later | **C11** and **C17** add further features (such as multithreading support). |

### 2.1 Why C Became Popular

1. Small, simple set of keywords.
2. Fast, because it is close to the machine.
3. Portable: the same program can be compiled on different computers.
4. Supports low-level operations (pointers, bit operations) as well as high-level structure (functions).
5. Rich library of ready-made functions.

### 2.2 Features, Advantages and Disadvantages

| Advantages | Disadvantages |
|---|---|
| Fast and efficient | No built-in support for object-oriented programming |
| Portable and widely supported | No automatic bounds checking on arrays |
| Structured programming with functions | Manual memory management can cause errors |
| Low-level access with pointers | Less safe for beginners than modern languages |

## 3. Basic Structure of a C Program

A C program is made of the following sections. Only `main()` is mandatory.

| # | Section | Purpose | Required? |
|---|---|---|---|
| 1 | Documentation | Comments describing the program | Optional |
| 2 | Link | `#include` lines that bring in header files | Needed when library functions are used |
| 3 | Definition | `#define` symbolic constants and macros | Optional |
| 4 | Global declaration | Variables and function prototypes visible to all functions | Optional |
| 5 | `main()` function | Where execution starts | **Required** |
| 6 | Sub-programs | Other user-defined functions | Optional |

```c
/* Documentation: program to print a greeting */
#include <stdio.h>                 /* link section */

#define COLLEGE "RJU BCA"          /* definition section */

void greet(void);                  /* global declaration (prototype) */

int main(void)                     /* main function */
{
    greet();
    return 0;
}

void greet(void)                   /* sub-program */
{
    printf("Welcome to %s\n", COLLEGE);
}
```

The complete, tested version is [Program 02](../../Programs/Program-02-Basic-Structure-of-a-C-Program/README.md).

### 3.1 Line-by-Line Explanation

- `#include <stdio.h>`: asks the preprocessor to insert the standard input/output header, which declares `printf` and `scanf`.
- `int main(void)`: every program starts executing here. `int` means it returns an integer to the operating system.
- `{ ... }`: braces enclose the body of a function.
- `printf(...)`: prints text on the screen.
- `return 0;`: tells the operating system the program ended successfully.
- `;`: every statement ends with a semicolon.

### 3.2 Compile and Run

```text
Source code (hello.c) --> compiler --> object code --> linker --> executable (hello)
```

```bash
gcc hello.c -o hello
./hello
```

## 4. Important Rules

1. C is **case-sensitive**: `Main` and `main` are different.
2. Execution always begins at `main()`.
3. Statements end with `;`.
4. Blocks use `{` and `}`.
5. Every variable must be declared before use.

## 5. Exam-Oriented Answers

### 5-mark: Explain the basic structure of a C program.

**Introduction.** A C program is organised into a fixed set of sections so that code is readable and easy to maintain.

**Sections.**
1. *Documentation section:* comments giving the program's name and purpose.
2. *Link section:* `#include` statements that link header files such as `stdio.h`.
3. *Definition section:* symbolic constants created with `#define`.
4. *Global declaration section:* global variables and function prototypes usable in all functions.
5. *main() function section:* execution starts here; it contains declarations and executable statements inside braces.
6. *Sub-program section:* user-defined functions called from `main()`.

**Example.** Use the greeting program above.

**Conclusion.** Only `main()` is compulsory, but following this layout produces well-organised programs.

### 5-mark: Write a short note on the history of C.

Write the table above in sentences: BCPL, B, C by Dennis Ritchie in 1972 at Bell Labs for UNIX, K&R C (1978), ANSI C (1989), C99, C11. Add two or three reasons for its popularity.

## 6. Summary

C was created by Dennis Ritchie in 1972 for UNIX and standardised as ANSI C in 1989. A C program has documentation, link, definition, global declaration, `main()` and sub-program sections, and execution always starts at `main()`.

---

[Back to Unit Introduction](Introduction.md) | [Next: Character Set, Tokens, Keywords and Comments](Topic-02-Character-Set-Tokens-Keywords-and-Comments.md)
