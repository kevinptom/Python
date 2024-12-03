
player1 = input("Enter player1 name:")
player2 = input("Enter player2 name:")
def game():
    sticks = 16
    while sticks >0:
        if sticks > 0:
            take = int(input(f"Enter number of sticks taken by {player1} (you can take stick 1 or 2 or 3)"))
            if take == 1 or take == 2 or take == 3:
                sticks = sticks - take
                print(player1,"sticks remaining:",sticks)
            else:
                print(take,"sticks is not allowed")

        elif (sticks<=0):
            print(player1,"is loser")

        if sticks > 0:
            take = int(input(f"Enter number of sticks taken by {player2}(you can take stick 1 or 2 or 3)"))
            if take == 1 or take == 2 or take == 3:
                sticks = sticks - take
                print(player2, "sticks remaining:", sticks)
            else:
                print(take, "sticks is not allowed")

        elif (sticks <= 0):
            print(player2, "is loser")
game()




