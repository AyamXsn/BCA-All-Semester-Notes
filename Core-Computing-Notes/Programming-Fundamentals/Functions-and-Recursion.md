# Functions and Recursion

## 1. Function
A function is a reusable unit of code that performs a task. It may accept parameters and return a result.

## 2. Benefits
Functions improve decomposition, reuse, testing, readability, and maintenance.

## 3. Parameters and arguments
A parameter appears in a function definition; an argument is the value supplied at a call. Languages differ in how arguments are passed and how objects are shared or copied.

## 4. Return values and scope
A return value sends a result to the caller. Scope determines where a name can be accessed. Local variables usually exist only within a function invocation.

## 5. Recursion
A recursive function calls itself on a smaller or simpler input. It needs:
- A base case that stops recursion.
- A recursive case that makes progress toward the base case.

Example:
```python
def factorial(n):
    if n < 0:
        raise ValueError("n must be non-negative")
    if n <= 1:
        return 1
    return n * factorial(n - 1)
```

## 6. Recursion versus iteration
Recursion can express tree and divide-and-conquer problems naturally, but uses call-stack space. Iteration often uses less stack space and can be more efficient for simple repetition.

## 7. Exercises
Write functions for prime checking, greatest common divisor, Fibonacci values, and list statistics. Compare recursive and iterative factorial.
