#not anymore :D
from node import *
from algs import *
import pygame
import random

pygame.init()
Width = 1280 # 965, 315, 275
Height = 720
Red = (255, 16, 16)
Green = (16, 255, 16)
Blue = (16, 16, 255)
Black = (0, 0, 0)
White = (255, 255, 255)
smallfont = pygame.font.SysFont('Corbel',35)
screen = pygame.display.set_mode([Width, Height])
numOfNodes = 25
nodes = {}

def graphMaker(numOfNodes, maze = False):
    global nodes
    nodes = {}
    color = White
    if maze:
        color = Black
    for i in range(numOfNodes):
        for j in range(numOfNodes):
            x = Width/2 - numOfNodes * 13 + i*26
            y = Height/2 - numOfNodes * 13 + j*26
            rect = pygame.Rect((x, y), (25, 25))
            s = node(color, rect)
            nodes[(i, j)] = s

def reset_(numOfNodes):
    for i in range(numOfNodes):
        for j in range(numOfNodes):
            if nodes[(i, j)].color not in [Black, Blue]:
                nodes[(i, j)].color = White

def convert(n):
    x, y = n
    x = x-((x-(Width/2-numOfNodes*13)) % 26)
    y = y-((y-(Height/2-numOfNodes*13)) % 26)
    i = (x-Width/2 + numOfNodes*13)/26
    j = (y-Height/2 + numOfNodes*13)/26
    return (i, j)

#Initialize variables
turned = False
mnodes = [] # maze nodes
lm = 0 # length of maze nodes
pnodes = [] # path nodes
graphMaker(numOfNodes)
goal = [None, None, None]
visited = 0
BFSR = pygame.Rect((125, Height/2 - 100), (150, 50)) # R at the end means Rectangle
BFSText = smallfont.render('BFS' , True , (0,0,0))
DFSR = pygame.Rect((125, Height/2), (150, 50))
DFSText = smallfont.render('DFS' , True , (0,0,0))
reset = pygame.Rect((125, Height/2 + 100), (150, 50))
resetText = smallfont.render('Reset' , True , (0,0,0))
DFS_mazeR = pygame.Rect((1005, Height/2 - 100), (150, 50))
DFS_mazeText = smallfont.render('DFS Maze' , True , (0,0,0))
visitedR = pygame.Rect((10, 100), (275, 50))
FPS = 60


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((25,25,25))

    if len(mnodes) > 0:
        nodes[mnodes.pop(0)].color = White
    if len(pnodes) > 0: 
        colors = [(154, 30, 50), (183, 115, 24), (245, 101, 66), (100,15,74), (15, 76, 92), (55, 94, 151)] #
        ci = 5 - (numOfNodes**2 - visited)//105
        if lm:
            ci = 5 - (lm - visited) // (lm//6)
        if ci == -1:
            ci = 0
        color = colors[ci]
        color = (random.randint(-10, 10)+color[0], random.randint(-10, 10)+color[1], random.randint(-10, 10)+color[2])
        if pnodes[0] == True:
            if len(pnodes[1]) > 0:
                nodes[pnodes[1].pop(0)].color = color
                visited += 1
            elif len(pnodes[2]) > 0:
                nodes[pnodes[2].pop()].color = (0, 255, 0)
                if len(pnodes[2]) == 0:
                    turned = False
        else:
            nodes[pnodes.pop(0)].color = color
            visited += 1

    elif len(pnodes) == 0:
        turned = False
    
    visitedNodesText = smallfont.render(f'Visited nodes: {visited}' , True , (0,0,0))
    pygame.draw.rect(screen, White, visitedR)

    x, y = pygame.mouse.get_pos()
    state = pygame.mouse.get_pressed()
    if 125 <= x <= 275 and (Height/2 - 100) <= y <= (Height/2 - 50) and not turned: 
        pygame.draw.rect(screen, (50,255,50), BFSR)
        if state[0] == True and None not in goal[0:1]:
            turned = True
            visited = 0
            pnodes = BFS(goal[0], goal[1], numOfNodes, nodes)
            reset_(numOfNodes)
    else:
        pygame.draw.rect(screen, White, BFSR)
    
    if 125 <= x <= 275 and (Height/2) <= y <= (Height/2 + 50) and not turned: 
        pygame.draw.rect(screen, (50,255,50), DFSR)
        if state[0] == True and None not in goal[0:1]: 
            turned = True
            visited = 0
            pnodes = DFS(goal[0], goal[1], numOfNodes, nodes) 
            reset_(numOfNodes)

    else:
        pygame.draw.rect(screen, White, DFSR)

    if 125 <= x <= 275 and (Height/2 + 100) <= y <= (Height/2 + 150): 
        pygame.draw.rect(screen, (255,50,50), reset)
        if state[0] == True:
            goal = [None, None, None]
            turned = False
            visited = 0
            pnodes = []
            mnodes = []
            graphMaker(numOfNodes)
    else:
        pygame.draw.rect(screen, White, reset)
    
    if 1005 <= x <= 1155 and (Height/2 - 100) <= y <= (Height/2 - 50) and not turned: 
        pygame.draw.rect(screen, (50,255,50), DFS_mazeR)
        if state[0] == True:
            goal = [None, None, None]
            mnodes, lm = DFS_maze(numOfNodes, nodes)
            graphMaker(numOfNodes, True)

    else:
        pygame.draw.rect(screen, White, DFS_mazeR)

    screen.blit(BFSText, (130, Height/2 - 100))
    screen.blit(DFSText, (130, Height/2))
    screen.blit(resetText, (130, Height/2 + 100))
    screen.blit(DFS_mazeText, (1005, Height/2-100))
    screen.blit(visitedNodesText, (10, 100))
    if not turned:
        if Width/2-((numOfNodes/2)*26)<=x<=Width/2+(numOfNodes/2)*26 and Height/2-((numOfNodes/2)*26)<=y<=Height/2+(numOfNodes/2)*26:
            if state[2] == True:
                if goal[2] == None and nodes[convert((x,y))].color != Black:
                    goal[2] = 1
                    goal[0] = convert((x, y))
                    nodes[goal[0]].color = Blue
                elif goal[1] == None and convert((x,y)) != goal[0] and nodes[convert((x,y))].color != Black:
                    goal[1] = convert((x,y))
                    nodes[goal[1]].color = Blue
            if state[0] == True and nodes[convert((x,y))].color != Blue:
                nodes[convert((x,y))].color = Black
    
    for i in range(numOfNodes):
        for j in range(numOfNodes):
            pygame.draw.rect(screen, nodes[(i,j)].color, nodes[(i,j)].rect)
    
    pygame.display.update()
    pygame.time.delay(int((1/FPS)*1000))

pygame.quit()