import requests


#r = requests.get('https://httpbin.org/basic-auth/user/pass', auth=('user', 'pass'))
#print(r.status_code)
r = requests.get('http://httpbin.org/get')  
print(r.headers) 

gl_response = requests.get("https://gitlab.com/api/v4//users/miltozz/projects")

print (f"Status code: {gl_response.status_code}")
print(type(gl_response.text))
print(type(gl_response.json()))

for i in gl_response.json():
    print(f"Project name: {i['name']}. Project url: {i['web_url']}\n")