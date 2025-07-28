import requests
r = requests.post('https://httpbin.org/post?a=b', data={'key': 'priya'})
print(r.text)
