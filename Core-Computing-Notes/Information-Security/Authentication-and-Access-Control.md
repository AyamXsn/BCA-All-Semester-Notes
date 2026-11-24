# Authentication and Access Control

## 1. Authentication
Authentication verifies a claimed identity. Factors include something you know, have, or are.

## 2. Multi-factor authentication
MFA combines two or more different factor categories. Two passwords are not two different factors.

## 3. Authorization
Authorization decides what an authenticated identity may do. Apply least privilege and deny by default where appropriate.

## 4. Access-control models
- DAC: resource owners can grant access.
- MAC: central policy/labels govern access.
- RBAC: permissions are assigned to roles.
- ABAC: decisions use attributes of subject, resource, action, and context.

## 5. Session security
Use unpredictable session identifiers, secure transport, appropriate cookie flags, expiration, rotation after privilege changes, and logout invalidation.

## 6. Exercise
Design roles and permissions for a learning portal with students, instructors, and administrators.
