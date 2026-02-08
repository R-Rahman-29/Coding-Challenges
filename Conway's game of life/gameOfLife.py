import pygame


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
        pygame.draw.rect(screen, YELLOW, (*topLeft, TILE_SIZE, TILE_SIZE))

#Defining main function
def main():
    running = True
    positions = set()
    positions.add((10, 10))

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

        screen.fill(GREY) #Defines background colour of the window
        drawGrid(positions) #Draws the grid
        pygame.display.update() #Updates the display

    pygame.quit() #Closes window

if __name__ == "__main__":
    main()