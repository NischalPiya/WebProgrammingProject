from flask import Flask, jsonify
import requests
import os
import json


app= Flask(__name__)

import time

canvas_api=os.environ['CANVAS_KEY']

@app.route('/')
def index():

        base_url='https://canvas.moravian.edu/api/v1/users/self/courses/5522/assignments'
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
        print(response)
        if response.status_code == 404:
            print("Please enter a valid 4-digit class code")
        if response.status_code == 401:
            print("Status code entered is not a class you are authorized to access")
        else:
            response.raise_for_status()
            data= json.loads(response.text)
            for homework in data :
                if homework['due_at']!='None':
                    print(homework['name'],homework['assignment_group_id'],homework['due_at'])
            return data
(list_assignment("1"))




