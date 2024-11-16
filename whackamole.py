import random

import pygame
#well
def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # Well Well Well
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        x,y = 0,0
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    button_x, button_y = event.pos
                    if x <= button_x < x+32 and y <= button_y < y+32:
                        x = random.randrange(0, 20) * 32
                        y = random.randrange(0, 16) * 32
                        print("You got it!")
                    else:
                        print("Nope you missed!!")
            screen.fill("light green")
            screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
            for i in range(1,33):
                pygame.draw.line(screen,'black', (32*i, 0 ), (32*i,512) )
            for i in range(1,33):
                pygame.draw.line(screen, 'black',(0, 32*i), (640, 32*i))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
