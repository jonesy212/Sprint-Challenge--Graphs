from room import Room
from player import Player
from world import World

from util import Queue, Stack

from random import shuffle
from ast import literal_eval

import multiprocessing

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

#Reverse of traversal_path
reversed_path = []
#visited
visited = {}

#dict to get opposite direction travelled

from_dir = {"n": "s", "s":"n", "w": "e", "e": "w"}

# Build starting room and exits
visited[player.current_room.id] = player.current_room.get_exits()

# run until all rooms have been visited
while len(visited) < len(room_graph):
    #if unvisted
    if player.current_room.id not in visited:
          #get the room exits
        exits = player. current_room.get_exits()
        #add room and exits to visited
        visited[player.current_room.id] = exits

    # need to back track to a previous room
    if len(visited) == len(room_graph):
        #to go back to a previous room
        go_back_a_room = reversed_path.pop()
    
        #add to the path
        traversal_path.amend(go_back_a_room)
        #move the player to the previous room
        player.travel(go_back_a_room)
    else:
        #Pick last available direction
        direction_options = len(visited[player.current_room.id])
        #randomize direction option from remaing options 
        direction_index = (
            random.randint(0, direction_options - 1) if direction_options > 0 else 0
        )
        direction = visited[player.current_room.id][direction_index]
        #remove choice so unvisited path
        visited[player.current_room.id].pop(direction_index)
        #move playaer to the next room
        player.travel(direction)
        #add to path tracker
        traversal_path.append(direction)
        #add inverse of direction to reversed_path
        reversed_traversal_path.append(from_dir[direction])
    if test:
        return traversal_path
    else:
        return len(traversal_path)


# class Graph:
#     def __init__(self):
#         self.rooms = {}
#         '''
#         0: {
#             'n': '?', 
#             's': '?', 
#             'w': '?', 
#             'e': '?'
#         }
#         '''
def bfs(self, starting_room, destination_room):

    #start in room 0
    #create an empty queue
    unexplored_picks = Queue()
    #enqueue a PATH to the starting vertex
    unexplored_picks.enqueue([starting_room])
    #create a set for visited vertices
    visited_picks = set()
    # picks random unexplored direction
    while unexplored_picks > 0:
        player.travel(direction)
        #randomize the order of the unexplored picks
        shuffle(unexplored_picks)
        #dequeue first path
        current_room_path = unexplored_picks.dequeue()
        #grab the last vertex in the path
        current_room = current_room_path[-1]
        #set destination room to the current_room w/ the question mark 
        destination_room= current_room['?']
        #if it hasn't been visited
        if current_room not in unexplored_picks:
            #check if the target is the destination
            if current_room == destination_room:
                #return path
                return current_room_path
        #mark it as visited
        visited_picks.add(current_room)
    #new verstions of the current room path
    # for next_room in self.get_ne


    # from players current room

    # travels and logs that direction, then loops.
    # path to the shorts room (BFS)
    # for a room with a `?`
    # instead of serching for target_vertex, 
    # search for an exit with a `?` as the value

    # return a list of room IDs.
    # convert list to a n/s/e/w directions
    # before adding traversal path 



# TRAVERSAL TEST - DO NOT MODIFY
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
