# Topic 2: Multi-Dimensional Arrays

**Unit V | HCAC-104 Programming in C**

## 1. Introduction

A **multi-dimensional array** is an array of arrays. The most common form is the **two-dimensional (2D) array**, which represents a table or matrix with rows and columns.

## 2. Two-Dimensional Arrays

### 2.1 Declaration and Initialization

```c
int m[2][3];                         /* 2 rows, 3 columns */
int a[2][3] = { {1, 2, 3},
                {4, 5, 6} };         /* row-wise initialization */
int b[][3]  = { {1, 2, 3}, {4, 5, 6} };  /* only the first size may be omitted */
```

Element `a[i][j]` is in row `i` and column `j` (both start at 0). Here `a[1][2]` is `6`.

```text
        col 0  col 1  col 2
row 0 :   1      2      3
row 1 :   4      5      6
```

### 2.2 Memory Layout
C stores 2D arrays in **row-major order**: the whole of row 0, then row 1, and so on.

### 2.3 Reading and Printing

```c
for (i = 0; i < 2; i++)
    for (j = 0; j < 3; j++)
        scanf("%d", &a[i][j]);

for (i = 0; i < 2; i++) {
    for (j = 0; j < 3; j++)
        printf("%4d", a[i][j]);
    printf("\n");
}
```

## 3. Matrix Operations

### 3.1 Addition
Both matrices must have the same size. `C[i][j] = A[i][j] + B[i][j]`. Tested: [Program 30](../../Programs/Program-30-Matrix-Addition/README.md).

### 3.2 Multiplication
If A is `m x n` and B is `n x p`, then C = A x B is `m x p`, and

```text
C[i][j] = A[i][0]*B[0][j] + A[i][1]*B[1][j] + ... + A[i][n-1]*B[n-1][j]
```

Example: row 1 of A = `1 2 3` and column 1 of B = `7 9 11` give `1*7 + 2*9 + 3*11 = 58`. Tested: [Program 31](../../Programs/Program-31-Matrix-Multiplication/README.md).

### 3.3 Transpose
`T[j][i] = A[i][j]`: rows become columns.

## 4. Three-Dimensional Arrays

`int cube[2][3][4];` is two tables of 3 rows and 4 columns. They are used less often and are processed with three nested loops.

## 5. Exam-Oriented Answers

### 5-mark: Explain two-dimensional arrays with declaration, initialization and an example.
Definition, the declaration forms, the row/column picture, and the read/print loops.

### 10-mark: Write a program to multiply two matrices and explain the logic.
State the size rule, give the formula, present [Program 31](../../Programs/Program-31-Matrix-Multiplication/README.md) with sample input and output, and explain the three nested loops.

## 6. Summary

A 2D array is a table accessed as `a[row][col]`, stored row by row. Matrix addition needs equal sizes; multiplication needs columns of A equal to rows of B.

---

[Previous: Arrays](Topic-01-Arrays.md) | [Next: Strings](Topic-03-Strings.md)
