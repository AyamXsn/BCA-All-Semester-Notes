# Topic 3: Jump Statements

**Unit III | HCAC-104 Programming in C**

## 1. Introduction

**Jump statements** transfer control to another part of the program without testing a condition at that point. The syllabus lists `goto`, `break`, `continue` and `exit`.

## 2. `break`

`break` immediately ends the nearest enclosing loop or `switch`.

```c
for (i = 1; i <= 10; i++) {
    if (i == 6)
        break;
    printf("%d ", i);
}
/* Output: 1 2 3 4 5 */
```

Common uses: leave a loop when the answer is found (for example, a divisor in a prime test, see [Program 18](../../Programs/Program-18-Prime-Number-Check/README.md)), and end each `case` in a `switch`.

## 3. `continue`

`continue` skips the remaining statements of the **current pass** and moves to the next one. In a `for` loop it jumps to the update expression; in `while` and `do-while` it jumps to the condition test.

```c
for (i = 1; i <= 5; i++) {
    if (i == 3)
        continue;
    printf("%d ", i);
}
/* Output: 1 2 4 5 */
```

Tested together with `break`: [Program 20](../../Programs/Program-20-Break-and-Continue-Demo/README.md).

### 3.1 `break` vs `continue`

| Basis | `break` | `continue` |
|---|---|---|
| Effect | Terminates the loop (or `switch`) | Skips the current iteration only |
| After it | Execution goes to the statement after the loop | Loop continues with the next iteration |
| Works in `switch` | Yes | No (only loops) |

## 4. `goto`

`goto label;` jumps to a statement marked by `label:` in the same function.

```c
read_next:
    scanf("%d", &n);
    if (n >= 0) {
        sum += n;
        goto read_next;
    }
```

Tested: [Program 21](../../Programs/Program-21-Goto-Statement-Demo/README.md).

**Why `goto` is discouraged.** It makes the flow hard to follow ("spaghetti code") and harder to debug. Structured loops and functions are almost always clearer. A legitimate use is leaving several nested loops at once or jumping to common clean-up code.

## 5. `exit()`

`exit(status)` (declared in `<stdlib.h>`) ends the **whole program** at once, wherever it is called.

```c
#include <stdlib.h>

if (fp == NULL) {
    printf("Cannot open file\n");
    exit(1);        /* non-zero: abnormal termination */
}
```

`exit(0)` (or `EXIT_SUCCESS`) means success; a non-zero value (or `EXIT_FAILURE`) means an error. Open files are closed and buffered output is flushed.

### 5.1 `break` vs `exit`

| Basis | `break` | `exit()` |
|---|---|---|
| Ends | Only the current loop or `switch` | The entire program |
| Needs header | No | `<stdlib.h>` |

## 6. Exam-Oriented Answers

### 5-mark: Explain `break` and `continue` with examples.
Definitions, two short examples with output, and the comparison table.

### 5-mark: What is the `goto` statement? Why is it avoided?
Syntax with a label, the example, and the disadvantages (hard-to-read, unstructured flow).

### 10-mark: Explain the jump statements of C.
Cover all four statements with syntax, examples and outputs, the two comparison tables, and a short conclusion that structured loops are preferred.

## 7. Summary

`break` leaves a loop or `switch`, `continue` skips to the next pass, `goto` jumps to a label and `exit()` ends the program. Use them sparingly and prefer clear structured code.

---

[Previous: Looping Statements](Topic-02-Looping-Statements.md) | [Back to Unit Introduction](Introduction.md)
