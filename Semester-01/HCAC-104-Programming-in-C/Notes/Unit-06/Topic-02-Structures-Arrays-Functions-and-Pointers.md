# Topic 2: Arrays of Structures, Structures with Functions and Pointer to Structure

**Unit VI | HCAC-104 Programming in C**

## 1. Array of Structures

### 1.1 Definition
An **array of structures** stores many records of the same structure type, such as all students of a class.

```c
struct Student st[50];

for (i = 0; i < n; i++)
    scanf("%d %49s %f", &st[i].roll, st[i].name, &st[i].marks);

printf("%s\n", st[2].name);       /* name of the third student */
```

Initialization:

```c
struct Student st[2] = { {1, "Ram", 70.0f}, {2, "Sita", 85.5f} };
```

Tested: [Program 40: Array of Structures](../../Programs/Program-40-Array-of-Structures/README.md), which finds the topper.

## 2. Structures and Functions

### 2.1 Passing a Structure by Value
The function receives a **copy**; the original is not changed.

```c
void print_point(struct Point p)
{
    printf("(%.1f, %.1f)\n", p.x, p.y);
}
```

### 2.2 Returning a Structure

```c
struct Point midpoint(struct Point a, struct Point b)
{
    struct Point m;
    m.x = (a.x + b.x) / 2;
    m.y = (a.y + b.y) / 2;
    return m;
}
```

### 2.3 Passing by Address
For large structures, or when the function must change the original, pass a pointer (next section). Passing by address avoids copying every member.

Tested: [Program 41: Structure and Function](../../Programs/Program-41-Structure-and-Function/README.md).

## 3. Pointer to Structure

### 3.1 Definition
A pointer can hold the address of a structure variable. Members are reached with the **arrow operator `->`**.

```c
struct Student s = {7, "Gita", 62.5f};
struct Student *p = &s;

printf("%d\n", p->roll);      /* same as (*p).roll */
p->marks = 70;
```

`p->marks` is shorthand for `(*p).marks`. The parentheses are needed because `.` binds tighter than `*`.

### 3.2 Modifying Through a Pointer

```c
void add_bonus(struct Student *p, float bonus)
{
    p->marks += bonus;
}
/* call: add_bonus(&s, 5.0f); */
```

Tested: [Program 42: Pointer to Structure](../../Programs/Program-42-Pointer-to-Structure/README.md).

## 4. Dot vs Arrow

| Operator | Used with | Example |
|---|---|---|
| `.` | A structure variable | `s.roll` |
| `->` | A pointer to a structure | `p->roll` |

## 5. Exam-Oriented Answers

### 5-mark: Explain array of structures with an example.
Definition, declaration, the read loop, and a program that finds the highest marks (Program 40).

### 5-mark: How are structures passed to functions?
By value (copy), by returning a structure, and by address with `->`; one short example each.

### 10-mark: Explain structures with arrays, functions and pointers.
Cover the three ideas with code, the dot vs arrow table and the outputs of Programs 40 to 42.

## 6. Summary

Arrays of structures hold many records. Structures can be passed or returned by value, or by pointer for efficiency and modification. Use `.` for variables and `->` for pointers.

---

[Previous: Structures](Topic-01-Structures.md) | [Next: Unions](Topic-03-Unions.md)
