from flask import Flask
import os
import time

app= Flask(__name__)
from RemindersApi import list_courses,list_assignment
from Reminders import r
from Phone_sms import phone_sms
canvas_api=os.environ['CANVAS_KEY']


@app.route('/')
def index():
    return "This is your Canvas Reminder"

@app.route('/courses')
def course_list():
    data = list_courses()
    return data

@app.route('/assignments')
def assignment():
    print()
    list = r.list_reminders()
    return "These are the assignments you currently have reminders for: " + str(list)

@app.route('/send_sms/<int:set_time>')
def send_text(set_time):
    while True:
        time.sleep(set_time)
        phone_sms()
        break
    return("Message has been sent")

@app.route('/list/<course_code>')
def assignment_list():
    return list_assignment("<course_code>")

if __name__=='__main__':
    app.run(debug=True)






