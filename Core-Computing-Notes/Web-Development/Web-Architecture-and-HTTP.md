# Web Architecture and HTTP

## 1. Web architecture
A browser (client) requests resources from a server. The server may execute application logic and query databases before returning a response. Modern applications can also use APIs and distributed services.

## 2. URL
A URL can contain a scheme, host, port, path, query, and fragment. The fragment is processed by the client and is not sent as part of the HTTP request target in the usual browser request.

## 3. HTTP
HTTP is a stateless application protocol. Requests include a method, target, headers, and optional body. Responses include a status code, headers, and optional body.

## 4. Common methods
GET retrieves a representation. POST submits data or requests processing. PUT replaces a resource representation. PATCH applies partial modification. DELETE requests removal. Actual semantics depend on server implementation and HTTP standards.

## 5. Status code classes
- 1xx informational
- 2xx success
- 3xx redirection
- 4xx client error
- 5xx server error

## 6. Cookies and sessions
HTTP cookies can store small client-side values and identifiers. A server-side session commonly stores session data on the server and uses a cookie to associate requests with it. Protect session identifiers and configure secure cookie attributes.
