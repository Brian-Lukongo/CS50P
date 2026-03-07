# Ask the user for their name and greet them
name = input("What's your name? ").strip().title()

#split users name into first name and last name
first, last = name.split(" ")



# Say hello to the user
print(f"hello, {first}")
