def moveCheck(move):
    return len(move) >= 2

def go_command(move, rooms, *args):
    if moveCheck(move):
        # check that they are allowed wherever they want to go
        if move[1] in rooms[rooms.get('Current')]:
            # set the current room to the new room
            rooms['Current'] = rooms[rooms.get('Current')][move[1]]
        # there is no door (link) to the new room
        else:
            print('You can\'t go that way!')

        return rooms.get('Current')


def get_item(move, rooms, inventory, *args):
    if moveCheck(move):
        # if the room contains an item, and the item is the one they want to get
        if "item" in rooms[rooms.get('Current')] and move[1] in rooms[rooms.get('Current')]['item']:
            # add the item to their inventory
            inventory += [move[1]]
            # display a helpful message
            print(move[1] + ' got!')
            # delete the item from the room
            del rooms[rooms.get('Current')]['item']
        # otherwise, if the item isn't there to get
        else:
            # tell them they can't get it
            print('Can\'t get ' + move[1] + '!')


def get_move():
    # .split() breaks it up into an list array
    # eg typing 'go east' would give the list:
    # ['go','east']
    move = ''
    while move == '':
        move = input('>')

    # split allows an items to have a space on them
    # get golden key is returned ["get", "golden key"]
    move = move.lower().split(" ", 1)
    return move


def describe(move, rooms, *args):
    if moveCheck(move):
        if "desc" in rooms[rooms.get('Current')]:
            if move[1] == rooms.get('Current').lower():
                print(f"You are in the {rooms.get('Current')}, it is...{rooms[rooms.get('Current')].get('desc')}")
            else:
                print(f"You can't look around {rooms.get('Current')}! You aren't in there!")
        else:
            print(f"You don't understand what you are looking at in the {rooms.get('Current')}")
