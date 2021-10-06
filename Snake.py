import pygame
import random
pygame.init()


def main():

    class APPLE:
        def __init__(self):
            self.x = random.randint(0, cell_number - 1)
            self.y = random.randint(0, cell_number - 1)
            self.pos = pygame.math.Vector2(self.x, self.y)

        def draw_apple(self):
            apple_rect = pygame.Rect(self.pos.x * cell_size, self.pos.y * cell_size, cell_size, cell_size)
            pygame.draw.rect(screen, (224, 25, 51), apple_rect)

    class SNAKE:
        def __init__(self):
            self.body = [pygame.math.Vector2(5, 7), pygame.math.Vector2(6, 7), pygame.math.Vector2(7, 7)]
            self.direction = pygame.math.Vector2(1, 0)

        def draw_snake(self):
            for block in self.body:
                block_rect = pygame.Rect(block.x * cell_size, block.y * cell_size, cell_size, cell_size)
                pygame.draw.rect(screen, (69, 69, 69), block_rect)

        def move_snake(self):
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]

    cell_size = 30
    cell_number = 15
    pygame.display.set_caption("Snake")
    screen = pygame.display.set_mode((cell_size * cell_number, cell_size * cell_number))
    clock = pygame.time.Clock()

    running = True
    apple = APPLE()
    snake = SNAKE()

    screen_update = pygame.USEREVENT
    pygame.time.set_timer(screen_update, 200)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == screen_update:
                snake.move_snake()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.direction = pygame.math.Vector2(0, -1)
                if event.key == pygame.K_DOWN:
                    snake.direction = pygame.math.Vector2(0, 1)
                if event.key == pygame.K_RIGHT:
                    snake.direction = pygame.math.Vector2(1, 0)
                if event.key == pygame.K_LEFT:
                    snake.direction = pygame.math.Vector2(-1, 0)
        screen.fill((50, 168, 82))
        apple.draw_apple()
        snake.draw_snake()
        pygame.display.flip()
        clock.tick(60)


if __name__ == '__main__':
    main()
