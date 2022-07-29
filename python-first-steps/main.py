from helper import validate_days

user_input = ""
while user_input != "exit":
    user_input = input(
        "Please provide the list of days to calculate hours(type 'exit' to stop): \n")
    for each in user_input.split():
        validate_days(each)
