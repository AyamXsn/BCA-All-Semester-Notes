# Secure Software Practices

## 1. Secure development
Security should be considered during requirements, design, coding, testing, deployment, and maintenance.

## 2. Input handling
Validate inputs on the server, use allowlists where practical, constrain lengths and types, and encode output for its context.

## 3. Injection prevention
Use parameterized SQL queries rather than building SQL by concatenating untrusted values. Avoid shell command construction from untrusted input.

## 4. Secrets
Do not commit passwords, API keys, or private keys. Use environment-specific secret management and rotate exposed credentials.

## 5. Dependencies
Use maintained dependencies, monitor known vulnerabilities, update deliberately, and review package sources.

## 6. Error handling and logging
Show users safe, useful error messages. Keep sensitive details out of public responses and logs. Protect logs from unauthorized access and tampering.

## 7. Exercise
Review a sample login/database workflow and list potential injection, credential, session, and information-disclosure risks.
