while True:
    age_str = input("Enter your age: ")
    if not age_str:
        print("Please enter your age:")
    else:
        break #exit while loop

age = int(age_str)
print("Your age is:", age)

if age > 18:
    print("Have a beer!")
elif age < 18:
    print("Go home")
else:
    print("Happy birhday")
    