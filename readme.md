# Section 5
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
