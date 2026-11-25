# Unit VII: Input Output and File Handling

**Subject:** HCAC-104 Programming in C | **Semester:** 1 | **Allotted time (official):** 5 hours

## 1. What This Unit Covers

Official syllabus topics: file handling concepts and access methods, `fopen`, `fclose`, `fflush`, `freopen`, formatted, character and direct I/O, random access, and error handling.

## 2. Topic Files

| # | Topic | File |
|---|---|---|
| 1 | File handling concepts and access methods | [Topic-01-File-Handling-Concepts.md](Topic-01-File-Handling-Concepts.md) |
| 2 | `fopen`, `fclose`, `fflush`, `freopen` and file modes | [Topic-02-File-Functions-and-Modes.md](Topic-02-File-Functions-and-Modes.md) |
| 3 | Formatted, character and direct I/O | [Topic-03-Formatted-Character-and-Direct-IO.md](Topic-03-Formatted-Character-and-Direct-IO.md) |
| 4 | Random access and error handling | [Topic-04-Random-Access-and-Error-Handling.md](Topic-04-Random-Access-and-Error-Handling.md) |

## 3. Tested Programs for This Unit

| Program | Shows |
|---|---|
| [44 Write a Text File](../../Programs/Program-44-Write-to-a-Text-File/README.md) | `fopen("w")`, `fprintf`, `fputs` |
| [45 Read a Text File](../../Programs/Program-45-Read-from-a-Text-File/README.md) | `fgets` loop |
| [46 Append](../../Programs/Program-46-Append-to-a-Text-File/README.md) | Mode `"a"` |
| [47 Copy a File](../../Programs/Program-47-Copy-a-File-Character-by-Character/README.md) | `fgetc`, `fputc` |
| [48 Formatted File I/O](../../Programs/Program-48-Formatted-File-IO/README.md) | `fprintf`, `fscanf` |
| [49 Binary Records](../../Programs/Program-49-Binary-File-fwrite-fread/README.md) | `fwrite`, `fread` |
| [50 Random Access](../../Programs/Program-50-Random-Access-fseek-ftell/README.md) | `fseek`, `ftell`, `rewind` |
| [51 Error Handling](../../Programs/Program-51-File-Error-Handling/README.md) | `NULL` check, `perror`, `feof`, `ferror` |

## 4. Summary

Files let programs keep data after they end. C reads and writes files through a `FILE *` pointer using a family of functions for text, characters, and binary blocks, with support for jumping to any position.

---

[Back to subject](../../README.md)
