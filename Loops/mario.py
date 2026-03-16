def main():
    print_square(3)

def print_square(size):
    for i in range(size):
        print_row(size)

def print_row(width):
    print("#" * width)

main()

'''
def main():
    print_square(3)

def print_square(size):
    # for each row in square
    for i in range(size):
        # for each column in square
        for j in range(size):
            # print "#" without newline
            print("#", end="")

        print()
main()
'''

'''
def main():
    print_row(4)

def print_row(width):
    print("?" * width)
main()
'''
'''
def main():
    print_column(3)

def print_column(height):
    print("#\n" * height, end="")
    

main()
'''
'''
for _ in range(3):
    print("#")
'''