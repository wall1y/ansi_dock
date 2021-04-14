import requests
from time import time, sleep

def send_request():
        r= requests.get('http://localhost:8080',"ping")
        print (r.text)


while True:
	sleep(5)
	send_request()
 
