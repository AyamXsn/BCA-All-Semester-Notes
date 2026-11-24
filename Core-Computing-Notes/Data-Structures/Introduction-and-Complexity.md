# Introduction to Data Structures and Complexity

## 1. Data structure
A data structure organizes data to support operations such as access, search, insertion, deletion, and traversal.

## 2. Abstract data type
An abstract data type (ADT) defines values and allowed operations without requiring a particular implementation. A stack ADT, for example, specifies push, pop, and peek.

## 3. Complexity
Time complexity describes growth in operation count; space complexity describes memory growth. Big-O is commonly used for asymptotic upper bounds.

| Complexity | Typical interpretation |
|---|---|
| O(1) | Constant |
| O(log n) | Logarithmic |
| O(n) | Linear |
| O(n log n) | Linearithmic |
| O(n²) | Quadratic |
| O(2ⁿ) | Exponential |

## 4. Trade-offs
An array provides fast indexed access but may be costly to resize. A linked list can insert after a known node efficiently but does not provide constant-time indexed access.

## 5. Choosing a structure
Consider operations, input size, memory constraints, ordering requirements, and expected update frequency.
