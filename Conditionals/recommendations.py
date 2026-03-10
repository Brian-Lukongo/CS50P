def main():
    difficulty = input("Difficult or casual?")

    
    players = input("Multiplacer or Single-player? ")
    
    if difficulty == "Difficult":
        if players == "Multiplayer":
            recommend("Poker")
        elif players == "Single-player":
            recommend("Klondike")
        else:
           print("Enter a valid number of players") 
    elif difficulty == "Casual":
        if players == "Multiplayer":
            recommend("Hearts")
        elif players == "Single-player":
            recommend("Clock")
        else:
           print("Enter a valid number of players") 
    else:
        print("Enter a valid difficulty")
        
def recommend(game):
    print("You might like", game)


main()



'''This program recommends a card game based on the user's preferences for difficulty and number of players.
def main():
    difficulty = input("Difficult or casual?")
    players = input("Multiplacer or Single-player? ")
    
    if difficulty == "Difficult":
        if players == "Multiplayer":
            recommend("Poker")
        elif players == "Single-player":
            recommend("Klondike")
        else:
           print("Enter a valid number of players") 
    elif difficulty == "Casual":
        if players == "Multiplayer":
            recommend("Hearts")
        elif players == "Single-player":
            recommend("Clock")
        else:
           print("Enter a valid number of players") 
    else:
        print("Enter a valid difficulty")
        
def recommend(game):
    print("You might like", game)


main()
'''