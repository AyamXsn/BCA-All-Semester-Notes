# Topic 4: Pointers

**Unit V | HCAC-104 Programming in C**

## 1. Introduction

### 1.1 Definition
A **pointer** is a variable that stores the **memory address** of another variable.

Every variable lives at some address in memory. The **address-of operator `&`** gives that address, and the **dereference (indirection) operator `*`** accesses the value stored at an address.

```text
variable x : value 42, address 2000
pointer  p : value 2000   (p "points to" x)
```

## 2. Declaration, Assignment and Initialization

```c
int x = 42;
int *p;        /* declaration: p can hold the address of an int */
p = &x;        /* assignment: p now points to x                */
int *q = &x;   /* declaration with initialization              */
```

The `*` in a declaration means "pointer to"; the `*` in an expression means "value at".

```c
printf("%d", *p);   /* prints 42 */
*p = 99;            /* changes x to 99 */
```

Tested: [Program 35: Pointer Basics](../../Programs/Program-35-Pointer-Basics/README.md).

### 2.1 Pointer Types

A pointer has a type that matches what it points to: `int *`, `char *`, `float *`. The type tells the compiler how many bytes to read and how far to move in pointer arithmetic.

### 2.2 The NULL Pointer
A pointer that points to nothing is set to `NULL` (from `<stddef.h>` and others). Always initialize pointers; an uninitialized pointer holds a random address, and dereferencing it crashes the program.

```c
int *p = NULL;
if (p != NULL)
    printf("%d", *p);
```

### 2.3 Printing an Address

```c
printf("%p\n", (void *)&x);    /* value differs from run to run */
```

## 3. Pointer Arithmetic

Only a few operations are meaningful on pointers:

| Operation | Meaning |
|---|---|
| `p + n` | Address of the element `n` positions after `p` (moves `n * sizeof(*p)` bytes) |
| `p - n` | `n` positions before `p` |
| `p++`, `p--` | Move to the next or previous element |
| `p2 - p1` | Number of elements between two pointers into the same array |
| `p1 == p2`, `p1 < p2` | Compare addresses |

Not allowed: adding two pointers, multiplying or dividing pointers.

Example with `int *p` and `sizeof(int)` equal to 4: if `p` holds 1000, then `p + 1` is 1004 and `p + 3` is 1012.

Tested: [Program 36: Pointer Arithmetic and Arrays](../../Programs/Program-36-Pointer-Arithmetic-and-Arrays/README.md).

## 4. Uses of Pointers

1. Call by reference (changing caller variables).
2. Working with arrays and strings efficiently.
3. Returning more than one value from a function.
4. Dynamic memory (beyond this unit's syllabus).
5. Building data structures such as linked lists (later courses).

## 5. Advantages and Disadvantages

| Advantages | Disadvantages |
|---|---|
| Direct memory access, fast | Easy to misuse; wrong pointers crash programs |
| Efficient parameter passing | Harder for beginners |
| Needed for arrays, strings, data structures | Uninitialized or dangling pointers cause bugs |

## 6. Common Mistakes

| Mistake | Problem |
|---|---|
| Using a pointer before assigning an address | Undefined behaviour |
| Forgetting `&` when assigning: `p = x;` | Type error or wrong value |
| Confusing `p` and `*p` | Address vs value |
| Dereferencing `NULL` | Crash |

## 7. Exam-Oriented Answers

### 5-mark: What is a pointer? Explain declaration and initialization.
Definition, `&` and `*`, the syntax lines, the example with output 42 then 99, and the NULL pointer.

### 5-mark: Explain pointer arithmetic.
The operations table and the example with addresses 1000, 1004, 1012.

### 10-mark: Explain pointers with their operations, advantages and an example program.
Definition, memory picture, declaration, `&` and `*`, arithmetic, uses, advantages and disadvantages, and [Program 35](../../Programs/Program-35-Pointer-Basics/README.md) with output.

## 8. Summary

A pointer stores an address. Use `&` to get an address and `*` to reach the value. Pointer arithmetic moves in units of the pointed-to type. Always initialize pointers.

---

[Previous: Strings](Topic-03-Strings.md) | [Next: Pointers, Arrays and Functions](Topic-05-Pointers-Arrays-and-Functions.md)
