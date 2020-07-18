from room import Room
from player import Player
from item import Items

# Declare the items
item = {
    "flashlight": Items("Flashlight",
                        "A small flashlight that lights up the current room"),
    "key": Items("Key",
                "A key that would open the treasure room")
}

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",
                     n_to="foyer"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""",
                    n_to="overlook", s_to="outside", e_to="narrow",
                    items=item["flashlight"]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
                    s_to="foyer", items=item["key"]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",
                    n_to="treasure", w_to="foyer"),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",
                    s_to="narrow"),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['narrow']
room['treasure'].s_to = room['narrow']


# Create input command parser
def input_parser():
    command = input("Please pick an option: n (north), s (south), w (west), e (east) ")
    return command

def use_item(player):
    use_item = input(f"In your inventory, you have the following items: {[i for i in player.inventory]}. Which item do you want to use?")
    return use_item

def pick_up_item(player):
    
    try: 
        player.inventory.append(player.current_room.items.name)

        print(f"You have picked up {player.current_room.items.name.split('and')}")

        player.current_room.items = None
    
    except:
        print("There are no items to be found in this room")

def check_inventory(player):
    try:

        print(f"In your inventory you have these items: {player.inventory}")
    
    except:

        print("You currently have no items in your inventory")

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player("Thatcher", room["outside"])

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
    print(f"{player.name}")
    print(f"You are currently in the {player.current_room.name}")
    print(f"{player.current_room.description}")

    # call input for user command
    command = input_parser()

    # q for quit
    if command == "q":
        print("See you later!")
        exit()

    # n for north
    if command == "n":
        try:

            if player.current_room.n_to:
                player.current_room = player.current_room.n_to
                print(f"You moved north and enter the {player.current_room.name} room")
        
        except:
            print(f"This is a dead end, move to another direction")
    
    # s for south
    if command == "s":
        try:
            if player.current_room.s_to:
                player.current_room = player.current_room.s_to
                print(f"You moved south and enter the {player.current_room.name} room")
        except:
            print(f"This is a dead end, move to another direction")
    
    # e for east
    if command == "e":
        try:
            if player.current_room.e_to:
                player.current_room = player.current_room.e_to
                print(f"You moved east and enter the {player.current_room.name} room")
        except:
            print(f"This is a dead end, move to another direction")
    
    # w for west
    if command == "w":
        try:
            if player.current_room.w_to:
                player.current_room = player.current_room.w_to
                print(f"You moved west and enter the {player.current_room.name} room")
        except:
            print(f"This is a dead end, move to another direction")
    
    else:
        print(f"Please enter a correct option")
    
    if command == "p":
        pick_up_item(player)
    
    if command == "u":
        try:
            command = use_item(player)

            if command == "key":

                if (player.current_room.name == "Narrow Passage") and ("key" in player.inventory):

                    print("You have the key, do you wish to use it to unlock the treasure door?")
                    room["narrow"].n_to = room['treasure']
                    player.inventory.remove("key")

                else:
                    if player.current_room.name == "Narrow Passage":

                        print("You do not have the key to unlock this door, please go back and find it")
                    elif 'key' in player.inventory:
                        print("you have no where to use this treasure key")

        except:

            print("You have no items you can use for this room, try searching for items in other room")
    
    if command == "c":
        check_inventory(player)


