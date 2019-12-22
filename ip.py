import requests


r = requests.get('https://ipapi.co/ip/')
r.text
print (r)
