from backend.db import db



class User(db.Model):
   __tablename__ = 'users'
   id = db.Column('user_id', db.Integer, primary_key = True)
   user_type=db.Column(db.String(50))
   name = db.Column(db.String(100))
   city = db.Column(db.String(50))  
   address = db.Column(db.String(200))
   password = db.Column(db.String(10))



   def __init__(self,id, name, city, address,password):
      self.id=id
      self.name = name
      self.city = city
      self.address = address
      self.password = password

   

