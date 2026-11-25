# HCAC-104 - Programming in C

**Semester:** 1 (First Year) | **Credit hours:** 3 | **Full marks:** 60 + 20 + 20 (pass 24 + 8 + 8) | **Nature:** Theory + Lab

## Subject Introduction

This course teaches structured programming in C: writing, compiling, debugging and running programs, designing algorithms and flowcharts, and using arrays, pointers, strings, structures, files and basic graphics.

Source: official RJU curriculum outline ([PDF](https://rju.edu.np/wp-content/uploads/2018/08/BCA-full-syllabus-1.pdf), [programme page](https://rju.edu.np/course/bca/)), transcribed and condensed here.

## Syllabus Units

Allotted lecture hours listed in the outline: **45**.

| Unit | Title | Hours | Topics (condensed) | Status |
|---|---|---|---|---|
| I | [Introduction to Programming Concept](Notes/Unit-01/Introduction.md) | 4 | Language translators, syntax and semantics, algorithm/flowchart/pseudocode, features of a good program, procedural, modular and object-oriented techniques. | Notes complete |
| II | [Introduction to C](Notes/Unit-02/Introduction.md) | 6 | History, structure of a C program, character set, tokens, keywords, comments, variables and constants, data types, type conversion, input/output, operators. | Notes complete |
| III | [Control Structure](Notes/Unit-03/Introduction.md) | 7 | if, if-else, nested if-else, switch, conditional operator, while, do-while, for, nested loops, goto, break, continue, exit. | Notes complete |
| IV | [Function](Notes/Unit-04/Introduction.md) | 6 | Function definition and return, prototype, call by value, call by reference, recursion. | Notes complete |
| V | [Array, Pointer and String](Notes/Unit-05/Introduction.md) | 7 | Arrays (one and multi-dimensional), strings and string functions, passing arrays and strings to functions, pointers, pointer arithmetic, arrays and pointers. | Notes complete |
| VI | [Structure and Union](Notes/Unit-06/Introduction.md) | 7 | Structures, initialisation and access, arrays of structures, structures and functions, pointer to structure, union, union vs structure. | Notes complete |
| VII | [Input Output and File Handling](Notes/Unit-07/Introduction.md) | 5 | File handling concepts and access methods, fopen, fclose, fflush, freopen, formatted/character/direct I/O, random access, error handling. | Notes complete |
| VIII | [Introduction to Graphics](Notes/Unit-08/Introduction.md) | 3 | Graphics modes, initialisation, graphics functions. | Notes complete |

## Notes Navigation

- **Unit I: Introduction to Programming Concept** ([overview](Notes/Unit-01/Introduction.md))
  - [Topic 1: Programming Languages and Language Translators](Notes/Unit-01/Topic-01-Language-Translators.md)
  - [Topic 2: Programming Design Tools (Algorithm, Flowchart, Pseudocode)](Notes/Unit-01/Topic-02-Programming-Design-Tools.md)
  - [Topic 3: Features of a Good Program](Notes/Unit-01/Topic-03-Features-of-a-Good-Program.md)
  - [Topic 4: Programming Techniques (Procedural, Modular, Object-Oriented)](Notes/Unit-01/Topic-04-Programming-Techniques.md)
- **Unit II: Introduction to C** ([overview](Notes/Unit-02/Introduction.md))
  - [Topic 1: History of C and Structure of a C Program](Notes/Unit-02/Topic-01-History-and-Structure-of-a-C-Program.md)
  - [Topic 2: Character Set, Tokens, Keywords and Comments](Notes/Unit-02/Topic-02-Character-Set-Tokens-Keywords-and-Comments.md)
  - [Topic 3: Variables, Constants and Data Types](Notes/Unit-02/Topic-03-Variables-Constants-and-Data-Types.md)
  - [Topic 4: Type Conversion, Input and Output](Notes/Unit-02/Topic-04-Type-Conversion-and-Input-Output.md)
  - [Topic 5: Operators](Notes/Unit-02/Topic-05-Operators.md)
- **Unit III: Control Structure** ([overview](Notes/Unit-03/Introduction.md))
  - [Topic 1: Selection Statements](Notes/Unit-03/Topic-01-Selection-Statements.md)
  - [Topic 2: Looping Statements](Notes/Unit-03/Topic-02-Looping-Statements.md)
  - [Topic 3: Jump Statements](Notes/Unit-03/Topic-03-Jump-Statements.md)
- **Unit IV: Function** ([overview](Notes/Unit-04/Introduction.md))
  - [Topic 1: Function Definition, Return and Prototype](Notes/Unit-04/Topic-01-Function-Concept.md)
  - [Topic 2: Call by Value and Call by Reference](Notes/Unit-04/Topic-02-Call-by-Value-and-Call-by-Reference.md)
  - [Topic 3: Recursion](Notes/Unit-04/Topic-03-Recursion.md)
- **Unit V: Array, Pointer and String** ([overview](Notes/Unit-05/Introduction.md))
  - [Topic 1: Arrays](Notes/Unit-05/Topic-01-Arrays.md)
  - [Topic 2: Multi-Dimensional Arrays](Notes/Unit-05/Topic-02-Multi-Dimensional-Arrays.md)
  - [Topic 3: Strings and String Functions](Notes/Unit-05/Topic-03-Strings.md)
  - [Topic 4: Pointers](Notes/Unit-05/Topic-04-Pointers.md)
  - [Topic 5: Pointers, Arrays and Functions](Notes/Unit-05/Topic-05-Pointers-Arrays-and-Functions.md)
- **Unit VI: Structure and Union** ([overview](Notes/Unit-06/Introduction.md))
  - [Topic 1: Structures](Notes/Unit-06/Topic-01-Structures.md)
  - [Topic 2: Arrays of Structures, Structures with Functions and Pointer to Structure](Notes/Unit-06/Topic-02-Structures-Arrays-Functions-and-Pointers.md)
  - [Topic 3: Unions](Notes/Unit-06/Topic-03-Unions.md)
- **Unit VII: Input Output and File Handling** ([overview](Notes/Unit-07/Introduction.md))
  - [Topic 1: File Handling Concepts and Access Methods](Notes/Unit-07/Topic-01-File-Handling-Concepts.md)
  - [Topic 2: `fopen`, `fclose`, `fflush`, `freopen` and File Modes](Notes/Unit-07/Topic-02-File-Functions-and-Modes.md)
  - [Topic 3: Formatted, Character and Direct I/O](Notes/Unit-07/Topic-03-Formatted-Character-and-Direct-IO.md)
  - [Topic 4: Random Access and Error Handling](Notes/Unit-07/Topic-04-Random-Access-and-Error-Handling.md)
- **Unit VIII: Introduction to Graphics** ([overview](Notes/Unit-08/Introduction.md))
  - [Topic 1: Graphics Modes and Initialization](Notes/Unit-08/Topic-01-Graphics-Modes-and-Initialization.md)
  - [Topic 2: Graphics Functions](Notes/Unit-08/Topic-02-Graphics-Functions.md)

## Programs (52 programs; 51 compiled and run)

Every program is a separate `.c` file with its own README showing the logic, compile command and real captured output. The exception is Program 52 (graphics), which needs the BGI library and is clearly marked as not tested here.

- **Unit I**
  - [Program 01: Largest of Three Numbers](Programs/Program-01-Largest-of-Three-Numbers/README.md)
- **Unit II**
  - [Program 02: Basic Structure of a C Program](Programs/Program-02-Basic-Structure-of-a-C-Program/README.md)
  - [Program 03: Sum of Two Numbers](Programs/Program-03-Sum-of-Two-Numbers/README.md)
  - [Program 04: Area and Circumference of Circle](Programs/Program-04-Area-and-Circumference-of-Circle/README.md)
  - [Program 05: Type Conversion Demo](Programs/Program-05-Type-Conversion-Demo/README.md)
  - [Program 06: Arithmetic and Relational Operators](Programs/Program-06-Arithmetic-and-Relational-Operators/README.md)
  - [Program 07: Increment and Decrement Operators](Programs/Program-07-Increment-and-Decrement-Operators/README.md)
  - [Program 08: Bitwise Operators](Programs/Program-08-Bitwise-Operators/README.md)
  - [Program 09: Logical Operators](Programs/Program-09-Logical-Operators/README.md)
  - [Program 10: Conditional Operator](Programs/Program-10-Conditional-Operator/README.md)
- **Unit III**
  - [Program 11: Even or Odd](Programs/Program-11-Even-or-Odd/README.md)
  - [Program 12: Grade Calculator](Programs/Program-12-Grade-Calculator/README.md)
  - [Program 13: Simple Calculator Switch](Programs/Program-13-Simple-Calculator-Switch/README.md)
  - [Program 14: Factorial using for Loop](Programs/Program-14-Factorial-using-for-Loop/README.md)
  - [Program 15: Reverse a Number using while](Programs/Program-15-Reverse-a-Number-using-while/README.md)
  - [Program 16: Menu Driven Program do while](Programs/Program-16-Menu-Driven-Program-do-while/README.md)
  - [Program 17: Fibonacci Series](Programs/Program-17-Fibonacci-Series/README.md)
  - [Program 18: Prime Number Check](Programs/Program-18-Prime-Number-Check/README.md)
  - [Program 19: Star Triangle Pattern](Programs/Program-19-Star-Triangle-Pattern/README.md)
  - [Program 20: Break and Continue Demo](Programs/Program-20-Break-and-Continue-Demo/README.md)
  - [Program 21: Goto Statement Demo](Programs/Program-21-Goto-Statement-Demo/README.md)
- **Unit IV**
  - [Program 22: Function Types](Programs/Program-22-Function-Types/README.md)
  - [Program 23: Call by Value Swap](Programs/Program-23-Call-by-Value-Swap/README.md)
  - [Program 24: Call by Reference Swap](Programs/Program-24-Call-by-Reference-Swap/README.md)
  - [Program 25: Factorial using Recursion](Programs/Program-25-Factorial-using-Recursion/README.md)
  - [Program 26: Fibonacci using Recursion](Programs/Program-26-Fibonacci-using-Recursion/README.md)
  - [Program 27: GCD using Recursion](Programs/Program-27-GCD-using-Recursion/README.md)
- **Unit V**
  - [Program 28: Array Sum Average Max Min](Programs/Program-28-Array-Sum-Average-Max-Min/README.md)
  - [Program 29: Bubble Sort](Programs/Program-29-Bubble-Sort/README.md)
  - [Program 30: Matrix Addition](Programs/Program-30-Matrix-Addition/README.md)
  - [Program 31: Matrix Multiplication](Programs/Program-31-Matrix-Multiplication/README.md)
  - [Program 32: String Library Functions](Programs/Program-32-String-Library-Functions/README.md)
  - [Program 33: Palindrome Check](Programs/Program-33-Palindrome-Check/README.md)
  - [Program 34: Count Vowels and Consonants](Programs/Program-34-Count-Vowels-and-Consonants/README.md)
  - [Program 35: Pointer Basics](Programs/Program-35-Pointer-Basics/README.md)
  - [Program 36: Pointer Arithmetic and Arrays](Programs/Program-36-Pointer-Arithmetic-and-Arrays/README.md)
  - [Program 37: Passing an Array to a Function](Programs/Program-37-Passing-an-Array-to-a-Function/README.md)
  - [Program 38: Passing a String to a Function](Programs/Program-38-Passing-a-String-to-a-Function/README.md)
- **Unit VI**
  - [Program 39: Student Structure](Programs/Program-39-Student-Structure/README.md)
  - [Program 40: Array of Structures](Programs/Program-40-Array-of-Structures/README.md)
  - [Program 41: Structure and Function](Programs/Program-41-Structure-and-Function/README.md)
  - [Program 42: Pointer to Structure](Programs/Program-42-Pointer-to-Structure/README.md)
  - [Program 43: Union Demo](Programs/Program-43-Union-Demo/README.md)
- **Unit VII**
  - [Program 44: Write to a Text File](Programs/Program-44-Write-to-a-Text-File/README.md)
  - [Program 45: Read from a Text File](Programs/Program-45-Read-from-a-Text-File/README.md)
  - [Program 46: Append to a Text File](Programs/Program-46-Append-to-a-Text-File/README.md)
  - [Program 47: Copy a File Character by Character](Programs/Program-47-Copy-a-File-Character-by-Character/README.md)
  - [Program 48: Formatted File IO](Programs/Program-48-Formatted-File-IO/README.md)
  - [Program 49: Binary File fwrite fread](Programs/Program-49-Binary-File-fwrite-fread/README.md)
  - [Program 50: Random Access fseek ftell](Programs/Program-50-Random-Access-fseek-ftell/README.md)
  - [Program 51: File Error Handling](Programs/Program-51-File-Error-Handling/README.md)
- **Unit VIII**
  - [Program 52: Graphics Basic Shapes](Programs/Program-52-Graphics-Basic-Shapes/README.md)

## Practical / Lab Work

Official lab items from the outline and where to find them:

| Official lab item | Where covered |
|---|---|
| Algorithm and flowchart design; basic C structure; variables, constants, I/O; operators and type conversion | Programs 01 to 10, [Unit I notes](Notes/Unit-01/Introduction.md) |
| if, if-else, switch; while, do-while, for, nested loops; jump statements | Programs 11 to 21 |
| Functions, parameter passing, call by reference, recursion | Programs 22 to 27 |
| Arrays, pointers, strings; structures and unions; structures with functions | Programs 28 to 43 |
| File handling (open, read, write, append), random access files, text formatting | Programs 44 to 51 |
| Graphics shapes and modes | Program 52 (untested, needs BGI) |
| Project: a simple C application with input, processing, output and storage in an external file | [Student Record Manager](Practical/Project-Student-Record-Manager/README.md) |

## Exercises

[Programming Exercises](Exercises/Programming-Exercises.md): 40 practice problems arranged by unit, with hints pointing to the tested programs.

## Important Questions and MCQs

- [Important Questions](Important-Questions.md): short, long, programming and output-prediction questions, plus unit-wise revision topics. None are guaranteed exam questions.
- [MCQ Questions](MCQ-Questions.md): 64 multiple-choice questions with answers and explanations.

## References

[References](References.md): books from the official outline and free online references.

## Completion Status

| Component | Status |
|---|---|
| Syllabus units transcribed | Done |
| Notes (Units I to VIII) | Done: every unit has an overview and topic files with exam-oriented answers |
| Programs / Practical | Done: 52 programs and 1 project; 51 programs and the project were compiled and run; Program 52 (graphics) needs BGI and was not run |
| Exercises | Done |
| Important questions and MCQs | Done |

**Syllabus vs supplementary:** the unit and topic structure follows the official outline. A few explanations go slightly beyond the condensed topic lists to make the ideas clear for beginners (for example nested structures, the operator precedence table and `perror`), and `graphics.h` follows traditional Turbo C/BGI behaviour.

**Known limits:** there are no verified past papers yet, so no question is labelled as "frequently asked". Programs are written for GCC on Linux with the C11 standard; Program 52 needs Turbo C/BGI or a compatible library.

---

[Back to Semester 01](../README.md) | [Back to repository home](../../README.md)
