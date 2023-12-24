from flask import Flask, jsonify, request

app = Flask(__name__)


books = [
    {
        'id': 1,
        'title': 'Clean Code',
        'autor': 'Robert C. Martin'
    },
    {
        'id': 2,
        'title': 'Clean Architecture',
        'autor': 'Robert C. Martin'
    },
    {
        'id': 3,
        'title': 'O que realmente importa? ',
        'autor': 'Anderson Calvalcante'
    },
]


# Build api routes:
# Get (All)
@app.route('/books', methods=['GET'])  # route path and type
def get_books():
    return jsonify(books)  # return json format


# Get (Id)
@app.route('/books/<int:id>', methods=['GET'])
def get_id(id):
    for book in books:
        if book.get('id') == id:
            return jsonify(book)


# Put (Id)
@app.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    book_updated = request.get_json()
    for index, book in enumerate(books):
        if book.get('id') == id:
            books[index].update(book_updated)
            return jsonify(books[index])


# Create
@app.route('/books', methods=['POST'])
def create_book():
    book_create = request.get_json()
    books.append(book_create)

    return jsonify(books)


# Delete (Id)
@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    for index, book in enumerate(books):
        if book.get('id') == id:
            del books[index]
    return jsonify(books)


app.run(port=5000, host='localhost', debug=True)
