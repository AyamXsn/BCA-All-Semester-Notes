# Topic 4: Random Access and Error Handling

**Unit VII | HCAC-104 Programming in C**

## 1. Random Access Functions

Every open file has a **file position indicator** that marks where the next read or write will happen. Random access means moving that indicator directly.

### 1.1 `fseek()`

```c
int fseek(FILE *fp, long offset, int origin);
```

| `origin` | Meaning |
|---|---|
| `SEEK_SET` | Offset measured from the beginning of the file |
| `SEEK_CUR` | From the current position |
| `SEEK_END` | From the end of the file |

Returns 0 on success. Example: jump to the 4th `int` (index 3):

```c
fseek(fp, 3 * (long)sizeof(int), SEEK_SET);
```

For text files only `SEEK_SET` with a value from `ftell`, or offset 0, is reliably portable; random access works best with **binary** files of fixed-size records.

### 1.2 `ftell()`

```c
long ftell(FILE *fp);
```

Returns the current position in bytes from the beginning of the file (or -1 on error).

### 1.3 `rewind()`

```c
void rewind(FILE *fp);
```

Moves the position back to the start of the file.

Tested: [Program 50: Random Access](../../Programs/Program-50-Random-Access-fseek-ftell/README.md).

### 1.4 Finding a Record by Number

If each record has `sizeof(struct Record)` bytes, record number `k` (counting from 0) starts at byte `k * sizeof(struct Record)`:

```c
fseek(fp, k * (long)sizeof(struct Record), SEEK_SET);
fread(&r, sizeof(struct Record), 1, fp);
```

## 2. Error Handling in File Operations

Operations on files can fail: the file may be missing, the disk may be full, permissions may be wrong. A robust program **checks** results.

### 2.1 Check the Return Value of `fopen`

```c
FILE *fp = fopen("report.txt", "r");
if (fp == NULL) {
    perror("report.txt");      /* prints: report.txt: No such file or directory */
    return 1;
}
```

`perror(msg)` prints `msg`, a colon, and the system's description of the last error. (The exact wording depends on the system.) It writes to the **standard error** stream.

### 2.2 `feof()` and `ferror()`

| Function | Returns non-zero when |
|---|---|
| `feof(fp)` | The end of the file has been reached |
| `ferror(fp)` | A read or write error occurred |
| `clearerr(fp)` | (Clears both indicators) |

```c
while ((ch = fgetc(fp)) != EOF)
    count++;

if (ferror(fp))
    printf("A read error occurred.\n");
else if (feof(fp))
    printf("End of file reached.\n");
```

**Common mistake:** `while (!feof(fp))` as the loop test. `feof` becomes true only **after** a read tries to go past the end, so the loop runs once too often. Test the return value of the read function instead (`fgets(...) != NULL`, `fscanf(...) == 3`, `fgetc(...) != EOF`).

### 2.3 Other Checks
- `fread`/`fwrite` return the number of items transferred; compare with the count requested.
- `fclose` returns 0 on success.
- The standard header `<errno.h>` provides `errno` for error codes.

Tested: [Program 51: File Error Handling](../../Programs/Program-51-File-Error-Handling/README.md).

## 3. Exam-Oriented Answers

### 5-mark: Explain `fseek()`, `ftell()` and `rewind()`.
Syntax and purpose of each, the `origin` table, and the example jumping to a record.

### 5-mark: How is error handling done in file operations?
`NULL` check after `fopen`, `perror`, `feof`, `ferror`, return values of `fread`/`fwrite`, and the loop-test advice.

### 10-mark: Explain random access files with a program.
Define sequential vs random access, the three functions, record-position formula, and present Program 50 with its tested output.

## 4. Summary

`fseek`, `ftell` and `rewind` move and report the file position, enabling random access to fixed-size records. Reliable programs check `fopen` for `NULL`, test read results, and use `perror`, `feof` and `ferror` to report problems.

---

[Previous: Formatted, Character and Direct I/O](Topic-03-Formatted-Character-and-Direct-IO.md) | [Back to Unit Introduction](Introduction.md)
