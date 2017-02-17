class Room:
    def __init__(self, description, items, n_door, e_door, s_door, w_door):
        self.description= description
        self.items = items
        self.n_door = n_door
        self.e_door = e_door
        self.s_door = s_door
        self.w_door = w_door
    
    player_is_here = False
    

class Door:
    unlocked = True
    
    def __init__(self):
        pass

class Player:
    inventory = []

    def __init__(self):
        
    def move(self, direction):
        pass

room1 = Room("You stand in an empty, windowless chamber.  The stone walls are damp and covered in moss.  The room has doors on the north, east, and west walls.", \
             [], True, True, False, True)

room1.player_is_here = True

if Room.player_is_here(self) = True:
    print self.description
