
import random
def secure():
    chars = "qwertyuiopasdfghjklzxcvbnm09876544213"
    length=int(input("Enter length :"))

    password = ""
    for a in range(length):
       password+=random.choice(chars)
    print(password)
secure()
secure()
secure()

def my_function(*hero):
    print("The greatest character is "+ hero[2])
my_function("superman","Hulk","Batman")



def my_function2(character1 ,character2,character3):
    print("The greatest character is " + character3)
my_function2(character1="superman",character2="Hulk", character3="Batman")












         