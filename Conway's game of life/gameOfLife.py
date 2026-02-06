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
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Conway's Game of Life")
    clock = pygame.time.Clock()

    return screen, clock

#Defining main function
def main():
    #Initialising pygame
    pygame.init()
    
    #Calling screen setup function
    screen, clock = screenSetUp()

    #Game loop
    running = True
    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK)
        pygame.display.update()

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()

