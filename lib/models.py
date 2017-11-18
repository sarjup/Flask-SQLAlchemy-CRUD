from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import datetime

db = SQLAlchemy()
ma = Marshmallow()


class Student(db.Model):
    """Model for tbl_student"""
    __tablename__='tbl_student'
    #define your model

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    city = db.Column(db.String(50))  
    addr = db.Column(db.String(200))
    pin = db.Column(db.String(10))

    def __init__(self,name,city,addr,pin):
        self.name = name
        self.city = city
        self.addr = addr
        self.pin = pin

    # def __repr__(self):
    #     return '<Student {0}>'.format(self.name)

class StudentSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields =('id','name','city','addr','pin')

student_schema = StudentSchema()
students_schema = StudentSchema(many = True)


