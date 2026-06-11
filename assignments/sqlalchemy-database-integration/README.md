# 📘 Assignment: Database Integration with SQLAlchemy

## 🎯 Objective

Extend a FastAPI application to use a database with SQLAlchemy ORM, replacing in-memory storage with persistent data. Practice database design, CRUD operations, and connecting APIs to relational databases.

## 📝 Tasks

### 🛠️ Set Up Database Models with SQLAlchemy

#### Description
Define SQLAlchemy models to represent data structures and create a database connection for persistence.

#### Requirements
Completed program should:

- Import SQLAlchemy and create an engine to connect to a SQLite database.
- Define a `User` model with fields: `id` (primary key), `name`, `email`, and `created_at`.
- Define a `Post` model with fields: `id` (primary key), `title`, `content`, `user_id` (foreign key), and `created_at`.
- Create tables in the database using `Base.metadata.create_all()`.
- Example model definition:
  ```python
  class User(Base):
      __tablename__ = "users"
      id = Column(Integer, primary_key=True)
      name = Column(String)
      email = Column(String, unique=True)
  ```

### 🛠️ Implement CRUD Operations

#### Description
Write functions to create, read, update, and delete records in the database using SQLAlchemy.

#### Requirements
Completed program should:

- Create a function to add a new user to the database.
- Create a function to retrieve all users.
- Create a function to retrieve a user by ID.
- Create a function to update a user's information.
- Create a function to delete a user by ID.
- Return appropriate data or status messages for each operation.

### 🛠️ Connect FastAPI Endpoints to the Database

#### Description
Integrate the CRUD functions with FastAPI endpoints to expose database operations via the API.

#### Requirements
Completed program should:

- Create a POST endpoint at `/users` to add a new user.
- Create a GET endpoint at `/users` to retrieve all users.
- Create a GET endpoint at `/users/{user_id}` to retrieve a specific user.
- Create a PUT endpoint at `/users/{user_id}` to update a user.
- Create a DELETE endpoint at `/users/{user_id}` to delete a user.
- Return appropriate HTTP status codes and error messages.
- Example POST request body:
  ```json
  {"name": "John Doe", "email": "john@example.com"}
  ```

### 🛠️ Add Relationships and Query Complex Data

#### Description
Implement relationships between models and create endpoints that return related data.

#### Requirements
Completed program should:

- Establish a one-to-many relationship between `User` and `Post` models.
- Create a POST endpoint at `/posts` to add a post for a specific user.
- Create a GET endpoint at `/users/{user_id}/posts` that returns all posts by a user.
- Handle foreign key constraints gracefully (e.g., return error if user doesn't exist).
- Example POST request body:
  ```json
  {"user_id": 1, "title": "My First Post", "content": "Hello, world!"}
  ```
