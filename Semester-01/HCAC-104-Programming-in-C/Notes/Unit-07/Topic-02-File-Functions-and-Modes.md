# Topic 2: `fopen`, `fclose`, `fflush`, `freopen` and File Modes

**Unit VII | HCAC-104 Programming in C**

## 1. `fopen()`

```c
FILE *fopen(const char *filename, const char *mode);
```

Opens the file and returns a `FILE *`. On failure (file not found, no permission) it returns **`NULL`**, so always check:

```c
FILE *fp = fopen("data.txt", "r");
if (fp == NULL) {
    printf("Cannot open data.txt\n");
    return 1;
}
```

## 2. File Modes

| Mode | Meaning | If the file exists | If it does not exist |
|---|---|---|---|
| `"r"` | Read | Opened from the start | Fails (`NULL`) |
| `"w"` | Write | **Erased** (emptied) | Created |
| `"a"` | Append | Writing goes at the end; old data kept | Created |
| `"r+"` | Read and write | Opened from the start | Fails |
| `"w+"` | Read and write | **Erased** | Created |
| `"a+"` | Read and append | Writing at the end | Created |

Add `b` for binary files: `"rb"`, `"wb"`, `"ab"`, `"rb+"` (also written `"r+b"`), `"wb+"`, `"ab+"`.

**Warning:** `"w"` destroys existing content without asking.

## 3. `fclose()`

```c
int fclose(FILE *fp);
```

Flushes buffered data, closes the file and releases resources. Returns 0 on success. Always close every file you open; unclosed files may lose data.

## 4. `fflush()`

```c
int fflush(FILE *fp);
```

Output is **buffered** (held in memory before being written). `fflush` forces buffered output to be written to the file immediately, for example after printing a prompt. `fflush(stdout)` flushes screen output.

Using `fflush` on an input stream such as `stdin` is not defined by the C standard, so do not rely on it to clear the keyboard buffer.

## 5. `freopen()`

```c
FILE *freopen(const char *filename, const char *mode, FILE *stream);
```

Closes the stream and reopens it with a different file or mode. A classic use is to **redirect** a standard stream:

```c
freopen("output.txt", "w", stdout);
printf("This line goes into output.txt, not the screen.\n");
```

After this, everything printed with `printf` is written to `output.txt`.

## 6. Writing, Reading and Appending Examples

| Task | Tested program |
|---|---|
| Create a file and write lines | [Program 44](../../Programs/Program-44-Write-to-a-Text-File/README.md) |
| Read a file line by line | [Program 45](../../Programs/Program-45-Read-from-a-Text-File/README.md) |
| Append to a file | [Program 46](../../Programs/Program-46-Append-to-a-Text-File/README.md) |

## 7. Exam-Oriented Answers

### 5-mark: Explain `fopen()` and the different file modes.
Syntax, the `NULL` check, the mode table (at least `r`, `w`, `a`, `r+`, `w+`, `a+`), and the warning about `"w"`.

### 5-mark: Write short notes on `fclose`, `fflush` and `freopen`.
One paragraph each with syntax and a one-line example.

## 8. Summary

`fopen` opens a file in a mode and returns `NULL` on failure; `fclose` closes it; `fflush` writes buffered output immediately; `freopen` re-associates a stream with another file, for example to redirect `stdout`.

---

[Previous: File Handling Concepts](Topic-01-File-Handling-Concepts.md) | [Next: Formatted, Character and Direct I/O](Topic-03-Formatted-Character-and-Direct-IO.md)
