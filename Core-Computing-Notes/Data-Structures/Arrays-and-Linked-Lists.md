# Arrays and Linked Lists

## 1. Array
An array stores elements in indexed positions, commonly in contiguous memory. Index access is typically O(1). Searching an unsorted array is O(n); insertion in the middle may require shifting O(n) elements.

## 2. Linked list
A linked list consists of nodes containing data and link(s) to other nodes. A singly linked node points to the next node; a doubly linked node also points backward.

## 3. Comparison
| Feature | Array | Linked list |
|---|---|---|
| Indexed access | O(1) | O(n) |
| Search unsorted | O(n) | O(n) |
| Insert at known position | May shift elements | O(1) link changes once node is known |
| Memory overhead | Low per element | Pointer(s) per node |
| Locality | Usually good | Usually weaker |

## 4. Applications
Arrays suit indexed collections and matrices. Linked lists can suit workloads with frequent local insertions/deletions when node references are already available.

## 5. Exercises
Implement traversal, search, insertion, and deletion for a singly linked list. Compare array and linked-list performance for a chosen workload.
