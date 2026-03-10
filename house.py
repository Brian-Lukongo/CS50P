
name = input ("What's is your name? ")
match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case  "Draco":
        print("Slytherin")
    case _:
        print("Who?")



''' # This program will ask the user for their name and then print out which Hogwarts house they belong to.
name = input ("What's is your name? ")

if name == "Harry" or name == "Hermione" or name == "Ron":
    print("Gryffindor")
elif name == "Draco":
    print("Slytherin")
else:
    print("who?")
'''



'''# This program will ask the user for their name and then print out which Hogwarts house they belong to.

name = input ("What's is your name? ")

if name == "Harry":
    print("Gryffindor")
elif name == "Hermione":
    print("Gryffindor")
elif name == "Ron":
    print("Gryffindor")
elif name == "Draco":
    print("Slytherin")
else:
    print("who?")
'''