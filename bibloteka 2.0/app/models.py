from datetime import datetime
from app import db

book_authors = db.Table(
    'book_authors',
    db.Column('author_id', db.Integer, db.ForeignKey('author.id')),
    db.Column('book_id', db.Integer, db.ForeignKey('book.id'))
)

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), index=True, unique=True)

    books = db.relationship(
        'Book',
        secondary=book_authors,
        back_populates='authors'
    )

    def __str__(self):
        return f"<Author {self.name}>"

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(300), index=True)
    year = db.Column(db.Integer)

    authors = db.relationship(
        'Author',
        secondary=book_authors,
        back_populates='books'
    )

    loans = db.relationship('Loan', backref='book', lazy='dynamic')

    def __str__(self):
        return f"<Book {self.title}>"

class Loan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    borrower = db.Column(db.String(200))
    borrowed_at = db.Column(db.DateTime, default=datetime.utcnow)
    returned_at = db.Column(db.DateTime, nullable=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))

    def __str__(self):
        return f"<Loan {self.borrower} {self.borrowed_at}>"


