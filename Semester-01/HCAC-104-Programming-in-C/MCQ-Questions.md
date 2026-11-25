# MCQ Questions - HCAC-104 Programming in C

Multiple-choice practice questions written for this repository from the syllabus topics. They are **not** copied from past papers and are not predictions of examination questions. Click "Answer" under each question to check yourself.

[Back to subject](README.md)

## Unit I: Introduction to Programming Concept

**Q1.** Which translator converts the whole source program into machine code before it runs?

- a) Interpreter
- b) Compiler
- c) Debugger
- d) Loader

<details><summary>Answer</summary>

**b) Compiler**. A compiler translates the entire program first; an interpreter translates and runs one statement at a time.

</details>

**Q2.** A program compiles without errors but prints a wrong result. This is a:

- a) Syntax error
- b) Linker warning
- c) Logical (semantic) error
- d) Typing mistake detected by the compiler

<details><summary>Answer</summary>

**c) Logical (semantic) error**. Syntax errors break grammar rules and stop compilation; logic errors have correct grammar but wrong meaning.

</details>

**Q3.** Which flowchart symbol represents a decision?

- a) Oval
- b) Rectangle
- c) Parallelogram
- d) Diamond

<details><summary>Answer</summary>

**d) Diamond**. Diamonds hold yes/no questions; ovals mark start/stop, rectangles are processes, parallelograms are input/output.

</details>

**Q4.** Pseudocode is:

- a) An informal, code-like description of an algorithm
- b) Machine code
- c) A compiled program
- d) A kind of flowchart

<details><summary>Answer</summary>

**a) An informal, code-like description of an algorithm**. Pseudocode cannot be compiled; it only describes the steps.

</details>

**Q5.** Which of the following is NOT a characteristic of an algorithm?

- a) It is definite
- b) It may run for an infinite number of steps
- c) It produces output
- d) It is finite

<details><summary>Answer</summary>

**b) It may run for an infinite number of steps**. An algorithm must be finite.

</details>

**Q6.** Organising a program around objects that combine data and functions is called:

- a) Procedural programming
- b) Modular programming
- c) Object-oriented programming
- d) Assembly programming

<details><summary>Answer</summary>

**c) Object-oriented programming**. Objects bundle data and methods; this is the object-oriented technique.

</details>

## Unit II: Introduction to C

**Q7.** C language was developed by:

- a) Ken Thompson
- b) Bjarne Stroustrup
- c) James Gosling
- d) Dennis Ritchie

<details><summary>Answer</summary>

**d) Dennis Ritchie**. Dennis Ritchie created C at Bell Laboratories around 1972.

</details>

**Q8.** Execution of every C program starts from:

- a) main()
- b) The first function defined
- c) The first #include line
- d) The last statement

<details><summary>Answer</summary>

**a) main()**. main() is the entry point.

</details>

**Q9.** Which is a valid identifier in C?

- a) 2total
- b) _total2
- c) total-2
- d) int

<details><summary>Answer</summary>

**b) _total2**. Identifiers cannot start with a digit, contain a hyphen, or be a keyword.

</details>

**Q10.** How many keywords does ANSI C (C89) have?

- a) 27
- b) 40
- c) 32
- d) 52

<details><summary>Answer</summary>

**c) 32**. ANSI C defines 32 reserved keywords.

</details>

**Q11.** Which header file declares printf() and scanf()?

- a) stdlib.h
- b) string.h
- c) math.h
- d) stdio.h

<details><summary>Answer</summary>

**d) stdio.h**. stdio.h is the standard input/output header.

</details>

**Q12.** What is the value of `7 / 2` when both operands are integers?

- a) 3
- b) 3.5
- c) 4
- d) 3.0

<details><summary>Answer</summary>

**a) 3**. Integer division discards the fractional part.

</details>

**Q13.** What does `printf("%d", 17 % 5);` print?

- a) 3
- b) 2
- c) 3.4
- d) 0

<details><summary>Answer</summary>

**b) 2**. 17 = 3 x 5 + 2, so the remainder is 2.

</details>

**Q14.** Which format specifier reads a double with scanf()?

- a) %d
- b) %c
- c) %lf
- d) %s

<details><summary>Answer</summary>

**c) %lf**. scanf needs %lf for double; %f is for float.

</details>

**Q15.** After `int x = 5;`, what does `printf("%d", x++);` print?

- a) 6
- b) 4
- c) Error
- d) 5

<details><summary>Answer</summary>

**d) 5**. Postfix ++ uses the old value first and then increases x.

</details>

**Q16.** What is the value of `12 & 10`?

- a) 8
- b) 14
- c) 6
- d) 22

<details><summary>Answer</summary>

**a) 8**. 1100 AND 1010 = 1000, which is 8.

</details>

**Q17.** The size of `char` in bytes is always:

- a) 2
- b) 1
- c) 4
- d) Depends on the compiler

<details><summary>Answer</summary>

**b) 1**. By definition sizeof(char) is 1.

</details>

**Q18.** The operator `?:` is called the:

- a) Comma operator
- b) Bitwise operator
- c) Conditional (ternary) operator
- d) Relational operator

<details><summary>Answer</summary>

**c) Conditional (ternary) operator**. It takes three operands: condition, value if true, value if false.

</details>

**Q19.** Which of these has the highest precedence?

- a) +
- b) ==
- c) &&
- d) *

<details><summary>Answer</summary>

**d) ***. Multiplication binds tighter than addition, comparison and logical AND.

</details>

**Q20.** A constant created with `#define` is processed by the:

- a) Preprocessor
- b) Linker
- c) Debugger
- d) Loader

<details><summary>Answer</summary>

**a) Preprocessor**. #define is a preprocessor directive that replaces text before compilation.

</details>

## Unit III: Control Structure

**Q21.** Which statement prevents fall-through in a switch?

- a) continue
- b) break
- c) goto
- d) return 0

<details><summary>Answer</summary>

**b) break**. Without break, execution continues into the next case.

</details>

**Q22.** Which loop always executes its body at least once?

- a) while
- b) for
- c) do-while
- d) nested for

<details><summary>Answer</summary>

**c) do-while**. do-while tests the condition after the body.

</details>

**Q23.** `for(;;)` creates:

- a) A syntax error
- b) A loop that never starts
- c) A loop that runs once
- d) An infinite loop

<details><summary>Answer</summary>

**d) An infinite loop**. With no condition, the loop never ends unless break or return is used.

</details>

**Q24.** What is printed by `for(i=1;i<=5;i++){ if(i==3) continue; printf("%d", i); }`?

- a) 1245
- b) 12
- c) 12345
- d) 45

<details><summary>Answer</summary>

**a) 1245**. continue skips only the pass where i is 3.

</details>

**Q25.** `goto` transfers control to:

- a) The next function
- b) A labelled statement
- c) The end of the loop only
- d) The top of the file

<details><summary>Answer</summary>

**b) A labelled statement**. goto jumps to a label in the same function.

</details>

**Q26.** Which header declares exit()?

- a) stdio.h
- b) string.h
- c) stdlib.h
- d) conio.h

<details><summary>Answer</summary>

**c) stdlib.h**. exit() is declared in stdlib.h.

</details>

**Q27.** Which type of expression cannot be used in a switch statement?

- a) int
- b) char
- c) enum
- d) float

<details><summary>Answer</summary>

**d) float**. switch works on integer types only.

</details>

**Q28.** In C, which value is treated as false?

- a) 0
- b) 1
- c) -1
- d) Any non-zero value

<details><summary>Answer</summary>

**a) 0**. Zero is false; every non-zero value is true.

</details>

## Unit IV: Function

**Q29.** A function that does not return a value has the return type:

- a) int
- b) void
- c) null
- d) empty

<details><summary>Answer</summary>

**b) void**. void means no value is returned.

</details>

**Q30.** A function prototype (declaration) ends with a:

- a) Closing brace
- b) Colon
- c) Semicolon
- d) Full stop

<details><summary>Answer</summary>

**c) Semicolon**. A prototype is a declaration, so it ends with `;`.

</details>

**Q31.** In call by value, changes made to the parameter inside the function:

- a) Change the caller's variable
- b) Cause a compile error
- c) Are saved in a file
- d) Do not affect the caller's variable

<details><summary>Answer</summary>

**d) Do not affect the caller's variable**. The function works on a copy.

</details>

**Q32.** Every correct recursive function must have a:

- a) Base case
- b) Global variable
- c) Loop
- d) Pointer parameter

<details><summary>Answer</summary>

**a) Base case**. The base case stops the recursion.

</details>

**Q33.** What does `gcd(12, 8)` return using Euclid's recursive definition?

- a) 2
- b) 4
- c) 8
- d) 24

<details><summary>Answer</summary>

**b) 4**. gcd(12,8) -> gcd(8,4) -> gcd(4,0) = 4.

</details>

**Q34.** The variables listed in a function's definition are called:

- a) Actual arguments
- b) Global variables
- c) Formal parameters
- d) Constants

<details><summary>Answer</summary>

**c) Formal parameters**. Actual arguments appear in the call; formal parameters in the definition.

</details>

**Q35.** To let a function change the caller's variable, you should pass:

- a) Its value
- b) Its type
- c) Its name as a string
- d) Its address

<details><summary>Answer</summary>

**d) Its address**. The function then works through a pointer.

</details>

## Unit V: Array, Pointer and String

**Q36.** The index of the first element of an array is:

- a) 0
- b) 1
- c) -1
- d) Depends on the declaration

<details><summary>Answer</summary>

**a) 0**. C arrays are zero-based.

</details>

**Q37.** For `int a[5];` the last valid index is:

- a) 5
- b) 4
- c) 6
- d) 3

<details><summary>Answer</summary>

**b) 4**. Indexes run from 0 to size - 1.

</details>

**Q38.** A C string always ends with:

- a) A space
- b) A newline
- c) The null character '\0'
- d) The letter 'e'

<details><summary>Answer</summary>

**c) The null character '\0'**. '\0' marks the end of the string.

</details>

**Q39.** `strcmp(a, b)` returns 0 when:

- a) a is longer than b
- b) a is shorter than b
- c) Both strings are empty only
- d) The strings are equal

<details><summary>Answer</summary>

**d) The strings are equal**. Zero means identical contents.

</details>

**Q40.** How many bytes does `char s[] = "Nepal";` occupy?

- a) 6
- b) 5
- c) 4
- d) 7

<details><summary>Answer</summary>

**a) 6**. Five letters plus the terminating '\0'.

</details>

**Q41.** If `p` points to `a[0]` of an int array, `p + 1` points to:

- a) a[0] plus one byte
- b) a[1]
- c) a[2]
- d) Garbage

<details><summary>Answer</summary>

**b) a[1]**. Pointer arithmetic moves by one element, not one byte.

</details>

**Q42.** Which operator gives the address of a variable?

- a) *
- b) ->
- c) &
- d) %

<details><summary>Answer</summary>

**c) &**. & is the address-of operator.

</details>

**Q43.** What does `strlen("BCA")` return?

- a) 4
- b) 2
- c) 0
- d) 3

<details><summary>Answer</summary>

**d) 3**. strlen does not count the terminating '\0'.

</details>

**Q44.** When an array is passed to a function, what is actually passed?

- a) The address of its first element
- b) A copy of the whole array
- c) Only the first value
- d) Its size

<details><summary>Answer</summary>

**a) The address of its first element**. Arrays decay to pointers, so the function can modify the original.

</details>

**Q45.** `a[i]` is equivalent to:

- a) &(a + i)
- b) *(a + i)
- c) a + *i
- d) *a + i

<details><summary>Answer</summary>

**b) *(a + i)**. Indexing is defined through pointer arithmetic.

</details>

**Q46.** To multiply an m x n matrix by an n x p matrix, the result size is:

- a) n x n
- b) m x n
- c) m x p
- d) p x m

<details><summary>Answer</summary>

**c) m x p**. Rows of the first and columns of the second give the result size.

</details>

## Unit VI: Structure and Union

**Q47.** Which operator accesses a member through a pointer to a structure?

- a) .
- b) &
- c) ::
- d) ->

<details><summary>Answer</summary>

**d) ->**. p->x is shorthand for (*p).x.

</details>

**Q48.** The memory size of a union is determined by its:

- a) Largest member (plus any padding)
- b) First member
- c) Sum of all members
- d) Last member

<details><summary>Answer</summary>

**a) Largest member (plus any padding)**. All members share the same memory.

</details>

**Q49.** A structure definition must end with:

- a) A colon
- b) A semicolon after the closing brace
- c) Nothing
- d) A comma

<details><summary>Answer</summary>

**b) A semicolon after the closing brace**. struct S { ... };

</details>

**Q50.** Which keyword creates a new name for an existing type?

- a) define
- b) union
- c) typedef
- d) static

<details><summary>Answer</summary>

**c) typedef**. typedef gives a type another name.

</details>

**Q51.** In a union, how many members hold a valid value at one time?

- a) All of them
- b) Two
- c) None
- d) One (the one written last)

<details><summary>Answer</summary>

**d) One (the one written last)**. Writing one member overwrites the shared memory.

</details>

**Q52.** Members of a structure variable (not a pointer) are accessed with:

- a) The dot operator
- b) The arrow operator
- c) The address operator
- d) The scope operator

<details><summary>Answer</summary>

**a) The dot operator**. s.roll for variables; p->roll for pointers.

</details>

## Unit VII: Input Output and File Handling

**Q53.** `fopen()` returns what when the file cannot be opened?

- a) 0 characters
- b) NULL
- c) EOF
- d) -1 as a string

<details><summary>Answer</summary>

**b) NULL**. Always compare the result with NULL.

</details>

**Q54.** Which mode erases the existing contents of a file when it is opened?

- a) "r"
- b) "a"
- c) "w"
- d) "rb"

<details><summary>Answer</summary>

**c) "w"**. Mode w truncates an existing file.

</details>

**Q55.** Which mode adds new data at the end of a file and keeps the old data?

- a) "w"
- b) "r"
- c) "w+"
- d) "a"

<details><summary>Answer</summary>

**d) "a"**. Append mode preserves existing content.

</details>

**Q56.** In `fseek(fp, offset, origin)`, which origin measures from the start of the file?

- a) SEEK_SET
- b) SEEK_CUR
- c) SEEK_END
- d) SEEK_BEGIN

<details><summary>Answer</summary>

**a) SEEK_SET**. SEEK_CUR is the current position, SEEK_END the end.

</details>

**Q57.** Which function writes a block of bytes to a binary file?

- a) fprintf
- b) fwrite
- c) fputs
- d) putchar

<details><summary>Answer</summary>

**b) fwrite**. fwrite(ptr, size, count, fp) writes count items.

</details>

**Q58.** `fgetc(fp)` returns which value at the end of the file?

- a) NULL
- b) 0
- c) EOF
- d) '\0'

<details><summary>Answer</summary>

**c) EOF**. That is why the result is stored in an int.

</details>

**Q59.** `rewind(fp)` does what?

- a) Deletes the file
- b) Closes the file
- c) Moves to the end
- d) Moves the file position to the start

<details><summary>Answer</summary>

**d) Moves the file position to the start**. Equivalent to returning the position to offset 0.

</details>

**Q60.** `ftell(fp)` returns:

- a) The current position in bytes from the start
- b) The number of lines
- c) The file size only
- d) The file name

<details><summary>Answer</summary>

**a) The current position in bytes from the start**. It reports the position indicator.

</details>

## Unit VIII: Introduction to Graphics

**Q61.** In graphics mode the screen coordinate (0, 0) is at the:

- a) Bottom-left corner
- b) Top-left corner
- c) Centre
- d) Top-right corner

<details><summary>Answer</summary>

**b) Top-left corner**. x increases to the right and y increases downward.

</details>

**Q62.** Passing `DETECT` to `initgraph()` means:

- a) Graphics is turned off
- b) The mode is set to text
- c) The best available driver and mode are chosen automatically
- d) A file is detected

<details><summary>Answer</summary>

**c) The best available driver and mode are chosen automatically**. DETECT asks the library to auto-detect the hardware.

</details>

**Q63.** `closegraph()` is used to:

- a) Clear one shape
- b) Save the picture
- c) Change the colour
- d) Shut down graphics mode and return to text mode

<details><summary>Answer</summary>

**d) Shut down graphics mode and return to text mode**. Call it at the end of a graphics program.

</details>

**Q64.** The header `graphics.h` belongs to:

- a) The Borland BGI library, not the standard C library
- b) The ANSI C standard library
- c) stdio.h
- d) The Linux kernel

<details><summary>Answer</summary>

**a) The Borland BGI library, not the standard C library**. That is why it is not available in GCC by default.

</details>

---

Total questions: 64

[Back to subject](README.md)
