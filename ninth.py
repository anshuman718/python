##a = 21

#b = 55

#c = 446

#average = (a+c+b)/3 

#print(average)
# The above written program is used to find average  of a given set of numbers.

def avg():#Function defination
# If we do not use the def function then we will have to run the program again and again to do a specific task with differnt sets of numbers.
 

 a = int(input("Enter your number:"))


 b = int(input("Enter your number:"))

 c = int(input("Enter your number:"))

 average = ( a +c+b)/3 
 print(average)
# By using def function we can enter the number four times as we have said python to give us the average four times .This saves lot of time and make the code short .
# It is a kind of an algorithm.
avg()#Function call
print('Thank you')
avg()
print("Thank you")
avg()
avg()
avg()