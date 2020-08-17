# A dictionary linking a room to other rooms
rooms = {
    'Current': '',

    'Hall': {
        'south': 'Kitchen',
        'east': 'Dining Room',
        'item': 'key',
        'desc': 'Dimly lit and somewhat eerie. Maybe should get that water stain checked out...'
    },

    'Kitchen': {
        'north': 'Hall',
        'item': 'monster',
        'desc': 'A terrible mess. There is a very strong, repulsive odor and every surface is discolored. '
                'Is that... blood? '
    },
    'Dining Room': {
        'west': 'Hall',
        'south': 'Garden',
        'north': 'Living Room',
        'item': 'potion',
        'desc': 'Very nice china, well polished serving utensils. Someone deeply cares for this room.'
    },
    'Garden': {
        'north': 'Dining Room',
        'desc': 'There are a bunch of bunnies trying to get into the vegetable patch. At least it looks '
                'like they are bunnies.... '
    },
    'Garage': {
        'south': 'Living Room',
        'item': 'wrench',
        'desc': 'Woah this is a cool! So many tools, so many grease stains. Reminds me of when I would '
                '\'help my dad\' in the garage (i.e. get yelled at for not shining the light correctly)'
    },
    'Living Room': {
        'north': 'Garage',
        'south': 'Dining Room',
        'item': 'weird chair',
    }
}
