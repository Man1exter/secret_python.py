

def movies():
    pass

def long_password():
    pass

def modules():
    pass

def password():
    pass

def tips_tricks():
    pass

def keylogger():
    print(" ")

def choice_way():

    choice_from_menu = int(input("Your choice number ==> "))

    if choice_from_menu == 1:
        keylogger()
    elif choice_from_menu == 2:
        tips_tricks()
    elif choice_from_menu == 3:
        password()
    elif choice_from_menu == 4:
        modules()
    elif choice_from_menu == 5:
        long_password()
    elif choice_from_menu == 6:
        movies()
    else:
        print("Wrong number.....")

def menu():
    print("..CHOICE YOUR WAY TO LEARN NEW METHOD IN PYTHON..")
    print("[1]")
    print("[2]")
    print("[3]")
    print("[4]")
    print("[5]")
    print("[6]")

def main():
    menu()
    choice_way()