#include <stdio.h>

int main(void) {
    int first, second;

    printf("Enter two integers: ");
    if (scanf("%d %d", &first, &second) != 2) {
        fprintf(stderr, "Invalid input.\n");
        return 1;
    }

    printf("Sum = %d\n", first + second);
    return 0;
}

/* Build: gcc -std=c11 -Wall -Wextra sum_two_numbers.c -o sum_two_numbers
   Sample input: 12 8
   Sample output: Sum = 20
*/
