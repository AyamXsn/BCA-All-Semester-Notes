# Topic 2: Character Set, Tokens, Keywords and Comments

**Unit II | HCAC-104 Programming in C**

## 1. Character Set

### 1.1 Definition
The **character set** is the collection of characters a C program is allowed to use. The compiler builds words, numbers and symbols from these characters.

### 1.2 Groups of Characters

| Group | Members |
|---|---|
| Letters | `A-Z`, `a-z` |
| Digits | `0-9` |
| Special characters | `+ - * / % = < > ! & \| ^ ~ ? : ; , . ' " ( ) [ ] { } # _ \ @ $` (some are used only in strings or comments) |
| White space | Blank space, horizontal tab, new line, form feed |

### 1.3 Escape Sequences
Some characters cannot be typed directly in text. C uses a backslash followed by a letter:

| Sequence | Meaning |
|---|---|
| `\n` | New line |
| `\t` | Horizontal tab |
| `\\` | Backslash |
| `\"` | Double quote |
| `\'` | Single quote |
| `\0` | Null character (end of a string) |
| `\a` | Alert (beep) |

## 2. Tokens

### 2.1 Definition
A **token** is the smallest meaningful unit of a C program. The compiler first splits the source code into tokens and then checks how they fit together.

### 2.2 Types of Tokens

| Token type | Description | Examples |
|---|---|---|
| Keywords | Reserved words with fixed meaning | `int`, `if`, `while` |
| Identifiers | Names given by the programmer | `total`, `student_age`, `main` |
| Constants | Fixed values | `10`, `3.14`, `'A'` |
| String literals | Text in double quotes | `"Hello"` |
| Operators | Symbols that perform operations | `+`, `*`, `==`, `&&` |
| Special symbols (punctuators) | Structure symbols | `( ) { } [ ] ; , #` |

Example: `int sum = a + 5;` consists of the tokens `int`, `sum`, `=`, `a`, `+`, `5`, `;`.

## 3. Keywords

### 3.1 Definition
**Keywords** (reserved words) are words whose meaning is fixed by the language. They cannot be used as variable or function names.

### 3.2 The 32 Keywords of ANSI C (C89)

| | | | | | | | |
|---|---|---|---|---|---|---|---|
| auto | break | case | char | const | continue | default | do |
| double | else | enum | extern | float | for | goto | if |
| int | long | register | return | short | signed | sizeof | static |
| struct | switch | typedef | union | unsigned | void | volatile | while |

Later standards add more (for example `inline` and `restrict` in C99).

### 3.3 Groups of Keywords by Use

| Use | Keywords |
|---|---|
| Data types | `int`, `char`, `float`, `double`, `void` |
| Type modifiers | `short`, `long`, `signed`, `unsigned` |
| Decisions | `if`, `else`, `switch`, `case`, `default` |
| Loops | `for`, `while`, `do`, `break`, `continue`, `goto` |
| Storage classes | `auto`, `extern`, `register`, `static` |
| User-defined types | `struct`, `union`, `enum`, `typedef` |
| Others | `const`, `volatile`, `sizeof`, `return` |

## 4. Identifiers

An **identifier** is the name of a variable, function, array, structure, etc.

**Rules**
1. May contain letters, digits and underscore `_`.
2. Must not start with a digit.
3. Cannot be a keyword.
4. Cannot contain spaces or special symbols such as `@`, `-`, `#`.
5. Case-sensitive: `Total` and `total` are different.

| Valid | Invalid | Reason |
|---|---|---|
| `marks1` | `1marks` | Starts with a digit |
| `total_sum` | `total-sum` | Hyphen not allowed |
| `_count` | `int` | Keyword |
| `Age` | `my age` | Space not allowed |

## 5. Comments

### 5.1 Definition
A **comment** is text that the compiler ignores. It explains code to human readers.

### 5.2 Types

```c
/* Multi-line comment.
   It can span many lines. */

// Single-line comment (allowed from C99 onward)

int x = 5;   /* comment at the end of a line */
```

### 5.3 Good Practice
- Explain *why*, not only *what*.
- Do not nest `/* ... */` comments; the first `*/` ends the comment.
- Keep comments up to date.

## 6. Exam-Oriented Answers

### 5-mark: What are tokens? Explain their types.
**Introduction.** Tokens are the smallest individual units of a C program.
**Types.** (1) Keywords, (2) Identifiers, (3) Constants, (4) String literals, (5) Operators, (6) Special symbols, each with a one-line definition and example (table above).
**Example.** Break `int sum = a + 5;` into tokens.
**Conclusion.** The compiler checks the correct arrangement of tokens during compilation.

### 5-mark: What are keywords? Write rules for naming identifiers.
Give the definition, list at least 10 keywords with their groups, then the five identifier rules with valid and invalid examples.

## 7. Summary

C programs are built from letters, digits, special characters and white space. These form six kinds of tokens. Keywords are reserved, identifiers follow naming rules, and comments are ignored by the compiler.

---

[Previous: History and Structure](Topic-01-History-and-Structure-of-a-C-Program.md) | [Next: Variables, Constants and Data Types](Topic-03-Variables-Constants-and-Data-Types.md)
