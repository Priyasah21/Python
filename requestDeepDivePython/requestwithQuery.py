import requests
payload={'key1':'value1','key2':'value2'}
r=requests.get('https://httpbin.org/get',params=payload)
print(r.json(),type(r.json()))
"https://httpbin.org/get?key1=value1&key2=value2"
