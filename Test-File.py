import os
import requests
from requests.auth import HTTPBasicAuth
import json

canvas_token="-6802~vCQq4tMSAu3iUshXBIIsMcloEGhhOmrPyclLOA8EfSMt6JqJJW1Nhwt8ltxuJ3gJ"

url="https://canvas.moravian.edu/api/v1/calendar_events"
headers={'Accept: application/vnd.github.mercy-preview+json'}

response = requests.get(url, auth=(canvas_token),headers=headers)
print(response)
