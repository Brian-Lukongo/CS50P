def main():
    user_input = input("Input: ")
    print("Output: ", end="")
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

    for c in user_input:
        if c not in vowels:
            print(c, end="")
    print()

if __name__ == "__main__":
    main()