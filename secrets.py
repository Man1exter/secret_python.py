import random
import string

def movies():
    pass

def long_password():
    letters = string.ascii_lowercase
    letters_up = string.ascii_uppercase

    size = int(input("How many [letters] in your password ===> "))

    result_str = ''.join(random.choice(letters) for i in range(size))
    result_str_up = ''.join(random.choice(letters_up) for i in range(size))

    print("...UPPERCASE... Random string of size - ", size, "is =====> ", result_str)
    print("...LOWERCASE... Random string of size - ", size, "is =====> ", result_str_up)

def modules():
    pass

def password():
    pass

def tips_tricks():
    pass

def keylogger():
    print("........Keylogger to => [Login/Password] <= in Python............")
    print("You can see how strong is your data...")
    print("[1/2] LOGIN AND PASSWORD = 10 LENGTH")
    print("[2/2] LOGIN AND PASSWORD = COUNT 3X [A]")

    login = input("login: ")
    password = input("password: ")
    print("Data login = > ", login," - password ", password)

    if len(login) >= 10:
        print("POWER OF LOGIN ======> 1/4 ")
        if len(password) >= 10:
            print("POWER OF PASSWORD ======> 2/4")
        else:
            print("You can lose your login too fast")
    else:
        print("You can lose your password too fast")


    if login.count("a") >= 3:
        print("POWER OF LOGIN ======> 3/4 ")
        if login.count("a") >= 3:
            print("POWER OF PASSWORD ======> 4/4")
        else:
            print("You can lose your login too fast")
    else:
        print("You can lose your password too fast")


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
    print(" => [1]  => KEYLOGGER [LOGIN/PASSWORD]")
    print(" => [2]  => TIPS/TRICKS")
    print(" => [3]  => PASSWORD(HIDE)")
    print(" => [4]  => MODULES")
    print(" => [5]  => LONG PASSWORD")
    print(" => [6]  => MOVIES IN PYTHON")

def main():
    menu()
    choice_way()
main()