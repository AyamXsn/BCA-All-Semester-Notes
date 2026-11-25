# Control Structures

## 1. Sequence
Statements execute in order unless control flow is changed.

## 2. Selection
Selection chooses a path based on a condition. Common constructs are `if`, `if-else`, nested conditions, and `switch`/`match` depending on language.

Example:
```python
score = 72
if score >= 40:
    print("Pass")
else:
    print("Try again")
```

## 3. Iteration
Loops repeat statements:
- `for`: commonly used when iterating over a sequence or known range.
- `while`: repeats while a condition remains true.
- do-while: checks the condition after the loop body in languages that support it.

## 4. Loop control
`break` exits a loop. `continue` skips to the next iteration. Use them when they make the control flow clearer.

## 5. Nested loops
A loop inside another loop is a nested loop. If both run n times, the body may run n² times.

## 6. Common errors
- Off-by-one boundaries.
- Conditions that never become false.
- Incorrect loop variable updates.
- Accidental assignment instead of comparison in languages where syntax permits it.

## 7. Exercises
Print a multiplication table, sum the first n positive integers, count digits in an integer, and generate a pattern using nested loops.
