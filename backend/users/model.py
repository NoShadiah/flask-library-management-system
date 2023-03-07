from backend.db import db

class User(db.Model):
   id = db.Column('user_id', db.Integer, primary_key = True)
   name = db.Column(db.String(100), nullable=False)
   city = db.Column(db.String(50))  
   addr = db.Column(db.String(200))
   pin = db.Column(db.String(10))
#    books = db.relationship('Book', backref= 'user')


def __init__(self,id,name,city,addr,pin,books):
        self.id=id
        self.name=name
        self.city=city
        self.addr=addr
        self.pin=pin
        # self.books=books

# db.create_all()