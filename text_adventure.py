#!usr/bin/env python

room_list = [ 
                [(0,0), "An entryway", [1,0,0,0] ]
                [(1,0), "A green storage closet with copier", [1,0,0,0] ]
                [(0,1), "A moldy couch sits in this room", [0,1,1,0] ]
                [(1,1), "A shrine to many-tentacled god", [0,1,1,1] ]
                [(2,1), "This hallway ends where the ceiling collapsed", 
                                                        [0,0,0,1] ]
            ]


class Room:
    def __init__(self, door_list, description):
        self.description= description
        self.door_list = door_list
    
    player_is_here = False
    



room_list = []
