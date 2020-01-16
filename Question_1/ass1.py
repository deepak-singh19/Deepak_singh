__author__ = 'BML'
import urllib.request
import requests
import json
import csv

request = requests.get("https://open-to-cors.s3.amazonaws.com/users.json")
request_text = request.text

data = json.loads(request_text)
print(data)

employ_data = open('EmployData.csv', 'w')
csvwriter = csv.writer(employ_data)
count = 0

for emp in data:

      if count == 0:

             header = emp.keys()

             csvwriter.writerow(header)

             count += 1

      csvwriter.writerow(emp.values())

employ_data.close()

