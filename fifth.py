mylist = ["bat" , "owl", "eagle","vulture" , "Lion" ]
#This is a type of list
yourlist = ["Dark forest" , "Night" ]
#this is the second list

mylist.insert(2,"vampire")
#This command inserts or adds an extra item which is not in the list at a specific place in between
mylist.append("Dracula")
#This command also adds an extra item in the last

mylist.extend(yourlist)

#This command is used to combine two lists

mylist.remove("eagle")
#This command removes a certain item from the list 

mylist.pop(4)

#This command also removes a certain item with the help of its location

print(mylist)