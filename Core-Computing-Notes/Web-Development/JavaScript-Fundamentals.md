# JavaScript Fundamentals

## 1. JavaScript
JavaScript is a programming language widely used in browsers and also in server-side runtimes such as Node.js.

## 2. Variables
Use `const` for bindings that are not reassigned and `let` for bindings that are reassigned. Avoid `var` in new code unless its function-scoping behaviour is specifically needed.

## 3. Types
Primitive types include string, number, bigint, boolean, undefined, symbol, and null. Objects include arrays and functions. JavaScript is dynamically typed.

## 4. Functions and arrays
```js
const values = [3, 5, 8];
const doubled = values.map(value => value * 2);
console.log(doubled);
```

## 5. DOM
The Document Object Model represents a document as objects that scripts can inspect and update. Use event listeners to respond to user actions.

## 6. Asynchronous work
Promises represent eventual completion/failure. `async`/`await` provides syntax for working with promises. Handle errors with `try`/`catch` where appropriate.

## 7. Security
Avoid inserting untrusted strings as HTML. Prefer safe text APIs, validate on the server, and protect sensitive operations against cross-site scripting and request-forgery risks.

## 8. Exercise
Create a form that validates a required field and displays a result without reloading the page.
