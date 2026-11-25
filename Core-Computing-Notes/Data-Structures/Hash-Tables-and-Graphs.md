# Hash Tables and Graphs

## 1. Hash table
A hash table maps keys to storage positions using a hash function. Collisions occur when different keys map to the same position.

## 2. Collision handling
- Chaining stores multiple entries in a bucket, often using a list.
- Open addressing searches for another slot using probing.
Load factor is the number of stored entries divided by table capacity. Resizing may reduce high load.

## 3. Graph
A graph consists of vertices and edges. It can be directed/undirected and weighted/unweighted.

## 4. Representations
- Adjacency matrix: O(V²) storage; edge lookup is O(1).
- Adjacency list: O(V+E) storage; efficient for sparse graphs.

## 5. Traversal
Breadth-first search (BFS) uses a queue. Depth-first search (DFS) uses recursion or an explicit stack. Both take O(V+E) with adjacency lists.

## 6. Applications
Routing, dependency analysis, social networks, maps, recommendation systems, and scheduling.

## 7. Exercises
Represent a small directed graph in both forms. Trace BFS and DFS from a selected vertex.
