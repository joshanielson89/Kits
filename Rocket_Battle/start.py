import pygame
from myLibrary import *
import time

## this will tell pygame to start
pygame.init()

## decide how big the window size will be
display_width = 800
display_height = 600
## this will keep track of time throughout the game
clock = pygame.time.Clock()

## this will make the screen display, you can also give your program a name
programName = "Your programs name here"
gameDisplay = start_display(display_width, display_height, programName)


## this block of code defines our ship
class Ship:
    def __init__(self, x_position, y_position, delta_x, delta_y, width, height):
        self.mX = x_position 						        # this sets where our x position will be
        self.mY = y_position 						        # this sets where our y position will be
        self.mDX = delta_x							        # this tells us how fast our ship moves
        self.mDY = delta_y							
        self.mWidth = width 						        # this sets our ships width
        self.mHeight = height 						        # this sets our ships height
        self.mImage = pygame.image.load('images/GC.jpg') 	# this tells us which picture to use for our ship

def makeShip():
	x_position = display_width * 0.45
	y_position = display_height * 0.85
	delta_x = 0
	delta_y = 0
	width = 100
	height = 88
	ship = Ship(x_position, y_position, delta_x, delta_y, width, height)
	return ship

def drawShip(ship):
	draw_image(gameDisplay, ship.mX, ship.mY, ship.mImage)

def moveShip(ship):
	ship.mX += ship.mDX
	ship.mY += ship.mDY
	if ship.mX < 0:
		ship.mX = 0
	if ship.mX + ship.mWidth > display_width:
		ship.mX = display_width - ship.mWidth
	if ship.mY + ship.mHeight > display_height:
		ship.mY = display_height - ship.mHeight
	if ship.mY < 0:
		ship.mY = 0

## this block is what calls the rest of our code 
def main_loop():
    gameOver = False 

    ship = makeShip() 			#this will make our ship
    ## this while loop will repeat over and over until the game ends
    while not gameOver:
    	## this for loop keeps track of all the keys that you push in the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT: ## this would be the X button in the top right corner
                pygame.quit()
                quit()
            ## this if statement will keep track of all keys pressed DOWN
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_LEFT:
                	# if the Left arrow key was pressed
                	ship.mDX = -3
                if event.key == pygame.K_RIGHT:
                	# if the Right arrow key was pressed
                	ship.mDX = 3
                if event.key == pygame.K_UP:
                	# if the Up arrow key was pressed
                	ship.mDY = -3
                if event.key == pygame.K_DOWN:
                	# if the Down arrow key was pressed
                	ship.mDY = 3
                if event.key == pygame.K_SPACE:
                	# if the Space key was pressed
                	print("space key pressed")
                if event.key == pygame.K_r:
                	# if the R key was pressed
                	print("restart key pressed")
            ## this if statement will keep track of all keys RELEASED
            if event.type == pygame.KEYUP:
                 if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                 	ship.mDX = 0
                 if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                 	ship.mDY = 0

        moveShip(ship)												## this will update our ships position
        gameDisplay.fill(black) 									## set the background to be black (other colors available in myLibrary.py)
        drawShip(ship)										 		## this will draw our ship

        # this will refresh the screen and make updates
        pygame.display.update()
        clock.tick(60)

main_loop()