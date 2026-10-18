kabaddi = 1
cricket = 2
volleyball = 3

game_Id = int(input("Enter game_Id: "))
player_Count = int(input("Enter number of players : "))

if (game_Id == kabaddi and player_Count == 7):
    print("Correct number of players for kabddi")

elif (game_Id == cricket and player_Count == 11):
    print("Correct number of players")

elif (game_Id == volleyball and player_Count == 6):
    print("Correct number of player")
else:
    print("Invalid game_Id or incorrect number of players")