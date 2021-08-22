# Roomba Sweep Challenge
# In Roomba Sweep Challenge, Identify Irona's next move.
# @Author Jayati Naik

from  itertools import chain
import sys

class Node:
    def __init__(self, i, j):
        self.i = i
        self.j = j

def decide_next_move(dirty_node):
    if(x == dirty_node.i  and y < dirty_node.j): # node on x-axis and y is positive
        return 'RIGHT'
    elif(x == dirty_node.i and y > dirty_node.j): # node on x-axis and y is negative
        return 'LEFT'
    elif(x < dirty_node.i and y == dirty_node.j): # node on y-axis and x is negative
        return 'DOWN'
    elif(x > dirty_node.i and y == dirty_node.j): # node on y-axis and x is positive
        return 'UP'
    elif(x > dirty_node.i and y < dirty_node.j): # node is in TOP RIGHT area
        return 'RIGHT'
    elif(x < dirty_node.i and y < dirty_node.j): # node is in BOTTOM RIGHT area
        return 'RIGHT'
    elif(x > dirty_node.i and y > dirty_node.j): # node is in TOP LEFT area
        return 'LEFT'
    elif(x > dirty_node.i and y < dirty_node.j): # node is in Bottom LEFT area
        return 'LEFT'


def check_for_dirty_node(list_of_nodes):
    flag = False
    for cell in list_of_nodes:
        if(grid[cell.i][cell.j] == 'd'):
            print("nearest dirty node x-location: ", cell.i)
            print("nearest dirty node y-location: ", cell.j)
            flag = True
            return cell
    if(not flag):
        return None

def get_nodes_located_on_axis(level):
    axis_nodes = []
    for i in range(1,level+1):
        if(0 <= y+i < w):
            axis_nodes.append(Node(x, y+i))
        if(0 <= y-i < w):
            axis_nodes.append(Node(x, y-i))
        if(0 <= x-i < h):
            axis_nodes.append(Node(x-i, y))
        if(0 <= x+i < h):
            axis_nodes.append(Node(x+i, y))
    return axis_nodes

def get_other_nodes(level):
    grid_nodes = []

    # Reference nodes to calculate diagonal nodes
    right_most_node = Node(x, y+level)
    left_most_node = Node(x, y-level)
    top_node = Node(x-level, y)
    bottom_node = Node(x+level, y)

    # calculate diagonal nodes
    for k in range(1,level+1):
        # LM ---> TOP (-1, +1 )
        if(0 <= left_most_node.i-k < h and left_most_node.i-k > top_node.i
            and 0 <= left_most_node.j+k < w and left_most_node.j+k < top_node.j):
            grid_nodes.append(Node(left_most_node.i-k, left_most_node.j+k))
        # LM ---> bottom (+1, +1 )
        if(0 <= left_most_node.i+k < h and left_most_node.i+k < bottom_node.i
            and 0 <= left_most_node.j+k < w and left_most_node.j+k < bottom_node.j):
            grid_nodes.append(Node(left_most_node.i+k, left_most_node.j+k))
        # RM ----> TOP (-1, -1)
        if( 0 <= right_most_node.i-k < h and right_most_node.i-k > top_node.i
            and 0 <= right_most_node.j-k < w and right_most_node.j-k > top_node.j):
            grid_nodes.append(Node(right_most_node.i-k, right_most_node.j-k))
        # RM ----> Bottom (+1, -1)
        if(0 <= right_most_node.i+k < h and right_most_node.i+k < bottom_node.i
            and 0 <= right_most_node.j-k < w and right_most_node.j-k > bottom_node.j):
            grid_nodes.append(Node(right_most_node.i+k, right_most_node.j-k))

    return grid_nodes

def get_list_of_nodes_at_level_i(level):
    nodes_on_axis = get_nodes_located_on_axis(level)

    other_nodes = get_other_nodes(level)

    return nodes_on_axis + other_nodes

def find_next_move(x, y):
    dirty_node = None
    for i in range(1, max(h,w)):
        list_of_nodes = get_list_of_nodes_at_level_i(i)
        dirty_node = check_for_dirty_node(list_of_nodes)
        if(dirty_node != None):
            next_move = decide_next_move(dirty_node)
            return next_move

count = 0
Lines =''

with open("input.txt") as fp:
    Lines = fp.readlines()

try:
    location = Lines[0].split(" ")
    x = int(location[0])
    y = int(location[1].strip('\n'))

    grid_size = Lines[1].split(" ")
    h = int(grid_size[0])
    w = int(grid_size[1].strip('\n'))

    if(x>=h or y>=w):
        raise Exception("Irona's current location is invalid. Please check the location passed in input.txt file.")
        sys.exit(1)

    grid = Lines[2:]
    grid = [sub.replace('\n', '') for sub in grid]

    if (len(grid) > h or len(grid[0]) > w):
        raise Exception("Invalid grid passed in input. Please check passed grid in input.txt file.")
        sys.exit(1)

except Exception as error:
        print('Error occured while reading input: ' + repr(error))
        sys.exit(1)

if(not 'd' in chain(*grid)): # Check if the grid is already clean.
    L = 'DONE'
elif(grid[x][y] == 'd'): # Check if Irona's current location is a dirty cell.
    L = 'CLEAN'
else:
    L = find_next_move(x, y)

print("NEXT MOVE", L)
with open("output.txt", "w") as fp:
    fp.writelines(L)
sys.exit(0)
