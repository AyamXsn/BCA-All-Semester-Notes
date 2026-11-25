# Topic 3: Variables, Constants and Data Types

**Unit II | HCAC-104 Programming in C**

## 1. Variables

### 1.1 Definition
A **variable** is a named memory location whose value can change while the program runs.

### 1.2 Declaration, Initialization and Assignment

```c
int age;            /* declaration: reserves memory */
age = 20;           /* assignment: stores a value  */
float price = 99.5f;  /* declaration with initialization */
int a = 1, b = 2, c;  /* several variables in one statement */
```

- A variable must be **declared before it is used**.
- An uninitialized local variable holds an unpredictable (garbage) value. Always initialize.
- Naming follows the identifier rules from [Topic 2](Topic-02-Character-Set-Tokens-Keywords-and-Comments.md).

### 1.3 Scope in Brief

| Kind | Declared | Visible |
|---|---|---|
| Local variable | Inside a function or block | Only in that function or block |
| Global variable | Outside all functions | In every function below the declaration |

## 2. Constants

### 2.1 Definition
A **constant** is a value that does not change during execution.

### 2.2 Types of Constants

| Type | Examples |
|---|---|
| Integer constant | `25`, `-7`, `0x1F` (hexadecimal), `017` (octal) |
| Real (floating) constant | `3.14`, `-0.5`, `2.5e3` |
| Character constant | `'A'`, `'5'`, `'\n'` |
| String constant | `"Nepal"` |

### 2.3 Ways to Create Named Constants

```c
#define PI 3.14159          /* symbolic constant (preprocessor, no semicolon) */
const int MAX_MARKS = 100;  /* const qualifier: a typed, read-only variable   */
```

| Basis | `#define` | `const` |
|---|---|---|
| Handled by | Preprocessor (text replacement) | Compiler |
| Has a data type | No | Yes |
| Uses memory | No | Yes |
| Ends with `;` | No | Yes |

## 3. Data Types

### 3.1 Definition
A **data type** tells the compiler what kind of value a variable holds, how much memory it needs and which operations are allowed.

### 3.2 Classification

| Category | Types |
|---|---|
| Primary (basic) | `int`, `char`, `float`, `double`, `void` |
| Derived | Array, pointer, function |
| User-defined | `struct`, `union`, `enum`, `typedef` |

### 3.3 Basic Data Types and Modifiers

The sizes below are **typical** on modern systems. The C standard only guarantees minimum ranges, so use `sizeof` to find the real size on your machine.

| Type | Typical size | Typical range | Format specifier |
|---|---|---|---|
| `char` | 1 byte | -128 to 127 (or 0 to 255) | `%c` |
| `unsigned char` | 1 byte | 0 to 255 | `%c`, `%u` |
| `short` | 2 bytes | -32,768 to 32,767 | `%hd` |
| `int` | 4 bytes | -2,147,483,648 to 2,147,483,647 | `%d` |
| `unsigned int` | 4 bytes | 0 to 4,294,967,295 | `%u` |
| `long` | 4 or 8 bytes | system dependent | `%ld` |
| `long long` | 8 bytes | about -9.2 x 10^18 to 9.2 x 10^18 | `%lld` |
| `float` | 4 bytes | about 6 to 7 decimal digits of precision | `%f` |
| `double` | 8 bytes | about 15 decimal digits of precision | `%lf` (in `scanf`), `%f` (in `printf`) |
| `long double` | 8, 12 or 16 bytes | extended precision | `%Lf` |

**Modifiers:** `signed`, `unsigned`, `short`, `long` change the size or the sign of a basic type. `void` means "no value" (for functions that return nothing, and for generic pointers).

### 3.4 The `sizeof` Operator

```c
#include <stdio.h>

int main(void)
{
    printf("int    : %zu bytes\n", sizeof(int));
    printf("double : %zu bytes\n", sizeof(double));
    return 0;
}
```

On a typical 64-bit system this prints 4 and 8.

### 3.5 Choosing a Type

| Need | Use |
|---|---|
| Counting, whole numbers | `int` |
| Very large whole numbers | `long long` |
| A single letter | `char` |
| Money, measurements with decimals | `double` |
| Memory-saving approximate decimals | `float` |

## 4. Worked Example

[Program 04](../../Programs/Program-04-Area-and-Circumference-of-Circle/README.md) uses a symbolic constant `PI`, a `double` variable for the radius, and prints the result with `%.2f`.

## 5. Exam-Oriented Answers

### 5-mark: What is a variable? How is it declared? Write the rules for naming it.
Give the definition, the declaration syntax `data_type variable_name;`, initialization, the identifier rules, and an example with output-free code.

### 5-mark: Explain the data types of C.
**Introduction.** A data type specifies the kind of data a variable can hold.
**Types.** Primary (`int`, `char`, `float`, `double`, `void`), derived (array, pointer, function), user-defined (`struct`, `union`, `enum`).
**Details.** Add the table of sizes and format specifiers.
**Conclusion.** Choosing the right type saves memory and avoids errors.

### 5-mark: Differentiate between `#define` and `const`.
Use the comparison table in section 2.3.

## 6. Summary

A variable is a named, changeable memory location; a constant is fixed. Data types decide memory size and meaning. Basic types are `int`, `char`, `float`, `double` and `void`, and modifiers adjust size and sign.

---

[Previous: Character Set, Tokens, Keywords and Comments](Topic-02-Character-Set-Tokens-Keywords-and-Comments.md) | [Next: Type Conversion, Input and Output](Topic-04-Type-Conversion-and-Input-Output.md)
