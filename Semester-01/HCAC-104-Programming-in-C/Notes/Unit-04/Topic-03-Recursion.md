# Topic 3: Recursion

**Unit IV | HCAC-104 Programming in C**

## 1. Introduction

### 1.1 Definition
**Recursion** is a technique in which a function calls **itself**, directly or indirectly, to solve a smaller version of the same problem.

### 1.2 Two Essential Parts
1. **Base case:** a simple situation answered directly; it stops the recursion.
2. **Recursive case:** the function calls itself with a **smaller** problem that moves toward the base case.

Without a reachable base case the calls never stop and the program crashes with a stack overflow.

## 2. Example: Factorial

Mathematical definition: `n! = n x (n-1)!` and `0! = 1! = 1`.

```c
unsigned long long fact(int n)
{
    if (n <= 1)
        return 1;                 /* base case */
    return n * fact(n - 1);       /* recursive case */
}
```

### 2.1 Tracing `fact(4)`

```text
fact(4) = 4 * fact(3)
              fact(3) = 3 * fact(2)
                            fact(2) = 2 * fact(1)
                                          fact(1) = 1   <- base case
              fact(2) = 2 * 1 = 2
              fact(3) = 3 * 2 = 6
fact(4) = 4 * 6 = 24
```

Tested: [Program 25](../../Programs/Program-25-Factorial-using-Recursion/README.md).

## 3. Example: Fibonacci

```c
long fib(int n)
{
    if (n == 0) return 0;
    if (n == 1) return 1;
    return fib(n - 1) + fib(n - 2);
}
```

Each call makes two more calls, so the work repeats and grows quickly for large `n`. Tested: [Program 26](../../Programs/Program-26-Fibonacci-using-Recursion/README.md).

## 4. Example: GCD by Euclid's Algorithm

```c
int gcd(int a, int b)
{
    if (b == 0)
        return a;
    return gcd(b, a % b);
}
```

Trace of `gcd(48, 18)`: `gcd(48,18)` -> `gcd(18,12)` -> `gcd(12,6)` -> `gcd(6,0)` -> **6**. Tested: [Program 27](../../Programs/Program-27-GCD-using-Recursion/README.md).

## 5. How Recursion Uses Memory

Each call gets its own **stack frame** holding its parameters and local variables. Frames are stacked while the calls go deeper and removed one by one as each call returns.

## 6. Recursion vs Iteration

| Basis | Recursion | Iteration (loops) |
|---|---|---|
| Mechanism | Function calls itself | `for`, `while`, `do-while` |
| Termination | Base case | Loop condition |
| Memory | Uses a stack frame per call | Uses fixed memory |
| Speed | Slower (call overhead) | Usually faster |
| Code | Short, natural for recursive problems | Often longer |
| Risk | Stack overflow if no base case | Infinite loop if no update |

## 7. Advantages and Disadvantages

| Advantages | Disadvantages |
|---|---|
| Shorter, cleaner code for problems such as factorial and trees | Uses more memory |
| Natural fit for self-similar problems | Slower because of repeated calls |
| Easier to prove correct by induction | Hard to debug for beginners |

## 8. Exam-Oriented Answers

### 5-mark: What is recursion? Explain with an example.
Definition, base and recursive case, the factorial function, the trace of `fact(4)`, and the conclusion.

### 5-mark: Differentiate between recursion and iteration.
Use the table in section 6.

### 10-mark: Explain recursion with programs for factorial, Fibonacci and GCD.
Definition and rules; the three functions; one trace; sample output from Programs 25 to 27; advantages and disadvantages; comparison with iteration.

## 9. Summary

A recursive function solves a problem by calling itself on a smaller input until it reaches a base case. It is elegant but uses extra stack memory, so choose it where it makes the solution clearer.

---

[Previous: Call by Value and Call by Reference](Topic-02-Call-by-Value-and-Call-by-Reference.md) | [Back to Unit Introduction](Introduction.md)
