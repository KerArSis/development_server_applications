import logging
import sys
from flask import Flask, jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_caching import Cache

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'

# Настройка кэша
app.config['CACHE_TYPE'] = 'SimpleCache'  # Используем встроенный кэш в памяти
app.config['CACHE_DEFAULT_TIMEOUT'] = 300  # Кэш хранится 300 секунд
cache = Cache(app)

db = SQLAlchemy(app)

# Настройка логирования
logger = logging.getLogger()
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s [%(levelname)s]: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)
file_handler = logging.FileHandler('/app/logs/app.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

logging.info("Application has started.")

# Определение модели книги для базы данных
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    author = db.Column(db.String(120), nullable=False)

# Создание таблиц базы данных
with app.app_context():
    db.create_all()
    logging.info("Database initialized with tables.")

@app.route('/')
def index():
    logging.info("Accessed home page.")
    return render_template('index.html')

@app.route('/books', methods=['GET'])
@cache.cached()  # Кэширование маршрута
def get_books():
    books = Book.query.all()
    logging.info(f"Fetched {len(books)} books from database.")
    return jsonify([{"id": book.id, "title": book.title, "author": book.author} for book in books])

@app.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()
    new_book = Book(title=data['title'], author=data['author'])
    db.session.add(new_book)
    db.session.commit()
    logging.info(f"Added new book: '{data['title']}' by '{data['author']}'.")
    cache.clear()  # Очистка кэша после добавления книги
    return jsonify({
        "message": "Book added successfully!",
        "book": {"id": new_book.id, "title": new_book.title, "author": new_book.author}
    }), 201

@app.route('/books/log', methods=['POST'])
def log_book():
    data = request.get_json()
    logging.info(f"Data received: {data}")
    return jsonify({
        "message": "Data received",
        "data_received": data
    }), 200

@app.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    book = Book.query.get_or_404(id)
    data = request.get_json()
    book.title = data.get('title', book.title)
    book.author = data.get('author', book.author)
    db.session.commit()
    logging.info(f"Updated book ID {id}: '{book.title}' by '{book.author}'.")
    cache.clear()  # Очистка кэша после обновления книги
    return jsonify({"id": book.id, "title": book.title, "author": book.author})

@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    book = Book.query.get_or_404(id)
    db.session.delete(book)
    db.session.commit()
    logging.info(f"Deleted book ID {id}.")
    cache.clear()  # Очистка кэша после удаления книги
    return '', 204

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
