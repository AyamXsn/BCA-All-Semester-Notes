# Memory Management

## 1. Role
Memory management tracks memory use, allocates and frees regions, protects address spaces, and supports virtual memory.

## 2. Contiguous allocation
A process may occupy one contiguous region. Fixed partitions can waste space internally; variable partitions can suffer external fragmentation.

## 3. Paging
Virtual memory is divided into pages and physical memory into frames. A page table maps virtual page numbers to frame numbers. Paging avoids external fragmentation in physical allocation but can cause internal fragmentation.

## 4. Segmentation
Segmentation divides an address space into logical variable-sized units such as code, data, and stack. It reflects program structure but may suffer external fragmentation.

## 5. Virtual memory
Virtual memory gives processes an address-space abstraction larger than available physical RAM. Demand paging loads pages when needed. A page fault occurs when a required page is not currently mapped as present.

## 6. Page replacement
FIFO, LRU, and optimal are common teaching algorithms. Optimal is a theoretical benchmark because it requires future knowledge.

## 7. Exercises
Translate a virtual address using a page table and page size. Trace FIFO and LRU replacement for a reference string.
