import sys

import pygame
import random
# python 3.9.7
# cell_number = 16

GREY = (69, 69, 69)
GREEN = (50, 168, 82)
RED = (224, 25, 51)


class Apple:
    def __init__(self):
        self.randomize()

    def draw_apple(self):
        apple_rect = pygame.Rect(self.pos.x * cell_size, self.pos.y * cell_size, cell_size, cell_size)
        pygame.draw.rect(screen, RED, apple_rect)

    def randomize(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = pygame.math.Vector2(self.x, self.y)


class Snake:
    def __init__(self):
        self.body = [pygame.math.Vector2(5, 7), pygame.math.Vector2(4, 7), pygame.math.Vector2(3, 7)]
        self.direction = pygame.math.Vector2(1, 0)
        self.new_block = False

    def draw_snake(self):
        for block in self.body:
            block_rect = pygame.Rect(block.x * cell_size, block.y * cell_size, cell_size, cell_size)
            pygame.draw.rect(screen, GREY, block_rect)

    def move_snake(self):
        if self.new_block == True:
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


class Game:
    def __init__(self):
        self.snake = Snake()
        self.apple = Apple()

    def update(self):
        self.snake.move_snake()
        self.check_overlap()
        self.check_collision()

    def draw_squares(self):
        self.apple.draw_apple()
        self.snake.draw_snake()

    def check_overlap(self):
        if self.apple.pos == self.snake.body[0]:
            self.apple.randomize()
            self.snake.add_block()

    def check_collision(self):
        if self.snake.body[0].x < 0 or self.snake.body[0].x >= cell_number:
            self.game_over()
        if self.snake.body[0].y < 0 or self.snake.body[0].y >= cell_number:
            self.game_over()
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()


    def game_over(self):
        pygame.quit()
        sys.exit()


# def main():


pygame.init()
cell_size = 30
cell_number = 16
pygame.display.set_caption("Snake")
screen = pygame.display.set_mode((cell_size * cell_number, cell_size * cell_number))
clock = pygame.time.Clock()

game = Game()

# running = True


screen_update = pygame.USEREVENT
pygame.time.set_timer(screen_update, 100)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == screen_update:
            game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                game.snake.direction = pygame.math.Vector2(0, -1)
            if event.key == pygame.K_DOWN:
                game.snake.direction = pygame.math.Vector2(0, 1)
            if event.key == pygame.K_RIGHT:
                game.snake.direction = pygame.math.Vector2(1, 0)
            if event.key == pygame.K_LEFT:
                game.snake.direction = pygame.math.Vector2(-1, 0)
    screen.fill(GREEN)
    game.draw_squares()
    pygame.display.flip()
    clock.tick(60)

# if __name__ == '__main__':
#    main()
