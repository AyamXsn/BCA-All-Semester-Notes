# Normalization and Transactions

## 1. Normalization
Normalization organizes relations to reduce redundancy and avoid update anomalies. It is based on dependencies and candidate keys.

## 2. Anomalies
- Insertion anomaly: a fact cannot be stored without an unrelated fact.
- Update anomaly: the same fact must be changed in multiple rows.
- Deletion anomaly: removing one fact accidentally removes another.

## 3. Normal forms
- 1NF: attributes contain atomic values under the chosen relational design; no repeating groups.
- 2NF: 1NF and no non-prime attribute depends on only part of a candidate key.
- 3NF: 2NF and no inappropriate transitive dependency of non-prime attributes on candidate keys; formal definitions use functional dependencies.
- BCNF: every determinant of a non-trivial functional dependency is a superkey.

## 4. Transactions
A transaction is a logical unit of database work. ACID properties:
- Atomicity: all-or-nothing.
- Consistency: preserves constraints.
- Isolation: concurrent transactions behave according to the isolation guarantees.
- Durability: committed changes persist according to system guarantees.

## 5. Concurrency and recovery
Locks, multiversion concurrency control, logs, checkpoints, and recovery procedures help coordinate concurrent access and restore consistent state. Isolation levels trade off concurrency and anomalies.

## 6. Exercises
Normalize an enrolment table using stated functional dependencies. Explain dirty reads, non-repeatable reads, and lost updates.
