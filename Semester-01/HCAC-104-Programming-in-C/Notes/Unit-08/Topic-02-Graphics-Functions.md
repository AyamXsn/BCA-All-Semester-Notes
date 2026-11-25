# Topic 2: Graphics Functions

**Unit VIII | HCAC-104 Programming in C**

All functions below belong to the BGI `graphics.h` library (see the note in the [unit introduction](Introduction.md)).

## 1. Drawing Functions

| Function | Syntax | Draws |
|---|---|---|
| `putpixel` | `putpixel(x, y, color);` | One pixel |
| `line` | `line(x1, y1, x2, y2);` | A line between two points |
| `rectangle` | `rectangle(left, top, right, bottom);` | A rectangle outline |
| `circle` | `circle(x, y, radius);` | A circle with centre `(x, y)` |
| `arc` | `arc(x, y, startangle, endangle, radius);` | Part of a circle (angles in degrees, anticlockwise from the 3 o'clock direction) |
| `ellipse` | `ellipse(x, y, startangle, endangle, xradius, yradius);` | An ellipse or part of it |
| `bar` | `bar(left, top, right, bottom);` | A filled rectangle (no outline) |
| `drawpoly` | `drawpoly(numpoints, polypoints);` | A polygon outline from an array of points |

## 2. Colour and Style Functions

| Function | Purpose |
|---|---|
| `setcolor(color)` | Colour for lines and outlines |
| `setbkcolor(color)` | Background colour |
| `setfillstyle(pattern, color)` | Fill pattern and colour for `bar`, `floodfill` |
| `setlinestyle(style, pattern, thickness)` | Solid, dotted, dashed lines and thickness |
| `floodfill(x, y, bordercolor)` | Fill an enclosed area starting from `(x, y)` |
| `cleardevice()` | Clear the screen using the background colour |

The 16 basic colours are numbered 0 to 15: `BLACK`, `BLUE`, `GREEN`, `CYAN`, `RED`, `MAGENTA`, `BROWN`, `LIGHTGRAY`, `DARKGRAY`, `LIGHTBLUE`, `LIGHTGREEN`, `LIGHTCYAN`, `LIGHTRED`, `LIGHTMAGENTA`, `YELLOW`, `WHITE`.

## 3. Text Functions

| Function | Purpose |
|---|---|
| `outtext(string)` | Print text at the current position |
| `outtextxy(x, y, string)` | Print text at `(x, y)` |
| `settextstyle(font, direction, size)` | Choose font, direction and size |

## 4. Example: Drawing Basic Shapes

```c
#include <graphics.h>
#include <conio.h>

int main(void)
{
    int gd = DETECT, gm;
    initgraph(&gd, &gm, "");

    setcolor(YELLOW);
    line(50, 50, 250, 50);
    rectangle(50, 80, 250, 180);
    circle(400, 130, 50);
    outtextxy(60, 200, "BCA Graphics Demo");

    getch();
    closegraph();
    return 0;
}
```

This is [Program 52](../../Programs/Program-52-Graphics-Basic-Shapes/README.md) (not compiled in the authoring environment).

## 5. Example: A Filled Circle

```c
setcolor(RED);
circle(200, 200, 60);
setfillstyle(SOLID_FILL, RED);
floodfill(200, 200, RED);      /* fill inside the circle up to the RED border */
```

`floodfill` stops at pixels of the given border colour, so the outline colour and the border argument must match.

## 6. Exam-Oriented Answers

### 5-mark: Explain any five graphics functions of C.
Pick `line`, `rectangle`, `circle`, `setcolor`, `outtextxy`; give syntax, meaning of each argument and one example line.

### 5-mark: Write a program to draw a circle and a rectangle.
Use the skeleton from Topic 1 with `circle` and `rectangle` calls, and state that BGI (Turbo C or a compatible library) is required.

### 10-mark: Explain graphics in C with initialization and drawing functions.
Text vs graphics mode, coordinates, `initgraph`, `graphresult`, `closegraph`, drawing, colour and text function tables, and one complete program.

## 7. Summary

BGI offers functions to draw pixels, lines, rectangles, circles, arcs and ellipses, set colours and fill styles, and write text. A drawing program always follows the same pattern: initialize, draw, wait, close.

---

[Previous: Graphics Modes and Initialization](Topic-01-Graphics-Modes-and-Initialization.md) | [Back to Unit Introduction](Introduction.md)
