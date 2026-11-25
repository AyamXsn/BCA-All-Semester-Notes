# Topic 4: Type Conversion, Input and Output

**Unit II | HCAC-104 Programming in C**

## Part A: Type Conversion

### 1. Introduction
When an expression mixes different data types, C converts values so that the operation can be carried out. This is called **type conversion**. There are two kinds: implicit and explicit.

### 2. Implicit (Automatic) Conversion
The compiler converts types by itself. Two common cases:

1. **Integer promotion:** `char` and `short` values are converted to `int` before arithmetic.
2. **Usual arithmetic conversion:** in an operation with two different types, the "smaller" type is converted to the "larger" one. The rough order is:

```text
int  ->  unsigned int  ->  long  ->  long long  ->  float  ->  double  ->  long double
```

```c
int    i = 7;
double d = 2.5;
double r = i + d;      /* i becomes 7.0, so r = 9.5 */
int    t = 3.99;       /* assigning double to int truncates: t = 3 */
char   c = 'A';
int    code = c + 1;   /* 'A' is 65, so code = 66 */
```

Assigning a larger type to a smaller one (for example `double` to `int`) **loses** information; the fraction is cut off, not rounded.

### 3. Explicit Conversion (Type Casting)
The programmer forces a conversion with the cast operator `(type)`.

```c
int a = 7, b = 2;
printf("%d\n",  a / b);           /* 3   (integer division) */
printf("%.2f\n", (double)a / b);  /* 3.50 (a is converted first) */
```

Note: `(double)a / b` casts `a` only, but then `b` is automatically converted too. `(double)(a / b)` would be wrong here: the division happens first and gives 3.

### 4. Comparison

| Basis | Implicit | Explicit |
|---|---|---|
| Done by | Compiler | Programmer |
| Syntax | None | `(type) expression` |
| Purpose | Make mixed expressions work | Force a particular result |
| Risk | Silent loss of data | Programmer is responsible |

Tested demonstration: [Program 05](../../Programs/Program-05-Type-Conversion-Demo/README.md).

## Part B: Input and Output

### 5. Introduction
Most input/output functions are declared in `<stdio.h>`. The commonly used ones are:

| Purpose | Formatted | Unformatted |
|---|---|---|
| Output | `printf` | `putchar`, `puts` |
| Input | `scanf` | `getchar`, `fgets` |

### 6. `printf`

```c
printf("format string", value1, value2, ...);
```

**Format specifiers**

| Specifier | Prints |
|---|---|
| `%d` or `%i` | `int` |
| `%u` | `unsigned int` |
| `%ld`, `%lld` | `long`, `long long` |
| `%f` | `float` / `double` |
| `%c` | one character |
| `%s` | string |
| `%x` | hexadecimal |
| `%o` | octal |
| `%e` | scientific notation |
| `%%` | the `%` sign |

**Width and precision**

```c
printf("[%5d]\n",  42);      /* [   42]   width 5, right aligned  */
printf("[%-5d]\n", 42);      /* [42   ]   left aligned            */
printf("[%.2f]\n", 3.14159); /* [3.14]    2 decimal places        */
printf("[%8.3f]\n", 3.14159);/* [   3.142] width 8, 3 decimals    */
```

### 7. `scanf`

```c
scanf("format string", &variable1, &variable2, ...);
```

Key points:
1. Put `&` (address-of) before ordinary variables: `scanf("%d", &age);`.
2. For a string stored in a `char` array, no `&` is needed: `scanf("%49s", name);`.
3. Use `%lf` for `double`, `%f` for `float`.
4. `scanf` returns the number of values successfully read; check it to detect bad input.
5. `%s` stops at white space. To read a whole line use `fgets`.

```c
int n;
if (scanf("%d", &n) != 1) {
    printf("Invalid input.\n");
}
```

### 8. Character and String I/O

```c
char ch = getchar();      /* reads one character */
putchar(ch);              /* prints one character */

char line[100];
fgets(line, sizeof line, stdin);   /* reads a whole line, safe from overflow */
puts(line);                        /* prints a string and adds a new line */
```

The function `gets()` was removed from the C standard (C11) because it cannot limit input length and causes buffer overflows. Never use it.

### 9. Worked Example
[Program 03](../../Programs/Program-03-Sum-of-Two-Numbers/README.md) reads two integers with `scanf`, checks the return value and prints the sum.

## 10. Exam-Oriented Answers

### 5-mark: What is type conversion? Explain implicit and explicit conversion with examples.
Definition, the two kinds, one example each (`int + double`; `(double)a / b`), and the comparison table.

### 5-mark: Explain `printf()` and `scanf()` with examples.
Syntax, the format specifier table, the need for `&` in `scanf`, an example reading and printing a number.

### 10-mark: Explain formatted and unformatted input/output functions of C.
Include: the role of `stdio.h`; `printf` and `scanf` (syntax, specifiers, width/precision, return value); `getchar`, `putchar`, `fgets`, `puts`; why `gets` is unsafe; a complete example program with sample input and output (use Program 03).

## 11. Summary

Mixed-type expressions are converted automatically (implicit) or by a cast (explicit). `printf` and `scanf` are the main formatted I/O functions; use matching format specifiers, remember `&` in `scanf`, and check `scanf`'s return value.

---

[Previous: Variables, Constants and Data Types](Topic-03-Variables-Constants-and-Data-Types.md) | [Next: Operators](Topic-05-Operators.md)
