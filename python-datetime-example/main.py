from datetime import datetime

user_input = input(
    "Enter goal and deadline, separated by comma \n e.g. learn python,10.12.2022 \n")

input_list = user_input.split(",")
print("----------")
print(f"input list{input_list}\n")

goal = input_list[0]
deadline = datetime.strptime(input_list[1], "%d.%m.%Y")

print(f"deadline: {deadline}")
print(f"deadline type is: {type(deadline)}\n")

now = datetime.today()
remaining = deadline - now
print(f"You have {remaining.days} days until the deadline!")
