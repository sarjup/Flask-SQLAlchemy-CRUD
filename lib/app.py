from flask import Flask
from models import db


app=Flask(__name__)
config = {
    'POSTGRES' : {
        'user':'saraju',
        'db':'db_student',
        'pw':'spalukasi',
        'host':'localhost',
        'port':'5432',
    },
}

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:%(pw)s@%(host)s:\
%(port)s/%(db)s' %config['POSTGRES']



# ....app config....
db.init_app(app)


@app.route('/')
def main():
    return 'Hello World!'
