thislist = ["Batman" ,  "Thor"  ,  "Captain america"  , "Hawkeye"   ]
thislist[0] = "Bruce wayne"

thislist[1:3] = ["Hulk", "Winter soldier"]

print(thislist)


#This command will print the list


print(len(thislist))



#This command will print the lenght of the list which is number of items
print(type(thislist))
#This command will print the type of data in the list 


print(thislist[1:3])

#This command will print the items in the list at the position from 1 to 3 .The item on third place is not included.The position of the first item is 0.

if "Thor" in thislist:

    print("yes,'Thor' is in the following list.")

    #This command help us to know whether an item is in the corresponding list or not.
    #It is also a type of boolean operator because we have given a condition.

    