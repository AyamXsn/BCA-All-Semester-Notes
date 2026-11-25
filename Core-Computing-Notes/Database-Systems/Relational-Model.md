# Relational Model and Keys

## 1. Relation
In the relational model, data is represented in relations, commonly displayed as tables. A row is a tuple; a column is an attribute. Each attribute has a domain of permitted values.

## 2. Keys
- Superkey: attributes that uniquely identify a tuple.
- Candidate key: a minimal superkey.
- Primary key: chosen candidate key.
- Foreign key: attribute(s) referencing a candidate key in another or the same relation.
- Composite key: key containing multiple attributes.

## 3. Integrity constraints
Entity integrity requires a primary key to be unique and non-null. Referential integrity requires foreign-key values to match referenced keys or be null where allowed. Domain constraints restrict permitted values.

## 4. Example schema
`STUDENT(student_id, full_name, email)` where `student_id` is primary key.
`ENROLLMENT(student_id, course_id, enrolled_on)` where student_id references STUDENT.

## 5. Relationships
One-to-one, one-to-many, and many-to-many relationships describe cardinality. A many-to-many relationship is commonly implemented using a junction table.

## 6. Exercises
Identify candidate keys in a sample relation. Design tables for students, courses, and enrolments while enforcing referential integrity.
