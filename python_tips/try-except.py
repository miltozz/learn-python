
randomList = ['a', 0, 2]

for item in randomList:
    try:
        print("The item is", item)
        r = 1/int(item)
        break
    except Exception as e:
        print(e, e.__class__)
        print("Oops!", e.__class__, "occurred.")
        print("Next item.")
        print()
print("The reciprocal(1/value) of", item, "is", r)