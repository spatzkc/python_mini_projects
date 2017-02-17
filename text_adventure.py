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
    def __init__(self, description, items, n_door, e_door, s_door, w_door):
        self.description= description
        self.items = items
        self.n_door = n_door
        self.e_door = e_door
        self.s_door = s_door
        self.w_door = w_door
    
    player_is_here = False
    



if Room.player_is_here(self) = True:
    print self.description
