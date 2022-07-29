import requests

res = requests.get("https://api.github.com/users/miltozz")

#print(res)
#print(type(res))

print (f"Status code: {res.status_code}")

#print(type(res.text))
print(type(res.json()))
print( "\n")

print(res.json())

res_dict = res.json()
print(res_dict.get("login") + "\n" + res_dict.get("url"))

#for i in res.json():
#    print(f"Project name: {i['name']}. Project url: {i['web_url']}\n")


#iterates dictionary keys
for i in res_dict:
    print(f"{i}: {res_dict.get(i)} \n")
    #same thing, different syntax
    print(f"{i}: {res_dict[i]} \n")