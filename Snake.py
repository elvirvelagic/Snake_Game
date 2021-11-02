import sys
import pygame
import random
from pygame.math import Vector2

# python 3.9.7
ORANGE = (255, 89, 0)
BROWN = (66, 34, 25)
BLACK = (0, 0, 0)
GREY = BROWN #(69, 69, 69)
GREEN = BLACK #(50, 168, 82)
RED = ORANGE #(224, 25, 51)
WHITE = (209, 207, 207)




class Apple:
    def __init__(self, cell_size, cell_number, screen):
        self.cell_size = cell_size
        self.cell_number = cell_number
        self.screen = screen
        self.x = self.y = self.pos = None
        self.randomize()

    def draw_apple(self):
        apple_rect = pygame.Rect(self.pos.x * self.cell_size, self.pos.y * self.cell_size, self.cell_size,
                                 self.cell_size)
        pygame.draw.rect(self.screen, RED, apple_rect)

    def randomize(self):
        self.x = random.randint(0, self.cell_number - 1)
        self.y = random.randint(0, self.cell_number - 1)
        self.pos = Vector2(self.x, self.y)


class Snake:
    def __init__(self, cell_size, screen):
        self.cell_size = cell_size
        self.screen = screen
        self.body = [Vector2(5, 7), Vector2(4, 7), Vector2(3, 7)]
        self.direction = Vector2(0, 0)
        self.new_block = False

    def draw_snake(self):
        for block in self.body:
            block_rect = pygame.Rect(block.x * self.cell_size, block.y * self.cell_size, self.cell_size, self.cell_size)
            pygame.draw.rect(self.screen, GREY, block_rect)

    def move_snake(self):
        if self.new_block:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]

    def add_block(self):
        self.new_block = True

    def reset(self):
        self.body = [Vector2(5, 7), Vector2(4, 7), Vector2(3, 7)]
        self.direction = pygame.math.Vector2(0, 0)


class Game:
    def __init__(self, cell_size, cell_number, screen, game_font):
        self.snake = Snake(cell_size, screen)
        self.apple = Apple(cell_size, cell_number, screen)
        self.cell_size = cell_size
        self.cell_number = cell_number
        self.screen = screen
        self.game_font = game_font

    def update(self):
        self.snake.move_snake()
        self.check_overlap()
        self.check_collision()

    def draw_squares(self):
        self.apple.draw_apple()
        self.snake.draw_snake()
        self.score()

    def check_overlap(self):
        if self.apple.pos == self.snake.body[0]:
            self.apple.randomize()
            self.snake.add_block()

        for block in self.snake.body[1:]:
            if block == self.apple.pos:
                self.apple.randomize()

    def check_collision(self):
        if self.snake.body[0].x < 0 or self.snake.body[0].x >= self.cell_number:
            self.game_over()
        if self.snake.body[0].y < 0 or self.snake.body[0].y >= self.cell_number:
            self.game_over()
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

    def score(self):
        score_str = str((len(self.snake.body) - 3) * 5)
        score_display = self.game_font.render(score_str, True, WHITE)
        score_x = (self.cell_size * self.cell_number - 40)
        score_y = 20
        score_rect = score_display.get_rect(center=(score_x, score_y))
        self.screen.blit(score_display, score_rect)

    def game_over(self):
        self.snake.reset()


def main():
    pygame.init()
    cell_size = 30
    cell_number = 16
    pygame.display.set_caption("Snake")
    screen = pygame.display.set_mode((cell_size * cell_number, cell_size * cell_number))
    clock = pygame.time.Clock()
    game_font = pygame.font.Font(None, 30)

    game = Game(cell_size, cell_number, screen, game_font)

    screen_update = pygame.USEREVENT
    pygame.time.set_timer(screen_update, 200)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == screen_update:
                game.update()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if game.snake.direction.y != 1:
                        game.snake.direction = Vector2(0, -1)
                if event.key == pygame.K_DOWN:
                    if game.snake.direction.y != -1:
                        game.snake.direction = Vector2(0, 1)
                if event.key == pygame.K_RIGHT:
                    if game.snake.direction.x != -1:
                        game.snake.direction = Vector2(1, 0)
                if event.key == pygame.K_LEFT:
                    if game.snake.direction.x != 1:
                        game.snake.direction = Vector2(-1, 0)
        screen.fill(GREEN)
        game.draw_squares()
        pygame.display.flip()
        clock.tick(60)


if __name__ == '__main__':
    main()
