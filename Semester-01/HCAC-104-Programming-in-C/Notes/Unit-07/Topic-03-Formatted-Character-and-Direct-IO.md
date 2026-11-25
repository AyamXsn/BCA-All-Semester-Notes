# Topic 3: Formatted, Character and Direct I/O

**Unit VII | HCAC-104 Programming in C**

## 1. Overview

| Category | Functions | Works on |
|---|---|---|
| Formatted I/O | `fprintf`, `fscanf` | Text with format specifiers |
| Character I/O | `fgetc`, `fputc`, `getc`, `putc` | One character at a time |
| String (line) I/O | `fgets`, `fputs` | Lines of text |
| Direct (block) I/O | `fread`, `fwrite` | Blocks of bytes, usually binary |

## 2. Formatted I/O

```c
fprintf(fp, "%d %s %.1f\n", roll, name, marks);     /* write */
int n = fscanf(fp, "%d %49s %f", &roll, name, &marks);  /* read */
```

- Works exactly like `printf` and `scanf`, but on a file.
- `fscanf` returns the number of items read, or `EOF` at the end. The loop `while (fscanf(...) == 3)` reads records until the end.

Tested: [Program 48: Formatted File I/O](../../Programs/Program-48-Formatted-File-IO/README.md).

## 3. Character I/O

```c
int ch;                         /* int, not char, so EOF can be detected */
while ((ch = fgetc(fp)) != EOF)
    putchar(ch);

fputc('A', fp);
```

- `fgetc(fp)` returns the next character or `EOF`.
- `fputc(ch, fp)` writes one character.
- `getc`/`putc` are similar (often implemented as macros).

Tested: [Program 47: Copy a File](../../Programs/Program-47-Copy-a-File-Character-by-Character/README.md).

## 4. Line I/O

```c
char line[200];
while (fgets(line, sizeof line, fp) != NULL)
    fputs(line, stdout);
```

`fgets` reads at most `size - 1` characters, stops after a newline (and keeps it), and returns `NULL` at the end of the file. See [Program 45](../../Programs/Program-45-Read-from-a-Text-File/README.md).

## 5. Direct (Binary) I/O

```c
size_t fwrite(const void *ptr, size_t size, size_t count, FILE *fp);
size_t fread (void *ptr,       size_t size, size_t count, FILE *fp);
```

| Argument | Meaning |
|---|---|
| `ptr` | Address of the data in memory |
| `size` | Size of one item in bytes (`sizeof`) |
| `count` | Number of items |
| `fp` | The file |

Both return the number of **items** transferred; compare it with `count` to detect problems.

```c
struct Record r = {1, 55.5f};
fwrite(&r, sizeof(struct Record), 1, fp);       /* save */
fread(&r,  sizeof(struct Record), 1, fp);       /* load */
```

Open with `"wb"` / `"rb"`. Binary files store the exact in-memory layout, so they are compact and fast, but not human-readable and not portable between different systems.

Tested: [Program 49: Binary File fwrite and fread](../../Programs/Program-49-Binary-File-fwrite-fread/README.md).

## 6. Comparison

| Basis | `fprintf` / `fscanf` | `fputc` / `fgetc` | `fwrite` / `fread` |
|---|---|---|---|
| Unit | Formatted items | One character | Block of bytes |
| File type | Text | Text | Binary |
| Readable by humans | Yes | Yes | No |
| Speed for records | Slower (conversion) | Slowest for large data | Fastest |

## 7. Exam-Oriented Answers

### 5-mark: Explain `fprintf` and `fscanf` with an example.
Syntax, return value of `fscanf`, and the record example with output from Program 48.

### 5-mark: Explain `fread` and `fwrite`.
Syntax table, return values, binary mode, and an example saving a structure.

### 10-mark: Explain formatted, character and direct I/O functions used in file handling.
Overview table, each category with syntax and an example, comparison table, plus outputs from Programs 47 to 49.

## 8. Summary

Use `fprintf`/`fscanf` for formatted text, `fgetc`/`fputc` for single characters, `fgets`/`fputs` for lines, and `fread`/`fwrite` for blocks of binary data such as structures.

---

[Previous: File Functions and Modes](Topic-02-File-Functions-and-Modes.md) | [Next: Random Access and Error Handling](Topic-04-Random-Access-and-Error-Handling.md)
