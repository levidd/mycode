from cheatdice import *

players = []

players.append(Cheat_Swapper())
players.append(Cheat_Loaded_Dice())
players.append(Levi_Cheater())
players.append(Levi_Cheater_2())

scores = [0] * len(players)

number_of_games = 100000
game_number = 0
print("Simulation running")
print("==================")
while game_number < number_of_games:

    # roll and cheat
    for player in players:
        player.roll()
        player.cheat()
    
    # find who got the max. if two were same, draw and no one wins
    dice_max = max(players, key=lambda x : sum(x.get_dice()))
    winning_player = []
    for i in range(len(players)):
        if sum(players[i].get_dice()) == dice_max:
            winning_player.append(i)
    
    if len(winning_player) == 1:
        scores[winning_player[0]] += 1

    game_number += 1

    percent = (float(game_number) / number_of_games) * 100
    if round(percent) % 10 == 0:
        print(f"{percent}% complete ....")


print("Simulation complete")
print("-------------------")
print("Final scores")
print("------------")
print(scores)


