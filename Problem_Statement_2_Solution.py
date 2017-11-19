import csv
import multiprocessing
import requests

def sendmail(to, subject, message):
    return requests.post(
        "https://api.mailgun.net/v3/<DOMAIN>/messages",
        auth=("api", "<API KEY here>"),
        data={"from": "Mailgun Sandbox <mailgun@DOMAIN>",
              "to": to,
              "subject": subject,
              "text": message})

with open('test.csv','r') as f:
	data=csv.reader(f, delimiter=',')
	for row in data:
		if len(row)>2:
			to=row[0]
			subject=row[1]
			message=','.join(row[2:])
			p = multiprocessing.Process(target=sendmail,args=(to,subject,message,))
			p.start()
