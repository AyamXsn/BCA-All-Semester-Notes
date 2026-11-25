# Topic 1: Function Definition, Return and Prototype

**Unit IV | HCAC-104 Programming in C**

## 1. Introduction

### 1.1 Definition
A **function** is a named, self-contained block of code that performs one specific task and can be called whenever needed. `main()` is itself a function.

### 1.2 Why Use Functions?
1. **Reusability:** write once, call many times.
2. **Modularity:** a big problem is divided into small parts.
3. **Easier debugging and testing:** each function can be tested alone.
4. **Shorter, clearer programs.**
5. **Teamwork:** different people write different functions.

### 1.3 Types of Functions

| Type | Description | Examples |
|---|---|---|
| Library (built-in) functions | Provided by the compiler's libraries | `printf`, `sqrt`, `strlen` |
| User-defined functions | Written by the programmer | `add`, `factorial` |

## 2. Parts of a Function

### 2.1 Function Prototype (Declaration)
Tells the compiler the function's name, return type and parameter types **before** it is used.

```c
int add(int a, int b);     /* prototype ends with a semicolon */
```

Parameter names are optional in a prototype: `int add(int, int);`

### 2.2 Function Definition

```c
return_type function_name(parameter_list)
{
    declarations;
    statements;
    return value;     /* omitted when return type is void */
}
```

```c
int add(int a, int b)       /* a and b are formal parameters */
{
    return a + b;
}
```

### 2.3 Function Call

```c
int result = add(3, 4);     /* 3 and 4 are actual arguments */
```

| Term | Meaning |
|---|---|
| Formal parameters | Variables in the function definition |
| Actual arguments | Values supplied in the call |
| Return type | Type of the value sent back (`void` if none) |

## 3. The `return` Statement

- `return expression;` ends the function and sends a value to the caller.
- The value should match the return type.
- A `void` function may use plain `return;` to exit early.
- `main()` returns an `int`; `0` means success.

## 4. Categories of Functions

| Category | Arguments | Return value | Example |
|---|---|---|---|
| 1 | No | No | `void greet(void)` |
| 2 | Yes | No | `void print_square(int n)` |
| 3 | No | Yes | `int read_default(void)` |
| 4 | Yes | Yes | `int add(int a, int b)` |

All four forms are shown in the tested [Program 22](../../Programs/Program-22-Function-Types/README.md).

## 5. Why the Prototype Matters

If a function is defined **after** `main()`, the prototype lets the compiler check the calls in `main()`. Without it, the compiler cannot verify the argument types and may report an error or warn about an implicit declaration.

## 6. Local and Global Variables (Brief)

Variables declared inside a function are **local** to it and disappear when it ends. Variables declared outside every function are **global** and visible to all functions below. Prefer parameters and return values to global variables.

## 7. Exam-Oriented Answers

### 5-mark: What is a function? Explain its advantages and syntax.
Definition, the five advantages, syntax of definition, prototype and call, and the `add` example.

### 5-mark: Explain function prototype, definition and call.
Describe each part with its syntax and the formal/actual parameter table.

### 10-mark: Explain the types and categories of functions in C with examples.
Library vs user-defined; four categories with a code example each (Program 22); prototype and return rules; advantages; conclusion.

## 8. Summary

A function is a reusable named block. A prototype declares it, a definition implements it and a call executes it. Functions are grouped by whether they take arguments and return values.

---

[Back to Unit Introduction](Introduction.md) | [Next: Call by Value and Call by Reference](Topic-02-Call-by-Value-and-Call-by-Reference.md)
