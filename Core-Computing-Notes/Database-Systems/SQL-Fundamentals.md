# SQL Fundamentals

SQL is a language used with relational database systems. Exact syntax and supported features vary by DBMS.

## 1. Categories
- DDL: define structures (`CREATE`, `ALTER`, `DROP`).
- DML: modify rows (`INSERT`, `UPDATE`, `DELETE`).
- DQL: query data (`SELECT`, commonly grouped with DML in practice).
- DCL: permissions (`GRANT`, `REVOKE`, where supported).
- TCL: transaction control (`COMMIT`, `ROLLBACK`, `SAVEPOINT`).

## 2. Example
```sql
CREATE TABLE Student (
    student_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    semester INTEGER CHECK (semester BETWEEN 1 AND 8)
);

INSERT INTO Student (student_id, name, semester)
VALUES (1, 'Asha', 1);

SELECT student_id, name
FROM Student
WHERE semester = 1
ORDER BY name;
```

## 3. Filtering and grouping
`WHERE` filters rows before grouping. `GROUP BY` forms groups. `HAVING` filters groups. Aggregate functions include `COUNT`, `SUM`, `AVG`, `MIN`, and `MAX`.

## 4. Joins
- INNER JOIN returns matching rows.
- LEFT JOIN returns all left rows plus matches from the right.
- RIGHT/FULL joins depend on DBMS support.
- CROSS JOIN forms combinations.

## 5. NULL
NULL represents missing/unknown/not-applicable data, not zero or an empty string. Use `IS NULL` and `IS NOT NULL`; comparisons with NULL use three-valued logic.

## 6. Exercises
Create two related tables, insert sample rows, query with a join, group by a category, and test a foreign-key constraint.
