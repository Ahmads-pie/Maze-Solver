Black = (0, 0, 0)
numOfNodes = None
nodes = None
def neighbors(node):
    neighbors_list = []
    if node[0] > 0 and nodes[(node[0]-1, node[1])].color != Black:
        neighbors_list.append((node[0]-1, node[1]))
    if node[0] < numOfNodes-1 and nodes[(node[0]+1, node[1])].color != Black:
        neighbors_list.append((node[0]+1, node[1]))
    if node[1] > 0 and  nodes[(node[0], node[1]-1)].color != Black:
        neighbors_list.append((node[0], node[1]-1))
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
    found = False
    while len(queue) > 0 and not found:
        node = queue.pop(0)
        for neighbor in neighbors(node):
            if neighbor not in visited and nodes[neighbor].color != (0,0,0):
                queue.append(neighbor)
                visited.append(neighbor)
                parents[neighbor] = node
            if neighbor == f:
                found = True
                break
    if found:
        current_node = f
        path = []
        while current_node != i:
            path.append(current_node)
            current_node = parents[current_node]
        path.append(i)
        return -1, visited, path
    
    return visited