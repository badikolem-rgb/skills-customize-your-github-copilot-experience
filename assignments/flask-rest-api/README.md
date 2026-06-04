# 📘 Assignment: Intro to REST APIs with Flask

## 🎯 Objective

Build a beginner-friendly REST API using Flask. Students will create routes, work with JSON input and output, and use query parameters to filter results.

## 📝 Tasks

### 🛠️ Create the Flask API

#### Description
Build a Flask application that serves a small book collection through several API routes.

#### Requirements
Completed program should:

- Use Flask to create an app instance.
- Add a root route (`/`) that returns a welcome message as JSON.
- Add a `/books` route that returns a list of books in JSON format.
- Add a `/books/<int:book_id>` route that returns a single book by its ID.

### 🛠️ Add book creation support

#### Description
Add a POST route to accept new books and add them to the collection.

#### Requirements
Completed program should:

- Accept JSON data at `POST /books`.
- Require `id`, `title`, `author`, and `year` fields in the request body.
- Return the created book with a success status code.
- Return a clear error message if required data is missing.

### 🛠️ Add search with query parameters

#### Description
Use query parameters to let users search books by author.

#### Requirements
Completed program should:

- Add a `GET /search` route that accepts an optional `author` query parameter.
- Return all books when no `author` is provided.
- Return matching books when `author` is specified.
- Return an empty list when no matches are found.

## 🚀 Running the Application

To start the API locally, run:

```bash
python starter-code.py
```

Then open `http://127.0.0.1:5000/` in your browser or use a tool like Postman to test the routes.
