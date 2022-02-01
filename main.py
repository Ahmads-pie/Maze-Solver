# not anymore :D
from node import *
from algs import BFS
import pygame
import random

pygame.init()
Width = 1280
Height = 720
Red = (255, 16, 16)
Green = (16, 255, 16)
Blue = (16, 16, 255)
Black = (0, 0, 0)
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
            s = node((255, 255, 255), rect)
            nodes[(i, j)] = s

def convert(n):
    x, y = n
    x = x-((x-(Width/2-numOfNodes*13)) % 26)
    y = y-((y-(Height/2-numOfNodes*13)) % 26)
    i = (x-Width/2 + numOfNodes*13)/26
    j = (y-Height/2 + numOfNodes*13)/26
    return (i, j)

turned = False
visited = []
path = []
pnodes = []
graphMaker(numOfNodes)
goal = [None, None, None]
start = pygame.Rect((200, Height/2 - 100), (75, 50))
startText = smallfont.render('Start' , True , (0,0,0))
end  = pygame.Rect((200, Height/2 + 100), (75, 50))
endText = smallfont.render('Reset' , True , (0,0,0))
FPS = 120

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((25,25,25))
    if len(pnodes) > 0:
        color = (random.randint(40, 175), random.randint(40, 175), random.randint(40, 175))
        if pnodes[0] == -1:
            if len(pnodes[1]) > 0:
                nodes[pnodes[1].pop(0)].color = color
            
            elif len(pnodes[2]) > 0:
                nodes[pnodes[2].pop()].color = Green
        else:
            nodes[pnodes.pop(0)].color = color
        
    x, y = pygame.mouse.get_pos()
    state = pygame.mouse.get_pressed()

    if 200 <= x <= 275 and (Height/2 - 100) <= y <= (Height/2 - 50) and not turned: 
        pygame.draw.rect(screen, (50,255,50), start)
        if state[0] == True:
            turned = True
            pnodes = BFS(goal[0], goal[1], numOfNodes, nodes)#path nodes
            print(len(pnodes))
    
    else:
        pygame.draw.rect(screen, (255,255,255), start)
    if 200 <= x <= 275 and (Height/2 + 100) <= y <= (Height/2 + 150): 
        pygame.draw.rect(screen, (255,50,50), end)
        if state[0] == True:
            goal = [None, None, None]
            turned = False
            path = list()
            visited = list()
            graphMaker(numOfNodes)
    else:
        pygame.draw.rect(screen, (255,255,255), end)
    
    screen.blit(startText, (200, Height/2 - 100))
    screen.blit(endText, ((200, Height/2 + 100)))
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