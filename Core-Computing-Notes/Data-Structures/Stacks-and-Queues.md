# Stacks and Queues

## 1. Stack
A stack follows Last In, First Out (LIFO). Operations:
- push: add to top.
- pop: remove top.
- peek/top: inspect top.
A stack can be implemented using an array or linked list.

## 2. Queue
A queue follows First In, First Out (FIFO). Operations:
- enqueue: add at rear.
- dequeue: remove at front.
- front/peek: inspect next item.

## 3. Circular queue
A circular queue reuses array positions by wrapping indices around with modulo arithmetic. It avoids wasting space after repeated dequeue operations.

## 4. Priority queue
A priority queue removes elements according to priority rather than insertion order. A heap is a common implementation.

## 5. Applications
Stacks: function calls, undo, expression parsing, depth-first search. Queues: scheduling, buffering, breadth-first search, service systems.

## 6. Exercises
Convert an infix expression to postfix, validate balanced brackets, and simulate a queue of service requests.
