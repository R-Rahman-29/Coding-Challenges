import pygame
import random

#Declaring colours constants
BACKGROUND = "#46444b"
GRID = "#000000"
CELL = "#daa7ad"

#Declaring screen constants
WIDTH, HEIGHT = 600, 600
TILE_SIZE = 15
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
        pygame.draw.line(screen, GRID, (0, row * TILE_SIZE), (WIDTH, row * TILE_SIZE))
    
    #Draws vertical lines
    for col in range(GRID_WIDTH):
        pygame.draw.line(screen, GRID, (col * TILE_SIZE, 0), (col * TILE_SIZE, HEIGHT))

#Function for drawing each cell
def drawRec(positions):
    for position in positions:
        col, row = position
        topLeft = (col * TILE_SIZE, row * TILE_SIZE)
        pygame.draw.rect(screen, CELL, (*topLeft, TILE_SIZE, TILE_SIZE)) #Draws the yellow rectangle 

#Function for handling user input
def userInput(event, positions, playing):
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
            positions = ranPopulate(random.randrange(2, 5) * GRID_WIDTH)
    
    return positions, playing

#Function for randomly populating the grid 
def ranPopulate(num):
    positions = set()
    numClusters = num // 2 #Creates clusters instead of individuals
    clusterSize = random.randrange(3, 6) #Determines the size of each cluster

    for _ in range(numClusters):
        #Pick random centre point
        centreX = random.randrange(2, GRID_WIDTH - 2)
        centreY = random.randrange(2, GRID_HEIGHT - 2)

        #Add 3-5 cells around the centre point to create a cluster
        for _ in range(clusterSize):
            x = centreX + random.randrange(-1, 2) #Randomly picks a point around the centre point
            y = centreY + random.randrange(-1, 2) 
            
            if 0 <= x < GRID_WIDTH and 0 <= y < GRID_HEIGHT: #Checks if the point is within bounds
                positions.add((x, y)) #Adds the point to the set of positions

    return positions

#Function for updating which cells are alive for the next generation
def adjustGrid(positions):
    allNeighbours = set()
    newPositions = set()
    
    #Check if living cells survives 
    for position in positions: 
        neighbours = getNeighbours(position) #Get all neighbours 
        allNeighbours.update(neighbours)

        neighbours = list(filter(lambda x: x in positions, neighbours)) #Fitler to find out which neighbours are alive 

        #Implements rule: has 2 or 3 living neighbours, it survives
        if len(neighbours) in [2, 3]:
            newPositions.add(position)

    #Check if dead cells come to life 
    for position in allNeighbours:
        neighbours = getNeighbours(position) #Get all neighbours 
        neighbours = list(filter(lambda x: x in positions, neighbours)) #Checks which neighbours are alive

        #Implements rule: If dead and has 3 living neighbours, comes to life
        if len(neighbours) == 3: 
            newPositions.add(position)

    return newPositions

#Function for finding all neighbours of a cell
def getNeighbours(pos):
    x, y = pos 
    neighbours = []

    for dx in [-1, 0, 1]: #Checks left, same and right
        if x + dx < 0 or x + dx >= GRID_WIDTH:
            continue #Skip if out of bounds 

        for dy in [-1, 0, 1]: #Checks up, same and down
            if y + dy< 0 or y + dy >= GRID_HEIGHT:
                continue #Skips if out of bounds

            if dx == 0 and dy == 0:
                continue #Skips the cell itself

            neighbours.append((x + dx, y + dy))
            
    return neighbours 

#Defining main function
def main():
    playing = False
    running = True
    positions = set()
    count = 0
    updateFreq = 5 #Determines the speed of the game 

    #Initialising pygame
    pygame.init()
    
    #Calling screen setup function
    screenSetUp()

    #Game loop
    while running:
        clock.tick(FPS) #Controls the frame rate

        if playing: 
            count += 1

        if count >= updateFreq:
            count = 0
            positions = adjustGrid(positions)

        pygame.display.set_caption("Playing" if playing else "Paused") #Updates the window title to show if the simulation is playing or paused

        #Closes the window if the user clicks the close button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            positions, playing = userInput(event, positions, playing) #Calls user input function
        
        screen.fill(BACKGROUND) #Defines background colour of the window
        drawGrid(positions) #Draws the grid
        pygame.display.update() #Updates the display

    pygame.quit() #Closes window

if __name__ == "__main__":
    main()