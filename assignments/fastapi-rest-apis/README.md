# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a REST API using Python and the FastAPI framework. Students will create routes, work with request and response models, handle path and query parameters, and validate incoming data.

## 📝 Tasks

### 🛠️ Create the API Structure

#### Description
Use the starter code to build a FastAPI application that exposes several routes for a simple book collection.

#### Requirements
Completed program should:

- Use FastAPI to create an application instance.
- Include a root route (`/`) that returns a welcome message.
- Include a `/books` route that returns a list of books.
- Include a `/books/{book_id}` route that returns a single book by ID.

### 🛠️ Add Book Creation and Validation

#### Description
Extend the API to accept new book entries and validate incoming request data using Pydantic models.

#### Requirements
Completed program should:

- Define a `Book` model with `id`, `title`, `author`, and `year` fields.
- Add a `POST /books` route that accepts a new book and returns the created book.
- Validate input so that `title` and `author` are required strings and `year` is a positive integer.

### 🛠️ Support Searching and Query Parameters

#### Description
Add query parameter support to let users search the book collection by author.

#### Requirements
Completed program should:

- Add a `GET /search` route that accepts an optional `author` query parameter.
- Return all books when no `author` is provided.
- Return matching books when `author` is specified.
- Handle cases where no books match the query.

## 🚀 Running the Application

To run the API locally, use:

```bash
uvicorn starter_code:app --reload
```

Then visit `http://127.0.0.1:8000/docs` to explore the automatically generated API documentation.
