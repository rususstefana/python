
password = input("Please enter password:")

if password:
    print("We have a password")
else:
    print("you didn't enter anything")

    
if len(password) < 8:
    print("Password to short")
else:
    print("All good")