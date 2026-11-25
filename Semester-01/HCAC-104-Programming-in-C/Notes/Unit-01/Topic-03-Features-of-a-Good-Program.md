# Topic 3: Features of a Good Program

**Unit I | HCAC-104 Programming in C**

## 1. Introduction

A program that merely "works once" is not necessarily a good program. A good program is one that other people (and you, months later) can read, trust, fix and extend. This is a frequent 5-mark topic, so learn the features and an example for each.

## 2. Important Features

### 2.1 Correctness
The program produces the right output for all valid inputs, including special cases. Example: a program that finds the largest of three numbers must also work when two numbers are equal.

### 2.2 Readability
The code is easy to read. This comes from meaningful variable names (`total_marks`, not `x`), consistent indentation and spacing.

### 2.3 Documentation (Comments)
Comments explain *why* the code does something and what each part is for. Good comments help maintenance and teamwork.

### 2.4 Efficiency
The program uses reasonable time and memory. A solution that finishes quickly and wastes little memory is preferred.

### 2.5 Modularity
The program is split into small, separate parts (functions), each doing one job. This makes testing and reuse easier.

### 2.6 Robustness
The program handles wrong or unexpected input without crashing. Example: refusing to divide by zero and showing a clear message instead.

### 2.7 Portability
The program can run on different computers or operating systems with little or no change. Using standard C instead of compiler-specific features improves portability.

### 2.8 Maintainability and Extensibility
Fixing bugs and adding features is easy because the code is clean and modular.

### 2.9 User-Friendliness
Prompts and messages are clear, so the user knows what to enter and what the result means.

## 3. Example: Poor vs Good Style

Poor:

```c
int f(int a,int b){return a*b;}
```

Better:

```c
/* Returns the area of a rectangle. */
int rectangle_area(int length, int width)
{
    return length * width;
}
```

## 4. Quick Revision Table

| Feature | One-line meaning |
|---|---|
| Correctness | Gives the right answer |
| Readability | Easy to read |
| Documentation | Explained by comments |
| Efficiency | Saves time and memory |
| Modularity | Built from small functions |
| Robustness | Survives bad input |
| Portability | Runs on many systems |
| Maintainability | Easy to fix and extend |
| User-friendliness | Easy to use |

## 5. Summary

A good program is correct first, then readable, documented, modular, efficient, robust and portable. These qualities lower cost and effort in the long run.

## 6. Exam-Oriented Answers

### 5-mark: What are the features of a good program?
**Introduction.** A good program is correct, understandable and easy to maintain.
**Points.** Correctness, readability, documentation, efficiency, modularity, robustness, portability and maintainability, each with a one-line meaning (see the revision table).
**Example.** Show the poor and better `rectangle_area` code.
**Conclusion.** These features reduce long-term cost and effort.

---

[Previous: Programming Design Tools](Topic-02-Programming-Design-Tools.md) | [Next: Programming Techniques](Topic-04-Programming-Techniques.md)
