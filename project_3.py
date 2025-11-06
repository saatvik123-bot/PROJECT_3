import pygame
import sys


pygame.init()

screen = pygame.display.set_mode((640, 480))

pygame.display.set_caption("My First Game Screen")

bg_color = (255, 255, 255)

rect_color = (0, 128, 255)
rect_width, rect_height = 200 ,100
rect = pygame.Rect(0, 0, rect_width, rect_height)
rect.center = (640 // 2, 480 // 2)

font = pygame.font.SysFont(None, 36)
text = font.render('Hello Pygame!', True, (0, 0, 0))
text_rect = text.get_Rect(centre=(640 // 2, 50))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(bg_color)
    pygame.draw.rect(screen, rect_color, rect)
    screen.blit(text, text_rect)
    pygame.display.flip()

pygame.quit()
sys.exit()