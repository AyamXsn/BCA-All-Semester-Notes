# Topic 2: Call by Value and Call by Reference

**Unit IV | HCAC-104 Programming in C**

## 1. Introduction

When a function is called, the arguments can be passed in two ways. The difference decides whether the function can change the caller's variables.

## 2. Call by Value

### 2.1 Definition
The **value** of each actual argument is copied into the formal parameter. The function works on the copy, so the original variable is **not** changed.

### 2.2 Example

```c
void swap_value(int a, int b)
{
    int temp = a;
    a = b;
    b = temp;
}
/* swap_value(x, y) leaves x and y unchanged */
```

Tested output of [Program 23](../../Programs/Program-23-Call-by-Value-Swap/README.md): inside the function the copies are swapped, but `x` and `y` in `main()` keep their values.

## 3. Call by Reference

### 3.1 Definition
The **address** of the variable is passed (using `&`) and the function receives a pointer. Through the pointer, the function can read and change the original variable.

(Strictly, C passes everything by value; passing a pointer by value achieves the effect of call by reference.)

### 3.2 Example

```c
void swap_ref(int *a, int *b)
{
    int temp = *a;
    *a = *b;
    *b = temp;
}
/* call: swap_ref(&x, &y); */
```

Tested: [Program 24](../../Programs/Program-24-Call-by-Reference-Swap/README.md).

## 4. How They Work in Memory

```text
Call by value                    Call by reference
main:   x = 10   y = 20          main:   x = 10 (addr 100)   y = 20 (addr 104)
swap:   a = 10   b = 20          swap:   a = 100             b = 104   (pointers)
        (separate copies)                *a is x, *b is y   (same memory)
```

(Addresses above are illustrative.)

## 5. Comparison

| Basis | Call by value | Call by reference |
|---|---|---|
| What is passed | Copy of the value | Address of the variable |
| Formal parameters | Ordinary variables | Pointers |
| Original variable changed? | No | Yes |
| Call syntax | `f(x)` | `f(&x)` |
| Extra memory | Copy needed | Only an address |
| Safety | Safer, original protected | Function can modify original |
| Typical use | Calculations returning one result | Returning several results, swapping, large data |

## 6. Returning More Than One Value

A function returns only one value, but with pointers it can fill several variables:

```c
void min_max(int a, int b, int *min, int *max)
{
    if (a < b) { *min = a; *max = b; }
    else       { *min = b; *max = a; }
}
```

## 7. Arrays Are Different

An array name passed to a function becomes a pointer to its first element, so the function can modify the original array. See [Unit V, Topic 5](../Unit-05/Topic-05-Pointers-Arrays-and-Functions.md).

## 8. Exam-Oriented Answers

### 5-mark: Differentiate between call by value and call by reference.
Reproduce the comparison table in sentences, then add the two swap examples.

### 10-mark: Explain call by value and call by reference with a swapping program.
Definitions, both swap programs, the memory diagram, the outputs from Programs 23 and 24, the comparison table and a conclusion.

## 9. Summary

Call by value copies the data and protects the original; call by reference passes addresses so the function can change the original. Use pointers when a function must modify caller variables.

---

[Previous: Function Concept](Topic-01-Function-Concept.md) | [Next: Recursion](Topic-03-Recursion.md)
