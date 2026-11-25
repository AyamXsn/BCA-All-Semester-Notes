# Unit VIII: Introduction to Graphics

**Subject:** HCAC-104 Programming in C | **Semester:** 1 | **Allotted time (official):** 3 hours

## 1. What This Unit Covers

Official syllabus topics: graphics modes, initialization of graphics, and graphics functions.

## 2. Topic Files

| # | Topic | File |
|---|---|---|
| 1 | Graphics modes and initialization | [Topic-01-Graphics-Modes-and-Initialization.md](Topic-01-Graphics-Modes-and-Initialization.md) |
| 2 | Graphics functions | [Topic-02-Graphics-Functions.md](Topic-02-Graphics-Functions.md) |

## 3. Program for This Unit

[Program 52: Basic Shapes with graphics.h](../../Programs/Program-52-Graphics-Basic-Shapes/README.md) is included, but it is **not compiled or tested** in the authoring environment because `graphics.h` is not part of standard C. Read its README for how to run it.

## 4. Important Note About `graphics.h`

The graphics functions in this unit come from the **BGI (Borland Graphics Interface)** library of Turbo C/C++. They are not in the C standard library and are not available in GCC by default. To practise, use Turbo C/C++ (for example inside DOSBox) or install a compatible library such as WinBGIm or SDL_bgi. Exact setup differs between systems.

## 5. Summary

C programs can draw shapes by switching the screen to a graphics mode and calling drawing functions such as `line`, `rectangle` and `circle`.

---

[Back to subject](../../README.md)
