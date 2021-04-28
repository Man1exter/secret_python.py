import random
import string

def movies():
    print("secret movies in python..(info about it BONUS)")

def long_password():
    letters = string.ascii_lowercase
    letters_up = string.ascii_uppercase

    size = int(input("How many [letters] in your password ===> "))

    result_str = ''.join(random.choice(letters) for i in range(size))
    result_str_up = ''.join(random.choice(letters_up) for i in range(size))

    print("...UPPERCASE... Random string of size - ", size, "is =====> ", result_str)
    print("...LOWERCASE... Random string of size - ", size, "is =====> ", result_str_up)

def modules():

    print("..3 secret modules in python with info about it..")
    print("from ..... import ......")
    print("for example from random import randint")


def password():

    print("..show the best result with strong password to your account..")


def tips_tricks():
    print("..info about tricks/tips in python and info about it..")
    way = int(input("your way from menu => "))
    menuv2()
    if way == 1:
        t1()
    elif way == 2:
        t2()
    elif way == 3:
        t3()
    elif way == 4:
        t4()
    elif way == 5:
        t5()
    elif way == 6:
        t6()
    elif way == 7:
        t7()
    elif way == 8:
        t8()
    elif way == 9:
        t9()
    else:
        print("Wrong number.....")

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

def menuv2():
    print(" = > MENU < = ")
    print("[1] ..Merge Dictionaries")
    print("[2] ..String Joins")
    print("[3] ..Max occurance in List")
    print("[4] ..Value Swapping")
    print("[5] ..Range into List")
    print("[6] ..List Comprehension")
    print("[7] ..Dict Comprehension")
    print("[8] ..Adding Lists")
    print("[9] ..Extraction of Nested Lists")

def t1():
    print("[1] ..Merge Dictionaries")
    print("----------------------------")

    d1 = {"a": 1, "b": 2}
    d2 = {"c": 3, "d": 4}
    dict(d1, **d2)
    {**d1, **d2}

def t2():
    print("[2] ..String Joins")
    print("----------------------------")

    arr = ["Hey","bro","my","python","crew"]
    " <--> ".join(arr)
    " - ".join(arr)
    " ... ".join(arr)
    

def t3():
    print("[3] ..Max occurance in List")
    print("----------------------------")

    arr = [1,2,3,4,4,4,6,7,7,9]
    max(set(arr),key = arr.count)

def t4():
    print("[4] ..Value Swapping")
    print("----------------------------")

    a,b = 2,5
    a,b = b,a
    print(a)
    print(b)

def t5():
    print("[5] ..Range into List")
    print("----------------------------")

    arr = list(range(1,11))
    print(arr)

def t6():
    print("[6] ..List Comprehension")
    print("----------------------------")

    sqr = [ele ** 2 for ele in range(1,11)]
    print(sqr)

def t7():
    print("[7] ..Dict Comprehension")
    print("----------------------------")

def t8():
    print("[8] ..Adding Lists")
    print("----------------------------")

def t9():
    print("[9] ..Extraction of Nested Lists")
    print("----------------------------")

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