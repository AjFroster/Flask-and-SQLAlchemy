from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books-collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Book {self.title}>'

def setup_database(app):
    with app.app_context():
        db.create_all()

@app.route('/')
def home():
    books = Book.query.all()
    return render_template("index.html", books=books)

@app.route("/add", methods=['GET', 'POST'])
@app.route("/add/<int:book_id>", methods=['GET', 'POST'])
def add(book_id=None):
    book_to_edit = None
    if book_id:
        book_to_edit = Book.query.get(book_id)
    
    if request.method == 'POST':
        book_name = request.form['book_name']
        book_author = request.form['book_author']
        rating = request.form['rating']

        if book_to_edit:
            book_to_edit.title = book_name
            book_to_edit.author = book_author
            book_to_edit.rating = rating
        else:
            new_book = Book(title=book_name, author=book_author, rating=rating)
            db.session.add(new_book)

        db.session.commit()
        return redirect(url_for('home'))

    return render_template("add.html", book=book_to_edit)


@app.route('/update/<int:book_id>')
def update(book_id):
    return redirect(url_for('add', book_id=book_id))


@app.route('/delete/<int:book_id>')
def delete(book_id):
    book_to_delete = Book.query.get(book_id)
    if book_to_delete:
        db.session.delete(book_to_delete)
        db.session.commit()
    return redirect(url_for('home'))

if __name__ == "__main__":
    setup_database(app)
    app.run(debug=True)
