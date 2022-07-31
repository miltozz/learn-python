# list is basically array.
# a collection of ordered data
# mutable
# append() and pop()

list1 = ['max', 'min', 'bacon']

# print first list item
print(list1[0])

# add to list
list1.append("ham")

print(list1)


# iterate the third item of the list
list1 = ['one','two','three']
for item in list1[2]:
    print(item)

# skip first two items and start iteration from index 2
for item in list1[2:]:
    print(item)