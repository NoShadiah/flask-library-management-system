# from backend.db import db;

# class Book(db.Model):
#     __tablename__="books"
#     id = db.Column('book_id', db.Integer, primary_key = True, nullable = False) 
#     serial_no = db.Column(db.String(20) )
#     title = db.Column(db.String(200) )
#     price = db.Column(db.String(25), 'UGX', nullable = True)
#     description = db.Column(db.String(300))
#     image = db.Column(db.String, nullable = True)
#     copies = db.Column(db.String(500), nullable = True)
#     publish_date = db.Column(db.String(10), nullable = True)
#     publishing_company_id = db.Column(db.Integer, db.Foreignkey ('pub_comp_id'))
#     user_id = db.Column (db.Integer, db.Foreignkey('user_id'))
#     companies = db.relationship('PublishingCompany', backref = 'book')


# def __init__(self,id,serial_no,title,price,description,copies,publish_date,publishing_company_id,user_id,companies):
#     self.id = id
#     self.serial_no = serial_no
#     self.title = title
#     self.price = price
#     self.description = description
#     self.copies = copies
#     self.publish_date = publish_date
#     self.publishing_company_id = publishing_company_id
#     self.user_id = user_id
#     self.companies = companies
