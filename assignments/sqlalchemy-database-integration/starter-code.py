from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session, relationship
from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

# Database setup
DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Initialize FastAPI app
app = FastAPI()


# ============================================================================
# Task 1: Define SQLAlchemy Models
# ============================================================================

class User(Base):
    __tablename__ = "users"
    # TODO: Define User model with id, name, email, created_at columns
    # Hint: Use Column(Integer, primary_key=True) for id
    # Hint: Use Column(String, unique=True) for email
    # Hint: Use Column(DateTime, default=datetime.utcnow) for created_at
    # Hint: Define relationship to Post model
    pass


class Post(Base):
    __tablename__ = "posts"
    # TODO: Define Post model with id, title, content, user_id, created_at columns
    # Hint: Use Column(Integer, ForeignKey("users.id")) for user_id
    # Hint: Use relationship("User", back_populates="posts") to link to User


# Create tables
Base.metadata.create_all(bind=engine)


# ============================================================================
# Task 2 & 3: Pydantic Models for Request/Response
# ============================================================================

class UserCreate(BaseModel):
    name: str
    email: str


class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    created_at: datetime

    class Config:
        from_attributes = True


class PostCreate(BaseModel):
    user_id: int
    title: str
    content: str


class PostResponse(BaseModel):
    id: int
    title: str
    content: str
    user_id: int
    created_at: datetime

    class Config:
        from_attributes = True


# ============================================================================
# Task 2: CRUD Functions
# ============================================================================

def get_db():
    """Dependency to get database session"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# TODO: Implement create_user(db: Session, user: UserCreate) -> User
# TODO: Implement get_all_users(db: Session) -> List[User]
# TODO: Implement get_user_by_id(db: Session, user_id: int) -> User or None
# TODO: Implement update_user(db: Session, user_id: int, user: UserCreate) -> User or None
# TODO: Implement delete_user(db: Session, user_id: int) -> bool


# ============================================================================
# Task 3: FastAPI Endpoints
# ============================================================================

# TODO: POST /users - Create a new user
# TODO: GET /users - Retrieve all users
# TODO: GET /users/{user_id} - Retrieve a specific user
# TODO: PUT /users/{user_id} - Update a user
# TODO: DELETE /users/{user_id} - Delete a user


# ============================================================================
# Task 4: Relationship Endpoints
# ============================================================================

# TODO: POST /posts - Create a new post
# TODO: GET /users/{user_id}/posts - Get all posts by a user


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
