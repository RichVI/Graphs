from util import Queue
from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

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

#--------------------------------------------------------------------------------------------#
def adventure_maze(player, world, room_graph):
	rooms = []
	path = []
	visited = set()

	# Add player's starting room into rooms (1st Room)
	rooms.append(player.current_room.id) 
	
	# Loop unti visited room matches with world rooms
	while len(visited) != len(world.rooms):
		# Current room will always be top item on room stack
		current_room = rooms[-1]  
		# Add current room to visited rooms
		visited.add(current_room) 

		# create a neighbor_rooms dictionary {'s': 62, 'e': 5, 'w': 23}
		neighbor_rooms = room_graph[current_room][1]
		neighbor_rooms_queue = Queue()

		# Loop through the current room
		for direction, connected_room in neighbor_rooms.items(): 
			# Check if the room is already visited
			if connected_room not in visited: 

				# If not, then add it to the queue
				neighbor_rooms_queue.enqueue(connected_room)

		if neighbor_rooms_queue.size() > 0:
			# set next_room as the first item in the queue
			next_room = neighbor_rooms_queue.dequeue()

			# add the next room to the room stack
			rooms.append(next_room)  
		
		# If the queue is empty
		else:
			# pop the last item on rooms
			rooms.pop()  

			# Set the next_room as the last item on rooms
			next_room = rooms[-1]  
		
		for room_name, connected_room in neighbor_rooms.items(): 
			# Check if next_room is one of the neighbor rooms 
			if connected_room == next_room:   
				# Add the name of the room to the path
				path.append(room_name)      
		
	return path

traversal_path = adventure_maze(player, world, room_graph)
#--------------------------------------------------------------------------------------------#



# TRAVERSAL TEST
visited = set()
player.current_room = world.starting_room
visited.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited.add(player.current_room)

if len(visited) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")


# player.current_room.print_room_description(player)
# while True:
#     cmds = random.choice("nsew")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
