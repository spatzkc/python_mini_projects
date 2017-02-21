'''
Created on Feb 20, 2017

To test functions in text_adventure.py

@author: genkha91
'''
from text_adventure import make_dungeon


def test_make_dungeon():
    room_list = [ 
                [(0,0), "An entryway", [1,0,0,0] ],
                [(1,0), "A green storage closet with copier", [1,0,0,0] ],
                [(0,1), "A moldy couch sits in this room", [0,1,1,0] ],
                [(1,1), "A shrine to many-tentacled god", [0,1,1,1] ],
                [(2,1), "This hallway ends where the ceiling collapsed", 
                                                        [0,0,0,1] ]
            ]
    
    room_dict = make_dungeon(room_list)
    for coordinates, room in room_dict.items():

        print("The room with coordinates " + str(coordinates[0] ) + ", " + \
               str( coordinates[1] ) + " has description \"" + room.description\
                + "\" and its door list is ")
        print(room.door_list)

def

def main():
    #test_make_dungeon()
    
main()