# grabs user's birthday in one line, and stores day month and year in separate variables
birth_month, birth_day, birth_year = [int(x) for x in input("Enter birthday in 'month day year' format: ").split()]
print("Birthday: ", birth_month, birth_day, birth_year)

# grabs current date in one line, and stores day month and year in separate variables
current_month, current_day, current_year = [int(x) for x in input("Enter today's date in 'month day year' format: ").split()]
print("Today's date: ", current_month, current_day, current_year)
age = int(current_year) - int(birth_year)

# defines birth_month_not_passed as a variable outside of the function that follows
birth_month_not_passed = False

# subtracts 1 from the age because user's birth month hasn't passed yet
if int(current_month) < int(birth_month):
    age -= 1
    birth_month_not_passed = True

# if it is currently the user's birth month, and user's birth day has passed or is today, adds 1 back to age
if (birth_month_not_passed):
    if int(current_month) == int(birth_month) and int(current_day) >= int(birth_day):
        age += 1

# provides a space for fomatting
print("")
# tells the user their current age
print("As of today you are", age, "years old")
# tells the user if they are an old man
if age > 30:
    print("You are an old man.")
