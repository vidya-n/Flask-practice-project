import requests

x = requests.get('https://www.browse.ai/')

print(x.status_code)
print(x.headers)
print(x.text)
print(x.encoding)
print(x.url)
