import random
Black = (0, 0, 0)
numOfNodes = None
nodes = None

def neighbors(node, shuffle=False, maze = False):
    neighbors_list = []
    b = 1
    if maze:
        b = 2
    for i in range(-1, 2, 2):
        if 0 <= node[0]+i*b < numOfNodes:
            neighbors_list.append((node[0]+i*b, node[1]))
    for i in range(-1, 2, 2):
        if 0 <= node[1]+i*b < numOfNodes:
            neighbors_list.append((node[0], node[1]+i*b))
    if shuffle:
        random.shuffle(neighbors_list)

    return neighbors_list

def BFS(i, f, o_numOfNodes, o_nodes):
    global numOfNodes, nodes
    numOfNodes = o_numOfNodes
    nodes = o_nodes
    queue = [i]
    visited = [i]
    parents = {}
    while len(queue) > 0:
        node = queue.pop(0)
        for neighbor in neighbors(node):
            if neighbor not in visited and nodes[neighbor].color != (0,0,0):
                queue.append(neighbor)
                visited.append(neighbor)
                parents[neighbor] = node
            if neighbor == f:
                current_node = f
                path = []
                while current_node != i:
                    path.append(current_node)
                    current_node = parents[current_node]
                path.append(i)
                return True, visited, path
    
    return visited

def DFS(i, f, o_numOfNodes, o_nodes):
    global numOfNodes, nodes
    numOfNodes = o_numOfNodes
    nodes = o_nodes
    found = False
    queue = [i]
    visited = []
    parents = {}
    while len(queue):
        node = queue.pop()
        visited.append(node)
        if node == f:
            current_node = f
            path = []
            while current_node != i:
                path.append(current_node)
                current_node = parents[current_node]
            path.append(i)
            return True, visited, path
        
        for neighbor in neighbors(node, True):
            if neighbor not in visited and neighbor not in queue and nodes[neighbor].color != (0,0,0):
                queue.append(neighbor)
                parents[neighbor] = node
    
    return visited

def sign(num):
    if num > 0:
        return 1
    if num < 0:
        return -1
    return 0

def DFS_maze(o_numOfNodes, o_nodes):
    global numOfNodes, nodes
    numOfNodes = o_numOfNodes
    nodes = o_nodes
    queue = [(0, 0)]
    maze = []
    while len(queue) > 0:
        node = queue.pop()
        for neighbor in neighbors(node, True, True):
            if neighbor not in maze and neighbor not in queue:
                queue.append(neighbor)
                maze.append((sign(node[0]-neighbor[0])+(neighbor[0]), sign(node[1]-neighbor[1])+neighbor[1]))
                maze.append(neighbor)
    return maze, len(maze)