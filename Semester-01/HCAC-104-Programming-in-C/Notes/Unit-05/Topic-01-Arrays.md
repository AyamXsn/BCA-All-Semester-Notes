# Topic 1: Arrays

**Unit V | HCAC-104 Programming in C**

## 1. Introduction

### 1.1 Definition
An **array** is a collection of elements of the **same data type** stored in **contiguous (adjacent) memory locations** and accessed by a common name and an index.

### 1.2 Why Arrays?
Storing 100 marks needs 100 variables without arrays. With an array, `int marks[100];` stores them all and a loop can process them.

### 1.3 Characteristics
1. All elements have the same type.
2. Elements are stored one after another in memory.
3. The index starts at **0**; the last index is `size - 1`.
4. The size is fixed when the array is declared.
5. Elements are accessed in constant time by index.

## 2. Declaration, Initialization and Access

```c
int marks[5];                       /* declaration: 5 integers, indexes 0..4 */
int a[5] = {10, 20, 30, 40, 50};    /* full initialization */
int b[5] = {1, 2};                  /* remaining elements become 0 */
int c[] = {5, 6, 7};                /* size 3 is deduced */

a[0] = 99;                          /* write */
printf("%d", a[2]);                 /* read: prints 30 */
```

Memory picture of `a` (addresses illustrative, `int` = 4 bytes):

```text
index :   0     1     2     3     4
value :  [99]  [20]  [30]  [40]  [50]
addr  :  1000  1004  1008  1012  1016
```

## 3. Reading and Printing with Loops

```c
int a[5], i;
for (i = 0; i < 5; i++)
    scanf("%d", &a[i]);
for (i = 0; i < 5; i++)
    printf("%d ", a[i]);
```

## 4. Important Warning: No Bounds Checking

C does not check that an index is valid. Writing `a[5]` for a 5-element array changes memory that does not belong to the array and causes unpredictable behaviour. Always keep the index in `0` to `size - 1` and validate user-supplied sizes.

## 5. Common Operations

| Operation | Idea |
|---|---|
| Sum / average | Add elements in a loop |
| Largest / smallest | Start with `a[0]` and compare |
| Search | Compare each element with the key (linear search) |
| Sort | Repeatedly compare and swap (for example bubble sort) |
| Reverse | Swap `a[i]` with `a[n-1-i]` for the first half |

Tested programs: [28 Sum, Average, Max, Min](../../Programs/Program-28-Array-Sum-Average-Max-Min/README.md) and [29 Bubble Sort](../../Programs/Program-29-Bubble-Sort/README.md).

### 5.1 Bubble Sort Idea

```text
64 25 12 22 11   pass 1 ->  25 12 22 11 64
                 pass 2 ->  12 22 11 25 64
                 pass 3 ->  12 11 22 25 64
                 pass 4 ->  11 12 22 25 64   sorted
```

## 6. Advantages and Disadvantages

| Advantages | Disadvantages |
|---|---|
| Fast access by index | Size is fixed |
| Simple to use with loops | Insertion and deletion in the middle are slow |
| Memory is contiguous | Same type only |
| Basis of strings and matrices | No bounds checking |

## 7. Exam-Oriented Answers

### 5-mark: What is an array? Explain declaration and initialization.
Definition, characteristics, the declaration and initialization forms, and a short example that reads and prints.

### 5-mark: Write a program to find the largest element of an array.
Use [Program 28](../../Programs/Program-28-Array-Sum-Average-Max-Min/README.md) with its sample output.

## 8. Summary

An array stores same-type elements contiguously and uses zero-based indexes. It is processed with loops, but its size is fixed and C does not guard against invalid indexes.

---

[Back to Unit Introduction](Introduction.md) | [Next: Multi-Dimensional Arrays](Topic-02-Multi-Dimensional-Arrays.md)
