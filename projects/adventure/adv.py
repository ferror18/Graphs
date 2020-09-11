from room import Room
from player import Player
from world import World
from util import Stack, Queue
import copy

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

#U - Understand

'''
- I know which directions have rooms
-I don't know which room is at the end of each direction
-end result is an array with directions  to the fastest traversal
- Theoreticall limit is 917 but strech is 959
'''
#P - Plan
'''
- Get a map
    -Get exits from curent map
    -find which room correponds to which exit
    -add current room to visited
    -move to first next room 
    - repeat

- Find Shortest path
'''
#E - Execute
directions = ['n','s','e','w']
back = {'n': 's', 's':'n', 'w':'e', 'e': 'w'}
Map = {}
traversal_path = []
q = Queue()
s = Stack()
traceback_path = []
p2 = Player(world.starting_room)

# q.push(player.current_room.get_exits())
current = p2.current_room.id
n = p2.current_room.get_exits()
room_map = {}
for i in directions:
        if i in n:
            room_map[i] = '?'
        else:
            room_map[i] = None
Map[current] = room_map

# Map = Graph()

def find_unxplored(room):
    q = Queue()
    visited = {}
    path = []
    q.enqueue(room)
    while q.size()>0:
        print('Queue', q)
        current = q.dequeue()
        print(visited, current)
        n = Map[current]
        if '?' in n.values():
            path.append(current)
            print('traceback',path)
            return path
        for i in n.items():
            d = i[0]
            id = i[1]
            if id != None and id not in visited:
                q.enqueue(id)
                break
        visited[current] = None
        path.append(current)
        print('traceback',path)

    print('traceback',path)
    return path

while len(Map) < len(room_graph):
    current = p2.current_room.id
    n = p2.current_room.get_exits()
    
    for i in directions:
        if i in n:
            print(n)
            next_room = p2.current_room.get_room_in_direction(i).id
            if next_room not in Map:
                print('Current room:', p2.current_room.id)
                print(f'Attemted to move "{i}" from {current} to {next_room}')
                old = copy.deepcopy(current)
                p2.travel(i)
                Map[old][i] = p2.current_room.id
                n2 = p2.current_room.get_exits()
                Map[p2.current_room.id] = {}
                for x in directions:
                    if x in n2:
                        Map[p2.current_room.id][x] = '?'
                    else:
                        Map[p2.current_room.id][x] = None
                Map[p2.current_room.id][back[i]] = old
                traceback_path.append(back[i])
                traversal_path.append(i)
                print(p2.current_room.id)
                print(Map)
                break
            elif Map[current][i] == '?':
                print('Current room:', p2.current_room.id)
                print(f'Attemted to move "{i}" from {current} to {next_room}')
                old = copy.deepcopy(current)
                p2.travel(i)
                Map[old][i] = p2.current_room.id
                n2 = p2.current_room.get_exits()
                Map[p2.current_room.id][back[i]] = old
                traceback_path.append(back[i])
                traversal_path.append(i)
                print(p2.current_room.id)
                print(Map)
                break
        if i == 'w':
            print('Dead End')
            traceback_path = []
            traceback_nodes = find_unxplored(p2.current_room.id)
            for i in range(len(traceback_nodes)-1):
                current = traceback_nodes[i]
                destination = traceback_nodes[i+1]
                for x in Map[current].items():
                    if x[1] == destination:
                        traceback_path.append(x[0])
                        break
            print('traceback',traceback_path)
            for i in traceback_path:
                print('Current room:', p2.current_room.id)
                print(f'Attemted to move "{i}" from {p2.current_room.id} to {Map[p2.current_room.id][i]}')
                p2.travel(i)
                # print(p2.current_room.id)
                traversal_path.append(i)
                # traceback_path = []
                # print(f'Traced back to {current}')

    # if current == 4:
    #     break


# while len(Map) < len(room_graph):
#     current = p2.current_room.id
#     n = p2.current_room.get_exits()
#     room_map = {}
#     for i in directions:
#             room_map[i] = p2.current_room.get_room_in_direction(i).id if p2.current_room.get_room_in_direction(i) != None else None
#     Map[current] = room_map
    
#     for i in Map.keys():
#         print(f'{i}:{Map[i]}')

#     for i in directions:
#         if i in n:
#             print(n)
#             next_room = Map[current][i]
#             # print('next room', next_room)
#             if next_room not in Map:
#                 print('Current room:', p2.current_room.id)
#                 print(f'Attemted to move "{i}" from {current} to {next_room}')
#                 p2.travel(i)
#                 traceback_path.append(back[i])
#                 traversal_path.append(i)
#                 print(p2.current_room.id)
#                 break
#         if i == 'w':
#             print(i, n[-1])
#             print('Traceback started', traversal_path)
#             for i in traceback_path[::-1]:
#                 print('Current room:', p2.current_room.id)
#                 print(f'Attemted to move "{i}" from {p2.current_room.id} to {Map[p2.current_room.id][i]}')
#                 p2.travel(i)
#                 # print(p2.current_room.id)
#                 traversal_path.append(i)
#                 traceback_path = []
#                 # print(f'Traced back to {current}')
#     # check_for_dead_end()
#     # print('Traceback', traceback_path)
#     # print('Traversal', traversal_path)
#     # break
#     if current == 4:
#         break


    

#R - Review





# TRAVERSAL TEST
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
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
