#not anymore :D
from node import *
from algs import *
import pygame
import random

pygame.init()
Width = 1280
Height = 720
Red = (255, 16, 16)
Green = (16, 255, 16)
Blue = (16, 16, 255)
Black = (0, 0, 0)
White = (255, 255, 255)
smallfont = pygame.font.SysFont('Corbel',35)
screen = pygame.display.set_mode([Width, Height])
numOfNodes = 24
nodes = {}

def graphMaker(numOfNodes):
    global nodes
    nodes = {}
    for i in range(numOfNodes):
        for j in range(numOfNodes):
            x = Width/2 - numOfNodes * 13 + i*26
            y = Height/2 - numOfNodes * 13 + j*26
            rect = pygame.Rect((x, y), (25, 25))
            s = node(White, rect)
            nodes[(i, j)] = s

def reset_(numOfNodes):
    for i in range(numOfNodes):
        for j in range(numOfNodes):
            if nodes[(i, j)].color not in [Green, Black, Blue]:
                nodes[(i, j)].color = White

def convert(n):
    x, y = n
    x = x-((x-(Width/2-numOfNodes*13)) % 26)
    y = y-((y-(Height/2-numOfNodes*13)) % 26)
    i = (x-Width/2 + numOfNodes*13)/26
    j = (y-Height/2 + numOfNodes*13)/26
    return (i, j)

turned = False
pnodes = []
graphMaker(numOfNodes)
goal = [None, None, None]
visited = 0
BFSR = pygame.Rect((200, Height/2 - 100), (75, 50))
BFSText = smallfont.render('BFS' , True , (0,0,0))
DFSR = pygame.Rect((200, Height/2), (75, 50))
DFSText = smallfont.render('DFS' , True , (0,0,0))
reset = pygame.Rect((200, Height/2 + 100), (75, 50))
resetText = smallfont.render('Reset' , True , (0,0,0))
FPS = 60

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((25,25,25))
    if len(pnodes) > 0:
        g = random.randint(30, 150)
        r = random.randint(30, 175)
        b = random.randint(30, 175)
        color = (r, g, b)
        if pnodes[0] == True:
            if len(pnodes[1]) > 0:
                nodes[pnodes[1].pop(0)].color = color
            elif len(pnodes[2]) > 0:
                nodes[pnodes[2].pop()].color = Green
                if len(pnodes[2]) == 0 :
                    turned = False
        else:
            nodes[pnodes.pop(0)].color = color

    elif len(pnodes) == 0:
        turned = False
    visitedNodesText = smallfont.render(f'Visited nodes: {visited}' , True , (0,0,0))

    x, y = pygame.mouse.get_pos()
    state = pygame.mouse.get_pressed()

    if 200 <= x <= 275 and (Height/2 - 100) <= y <= (Height/2 - 50) and not turned: 
        pygame.draw.rect(screen, (50,255,50), BFSR)
        if state[0] == True:
            turned = True
            pnodes = BFS(goal[0], goal[1], numOfNodes, nodes)#path nodes
            reset_(numOfNodes)
    else:
        pygame.draw.rect(screen, White, BFSR)
    
    if 200 <= x <= 275 and (Height/2) <= y <= (Height/2 + 50) and not turned: 
        pygame.draw.rect(screen, (50,255,50), DFSR)
        if state[0] == True:
            turned = True
            pnodes = DFS_maze( numOfNodes, nodes)#path nodes goal[0], goal[1],
            reset_(numOfNodes)

    else:
        pygame.draw.rect(screen, White, DFSR)

    if 200 <= x <= 275 and (Height/2 + 100) <= y <= (Height/2 + 150): 
        pygame.draw.rect(screen, (255,50,50), reset)
        if state[0] == True:
            goal = [None, None, None]
            turned = False
            pnodes = []
            graphMaker(numOfNodes)
    else:
        pygame.draw.rect(screen, White, reset)
    
    screen.blit(BFSText, (200, Height/2 - 100))
    screen.blit(DFSText, (200, Height/2))
    screen.blit(resetText, ((200, Height/2 + 100)))

    if not turned:
        if Width/2-((numOfNodes/2)*26)<=x<=Width/2+(numOfNodes/2)*26 and Height/2-((numOfNodes/2)*26)<=y<=Height/2+(numOfNodes/2)*26:
            if state[2] == True:
                if goal[2] == None:
                    goal[2] = 1
                    goal[0] = convert((x, y))
                    nodes[goal[0]].color = Green
                elif goal[1] == None and convert((x,y)) != goal[0]:
                    goal[1] = convert((x,y))
                    nodes[goal[1]].color = Blue
            if state[0] == True:
                nodes[convert((x,y))].color = Black
    
    for i in range(numOfNodes):
        for j in range(numOfNodes):
            pygame.draw.rect(screen, nodes[(i,j)].color, nodes[(i,j)].rect)
    
    pygame.display.flip()
    pygame.time.delay(int((1/FPS)*1000))

pygame.quit()