import pygame
import copy
import numpy as np
import pandas as pd
import random

pygame.init()

#Game info
Name = "Sudoku"
screenHeight = 9*50
screenWidth = screenHeight
tileSize = screenHeight // 9
marginSize = tileSize
borderSize = 1
borderColor = (100,100,100)
marginColor = (170, 170, 170)
tileColor = (200, 200, 200)
fontColor = (0,0,0)
speed = 100
clock = pygame.time.Clock()
font = pygame.font.SysFont('Times New Roman', 30)
winfont = pygame.font.SysFont('Times New Roman', 20, bold = True)
coords = (0,0)
winWidth = tileSize * 6
winHeight = tileSize * 2

#Read sudokus

sudokus = pd.read_csv('sudoku.csv')
rand = random.randint(0, len(sudokus)-1)

#Select sudoku
quiz = [sudokus['quizzes'][rand][j:j+9] for j in range (0, 81, 9)]
solution = [sudokus['solutions'][rand][j:j+9] for j in range (0, 81, 9)]

for j in range(9):
    quiz[j] = list(quiz[j])
    solution[j] = list(solution[j])


quiz = [[int(float(j)) for j in i] for i in quiz]
solution = [[int(float(j)) for j in i] for i in solution]

sudoku =        copy.deepcopy(quiz)

win = pygame.display.set_mode((screenWidth + borderSize * 2, screenHeight + borderSize * 2 + marginSize*2))

def updateDisplay(sudoku, locked, valid, solved, showSolver):
    pygame.display.set_caption(Name)
    win.fill(borderColor)
    pygame.draw.rect(win, marginColor, (0, screenHeight + borderSize*2, screenWidth + borderSize * 2, marginSize * 2))
    for i in range(9):
        for j in range(9):
            rect = (i*tileSize + borderSize, j*tileSize + borderSize, tileSize - borderSize*2, tileSize - borderSize * 2)
            pygame.draw.rect(win, tileColor, rect)
    for i in range(9):
        for j in range(9):
                if sudoku[i][j] == 0:
                    pass
                else:
                    if locked[i][j] == True:
                        textSurface = font.render(str(sudoku[i][j]), False, (0,0,0))
                    elif valid [i][j] == False:
                        textSurface = textSurface = font.render(str(sudoku[i][j]), False, (150,0,0))
                    else:
                        textSurface = textSurface = font.render(str(sudoku[i][j]), False, (0,150,0))
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

    #Solver button
    if showSolver == True:
        solveText = winfont.render("Solve", False, (0, 0, 0))
        pygame.draw.rect(win, (100, 100, 100), (tileSize//2, screenHeight + borderSize * 2 + marginSize//2, int(tileSize*2), int(tileSize)), 2)
        win.blit(solveText, solveText.get_rect(center = (int(1.5*tileSize), int(screenHeight + borderSize * 2 + marginSize))))

    #Draw winscreen if game is won
    if solved == True:
        #pygame.draw.rect(win, (100, 100, 100), (screenWidth//2 - winWidth//2, screenHeight//2 - winHeight // 2, winWidth, winHeight))

        #Add wintext on screen
        statusText = winfont.render("Solved. Get new puzzle?", False, (0,100,0))
        yesText = winfont.render("Yes", False, (0, 100, 0))
        noText = winfont.render("No", False, (100, 0, 0))

        pygame.draw.rect(win, (100, 100, 100), (tileSize * 3, screenHeight + borderSize * 2 + marginSize, int(tileSize*1.5) - 10, int(tileSize*.75)), 2)
        pygame.draw.rect(win, (100, 100, 100), (tileSize * 3 + int(tileSize * 1.5) + 10, screenHeight + borderSize * 2 + marginSize, int(tileSize*1.5) - 10, int(tileSize*.75)), 2)
        win.blit(statusText, statusText.get_rect(center = ((screenWidth + borderSize*2)//2, screenHeight + borderSize*2 + marginSize // 2)))
        win.blit(yesText, yesText.get_rect(center = (int(tileSize*3.75) - 5, screenHeight + borderSize + marginSize*1.5 - 5)))
        win.blit(noText, noText.get_rect(center = (int(tileSize*(1.75+3.75)-7.5), screenHeight + borderSize + marginSize*1.5 - 5)))


    pygame.display.update()

def possible(i, j, n):

    if n != 0:
        #Check row
        for k in range(9):
            if j != k:
                if n == sudoku[i][k]:
                    return False

        #Check column
        for k in range(9):
            if i != k:
                if n == sudoku[k][j]:
                    return False

        #Check square
        row = (i//3)*3
        col = (j//3)*3

        for k in range(row, row+3):
            for l in range(col, col+3):
                if i != k and j != l:
                    if n == sudoku[k][l]:
                        return False

    return True

def solve(sudoku):
    for i in range(10):
        for j in range(10):
            if sudoku[i][j] == 0:
                for k in range(1,10):
                    if possible(i, j, k):
                        board[i][j] = k
                        solve(grid)
                        board[i][j] = 0
            return


def put_number(currentValue):
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
                    if keys[pygame.K_BACKSPACE]:
                        value = 0
                        wait = False
                        break
                    if keys[pygame.K_ESCAPE]:
                        value = currentValue
                        wait = False
                        break
    return value

run = True
pos = [0,0]
solved = False
showSolver = True
locked = [[],[],[],[],[],[],[],[],[]]

for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            locked[i].append(False)
        else:
            locked[i].append(True)

while run:

    valid = [[],[],[],[],[],[],[],[],[]]
    clock.tick(speed)

    for i in range(9):
        for j in range(9):
            if possible(i, j, sudoku[i][j]):
                valid[i].append(True)
            else:
                valid[i].append(False)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break

        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()

            if showSolver == True:
                solveX1, solveX2 = tileSize//2, tileSize//2 + int(tileSize*2)
                solveY1, solveY2 = screenHeight + borderSize * 2 + marginSize//2, screenHeight + borderSize * 2 + marginSize//2 + int(tileSize)

                if pos[0] > solveX1 and pos[0] < solveX2 and pos[1] > solveY1 and pos[0] < solveY2:
                    sudoku = copy.deepcopy(solution)
                    solved = True


            if solved == True:
                #Specify box positions
                yesX1, yesX2 = tileSize * 3, tileSize * 3 + int(tileSize*1.5) - 10
                yesY1, yesY2 = screenHeight + borderSize * 2 + marginSize, screenHeight + borderSize * 2 + marginSize + int(tileSize*.75)

                noX1, noX2 = tileSize * 3 + int(tileSize * 1.5) + 10, tileSize * 3 + int(tileSize * 1.5) + 10 + int(tileSize*1.5) - 10
                noY1, noY2 = screenHeight + borderSize * 2 + marginSize, screenHeight + borderSize * 2 + marginSize + int(tileSize*.75)

                if pos[0] > yesX1 and pos[0] < yesX2 and pos[1] > yesY1 and pos[1] < yesY2:
                    solved = False
                    showSolver = True

                    #Select random sudoku
                    rand = random.randint(0, len(sudokus)-1)
                    quiz = [sudokus['quizzes'][rand][j:j+9] for j in range (0, 81, 9)]
                    solution = [sudokus['solutions'][rand][j:j+9] for j in range (0, 81, 9)]

                    for j in range(9):
                        quiz[j] = list(quiz[j])
                        solution[j] = list(solution[j])

                    quiz = [[int(float(j)) for j in i] for i in quiz]
                    solution = [[int(float(j)) for j in i] for i in solution]
                    sudoku = copy.deepcopy(quiz)

                    locked = [[],[],[],[],[],[],[],[],[]]

                    for i in range(9):
                        for j in range(9):
                            if sudoku[i][j] == 0:
                                locked[i].append(False)
                            else:
                                locked[i].append(True)

                elif pos[0] > noX1 and pos[0] < noX2 and pos[1] > noY1 and pos[1] < noY2:
                    print("Goodbye.")
                    run = False
                    break

            for i in range(9):
                for j in range(9):
                    if pos[0] > tileSize*j and pos[0] < tileSize*(j+1) and pos[1] > tileSize*i and pos[1] < tileSize*(i+1):
                        if locked[i][j] == False:
                            pygame.draw.rect(win, (255,255,255), (j*tileSize + borderSize*2, i*tileSize + borderSize*2, tileSize - borderSize*3, tileSize - borderSize*3))
                            pygame.display.update()
                            val = put_number(sudoku[i][j])
                            sudoku[i][j] = val

                            if possible(i, j, sudoku[i][j]):
                                valid[i][j] = True
                            else:
                                valid[i][j] = False

                        break
                else:
                    continue
                break


    num_zero = sum(e.count(0) for e in sudoku)
    num_valid = sum(e.count(True) for e in valid)

    if num_valid == 81 and num_zero == 0:
        solved = True
        showSolver = False
    else:
        solved = False
        showSolver = True


    updateDisplay(sudoku, locked, valid, solved, showSolver)
