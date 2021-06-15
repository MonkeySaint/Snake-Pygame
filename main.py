# Name: Kyle Vardy
# Date: June 7, 2021
# Purpose: To create snake in python.

# Imports
import pygame
import random
import sys


# Classes
class Snake(object):
    def __init__(self):
        self.length = 1
        self.tail = [((screenWidth / 2), (screenHeigh / 2))]
        self.direction = random.choice([moveUp, moveDown, moveLeft, moveRight])
        self.colour = (0, 255, 0)
        self.borderColour = (0, 200, 0)

    def getHeadPos(self):
        return self.tail[0]

    def turn(self, point):
        if self.length > 1 and (point[0] * -1, point[1] * -1) == self.direction:
            return
        self.direction = point

    def move(self):
        currentHeadPos = self.getHeadPos()
        x, y = self.direction
        newHeadPos = (((currentHeadPos[0] + (x*gridSize)) % screenWidth), (currentHeadPos[1] + (y * gridSize)) % screenHeigh)
        if len(self.tail) > 2 and newHeadPos in self.tail[2:]:
            self.reset
        else:
            self.tail.insert(0, newHeadPos)
        if len(self.tail) > self.length:
            self.tail.pop

    def reset(self):
        self.length = 1
        self.tail = [((screenWidth / 2), (screenHeigh / 2))]
        self.direction = random.choice([moveUp, moveDown, moveLeft, moveRight])

    def draw(self, surface):
        for item in self.tail:
            pygame.draw.rect(surface, self.colour, (item[0], item[1], gridSize, gridSize))
            pygame.draw.rect(surface, self.borderColour, (item[0], item[1], gridSize, gridSize), 1)


class Food(object):
    def __init__(self):
        self.pos = (0, 0)
        self.colour = (255, 0, 0)
        self.randomPos()

    def randomPos(self):
        self.pos = (random.randint(0, gridWidth - 1) * gridSize, random.randint(0, gridHeight - 1) * gridSize)

    def draw(self, surface):
        pygame.draw.rect(surface, self.colour, (self.pos[0], self.pos[1], gridSize, gridSize))


def drawGrid(surface):
    for y in range(0, int(gridHeight)):
        for x in range(0, int(gridWidth)):
            if (x + y) % 2 == 0:
                pygame.draw.rect(surface, (0, 0, 0), (x * gridSize, y * gridSize, gridSize, gridSize))
                return
            pygame.draw.rect(surface, (255, 255, 255), (x * gridSize, y * gridSize, gridSize, gridSize))


# Global variables
screenWidth = 400
screenHeigh = 400
gridSize = 20
gridWidth = screenHeigh / gridSize
gridHeight = screenWidth / gridSize
moveUp = (0, -1)
moveDown = (0, 1)
moveLeft = (-1, 0)
moveRight = (1, 0)
score = 0

# Initializes classes
pygame.init()
pygame.font.init()
snake = Snake()
food = Food()

# Creates the display
canvas = pygame.display.set_mode((screenWidth, screenHeigh))
pygame.display.set_caption("Snake")

font = pygame.font.Font("../Snake/ErbosDraco1StOpenNbpRegular-l5wX.ttf", 30)

# Starts the main loop
run = True

# Main loop where everything is drawn and calculated
while run:
    # Updates the canvas

    # Limits the frames per second to 60
    pygame.time.Clock().tick(10)

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_UP:
                snake.turn(moveUp)
            if e.key == pygame.K_DOWN:
                snake.turn(moveDown)
            if e.key == pygame.K_LEFT:
                snake.turn(moveLeft)
            if e.key == pygame.K_RIGHT:
                snake.turn(moveRight)
    drawGrid(canvas)
    snake.move()
    if snake.getHeadPos() == food.pos:
        snake.length += 1
        score += 1
        food.randomPos()
    snake.draw(canvas)
    food.draw(canvas)
    canvas.blit(canvas, (0,0))
    label = font.render(str(score), False, (255, 255, 255))
    canvas.blit(label, (12, screenHeigh - 42))
    pygame.display.update()

# Exits the game
pygame.quit()
# End of program.
