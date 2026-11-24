# Database Concepts and Architecture

## 1. Database
A database is an organized collection of related data. A database management system (DBMS) provides facilities to define, store, query, update, secure, and recover data.

## 2. Why use a DBMS?
A DBMS can reduce uncontrolled duplication, support concurrent access, enforce constraints, provide access control, and support backup/recovery. It also introduces administration and resource overhead.

## 3. Three-schema idea
- External level: user/application views.
- Conceptual level: overall logical structure.
- Internal level: physical storage details.

Data independence means changes at one level can be isolated from other levels to a useful extent.

## 4. Database users
Database administrators manage security, availability, performance, backup, and recovery. Designers model data. Developers build applications and queries. End users use database-backed systems.

## 5. Data models
Common models include relational, document, key-value, graph, and object-oriented approaches. The relational model represents data using relations (tables).

## 6. Exercises
Explain the difference between a DBMS and a database. Draw a three-schema architecture diagram and identify the responsibilities of a DBA.
