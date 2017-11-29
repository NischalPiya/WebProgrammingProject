from flask import Flask, jsonify
import requests
import os
import json

app= Flask(__name__)

import time

canvas_api=os.environ['CANVAS_KEY']

@app.route('/')
def index():

        base_url='https://canvas.moravian.edu/api/v1/users/self/courses/5519/assignments'
        headers = {"Authorization": "Bearer " + canvas_api}
        r= requests.get(base_url,headers=headers)
        data= r.json()

        return jsonify(data)


if __name__=='__main__':

    app.run(debug=True)




def list_assignment(course_code):

        base_url = 'https://canvas.moravian.edu/api/v1/users/self/courses/'+course_code+'/assignments'
        headers = {"Authorization": "Bearer " + canvas_api}
        response = requests.get(base_url, headers=headers)
        response.raise_for_status()
        data= json.loads(response.text)

        for homework in data :
           if homework['due_at']!='None':
            print(homework['name'],homework['assignment_group_id'],homework['due_at'])
(list_assignment('5522'))







