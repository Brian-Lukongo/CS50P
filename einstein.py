def main():
    # Ask the user for the mass of an object
    mass= int(input("What's the mass of the object? "))
    # Calculate the energy using Einstein's formula E=mc^2
    energy = mass * 300000000**2
    
    print("The energy is", energy)

main()