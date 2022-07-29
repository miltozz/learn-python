by_sixty = 60
seconds_string = "seconds"

print("Seconds of a day are: " + str(24*60 * by_sixty) + " " + seconds_string)

# python3 syntax
print(f"Seconds of a day are: {24*60 * by_sixty} {seconds_string}")

# function
def days_to_hours(no_of_days=1):
    if no_of_days > 0:
        return f"The hours of {no_of_days} day(s) are {no_of_days*24}"
    elif no_of_days == 0:
        return "Zero days!"
    else:
        return "Invalid input!"


# print function's return
print(f"Two days: {days_to_hours(2)}")

# assign function return to var and print var
three_days = days_to_hours(3)
print(three_days)

# get user input, assign to var
user_days = input("Give us the number of days: \n ")

# print function's return, with user input as argument, cast to int
print(f"print user days: {days_to_hours(int(user_days))}")

# assign function's return to var, with user input as argument, cast to int, then add 1. print the var
some_var = days_to_hours(int(user_days)+1)
print("some_var: " + some_var)

# isdigit() check
print(user_days.isdigit())
