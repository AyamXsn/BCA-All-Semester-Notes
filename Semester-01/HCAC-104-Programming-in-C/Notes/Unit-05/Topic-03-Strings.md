# Topic 3: Strings and String Functions

**Unit V | HCAC-104 Programming in C**

## 1. Introduction

### 1.1 Definition
In C a **string** is an array of `char` that ends with the **null character `'\0'`**. C has no separate string type.

```c
char name[6] = "Nepal";      /* stored as N e p a l \0  (6 bytes) */
char city[]  = "Janakpur";   /* size deduced: 9 bytes with '\0' */
```

```text
index :  0    1    2    3    4    5
char  : 'N'  'e'  'p'  'a'  'l'  '\0'
```

The array must be one larger than the number of visible characters to hold `'\0'`.

## 2. Input and Output of Strings

| Task | Code | Note |
|---|---|---|
| Print | `printf("%s", name);` or `puts(name);` | |
| Read one word | `scanf("%49s", name);` | Stops at white space; no `&`; the number limits input |
| Read a line | `fgets(line, sizeof line, stdin);` | Keeps the newline `\n` if it fits |
| Read a character | `getchar()` | |

Remove the newline kept by `fgets` with `line[strcspn(line, "\n")] = '\0';`.

## 3. String Functions from `<string.h>`

| Function | Purpose | Example | Result |
|---|---|---|---|
| `strlen(s)` | Number of characters (not counting `'\0'`) | `strlen("Nepal")` | 5 |
| `strcpy(d, s)` | Copy `s` into `d` | `strcpy(d, "Hi")` | `d` is "Hi" |
| `strcat(d, s)` | Append `s` to the end of `d` | `strcat(d, "!")` | "Hi!" |
| `strcmp(a, b)` | Compare: 0 if equal, negative if `a` < `b`, positive if `a` > `b` | `strcmp("a", "b")` | negative |
| `strchr(s, c)` | Find first occurrence of a character | | pointer or `NULL` |
| `strstr(s, t)` | Find a substring | | pointer or `NULL` |

Important points:
1. Use `strcmp`, **not** `==`, to compare strings. `==` compares addresses.
2. `strcpy` and `strcat` do not check the destination size; make sure it is large enough.
3. `strcmp` compares character codes (ASCII order), so uppercase letters come before lowercase.

Tested: [Program 32: String Library Functions](../../Programs/Program-32-String-Library-Functions/README.md).

## 4. Processing a String Manually

Because a string ends in `'\0'`, a loop can walk through it:

```c
int count_chars(const char *s)
{
    int n = 0;
    while (s[n] != '\0')
        n++;
    return n;       /* same result as strlen */
}
```

Tested examples: [Program 33: Palindrome](../../Programs/Program-33-Palindrome-Check/README.md) and [Program 34: Vowels and Consonants](../../Programs/Program-34-Count-Vowels-and-Consonants/README.md).

## 5. Passing Strings to Functions

A string is passed as a pointer to its first character: `void to_upper(char *s)`. The function changes the caller's characters. See [Program 38](../../Programs/Program-38-Passing-a-String-to-a-Function/README.md) and [Topic 5](Topic-05-Pointers-Arrays-and-Functions.md).

## 6. Character Functions from `<ctype.h>`

`isalpha`, `isdigit`, `isupper`, `islower`, `toupper`, `tolower` test or convert single characters.

## 7. Character Array vs String Pointer

| Basis | `char s[] = "Hi";` | `char *p = "Hi";` |
|---|---|---|
| Storage | Copy in a modifiable array | Pointer to a read-only string literal |
| Can modify characters | Yes | No (undefined behaviour) |
| `sizeof` | Size of the array (3) | Size of a pointer |

## 8. Exam-Oriented Answers

### 5-mark: What is a string? Explain any four string functions.
Definition with `'\0'`, then `strlen`, `strcpy`, `strcat` and `strcmp` with syntax, a short example and result.

### 5-mark: Write a program to check whether a string is a palindrome.
Use [Program 33](../../Programs/Program-33-Palindrome-Check/README.md) with its sample output.

## 9. Summary

A C string is a `char` array terminated by `'\0'`. Use `fgets` or width-limited `scanf` to read it safely, `<string.h>` functions to manipulate it, and `strcmp` rather than `==` to compare.

---

[Previous: Multi-Dimensional Arrays](Topic-02-Multi-Dimensional-Arrays.md) | [Next: Pointers](Topic-04-Pointers.md)
