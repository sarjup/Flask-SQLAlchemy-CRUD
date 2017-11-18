from flask import Flask, render_template, request, flash, url_for, redirect, jsonify
from models import db,ma,Student
from models import student_schema, students_schema
from lib.student_api import StudentApi
from json import dumps



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

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'hello world'



# ....app config....
db.init_app(app)
ma.init_app(app)


@app.route('/')
def index():
    return render_template('index.html')

    
# endpoint to create new student
@app.route("/api/students",methods=['POST'])
def add_student():
    student = StudentApi.create_student(request)
    result = student_schema.dump(student)
    return jsonify(result.data)
# endpoint for query all student  
@app.route("/api/students", methods=['GET'])
def get_student():
    data = StudentApi.query_students()
    result = students_schema.dump(data)
    return jsonify(result.data)

# endpoint to get student detail by id
@app.route("/api/students/<id>", methods=['GET'])
def student_detail(id):
    student = StudentApi.get_student(id)
    return student_schema.jsonify(student)

# endpoint to update student
@app.route("/api/students/<id>", methods=['PUT'])
def student_update(id):
    
    student = StudentApi.query_student(id,request)
    return student_schema.jsonify(student)

# endpoint to delete student
@app.route("/api/students/<id>",methods=['DELETE'])
def student_delete(id):
    student = StudentApi.delete_student(id)
    return student_schema.jsonify(student)

    


