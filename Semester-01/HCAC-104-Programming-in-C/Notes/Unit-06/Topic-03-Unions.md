# Topic 3: Unions

**Unit VI | HCAC-104 Programming in C**

## 1. Introduction

### 1.1 Definition
A **union** is a user-defined data type like a structure, but **all members share the same memory location**. Only one member can hold a valid value at a time.

```c
union Data {
    int   i;
    float f;
    char  c;
};
```

The size of a union is the size of its **largest member** (plus any padding the compiler adds).

## 2. Using a Union

```c
union Data u;
u.i = 65;            /* u.i is valid */
u.f = 3.5f;          /* now u.f is valid; u.i is no longer meaningful */
```

Writing one member overwrites the others. Read only the member you wrote most recently.

Tested: [Program 43: Union Demo](../../Programs/Program-43-Union-Demo/README.md), which prints the size of a structure and a union with the same members.

## 3. Memory Picture

```text
struct S { int i; float f; char c; }     union U { int i; float f; char c; }

|  i (4) | f (4) | c (1 + padding) |      |  i / f / c share the same 4 bytes |
 separate memory for each member           one shared memory area
```

## 4. Structure vs Union

| Basis | Structure | Union |
|---|---|---|
| Keyword | `struct` | `union` |
| Memory | Each member has its own space | All members share one space |
| Size | At least the sum of the members (with padding) | Size of the largest member |
| Members usable at the same time | All | Only the last written |
| Initialization | All members may be initialized | Only the first member in the braces form |
| Typical use | Records (student, employee) | Saving memory when only one of several alternatives is needed |

## 5. Advantages and Disadvantages of Unions

| Advantages | Disadvantages |
|---|---|
| Saves memory | Only one member valid at a time |
| Useful for hardware registers and variant data | Easy to read the wrong member |
| Same data can be viewed in different ways | Less readable code |

## 6. Exam-Oriented Answers

### 5-mark: What is a union? Differentiate between structure and union.
Definition, syntax, the memory picture and the comparison table.

### 5-mark: Write a program to show that union members share memory.
Use [Program 43](../../Programs/Program-43-Union-Demo/README.md) and mention that sizes depend on the system.

### 10-mark: Explain structures and unions with examples.
Combine Topic 1 and Topic 3: definitions, syntax, access, an example program for each, memory pictures, the comparison table and a conclusion.

## 7. Summary

A union stores its members in one shared memory area, so it uses as much memory as its largest member but holds only one value at a time. A structure keeps all members separately.

---

[Previous: Arrays of Structures, Functions and Pointers](Topic-02-Structures-Arrays-Functions-and-Pointers.md) | [Back to Unit Introduction](Introduction.md)
