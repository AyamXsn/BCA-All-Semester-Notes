# Topic 1: Programming Languages and Language Translators

**Unit I | HCAC-104 Programming in C**

## 1. Introduction

A computer's processor understands only **machine language**, which is made of binary digits (0 and 1). Writing programs in binary is slow and error-prone, so humans created easier languages. Because the processor cannot run those languages directly, a **language translator** is needed to convert them into machine code.

## 2. Levels of Programming Languages

| Level | Example | Description |
|---|---|---|
| Machine language | Binary patterns such as `10110000 01100001` | The only language the CPU executes directly. |
| Assembly language | `MOV A, B` | Uses short symbolic names (mnemonics) instead of binary. |
| High-level language | C, C++, Java, Python | Uses English-like words and mathematical notation. |

### 2.1 Advantages and Disadvantages

| Level | Advantages | Disadvantages |
|---|---|---|
| Machine | Fastest execution; no translation needed | Very hard to write and debug; different for each CPU |
| Assembly | Faster and smaller programs; direct hardware control | Still hard to learn; depends on CPU type; needs an assembler |
| High-level | Easy to learn, read and maintain; portable between machines | Needs a compiler or interpreter; usually less direct hardware control |

## 3. Language Translators

A **language translator** is a program that converts a program written in one language into another language, usually into machine code.

### 3.1 Assembler

Converts **assembly language** into machine code. Each assembly instruction usually maps to one machine instruction.

### 3.2 Compiler

Translates the **whole source program** into machine code (an executable file) in one go, **before** the program runs. If errors exist, the compiler reports them and does not produce the executable.

- Example: the C compiler `gcc` turns `program.c` into an executable file.

### 3.3 Interpreter

Translates and executes the program **one statement at a time**. It does not usually produce a separate executable file.

- Example: the standard Python implementation interprets Python code.

### 3.4 Compiler vs Interpreter

| Basis | Compiler | Interpreter |
|---|---|---|
| Translation unit | Whole program at once | One statement at a time |
| Output | Separate executable (object) file | Usually no separate file |
| Execution speed | Faster once compiled | Slower, since translation repeats every run |
| Error reporting | Reports many errors after scanning the program | Stops at the first error it reaches |
| Memory | Executable is kept for later runs | Source and interpreter needed every run |
| Typical examples | C, C++ | Python, JavaScript (typically) |

## 4. Syntax and Semantics

- **Syntax** is the set of grammar rules of a language: how statements must be written. A **syntax error** breaks those rules, and the compiler rejects the program.
  - Example: `printf("Hi")` without the closing semicolon in C.
- **Semantics** is the meaning of a correctly written statement: what it actually does. A **semantic (logic) error** passes the compiler but produces wrong results.
  - Example: writing `area = length + width;` when you meant `length * width`. The compiler accepts it, but the answer is wrong.

## 5. The C Build Process (Overview)

```text
Source code (.c)  --compiler-->  Object code (.o)  --linker-->  Executable
```

You will see this in practice in the program example: [Program-01](../../Programs/Program-01-Largest-of-Three-Numbers/README.md).

## 6. Summary

- Machine language is native to the CPU; assembly and high-level languages need translators.
- An assembler handles assembly; compilers translate the whole program; interpreters translate line by line.
- Syntax is about correct form; semantics is about correct meaning.

## 7. Exam-Oriented Answers

### 5-mark: Differentiate between a compiler and an interpreter.
**Introduction.** Both convert high-level source code into a form the computer can run.
**Points.** (1) A compiler translates the whole program at once, an interpreter one statement at a time. (2) A compiler creates a separate executable file; an interpreter usually does not. (3) Compiled programs run faster. (4) A compiler reports many errors after scanning the program; an interpreter stops at the first error. (5) C is normally compiled; Python is normally interpreted.
**Conclusion.** Compilers favour speed; interpreters favour quick testing.

### 5-mark: Explain language translators.
Define a translator, then describe the assembler (assembly to machine code), compiler and interpreter with one example each, and finish with the comparison table.

### 10-mark: Explain programming languages and their translators.
Describe machine, assembly and high-level languages with the advantages and disadvantages table; explain the three translators; compare compiler and interpreter; explain syntax and semantic errors with examples; add the C build process diagram.

---

[Back to Unit Introduction](Introduction.md) | [Next: Programming Design Tools](Topic-02-Programming-Design-Tools.md)
