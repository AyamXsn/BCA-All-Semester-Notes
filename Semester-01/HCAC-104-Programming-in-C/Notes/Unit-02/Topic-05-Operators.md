# Topic 5: Operators

**Unit II | HCAC-104 Programming in C**

## 1. Introduction

An **operator** is a symbol that tells the compiler to perform an operation on values. The values are called **operands**. An **expression** combines operands and operators, such as `a + b * 2`.

By number of operands: **unary** (one), **binary** (two) and **ternary** (three).

## 2. Arithmetic Operators

| Operator | Meaning | Example (`a = 17, b = 5`) | Result |
|---|---|---|---|
| `+` | Addition | `a + b` | 22 |
| `-` | Subtraction | `a - b` | 12 |
| `*` | Multiplication | `a * b` | 85 |
| `/` | Division | `a / b` | 3 (integer division) |
| `%` | Remainder (modulus) | `a % b` | 2 |

- Dividing two integers gives an integer: `17 / 5` is `3`, not `3.4`.
- `%` works only with integers.
- Division or modulus by zero is undefined; always check.

## 3. Relational Operators

They compare two values and give **1 (true)** or **0 (false)**.

| Operator | Meaning |
|---|---|
| `<` | less than |
| `>` | greater than |
| `<=` | less than or equal to |
| `>=` | greater than or equal to |
| `==` | equal to |
| `!=` | not equal to |

Common mistake: `=` assigns, `==` compares.

## 4. Logical Operators

| Operator | Name | Result |
|---|---|---|
| `&&` | AND | true only if both operands are true |
| `\|\|` | OR | true if at least one operand is true |
| `!` | NOT | reverses true/false |

Truth table:

| A | B | A && B | A \|\| B | !A |
|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 1 |
| 0 | 1 | 0 | 1 | 1 |
| 1 | 0 | 0 | 1 | 0 |
| 1 | 1 | 1 | 1 | 0 |

In C any non-zero value is true. `&&` and `||` use **short-circuit evaluation**: in `a && b`, if `a` is false, `b` is not evaluated.

## 5. Increment and Decrement Operators

| Form | Name | Effect |
|---|---|---|
| `++a` | Prefix increment | increase `a` first, then use the value |
| `a++` | Postfix increment | use the value, then increase `a` |
| `--a` | Prefix decrement | decrease first, then use |
| `a--` | Postfix decrement | use, then decrease |

```c
int a = 5;
int x = a++;   /* x = 5, a = 6 */
int y = ++a;   /* a = 7, y = 7 */
```

Avoid changing the same variable twice in one expression (for example `a = a++ + ++a;`); the result is undefined.

Tested demonstration: [Program 07](../../Programs/Program-07-Increment-and-Decrement-Operators/README.md).

## 6. Assignment Operators

| Operator | Example | Same as |
|---|---|---|
| `=` | `a = 5` | store 5 in `a` |
| `+=` | `a += 3` | `a = a + 3` |
| `-=` | `a -= 3` | `a = a - 3` |
| `*=` | `a *= 3` | `a = a * 3` |
| `/=` | `a /= 3` | `a = a / 3` |
| `%=` | `a %= 3` | `a = a % 3` |

## 7. Bitwise Operators

They work on individual **bits** of integers.

| Operator | Meaning | `a = 12` (1100), `b = 10` (1010) |
|---|---|---|
| `&` | AND | `a & b` = 8 (1000) |
| `\|` | OR | `a \| b` = 14 (1110) |
| `^` | XOR (1 when bits differ) | `a ^ b` = 6 (0110) |
| `~` | NOT (flip all bits) | `~a` flips every bit |
| `<<` | Left shift | `a << 2` = 48 (multiplies by 4) |
| `>>` | Right shift | `a >> 1` = 6 (divides by 2) |

Tested demonstration: [Program 08](../../Programs/Program-08-Bitwise-Operators/README.md).

## 8. Conditional (Ternary) Operator

```c
variable = (condition) ? value_if_true : value_if_false;
```

```c
int larger = (a > b) ? a : b;
```

It is a compact form of `if-else` for simple choices. Tested: [Program 10](../../Programs/Program-10-Conditional-Operator/README.md).

## 9. Comma Operator

The comma operator evaluates its left operand, discards it, then evaluates the right operand and gives that value.

```c
int a, b;
b = (a = 3, a + 2);   /* a = 3 first, then b = 5 */
```

It is most often seen in `for` loops: `for (i = 0, j = 9; i < j; i++, j--)`.

(Note: the commas separating declarations or function arguments are not comma operators.)

## 10. Other Operators

| Operator | Use |
|---|---|
| `sizeof` | Size in bytes of a type or variable |
| `&` (unary) | Address of a variable |
| `*` (unary) | Value at an address (pointers) |
| `.` and `->` | Structure member access |
| `[]` and `()` | Array subscript and function call |

## 11. Precedence and Associativity

Higher rows are evaluated first. Operators on the same row use the stated associativity.

| Level | Operators | Associativity |
|---|---|---|
| 1 | `()` `[]` `.` `->` postfix `++` `--` | left to right |
| 2 | prefix `++` `--`, unary `+` `-`, `!`, `~`, cast, `*`, `&`, `sizeof` | right to left |
| 3 | `*` `/` `%` | left to right |
| 4 | `+` `-` | left to right |
| 5 | `<<` `>>` | left to right |
| 6 | `<` `<=` `>` `>=` | left to right |
| 7 | `==` `!=` | left to right |
| 8 | `&` | left to right |
| 9 | `^` | left to right |
| 10 | `\|` | left to right |
| 11 | `&&` | left to right |
| 12 | `\|\|` | left to right |
| 13 | `?:` | right to left |
| 14 | `=` `+=` `-=` etc. | right to left |
| 15 | `,` | left to right |

**Example.** `x = 2 + 3 * 4 - 6 / 2;`
1. `3 * 4 = 12` and `6 / 2 = 3` (level 3, left to right)
2. `2 + 12 - 3`: left to right gives `14 - 3 = 11`
3. `x = 11`

Use parentheses to make the order obvious.

## 12. Tested Programs

[06 Arithmetic and Relational](../../Programs/Program-06-Arithmetic-and-Relational-Operators/README.md) | [09 Logical](../../Programs/Program-09-Logical-Operators/README.md)

## 13. Exam-Oriented Answers

### 5-mark: Explain the arithmetic operators with examples.
Operator table, note on integer division and `%`, and a short example `17 / 5 = 3`, `17 % 5 = 2`.

### 5-mark: Differentiate between prefix and postfix increment.
Use the table in section 5 and the example with `x` and `y`.

### 5-mark: Explain the bitwise operators.
The table in section 7 with the 12 and 10 example.

### 10-mark: Explain the operators of C with examples.
Classify into arithmetic, relational, logical, increment/decrement, assignment, bitwise, conditional and comma operators. Give a table and an example for each, then the precedence table, then one worked expression.

## 14. Summary

C has arithmetic, relational, logical, increment/decrement, assignment, bitwise, conditional and comma operators. Precedence and associativity decide the order of evaluation. Relational and logical operators produce 1 or 0.

---

[Previous: Type Conversion, Input and Output](Topic-04-Type-Conversion-and-Input-Output.md) | [Back to Unit Introduction](Introduction.md)
