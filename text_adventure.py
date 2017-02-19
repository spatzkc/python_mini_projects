#!usr/bin/env python

#===============================================================================
# 2/2/17
# Kevin Spatz and Vincent Gammill
# A Text-Based Adventure Game to explore python.
#===============================================================================

#===============================================================================
# # A list of lists, with each of the inner lists holding all data to create a
# room object.
#[(room coordinates), "Room description", 
#[boolean statements for existence of N, E, S, W doors] ] 
#===============================================================================

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

class Room:
    def __init__(self, coordinates, description, door_list):
        self.description= description
        self.door_list = door_list
    
    player_is_here = False
    


room_list = []
#===============================================================================
# System for tracking player movement through rooms.  Uses (x,y) coordinates.
# Adds or subtracts numbers to (x,y) coordinates.
#===============================================================================

def check_for_door(x, y, room_dict, walk_direction):
    #Looks in the room the player is standing in and 
    #checks to see if there is a door in the direction the player wants to walk.
    if walk_direction == "N" and room_dict[x, y].door_list[0] == 1:
        return True
    elif walk_direction == "E" and room_dict[x, y].door_list[1] == 1:
        return True
    elif walk_direction == "S" and room_dict[x, y].door_list[2] == 1:
        return True
    elif walk_direction == "W" and room_dict[x, y].door_list[3] == 1:
        return True
    else:
        return False


def go_through_door(player_coordinates, walk_direction):
    #allows player to move different directions in the game
        if walk_direction == "N":
            #adjusts y-coordinates
            player_coordinates[1] += 1
        elif walk_direction == "S":
            #adjusts y-coordinates
            player_coordinates[1] -= 1
        elif walk_direction == "E":
            #adjusts x-coordinates
            player_coordinates[0] += 1
        elif walk_direction == "W":
            #adjusts x-coordinates
            player_coordinates[0] -= 1
        else:
            print ("Sorry, that is not a valid input.  Please input N, S, E, or \
             W.")
            
def main():
    room_dict = make_dungeon(room_list)
    #generates rooms in dungeon
    player_coordinates = [0, 0]
    #player start position
    game_running = True
    while game_running:
        walk_direction = raw_input("Choose a direction (N, E, S, W): ").upper()
        x = player_coordinates[0]
        y = player_coordinates[1]
        if check_for_door(x, y, room_dict, walk_direction) == True:
            go_through_door(player_coordinates, walk_direction)
        else:
            print ("Sorry, you cannot go that way.")
        
        
        
        
        