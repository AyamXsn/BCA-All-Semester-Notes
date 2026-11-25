# Programming Exercises - HCAC-104 Programming in C

Practice problems for each unit. Try them yourself first. For a model approach, study the tested program mentioned in each hint. Compile with `gcc -Wall -Wextra -o program file.c` and test with several inputs, including unusual ones (zero, negative numbers, empty input).

[Back to subject](../README.md)

## Unit I: Programming Concepts

1. Write the algorithm and draw a flowchart to find the sum of the first n natural numbers.
2. Write pseudocode to check whether a number is positive, negative or zero.
3. Draw a flowchart for a program that reads marks and prints "Pass" if marks are at least 40, otherwise "Fail".

## Unit II: Introduction to C

4. Read the length and width of a rectangle and print its area and perimeter. *Hint: [Program 04](../Programs/Program-04-Area-and-Circumference-of-Circle/README.md).*
5. Convert a temperature from Celsius to Fahrenheit (`F = C * 9 / 5 + 32`). Watch out for integer division.
6. Read a three-digit number and print the sum of its digits using `%` and `/`.
7. Read two integers and swap them using a temporary variable, then without one.
8. Print the ASCII code of a character typed by the user.
9. Read the principal, rate and time and print simple interest.

## Unit III: Control Structure

10. Read three numbers and print them in ascending order using `if`.
11. Check whether a year is a leap year (divisible by 4, but century years must be divisible by 400).
12. Print the multiplication table of a number up to 10. *Hint: [Program 14](../Programs/Program-14-Factorial-using-for-Loop/README.md).*
13. Check whether a number is an Armstrong number (for example 153 = 1^3 + 5^3 + 3^3).
14. Print the sum of all even numbers from 1 to n.
15. Print an inverted star triangle and a pyramid. *Hint: [Program 19](../Programs/Program-19-Star-Triangle-Pattern/README.md).*
16. Write a menu-driven program with options for area of a circle, area of a rectangle and exit. *Hint: [Program 16](../Programs/Program-16-Menu-Driven-Program-do-while/README.md).*

## Unit IV: Function

17. Write a function `is_prime(int n)` that returns 1 or 0 and use it to print all primes up to 50.
18. Write a function that returns the largest of three integers.
19. Write a recursive function to compute the sum of the digits of a number.
20. Write a recursive function to compute x raised to the power n.
21. Write a function using pointers that returns both the quotient and the remainder of two integers. *Hint: [Program 24](../Programs/Program-24-Call-by-Reference-Swap/README.md).*

## Unit V: Array, Pointer and String

22. Reverse the elements of an array in place.
23. Search for a value in an array (linear search) and print its position.
24. Find the second largest element of an array.
25. Transpose a matrix. *Hint: [Program 30](../Programs/Program-30-Matrix-Addition/README.md).*
26. Find the sum of the diagonal elements of a square matrix.
27. Write your own `my_strlen` and `my_strcpy` functions without using `<string.h>`.
28. Count the words in a line of text. *Hint: [Program 34](../Programs/Program-34-Count-Vowels-and-Consonants/README.md).*
29. Use a pointer to print the elements of an array in reverse order. *Hint: [Program 36](../Programs/Program-36-Pointer-Arithmetic-and-Arrays/README.md).*

## Unit VI: Structure and Union

30. Create a structure for an employee (id, name, salary) and print the employee with the highest salary. *Hint: [Program 40](../Programs/Program-40-Array-of-Structures/README.md).*
31. Define a structure for a date and write a function that compares two dates.
32. Define a structure for a complex number and write functions to add and multiply two complex numbers.
33. Print the sizes of a structure and a union containing the same members and explain the difference. *Hint: [Program 43](../Programs/Program-43-Union-Demo/README.md).*

## Unit VII: File Handling

34. Read a text file and count its characters, words and lines.
35. Copy the contents of one file to another, converting all letters to upper case.
36. Store n student records in a text file and read them back. *Hint: [Program 48](../Programs/Program-48-Formatted-File-IO/README.md).*
37. Extend the [Student Record Manager](../Practical/Project-Student-Record-Manager/README.md) with a delete option or an edit-marks option.
38. Using `fseek`, read the last record of a binary file without reading the others. *Hint: [Program 50](../Programs/Program-50-Random-Access-fseek-ftell/README.md).*

## Unit VIII: Graphics

39. Draw a house (a rectangle, a triangle roof made of lines and a door) using BGI functions. Needs a BGI-compatible environment.
40. Draw three concentric circles with different colours.
