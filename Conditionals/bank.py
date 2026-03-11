# The program will ask the user to enter a greeting. If the greeting starts with "hello", the program will output $0. If the greeting starts with "h" (but not "hello"), the program will output $20. Otherwise, the program will output $100.
user_input = input("Enter a greeting: ")
user_input = user_input.lower(). strip()

if user_input.startswith("hello"):
    print("$0")
elif user_input.startswith("h"):
    print("$20")
else:
    print("$100")