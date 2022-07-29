def days_to_hours(no_of_days=1):
    return f"The hours of {no_of_days} day(s) are {no_of_days*24}"


def validate_days():
    try:
        user_input_int = int(each)
        if user_input_int > 0:
            print(days_to_hours(user_input_int))
        elif user_input_int == 0:
            print("Zero days!")
        else:
            print("Negative number!")

    except ValueError:
        if user_input != "exit":
            print("Invalid input")


user_input = ""
while user_input != "exit":
    user_input = input(
        "Please provide the list of days to calculate hours(type 'exit' to stop): \n")
    for each in user_input.split():
        validate_days()
