from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


# Create input command parser
def input_parser():
    command = input("Please pick an option: n (north), s (south), w (west), e (east) ")
    return command

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
new_player = Player("Thatcher", room["outside"])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

while True:
    # print player's name, cur room, room des
    print(f"{new_player.name}")
    print(f"You are currently in the {new_player.current_room.name}")
    print(f"{new_player.current_room.description}")

    # call input for user command
    command = input_parser()

    # q for quit
    if command == "q":
        print("See you later!")
        exit()

    # n for north
    if command == "n":
        try:
            new_player = Player("Thatcher", new_player.current_room.n_to)
            print(f"You moved north and enter the {new_player.current_room.name} room")
        except:
            print(f"This is a dead end, move to another direction")
    
    # s for south
    if command == "s":
        try:
            new_player = Player("Thatcher", new_player.current_room.s_to)
            print(f"You moved south and enter the {new_player.current_room.name} room")
        except:
            print(f"This is a dead end, move to another direction")
    
    # e for east
    if command == "e":
        try:
            new_player = Player("Thatcher", new_player.current_room.e_to)
            print(f"You moved east and enter the {new_player.current_room.name} room")
        except:
            print(f"This is a dead end, move to another direction")
    
    # w for west
    if command == "w":
        try:
            new_player = Player("Thatcher", new_player.current_room.w_to)
            print(f"You moved west and enter the {new_player.current_room.name} room")
        except:
            print(f"This is a dead end, move to another direction")
    
    else:
        print(f"Please enter a correct option")

