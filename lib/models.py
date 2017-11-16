from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#define your models classes hereafter
class BaseModel(db.Model):
    """Base data model for all objects"""

    __abstract__=True

    def __init__(self, *args):
        super().__init__(*args)

    def __repr__(self):
        """Define a base way to print models"""
        return '%s(%s)' % (self.__class__.__name__, {
            column: value
            for column, value in self._to_dict().items()
        })

    def json(self):
        """
                Define a base way to jsonify models, dealing with datetime objects
        """
        return {
            column: value if not isinstance(value, datetime.date) else value.strftime('%Y-%m-%d')
            for column, value in self._to_dict().items()
        }



class Student(BaseModel, db.Model):
    """Model for tbl_student"""
    __tablename__='tbl_student'
    #define your model

    id = db.Column(db.Integer, unique=True, primary_key = True)
    name = db.Column(db.String(100))
    city = db.Column(db.String(50))  
    addr = db.Column(db.String(200))
    pin = db.Column(db.String(10))

    def __init__(self,name,city,addr,pin):
        self.name = name
        self.city = city
        self.addr = addr
        self.pin = pin


