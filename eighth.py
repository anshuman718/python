print("snake water gun")
print("Enter w for water and g for gun and s for snake")
s = "snake"
w = "water"
g = "gun"

# Get user input

user_choice = input("Enter your choice")
import random 
computer_choice = random.choice([s,w,g])

# Print the choices 
print("you chose:" , user_choice)
print("computer chose:", computer_choice)

# Determine the winner 
if user_choice == "s" and computer_choice== w:
            print("you win")



elif user_choice == "w" and computer_choice== g:
            print("you win")


elif user_choice == "G" and    computer_choice== s:
          print("you winner")



elif user_choice == "s" and computer_choice== g:
        print("you are loser")


elif user_choice == "g" and computer_choice== w:
      print("you have lose")


elif user_choice == "w" and computer_choice== s:
        print("you loser")

else:
        print("It is a tie ")
# This is a game made by using python .We have told the computer to import its choice and we will import ours .
# There will be a pair of two choices and we have given it the condition that who will win in each case.
# If the pair of choices will not match from the conditions given here then it will be a draw as we have instructed.
