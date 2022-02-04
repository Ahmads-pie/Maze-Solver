Black = (0, 0, 0)
numOfNodes = None
nodes = None
def neighbors(node):
    neighbors_list = []
    if node[0] > 0 and nodes[(node[0]-1, node[1])].color != Black:
        neighbors_list.append((node[0]-1, node[1]))
    
    if node[1] > 0 and  nodes[(node[0], node[1]-1)].color != Black:
        neighbors_list.append((node[0], node[1]-1))
    
    if node[0] < numOfNodes-1 and nodes[(node[0]+1, node[1])].color != Black:
        neighbors_list.append((node[0]+1, node[1]))

    if node[1] < numOfNodes-1 and nodes[(node[0], node[1]+1)].color != Black:
        neighbors_list.append((node[0], node[1]+1))
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
        
        for neighbor in neighbors(node):
            if neighbor not in visited and neighbor not in queue and nodes[neighbor].color != (0,0,0):
                queue.append(neighbor)
                parents[neighbor] = node
    
    return visited


def allowed(node, parent, maze):
    for n in neighbors(node):
        if n in maze and n != parent:
            return False
    
    allowed_nodes = []
    for i in range(-1,2,2):
        for j in range(-1,2,2):
            if node[i] > 0 and node[j] > 0 and node[i] < numOfNodes-1 and node[j] < numOfNodes-1:
                allowed_nodes.append((node[i], node[j]))
    
    for n in allowed_nodes:
        if n in maze:
            return False
    
    return True


def DFS_maze(o_numOfNodes, o_nodes):
    global numOfNodes, nodes
    numOfNodes = o_numOfNodes
    nodes = o_nodes
    queue = [(0,0)]
    maze = []
    while len(queue) > 0:
        node = queue.pop()
        for n in neighbors(node): # n: neighbor
            if allowed(n, node, maze):
                queue.append(n)
                maze.append(n)
    return maze