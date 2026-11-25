# Topic 5: Pointers, Arrays and Functions

**Unit V | HCAC-104 Programming in C**

## 1. Arrays and Pointers

In most expressions the name of an array is converted to a pointer to its first element.

```c
int a[5] = {10, 20, 30, 40, 50};
int *p = a;         /* same as p = &a[0]; */
```

| Array notation | Pointer notation | Meaning |
|---|---|---|
| `a[i]` | `*(a + i)` | Element at index `i` |
| `&a[i]` | `a + i` | Address of element `i` |
| `p[i]` | `*(p + i)` | Pointer can also be indexed |

Tested: [Program 36](../../Programs/Program-36-Pointer-Arithmetic-and-Arrays/README.md), which prints the elements using both `*(p + i)` and `*p++`.

### 1.1 Differences Between an Array Name and a Pointer

| Basis | Array name | Pointer variable |
|---|---|---|
| Can be changed (`a++`) | No (fixed address) | Yes |
| `sizeof` | Size of the whole array | Size of a pointer |
| Memory | Reserved for all elements | Only space for an address |

## 2. Passing Arrays to Functions

An array argument is passed as a pointer to its first element, so:

1. The function can change the caller's array.
2. The size is **not** passed automatically, so pass it as another argument.

```c
int sum_array(const int arr[], int n);   /* same as const int *arr */
void double_all(int arr[], int n);
```

Use `const` when the function should only read the array.

Tested: [Program 37: Passing an Array to a Function](../../Programs/Program-37-Passing-an-Array-to-a-Function/README.md).

For 2D arrays, every dimension except the first must be given: `void show(int m[][3], int rows);`

## 3. Passing Strings to Functions

A string is a `char` array, so it is passed as `char *` (or `const char *` if read-only). The end is found with `'\0'`, so no size argument is needed.

```c
void to_upper(char *s)
{
    while (*s != '\0') {
        *s = (char)toupper((unsigned char)*s);
        s++;
    }
}
```

Tested: [Program 38](../../Programs/Program-38-Passing-a-String-to-a-Function/README.md).

## 4. Pointers and Strings

```c
char s[] = "Nepal";
char *p = s;
while (*p != '\0') {
    putchar(*p);
    p++;
}
```

## 5. Exam-Oriented Answers

### 5-mark: Explain the relationship between arrays and pointers.
State that the array name is the address of the first element, give the notation table, and the `p = a` example with `*(p + i)`.

### 5-mark: How are arrays passed to functions? Explain with an example.
Pointer to first element, size passed separately, changes affect the original; use Program 37.

### 10-mark: Explain pointers, arrays and strings and how they are passed to functions.
Combine the array/pointer equivalence table, differences table, array passing with `double_all`, string passing with `to_upper`, and conclude with the three tested programs 36 to 38.

## 6. Summary

An array name acts as the address of its first element, so `a[i]` equals `*(a + i)`. Arrays and strings are passed to functions as pointers, which means the function can modify the caller's data.

---

[Previous: Pointers](Topic-04-Pointers.md) | [Back to Unit Introduction](Introduction.md)
