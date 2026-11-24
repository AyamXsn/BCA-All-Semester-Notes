# Stack Using Python

```python
stack = []

# Push
stack.append("A")
stack.append("B")

# Peek
print(stack[-1])  # B

# Pop
item = stack.pop()
print(item)       # B
print(stack)      # ['A']
```

A Python list supports append/pop at the end efficiently for a simple stack. A stack follows LIFO: last in, first out.

Exercise: use a stack to check whether brackets in a string are balanced.
