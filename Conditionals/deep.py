# This program checks if the user's input matches the answer to the great Question of Life, the Universe and Everything.
user_input = input("What is the great Question of Life, the Universe and Everything? ")
user_input = user_input.lower(). strip()  # Convert input to lowercase for case-insensitive comparison
if user_input == "42" \
    or user_input == "forty-two" \
    or user_input == "forty two":
    print("Yes")
else:
    print("No")
