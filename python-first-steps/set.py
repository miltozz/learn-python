# set is an unordered collection
# no duplicates
# mutable
# add()
# pop() -random

def print_set(a_set):
    for item in a_set:
        print(item)

    print("--------------------")


set2 = {"cheese", "bacon", "ham"}
print_set(set2)
set2.add("lettuce")
print_set(set2)
set2.pop()

print_set(set2)

print(set2)
