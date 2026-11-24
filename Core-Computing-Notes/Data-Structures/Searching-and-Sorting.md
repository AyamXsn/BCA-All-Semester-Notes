# Searching and Sorting

## 1. Linear search
Checks each item until a match is found or the sequence ends. Time: O(n); extra space: O(1) for an iterative version.

## 2. Binary search
Requires sorted data. Compare with the middle element and discard half the remaining search interval. Time: O(log n); iterative extra space: O(1).

## 3. Sorting overview
Sorting arranges values by a chosen order. Stability means equal-key items retain their relative order.

| Algorithm | Average time | Worst time | Stable (typical form) |
|---|---:|---:|---|
| Bubble sort | O(n²) | O(n²) | Yes |
| Insertion sort | O(n²) | O(n²) | Yes |
| Selection sort | O(n²) | O(n²) | Usually no |
| Merge sort | O(n log n) | O(n log n) | Yes |
| Quicksort | O(n log n) | O(n²) | Usually no |

## 4. Algorithm choice
Insertion sort can be effective for small or nearly sorted input. Merge sort offers predictable O(n log n) time but usually needs extra memory for arrays. Quicksort is often fast in practice but needs a strategy to avoid poor pivots.

## 5. Exercises
Trace binary search, implement insertion sort, and compare merge sort and quicksort on several input patterns.
