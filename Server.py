from flask import Flask
import os
import time
import datetime
import json
from RemindersApi import list_courses,list_assignment
from Reminders import r
from Phone_sms import phone_sms

canvas_api=os.environ['CANVAS_KEY']
app= Flask(__name__)


@app.route('/')
def index():
    return "Welcome to Canvas Reminder"

@app.route('/courses')
def course_list():
    courses = []
    curr_date = datetime.datetime.strptime(datetime.datetime.today().strftime('%Y-%m-%d'),'%Y-%m-%d')
    for all_courses in list_courses():
        end_date = datetime.datetime.strptime(all_courses['end_at'][0:10], '%Y-%m-%d')
        if end_date > curr_date:
            courses.append(all_courses['name']+ " " +str(all_courses['id'])+" ")
    return json.dumps(courses)

@app.route('/assignments/<string:course_code>')
def assignment_list(course_code):
    names = []
    for assignments in list_assignment(course_code):
        if assignments['due_at'] != None:
            names.append(assignments['name']+ " " + str(assignments['id'])+ " " + str(assignments['due_at'][0:10]+" "))
    return json.dumps(names)

@app.route('/add_reminder/<string:course_code>/<string:assign_id>')
def add_reminder(course_code, assign_id):
    checker = r.new_canvas_reminder(course_code,assign_id)
    if checker == 1:
        return("Assignment added successfully")
    elif checker == 0:
        return("Error: Course code or assignment id is invalid")
    else:
        return("Reminder already exist")

@app.route('/remove_reminder/<string:course_code>/<string:assign_id>')
def remove_reminder(course_code, assign_id):
    checker = r.delete_canvas_reminder(course_code,assign_id)
    if checker == 1:
        return("Assignment removed successfully")
    elif checker == 0:
        return("Error: Course code or assignment id is invalid")
    else:
        return("Reminder doesn't exist")

@app.route('/list_reminders')
def print_reminders():
    list = []
    for reminders in r.list_reminders():
        list.append(reminders)
    return json.dumps(list)

@app.route('/send_sms/<int:set_time>')
def send_text(set_time):
    while True:
        time.sleep(set_time)
        phone_sms()
        break


    return("Message has been sent")




if __name__=='__main__':
    app.run(debug=True)




