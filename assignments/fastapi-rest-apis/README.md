# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a simple REST API using the FastAPI framework to practice creating endpoints, handling HTTP methods, and working with request/response data.

## 📝 Tasks

### 🛠️ Create Basic Endpoints

#### Description
Set up a FastAPI application and create simple GET endpoints that return JSON responses.

#### Requirements
Completed program should:

- Initialize a FastAPI application.
- Create a GET endpoint at `/` that returns a welcome message as JSON.
- Create a GET endpoint at `/items` that returns a list of sample items.
- Example response for `/`:
  ```json
  {"message": "Welcome to the API"}
  ```
- Example response for `/items`:
  ```json
  [{"id": 1, "name": "Item 1"}, {"id": 2, "name": "Item 2"}]
  ```

### 🛠️ Add Path and Query Parameters

#### Description
Extend the API to accept dynamic data through path parameters and query parameters.

#### Requirements
Completed program should:

- Create a GET endpoint at `/items/{item_id}` that accepts an item ID as a path parameter.
- Return the item details as JSON (e.g., `{"id": 1, "name": "Item 1"}`).
- Create a GET endpoint at `/search` that accepts an optional `query` parameter.
- Return matching results or a message indicating no results found.

### 🛠️ Handle POST Requests

#### Description
Implement POST endpoints to accept and process data from clients.

#### Requirements
Completed program should:

- Create a POST endpoint at `/items` that accepts item data from the request body.
- Validate that the request body contains required fields (e.g., `name`).
- Return the created item with an assigned ID.
- Example request body:
  ```json
  {"name": "New Item", "description": "A test item"}
  ```
- Example response:
  ```json
  {"id": 3, "name": "New Item", "description": "A test item"}
  ```

### 🛠️ Add Error Handling and Status Codes

#### Description
Implement proper HTTP status codes and error handling for edge cases.

#### Requirements
Completed program should:

- Return a 404 status code when an item is not found.
- Return a 400 status code for invalid request data.
- Return appropriate success status codes (200, 201) for successful requests.
- Include descriptive error messages in responses.
- Example 404 response:
  ```json
  {"detail": "Item not found"}
  ```
