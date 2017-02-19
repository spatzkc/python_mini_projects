class Room:
    def __init__(self, coordinates, description, door_list):
        self.description= description
        self.door_list = door_list

room_list = [ 
                [(0,0), "An entryway", [1,0,0,0] ],
                [(1,0), "A green storage closet with copier", [1,0,0,0] ],
                [(0,1), "A moldy couch sits in this room", [0,1,1,0] ],
                [(1,1), "A shrine to many-tentacled god", [0,1,1,1] ],
                [(2,1), "This hallway ends where the ceiling collapsed", 
                                                        [0,0,0,1] ]
             ]
          

def make_dungeon(list_of_rooms):
    #===========================================================================
    # Pre: starts with a 2D array full of room info
    # Post: a dictionary of room objects with coordinate tuple (x,y) as key
    #===========================================================================
    rooms_dictionary = {}
    for i in list_of_rooms:
        rooms_dictionary[i[0]] = Room( i[0], i[1], i[2] )
    return rooms_dictionary

print (make_dungeon(room_list))

#def check_for_door(player_room, walk_direction):

#check_for_door(room_dict[(x, y)], walk_direction)

