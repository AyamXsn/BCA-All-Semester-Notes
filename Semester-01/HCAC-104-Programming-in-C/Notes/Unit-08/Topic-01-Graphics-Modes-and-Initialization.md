# Topic 1: Graphics Modes and Initialization

**Unit VIII | HCAC-104 Programming in C**

## 1. Introduction

A computer screen normally works in **text mode**, showing characters in a grid. To draw lines, circles and colours, the program switches the screen to **graphics mode**, where the display is a grid of tiny dots called **pixels**.

## 2. Screen Coordinates

- The screen is a grid of pixels.
- The origin `(0, 0)` is the **top-left** corner.
- `x` increases to the right and `y` increases **downward**.
- On a 640 x 480 screen the bottom-right pixel is `(639, 479)`.

```text
(0,0) ------------------> x
  |
  |
  v
  y
```

## 3. Graphics Drivers and Modes

A **graphics driver** is the code that talks to a type of display adapter. A **graphics mode** selects the resolution and number of colours for that driver. In Turbo C's BGI library, examples of drivers are CGA, EGA and VGA.

| Driver (BGI) | Typical use | Example resolution and colours |
|---|---|---|
| CGA | Old low-resolution adapters | 320 x 200, 4 colours |
| EGA | Enhanced adapters | 640 x 350, 16 colours |
| VGA | Common standard in BGI programs | 640 x 480, 16 colours |

Instead of choosing a driver by hand, a program can use the constant **`DETECT`**, which asks the library to pick the best driver and highest mode available.

## 4. Initializing Graphics: `initgraph()`

```c
void initgraph(int *graphdriver, int *graphmode, char *pathtodriver);
```

| Argument | Meaning |
|---|---|
| `graphdriver` | Address of an `int` holding the driver number (set it to `DETECT` for auto-detection) |
| `graphmode` | Address of an `int` that receives (or holds) the mode |
| `pathtodriver` | Folder containing the BGI driver files; `""` means the current folder |

```c
int gd = DETECT, gm;
initgraph(&gd, &gm, "");        /* or "C:\\TC\\BGI" in classic Turbo C */
```

## 5. Checking for Errors: `graphresult()`

```c
if (graphresult() != grOk) {
    printf("Graphics error\n");
    return 1;
}
```

`graphresult()` returns `grOk` when the last graphics operation succeeded; otherwise it returns an error code (for example when the driver file is not found).

## 6. Leaving Graphics Mode: `closegraph()`

`closegraph()` shuts down the graphics system and returns the screen to text mode. `getch()` (from `<conio.h>`) is used before it to pause until a key is pressed so the drawing stays visible.

## 7. Typical Program Skeleton

```c
#include <graphics.h>
#include <conio.h>

int main(void)
{
    int gd = DETECT, gm;

    initgraph(&gd, &gm, "");
    /* drawing statements go here */
    getch();
    closegraph();
    return 0;
}
```

## 8. Useful Query Functions

| Function | Returns |
|---|---|
| `getmaxx()` | Largest x coordinate of the current mode |
| `getmaxy()` | Largest y coordinate |
| `getmaxcolor()` | Largest colour value |

## 9. Exam-Oriented Answers

### 5-mark: What is a graphics mode? Explain how graphics is initialized in C.
Text mode vs graphics mode, pixels and coordinates, `DETECT`, the syntax and arguments of `initgraph`, the `graphresult` check, `closegraph`, and the skeleton program.

### 5-mark: Explain `initgraph()` and `closegraph()`.
Give the syntax, the argument table and the role of each.

## 10. Summary

Graphics mode treats the screen as a grid of pixels with the origin at the top-left. A BGI program calls `initgraph` (usually with `DETECT`), checks `graphresult`, draws, waits for a key and calls `closegraph`.

---

[Back to Unit Introduction](Introduction.md) | [Next: Graphics Functions](Topic-02-Graphics-Functions.md)
