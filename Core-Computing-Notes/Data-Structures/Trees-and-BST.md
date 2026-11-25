# Trees and Binary Search Trees

## 1. Tree terminology
A tree is a hierarchical structure of nodes and edges. The root has no parent. A leaf has no children. A subtree is a node and its descendants. Height measures the longest downward path under a stated convention.

## 2. Binary tree
Each node has at most two children, often called left and right.

## 3. Binary search tree
For a BST with unique keys, keys in the left subtree are smaller than the node key and keys in the right subtree are larger. Search, insert, and delete take O(h), where h is tree height. A balanced tree has h = O(log n); an unbalanced tree can degrade to O(n).

## 4. Traversals
- Preorder: node, left, right.
- Inorder: left, node, right.
- Postorder: left, right, node.
- Level order: visit by depth using a queue.

## 5. Balanced trees
AVL and red-black trees maintain balance conditions so operations remain logarithmic in height.

## 6. Exercises
Draw a BST after inserting a sequence of keys. Write recursive traversals and search. Explain why sorted insertion can create a skewed tree.
