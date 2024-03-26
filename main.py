
import pygame

def main():

    #Only run if not imported
    print("Running program...")

    #Start the pygame window
    pygame.init()

    #Window setup
    gameWindow = pygame.display.set_mode((1200, 500))
    pygame.display.set_caption("Connect X by BARJ")

    running = True

    #Get Runtime Events
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    running = False

        gameWindow.fill((255, 255, 255))
            
        pygame.draw.circle(gameWindow, (0, 0, 255), (250, 250), 75)

        pygame.display.flip()

    #Close pygame
    pygame.quit()


if __name__ == "main":
     main()