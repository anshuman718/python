
f = open("fourteenth.py" , "r")

print(f.read())

# We can also use python to read a file and make changes in it ,here we have instructed it to just read and open a particular file.


for x in "apples":
    print(x)



people = ["Harry","Carry","Garry","Larry"]

for g in people:
    if g == "Garry":
        continue
    print(g)


languages = ["Tough","Easy"]
OOP = ["python","Javascript","Java","PHP"]

for a in languages:
    for s in OOP:
        print(a,s)



def my_formula(gname,fname,
iname):
    print(gname+""+fname+ "" + iname)

my_formula("Hail! ","Lord ","Henry")


def my_theory(country = "United kingdom"):

    print("I am from " + country)

my_theory("USA")
my_theory("France")
my_theory("Itlay")

my_theory()



def my_calculation(c):
    return 16 / c

print(my_calculation(29))
print(my_calculation(60))
print(my_calculation(4))