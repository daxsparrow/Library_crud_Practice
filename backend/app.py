#from typing_extensions import Required
from operator import ge
from extensions import db, app
from flask import request
from database.models import book, reader


@app.route('/add_book', methods=['POST'])
def add_book():
     data =  request.json
     book1 = book(name = data['name'], pages=data['pages'], editorial=data['editorial'], author=data['author'],genre=data['genre'], status=data['stattus'],
     isbn=data['isbn'], ubication=data['ubication'], mount=data['mount'])
     db.session.add(book1)
     db.session.commit()
     print(data)
     return 'received'

@app.route ('/add_reader', methods=['POST'])
def add_reader():
     data = request.json
     reader1 = reader(name=data['name'], last_name=data['last_name'],dni=data['dni'], direction=data['direction'],
     telephone=data['telephone'], age=data['age'])
     db.session.add(reader1)
     db.session.commit()
     return 'received'

if __name__ == "__main__":
    app.run(debug=True)