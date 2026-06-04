from flask import Flask, request, jsonify, abort

app = Flask(__name__)

books = [
    {"id": 1, "title": "Flask Basics", "author": "Ava Student", "year": 2024},
    {"id": 2, "title": "Building APIs", "author": "Leo Learner", "year": 2025},
]

@app.route("/", methods=["GET"])
def root():
    return jsonify({"message": "Welcome to the Flask Book API"})

@app.route("/books", methods=["GET"])
def list_books():
    return jsonify(books)

@app.route("/books/<int:book_id>", methods=["GET"])
def get_book(book_id):
    for book in books:
        if book["id"] == book_id:
            return jsonify(book)
    abort(404, description="Book not found")

@app.route("/books", methods=["POST"])
def create_book():
    data = request.get_json()
    if not data:
        abort(400, description="Request must be JSON")

    required_fields = ["id", "title", "author", "year"]
    if not all(field in data for field in required_fields):
        abort(400, description="Missing required book fields")

    new_book = {
        "id": data["id"],
        "title": data["title"],
        "author": data["author"],
        "year": data["year"],
    }
    books.append(new_book)
    return jsonify(new_book), 201

@app.route("/search", methods=["GET"])
def search_books():
    author = request.args.get("author")
    if not author:
        return jsonify(books)

    matches = [book for book in books if author.lower() in book["author"].lower()]
    return jsonify(matches)

if __name__ == "__main__":
    app.run(debug=True)
