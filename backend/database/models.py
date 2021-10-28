#from operator import ge
from re import A
from extensions import db


class book(db.Model):
    __tablename__ = 'Book'
    id_book = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    pages = db.Column(db.Integer)
    editorial = db.Column(db.String(255))
    author = db.Column(db.String(255))
    genre = db.Column(db.String(255))
    stattus = db.Column(db.Integer)
    isbn = db.Column(db.String(255))
    ubication = db.Column(db.String(10))
    mount = db.Column(db.Integer)

    def __init__(self, name, pages, editorial, author, genre, status,isbn, ubication, mount):
        #self.id_book = idbook
        self.name = name
        self.pages = pages
        self.editorial = editorial
        self.author = author
        self.genre = genre
        self.stattus = status
        self.isbn = isbn
        self.ubication = ubication
        self.mount = mount
       


class reader(db.Model):
    __tablename__ = 'Reader'
    id_reader = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    dni = db.Column(db.String(255))
    direction = db.Column(db.String(255))
    telephone = db.Column(db.String(255))
    age = db.Column(db.Integer)

    def __init__(self, name, last_name, dni, direction, telephone,age):
        self.name = name,
        self.last_name = last_name,
        self.dni = dni,
        self.direction = direction,
        self.telephone = telephone,
        self.age =  age

# class loan(db.Model):
#     __tablename__ = 'Loan'
#     id = db.Column(db.Integer, primary_key=True)
#     id_book = db.Column(db.Integer, db.ForeignKey('Book.id_book'))
#     id_reader = db.Column(db.Integer, db.ForeignKey('Reader.id_reader'))
#     begindate = db.Column(db.DateTime)
#     enddate = db.Column(db.Datetime)
#     statuss = db.Column(db.Integer)