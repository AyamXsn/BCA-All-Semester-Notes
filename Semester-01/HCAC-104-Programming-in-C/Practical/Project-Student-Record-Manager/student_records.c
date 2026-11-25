/*
 * Program : Student Record Manager (mini project)
 * Uses    : structures, functions, loops, switch, binary file I/O
 * Stores  : records in the binary file "students.dat" (kept between runs)
 */
#include <stdio.h>

#define FILE_NAME "students.dat"

struct Student {
    int roll;
    char name[40];
    float marks;
};

/* Look for a roll number in the file; return 1 and fill *out if found. */
static int find_student(int roll, struct Student *out)
{
    struct Student s;
    FILE *fp = fopen(FILE_NAME, "rb");

    if (fp == NULL)
        return 0;
    while (fread(&s, sizeof s, 1, fp) == 1) {
        if (s.roll == roll) {
            *out = s;
            fclose(fp);
            return 1;
        }
    }
    fclose(fp);
    return 0;
}

static void add_student(void)
{
    struct Student s, existing;
    FILE *fp;

    printf("Roll: ");
    if (scanf("%d", &s.roll) != 1) { printf("Invalid roll.\n"); return; }
    if (find_student(s.roll, &existing)) {
        printf("Roll %d already exists.\n", s.roll);
        return;
    }
    printf("Name (one word): ");
    if (scanf("%39s", s.name) != 1) { printf("Invalid name.\n"); return; }
    printf("Marks: ");
    if (scanf("%f", &s.marks) != 1) { printf("Invalid marks.\n"); return; }

    fp = fopen(FILE_NAME, "ab");
    if (fp == NULL) {
        printf("Cannot open %s for writing.\n", FILE_NAME);
        return;
    }
    fwrite(&s, sizeof s, 1, fp);
    fclose(fp);
    printf("Saved.\n");
}

static void list_students(void)
{
    struct Student s;
    int count = 0;
    FILE *fp = fopen(FILE_NAME, "rb");

    if (fp == NULL) {
        printf("No records yet.\n");
        return;
    }
    printf("%-6s %-20s %s\n", "Roll", "Name", "Marks");
    while (fread(&s, sizeof s, 1, fp) == 1) {
        printf("%-6d %-20s %.1f\n", s.roll, s.name, s.marks);
        count++;
    }
    fclose(fp);
    printf("Total records: %d\n", count);
}

static void search_student(void)
{
    int roll;
    struct Student s;

    printf("Roll to search: ");
    if (scanf("%d", &roll) != 1) { printf("Invalid roll.\n"); return; }
    if (find_student(roll, &s))
        printf("Found: %d %s %.1f\n", s.roll, s.name, s.marks);
    else
        printf("Roll %d not found.\n", roll);
}

int main(void)
{
    int choice;

    do {
        printf("\n1. Add student\n2. List students\n3. Search by roll\n0. Exit\nChoice: ");
        if (scanf("%d", &choice) != 1) {
            printf("Invalid input.\n");
            return 1;
        }
        switch (choice) {
        case 1: add_student(); break;
        case 2: list_students(); break;
        case 3: search_student(); break;
        case 0: printf("Goodbye.\n"); break;
        default: printf("Wrong choice.\n");
        }
    } while (choice != 0);
    return 0;
}
