#!/usr/bin/python3

from pyapi.Rooms import rooms
from pyapi.GameUtils import *


# Replace RPG starter project with this code when new instructions are live

def showInstructions():
    # print a main menu and the commands
    print('''
RPG Game
========
Commands:
  go [direction]
  get [item]
''')


def showStatus():
    # print the player's current status
    print('---------------------------')
    print('You are in the ' + rooms.get('Current'))
    # print the current inventory
    print('Inventory : ' + str(inventory))
    # print an item if there is one
    if "item" in rooms[rooms.get('Current')]:
        print('You see a ' + rooms[rooms.get('Current')]['item'])
    print("---------------------------")


# an inventory, which is initially empty
inventory = []

# start the player in the Hall
rooms["Current"] = 'Hall'

options = {
    "go": go_command,
    "get": get_item,
    "look": describe
}

showInstructions()

# loop forever
while True:

    showStatus()

    # get the player's next 'move'
    move = get_move()

    if move[0] in options:
        options.get(move[0])(move, rooms, inventory)

    ## If a player enters a room with a monster
    if 'item' in rooms[rooms.get("Current")] and 'monster' in rooms[rooms.get("Current")]['item']:
        print('A monster has got you... GAME OVER!')
        break

    ## Define how a player can win
    if rooms.get("Current") == 'Garden' and 'key' in inventory and 'potion' in inventory:
        print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
        break
