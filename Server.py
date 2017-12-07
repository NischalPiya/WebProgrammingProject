from flask import Flask
import os
import time

app= Flask(__name__)
from Reminders import r,list_courses,list_assignment
from Phone_sms import phone_sms
canvas_api=os.environ['CANVAS_KEY']


@app.route('/')
def index():
    return "This is your Canvas Reminder"

@app.route('/assignment')
def assignment():
    list = r.list_reminders()
    return str(list)

@app.route('/courses')
def course_list():
    return list_courses()

@app.route('/send_sms/<time>')
def send_text(time):
    while True:
        time.sleep()
        phone_sms()
        break
    return("Message has been sent")

@app.route('/list/<course_code>')
def assignment_list():
    return list_assignment("<course_code>")

if __name__=='__main__':
    app.run(debug=True)






