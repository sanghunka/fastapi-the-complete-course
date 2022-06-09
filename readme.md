# Section 5:Project 1 - Getting Started with FastAPI
## 48. FastAPI Project: Swagger, HTTP Request Methods, and Status Codes Overview 

### View OpenAPI Schema
- FastAPI generates the OpenAPI schema so you can view
- http://127.0.0.1:8000/openapi.json
- Helps the developer create RESTful APIs based on standards so individuals can use the APIs easily

### Suagger-UI
- http://127.0.0.1:8000/docs

### FastAPI uses HTTP Request Methods
- GET: Read method that retrieves data
- POST: Create method, to submit data
- PUT: Update the entire resource
- PATCH: Update part of the resource
- DELETE: Delete the resource

also known as CRUD operations

- TRACE: performs a message loop-back to the target
- OPTIONS: Describes communication options to the target
- CONNECT: Creates a tunnel to the server, based on the target resource

### FastAPI response status code
- 1xx: Information Response: Request processing
- 2xx: Success: Request successfully complete
- 3xx: Redirection: Further action must be complete
- 4xx: Client Errors: An error was caused by the request from the client
- 5xx: Server Errors: An error has occured on the server

## 49. FastAPI Project: Swagger and HTTP Decorators
- uvicorn books:app --reload

## 53. FastAPI Project: Path Parameters
If you going to be using path parameters, the path parameters must be underneath any kind of API that's going to be
following the same kind of path. 

## 54. FastAPI Project: Enumeration Path Parameters
- enum mixin
  - https://docs.python.org/3/library/enum.html#others

## 61. FastAPI Assignment Solution
- `/assignment/` Query parameter
- `/{assignment}` Path parameter

# Section 8:HTTP Exceptions and Status Codes

## 78. FastAPI Project: Form Fields

```async def book_login(username: str = Form(...), password: str = Form(...)):```

- If we do not use this form, then our application in FastAPI is going to automatically assume that this is a query parameter 
- Do not have to type `...` after FastAPI 0.78

## Quiz 4:
- Question 1:API Headers are what?
  - [ ] Allow APIs to send additional information to each request/response
  - [ ] Are Key:Value pairs
  - [x] Both 

# Section 11:API Request Methods

## Quiz 5:

### Question 1:

- What is Depends() in FastAPI?
  - [x] A way to declare things that are required for the application/function to work by injecting the dependencies
  - [ ] A way to say that this function may or may not depend on something

# Section 10:Setup Database

## 90. FastAPI Project: SQLite3 Setting Up Todos

- .schema
- .quit
- .mode markdown
  - mode should be one of: ascii box column csv html insert json line list markdown quote table tabs tcl

# Section 12 Authentication & Authorization

## 96. JSON Web Token (JWT) Overview

### What is a JSON Web Token

- JSON Web Token is a self-contained way to securely transmit data and information between two parties using a JSON Object.
- JSON Web Tokens can be trusted because each JWT can be digitally signed, which in return allows toe server to know if the JWT has been changed at all
- JWT should be used when dealing with authorization (JWT is not an authentication method)
- JWT is a great way for information to be exchanged between the server and client

### JSON Web Token Structure

`aaaaaaaa.bbbbbbbb.cccccccc`

- A JSON Web Token is created of three separated parts separated by dots(.) which include:
  - Header: (a)
  - Payload: (b)
  - Signature: (c)

### JWT Header

```json
{
  "alg": "HS256",
  "typ": "JWT"
}
```

- A JWT Header usually consist of two parts:
  - "alg" The algorithm for signing
  - "typ" The specific type of token
- The JWT header is then encoded using Base64 to create the first part of the JWT (a)

### JWT Payload

```json
{
  "sub": "1234567890",
  "name": "John Doe",
  "iat": 1516239022
}
```

- A JWT Payload consists of the data. The payloads data contains claims, and there are three different types of claims.
  - Registered
  - Public
  - Private
- The JWT Payload is then encoded using Base64 to create the second part of the JWT (b)

### JWT Signature


```
HMACSHA256(
  base64UrlEncode(header) + "." +
  base64UrlEncode(payload),
  secret)
```

- A JWT Signature is created by using the algorithm in the header to hash out the encoded header, encoded payload with a secret.
- The secret can be anything, but is saved somewhere on the server that the client does not have access to
- The signature is the third and final part of a JWT (c)

[https://jwt.io/](https://jwt.io/)

# Section 15:Routing

## 130. Routing Introduction

### What is routing

- Rare that you want your entire application to be on a single file
- Flexible tool to structure your application
- Scalable architecture
- Organize file structure
