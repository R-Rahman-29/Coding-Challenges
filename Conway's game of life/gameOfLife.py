import pygame
#import random


#Declaring colours constants
BLACK = (0, 0, 0)
GREY = (128, 128, 128)
YELLOW = (255, 255, 0)

#Declaring screen constants
WIDTH, HEIGHT = 600, 600
TILE_SIZE = 20
GRID_WIDTH = WIDTH // TILE_SIZE
GRID_HEIGHT = HEIGHT // TILE_SIZE
FPS = 60

#Function for setting up the screen
def screenSetUp():
    #Setting up the screen
    global screen, clock #Declaring screen and clock as global variables
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    pygame.display.set_caption("Rayan's Game of Life")

#Function for drawing the grid
def drawGrid(positions):
    drawRec(positions)

    #Draws horizontal lines
    for row in range(GRID_HEIGHT):
        pygame.draw.line(screen, BLACK, (0, row * TILE_SIZE), (WIDTH, row * TILE_SIZE))
    
    #Draws vertical lines
    for col in range(GRID_WIDTH):
        pygame.draw.line(screen, BLACK, (col * TILE_SIZE, 0), (col * TILE_SIZE, HEIGHT))

#Function for drawing each cell
def drawRec(positions):
    for position in positions:
        col, row = position
        topLeft = (col * TILE_SIZE, row * TILE_SIZE)
        pygame.draw.rect(screen, YELLOW, (*topLeft, TILE_SIZE, TILE_SIZE)) #Draws the yellow rectangle 

#Function for handling user input
def userInput(event,positions):
    playing = True

    #Code for adding cells to the grid on mouse click
    if event.type == pygame.MOUSEBUTTONDOWN: #Checks if the mouse button is clicked
        x, y = pygame.mouse.get_pos() #Gets the mouse position
        #Converts pixel coordinates to grid coordinates
        col = x // TILE_SIZE 
        row = y // TILE_SIZE 
        pos = (col, row) 

        #Checks if cell is alive
        if pos in positions:
            positions.remove(pos) #If it is, remove it
        else:
            positions.add(pos) #If it is not, add it
    
    #Gets key presses
    if event.type == pygame.KEYDOWN:
        #Pausing the simulation
        if event.key == pygame.K_SPACE: #Checks if space bar is pressed
            playing = not playing 
    
        #Clears the grid 
        if event.key == pygame.K_c: #Checks if c key is pressed
            positions = set() #Resets the grid
            playing = False 

        #Randomly populates the grid
        if event.key == pygame.K_r:
            positions = set()

    #Function for randomly populating the grid 
    #def ranPopulate():


#Defining main function
def main():
    running = True
    positions = set()

    #Initialising pygame
    pygame.init()
    
    #Calling screen setup function
    screenSetUp()

    #Game loop
    while running:
        clock.tick(FPS) #Controls the frame rate

        #Closes the window if the user clicks the close button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            userInput(event, positions) #Calls user input function
        
        screen.fill(GREY) #Defines background colour of the window
        drawGrid(positions) #Draws the grid
        pygame.display.update() #Updates the display

    pygame.quit() #Closes window

if __name__ == "__main__":
    main()