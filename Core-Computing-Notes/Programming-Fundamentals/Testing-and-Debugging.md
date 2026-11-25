# Testing and Debugging

## 1. Software defect
A defect is an error in a program or its requirements/design. A failure is observable incorrect behaviour during execution.

## 2. Types of errors
- Syntax error: violates language grammar.
- Runtime error: occurs while the program runs.
- Logic error: program runs but produces the wrong result.
- Integration/interface error: components do not work together as expected.

## 3. Testing levels
- Unit testing: checks a small component.
- Integration testing: checks interactions between components.
- System testing: checks the complete system.
- Acceptance testing: evaluates whether user/business needs are met.

## 4. Test cases
A test case includes input, preconditions, expected result, and sometimes postconditions. Include normal, boundary, invalid, and exceptional inputs.

## 5. Debugging process
Reproduce the failure, isolate the cause, inspect state, form a hypothesis, make a minimal correction, and rerun relevant tests.

## 6. Example boundary tests
For a function accepting ages 0–120, test 0, 1, 120, 121, and invalid text if input is textual.

## 7. Exercises
Design tests for a calculator, login form, and function that returns the largest element in an array.
