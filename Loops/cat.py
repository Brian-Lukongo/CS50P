#Write a program that prompts the user for a number n and then prints "meow" n times.
def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            break
    return n
        
def meow(n):
    for _ in range(n):
        print("meow")

main()

'''
while True:
    n = int(input("What's n? "))
    if n > 0:
        break

for _ in range(n):
    print("meow")
'''

'''
print("Meow\n" * 3, end="")
'''
'''
for _ in range(3):
    print("meow")
'''
'''
for i in [0, 1, 2]:
    print("meow")'''
'''
i = 0
while i < 3:
    print("meow")
    i += 1
'''
'''
i = 3
while i != 0:
    print("meow")
    i = i - 1
'''
'''
print("meow")
print("meow")
print("meow")   
'''