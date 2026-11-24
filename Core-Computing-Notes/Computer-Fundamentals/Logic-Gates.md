# Logic Gates and Boolean Algebra

## 1. Boolean variables
Boolean variables take one of two values: 0/false or 1/true. Boolean algebra describes logical operations used in digital circuits and program conditions.

## 2. Fundamental gates
- AND: output is 1 only when every input is 1.
- OR: output is 1 when at least one input is 1.
- NOT: reverses the input.
- NAND: NOT of AND.
- NOR: NOT of OR.
- XOR: output is 1 when inputs differ.
- XNOR: output is 1 when inputs are equal.

## 3. Two-input truth table
| A | B | AND | OR | NAND | NOR | XOR | XNOR |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 0 | 0 | 1 | 1 | 0 | 1 |
| 0 | 1 | 0 | 1 | 1 | 0 | 1 | 0 |
| 1 | 0 | 0 | 1 | 1 | 0 | 1 | 0 |
| 1 | 1 | 1 | 1 | 0 | 0 | 0 | 1 |

## 4. Important laws
- Identity: A+0=A; A·1=A.
- Domination: A+1=1; A·0=0.
- Idempotent: A+A=A; A·A=A.
- Complement: A+Ā=1; A·Ā=0.
- Commutative: A+B=B+A; AB=BA.
- De Morgan: ̅(A·B)=Ā+B̄; ̅(A+B)=Ā·B̄.

Here `+` denotes OR, `·` denotes AND, and bar denotes NOT.

## 5. Combinational and sequential circuits
Combinational circuit output depends on current inputs. Sequential circuit output can also depend on stored state, often represented by flip-flops or registers.

## 6. Applications
Logic gates form arithmetic units, comparators, control circuits, memory elements, and digital communication hardware.

## 7. Exercise
Construct a truth table for \(Y=(A · B)+̅C\). Simplify a Boolean expression using De Morgan's laws.

## 8. Summary
Logic gates implement Boolean operations physically. Truth tables and Boolean laws help design and simplify digital circuits.
