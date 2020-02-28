import pygame
import numpy as np

pygame.init()

#Game info
Name = "Sudoku"
screenHeight = 9*50
screenWidth = screenHeight
tileSize = screenHeight // 9
borderSize = 1
borderColor = (100,100,100)
tileColor = (200, 200, 200)
fontColor = (0,0,0)
speed = 100
clock = pygame.time.Clock()
font = pygame.font.SysFont('Times New Roman', 30)
coords = (0,0)

sudoku =        [
                [5,3,0,0,7,0,0,0,0],
                [6,0,0,1,9,5,0,0,0],
                [0,9,8,0,0,0,0,6,0],
                [8,0,0,0,6,0,0,0,3],
                [4,0,0,8,0,3,0,0,1],
                [7,0,0,0,2,0,0,0,6],
                [0,6,0,0,0,0,2,8,0],
                [0,0,0,4,1,9,0,0,5],
                [0,0,0,0,8,0,0,7,9]
                ]

win = pygame.display.set_mode((screenWidth + borderSize * 2, screenHeight + borderSize * 2))

def updateDisplay(font, sudoku):
    pygame.display.set_caption(Name)
    win.fill(borderColor)
    for i in range(9):
        for j in range(9):
            rect = (i*tileSize + borderSize, j*tileSize + borderSize, tileSize - borderSize*2, tileSize - borderSize * 2)
            pygame.draw.rect(win, tileColor, rect)
    for i in range(9):
        for j in range(9):
                if sudoku[i][j] == 0:
                    pass
                else:
                    textSurface = font.render(str(sudoku[i][j]), False, (0,0,0))
                    win.blit(textSurface, (j*tileSize + tileSize//2 - textSurface.get_rect().width//2, i*tileSize + tileSize//2 - textSurface.get_rect().height//2))

    #Horizontal grid lines
    pygame.draw.line(win, (0,0,0), (0, tileSize*3), (screenWidth, tileSize*3), borderSize * 3)
    pygame.draw.line(win, (0,0,0), (0, tileSize*6), (screenWidth, tileSize*6), borderSize * 3)

    #Vertical grid lines
    pygame.draw.line(win, (0,0,0), (tileSize*3, 0), (tileSize*3, screenHeight), borderSize * 3)
    pygame.draw.line(win, (0,0,0), (tileSize*6, 0), (tileSize*6, screenHeight), borderSize * 3)

    #Border
    pygame.draw.line(win, (0,0,0), (0, 0), (0, screenHeight), borderSize * 3)
    pygame.draw.line(win, (0,0,0), (0, 0), (screenWidth, 0), borderSize * 3)
    pygame.draw.line(win, (0,0,0), (screenWidth, 0), (screenWidth, screenHeight), borderSize * 3)
    pygame.draw.line(win, (0,0,0), (0, screenHeight), (screenWidth, screenHeight), borderSize * 3)

    pygame.display.update()

def possible(x, y, n):
    pass

def solve(grid):
    for i in range(10):
        for j in range(10):
            if grid[i][j] == 0:
                for k in range(1,10):
                    if possible(i, j, k):
                        board[i][j] = k
                        solve(grid)
                        board[i][j] = 0
            return


def wait():
    wait = True
    while wait:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:

                    keys = pygame.key.get_pressed()

                    if keys[pygame.K_1]:
                        value = 1
                        wait = False
                        break
                    if keys[pygame.K_2]:
                        value = 2
                        wait = False
                        break
                    if keys[pygame.K_3]:
                        value = 3
                        wait = False
                        break
                    if keys[pygame.K_3]:
                        value = 3
                        wait = False
                        break
                    if keys[pygame.K_4]:
                        value = 4
                        wait = False
                        break
                    if keys[pygame.K_5]:
                        value = 5
                        wait = False
                        break
                    if keys[pygame.K_6]:
                        value = 6
                        wait = False
                        break
                    if keys[pygame.K_7]:
                        value = 7
                        wait = False
                        break
                    if keys[pygame.K_8]:
                        value = 8
                        wait = False
                        break
                    if keys[pygame.K_9]:
                        value = 9
                        wait = False
                        break
                    if keys[pygame.K_ESCAPE]:
                        value = 0
                        wait = False
                        break

    return value

run = True
pos = [0,0]
typeNumber = False

while run:

    clock.tick(speed)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break

        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            typeNumber = True

            for i in range(9):
                for j in range(9):
                    if pos[0] > tileSize*j and pos[0] < tileSize*(j+1) and pos[1] > tileSize*i and pos[1] < tileSize*(i+1):
                        pygame.draw.rect(win, (255,255,255), (j*tileSize + borderSize*2, i*tileSize + borderSize*2, tileSize - borderSize*3, tileSize - borderSize*3))
                        pygame.display.update()
                        sudoku[i][j] = wait()

                        break
                else:
                    continue
                break



    updateDisplay(font, sudoku)
