import requests
r= requests.get('https://api.github.com/events')
print(r.status_code)
print(r.headers['Content-Type'])
print(r.encoding)
print(r.text)
print(r.json())
