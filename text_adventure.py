class Room:
    def __init__(self, description, items, n_door, e_door, s_door, w_door):
        self.description= description
        self.items = items
        self.n_door = n_door
        self.e_door = e_door
        self.s_door = s_door
        self.w_door = w_door
    pass

class Door:
    unlocked = True
    pass

class Player:
    inventory = []
    
    def move(self, direction):
        pass
