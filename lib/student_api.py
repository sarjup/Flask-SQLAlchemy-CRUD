from lib.models import db,Student
from flask import flash
from json import dumps

class StudentApi(object):
    @staticmethod
    def create_student(request):
        new_student = None
        if not request.form['name'] or not request.form['city'] or not request.form['addr']:
            flash('please enter all the fields', 'error')
        else:
            name = request.form['name']
            city = request.form['city']
            addr = request.form['addr']
            pin = request.form['pin']

            new_student = Student(name,city,addr,pin)


            db.session.add(new_student)
            db.session.commit()
            flash("Record was successfully added")
            print new_student

        print 'who is new std', new_student

        return new_student

    @staticmethod
    def query_students():
        student_all = Student.query.all()
        
        return student_all

    @staticmethod
    def query_student(id,request):
        student = Student.query.get(id)
        if not request.form['name'] or not request.form['city'] or not request.form['addr']:
            flash("Please enter all the fields", 'error')
        else:
            name = request.form['name']
            city = request.form['city']
            addr = request.form['addr']

            student.name = name
            student.city = city
            student.addr = addr

            db.session.commit()
        return student

    @staticmethod
    def get_student(id):
        student = Student.query.get(id)
        return student

    @staticmethod
    def delete_student(id):
        student = Student.query.get(id)
        db.session.delete(student)
        db.session.commit()
        return student
