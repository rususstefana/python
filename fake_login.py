while True:
    # citim user-ul de la tastatura
    username = input('Username:')

    # daca nu a introdus nici o valoare ramanem in bucla
    if not username:
        print("Insert username")
        continue # continua bucla de la inceput

    # daca user name == corect exit while
    if username == "Stefana":
        break
    else:
        print("Unknown user")

print("Acces granted")   