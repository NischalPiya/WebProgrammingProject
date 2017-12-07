from flask import Flask
import requests
import os
import json
import datetime
app= Flask(__name__)
from Reminders import r,list_courses,list_assignment

canvas_api=os.environ['CANVAS_KEY']


@app.route('/')
def index():
    list = r.list_reminders()
    return str(list)
@app.route('/courses')
def course_list():
    return list_courses()


@app.route('/list/<course_code>')
def assignment_list():
    return list_assignment("<course_code>")

if __name__=='__main__':
    app.run(debug=True)






