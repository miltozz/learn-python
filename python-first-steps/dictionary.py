# dictionaries are unordered collections in key-value pairs
# not ordered
# no duplicate keys
# mutable values
# update()
# pop()

dict1 = {"ham": "good", "cheese": "very good", "lucky_number": 100}
cheesevalue = dict1.get("cheese")

# print dictionary values
print(dict1["ham"])
print(cheesevalue)

# print all dictionary values
for i in dict1.values():
    print(i)

# print all dictionary pairs
for i in dict1.items():
    print(i)

# pop pair by key
dict1.pop("ham")

#prints keys
for dict_item in dict1:
    print(dict_item)
