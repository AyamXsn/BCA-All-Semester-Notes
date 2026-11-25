# File Systems and Deadlocks

## 1. File system
A file system organizes persistent data into files and directories. It manages names, metadata, allocation, permissions, and recovery.

## 2. File allocation
Contiguous allocation offers good sequential access but can fragment. Linked allocation supports growth but makes random access slower. Indexed allocation uses an index structure to locate blocks.

## 3. Deadlock
A deadlock is a state where a set of processes wait indefinitely for resources held by one another.

## 4. Four necessary conditions
- Mutual exclusion.
- Hold and wait.
- No preemption.
- Circular wait.

All four must hold for a deadlock to occur in the classic model.

## 5. Handling deadlocks
- Prevention: break at least one necessary condition.
- Avoidance: allocate only if the system remains in a safe state.
- Detection and recovery: detect cycles/unsafe waits and recover.
- Ignore: used where the cost of handling is judged higher than the risk.

## 6. Exercises
Draw a resource-allocation graph and identify a possible cycle. Explain how ordering resources can prevent circular wait.
