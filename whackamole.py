import pygame
import random

def main():
    try:
        pygame.init()
        mole_image = pygame.image.load("mole.png")
        mole_image = pygame.transform.scale(mole_image, (32, 32))
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True

        mole_rect = mole_image.get_rect(topleft=(0, 0))

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if mole_rect.collidepoint(event.pos):
                        new_x = random.randint(0, 19) * 32
                        new_y = random.randint(0, 15) * 32
                        mole_rect.topleft = (new_x, new_y)

            screen.fill("light green")

            for x in range(0, 640, 32):
                pygame.draw.line(screen, "black", (x, 0), (x, 512))
            for y in range(0, 512, 32):
                pygame.draw.line(screen, "black", (0, y), (640, y))

            screen.blit(mole_image, mole_rect)

            pygame.display.flip()
            clock.tick(60)

    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
