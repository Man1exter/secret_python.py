import random
import string
from string import ascii_lowercase
import calendar
import turtle

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

    numbers = int(input("How many letters/numbers must have to use with password ====> "))
    passwords = int(input("How many passwords draw in section ====> "))


def password():
    print("..show the best result with strong password to your account..")
    print(" ")
    times = int(input("how many password to show => "))
    i = 0
    length_pass = int(input("write number of length your password => "))
    need_chars = string.ascii_letters + string.digits + '!@#$%^&*()'
    
    while i < times:
      print("Your STRONG password =====> ",''.join(random.choice(need_chars) for i in range(length_pass)))
      i += 1

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
    elif choice_from_menu == 7:
        calendar_show()
    elif choice_from_menu == 8:
        with_bot()
    elif choice_from_menu == 9:
        turtle_star()
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

    {i:j for i,j in enumerate(ascii_lowercase)if i < 6}
    {0:'a',1:"b",2:"c",3:"d",4:"e",5:"f"}
    print("---- .. ----- .. ------")
    {j:i for j,i in enumerate(ascii_lowercase)if i < 6}
    {0:'a',1:"b",2:"c",3:"d",4:"e",5:"f"}

    {i: i for i in range(6)}

def t8():
    print("[8] ..Adding Lists")
    print("----------------------------")

    am1 = [1,2,3,4]
    am2 = [5,6,7,8]
    am3 = am1 + am2
    print(am3)
    am1.append(am2)
    print(am1)

def t9():
    print("[9] ..Extraction of Nested Lists")
    print("----------------------------")

    list = [[1],[2],[3],[4],[5]]
    sum(list, [])

def calendar_show():
    
    year = int(input("Write year(..actually => 2021..) => "))
    month = int(input("Write month(..number..) => "))
    print(" ")
    print(calendar.month(year,month))

def with_bot():
    print(".....Function to speak with bot about something.....")


def turtle_star():

    screen = turtle.Screen()
    screen.setup(900,900)
    screen.bgcolor("black")

    spiral = turtle.Turtle()
    speed_user = int(input("Write speed turtle to draw star => "))
    spiral.speed(speed_user)

    color1 = input("write your 1 color => ")
    color2 = input("write your 2 color => ")
    color3 = input("write your 3 color => ")
    color4 = input("write your 4 color => ")

    color = (color1,color2,color3,color4)

    line = 0
    for elem in range(50):

        spiral.forward(elem * 10)
        spiral.right(144)
        spiral.color(color[line])
        
        if line == 3:
            line = 0
        else:
            line += 1


    

def menu():
    print("..CHOICE YOUR WAY TO LEARN NEW METHOD IN PYTHON..")
    print(" => [1]  => KEYLOGGER [LOGIN/PASSWORD]")
    print(" => [2]  => TIPS/TRICKS")
    print(" => [3]  => STRONG PASSWORD(HIDE)")
    print(" => [4]  => MODULES")
    print(" => [5]  => LONG PASSWORD")
    print(" => [6]  => MOVIES IN PYTHON")
    print(" => [7]  => CALENDAR")
    print(" => [8]  => SPEAK WITH BOT ABOUT SOMETHING")
    print(" => [9]  => DRAW STAR USING TURTLE")

def main():
    menu()
    choice_way()
main()