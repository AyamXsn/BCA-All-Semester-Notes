# Processes and Threads

## 1. Process
A process is a program in execution with its own execution context and resources. A process typically has an address space, program counter, registers, and OS-managed metadata.

## 2. Process states
A simplified model includes new, ready, running, waiting/blocked, and terminated. State transitions occur due to scheduling, I/O, interrupts, and completion.

## 3. Thread
A thread is an execution path within a process. Threads in the same process commonly share code, data, and open resources but have separate stacks and register contexts.

## 4. Context switch
The OS saves the state of one execution context and restores another. Switching enables multitasking but has overhead.

## 5. Inter-process communication
Processes can communicate through pipes, message queues, shared memory, sockets, and other mechanisms. Shared memory is fast but requires synchronization.

## 6. Synchronization
Mutexes, semaphores, condition variables, and monitors coordinate concurrent access. Incorrect synchronization can cause races or deadlocks.

## 7. Exercises
Draw process state transitions. Compare processes and threads. Give an example of a race condition and explain a mutex-based solution.
