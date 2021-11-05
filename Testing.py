import unittest
from Snake import Apple, Game
import pygame
from pygame.math import Vector2


def create_apple():
    cell_size = 30
    cell_number = 16
    screen = pygame.display.set_mode((cell_size * cell_number, cell_size * cell_number))

    return Apple(cell_size, cell_number, screen)


def create_game():
    pygame.init()
    cell_size = 30
    cell_number = 16
    screen = pygame.display.set_mode((cell_size * cell_number, cell_size * cell_number))
    game_font = pygame.font.Font(None, 30)

    return Game(cell_size, cell_number, screen, game_font)


class SnakeTest(unittest.TestCase):

    def test_snake_move(self):
        game = create_game()
        game.snake.direction = Vector2(1, 0)
        game.snake.body = [Vector2(5, 7), Vector2(4, 7), Vector2(3, 7)]
        game.snake.move_snake()
        new_pos = game.snake.body
        wanted_pos = [Vector2(6, 7), Vector2(5, 7), Vector2(4, 7)]
        self.assertEqual(new_pos, wanted_pos)

    def test_apple_spawn(self):
        times = 0
        while times < 1000:
            apple = create_apple()
            x = apple.x
            y = apple.y
            random_result = (x + 1) * (y + 1)
            wanted_result = 256
            self.assertLessEqual(random_result, wanted_result)
            times += 1

    def test_collision_walls(self):
        game = create_game()
        game.snake.direction = Vector2(1, 0)
        game.snake.body = [Vector2(15, 7), Vector2(14, 7), Vector2(13, 7)]
        game.snake.move_snake()
        game.check_collision()
        new_pos = game.snake.body
        wanted_pos = [Vector2(5, 7), Vector2(4, 7), Vector2(3, 7)]
        self.assertEqual(new_pos, wanted_pos)

    def test_overlap(self):
        game = create_game()
        game.snake.direction = Vector2(1, 0)
        game.snake.body = [Vector2(5, 7), Vector2(4, 7), Vector2(3, 7)]
        game.apple.pos = Vector2(6, 7)
        game.snake.move_snake()
        game.check_overlap()
        new_pos = game.apple.pos
        not_wanted = Vector2(6, 7)
        self.assertIsNot(new_pos, not_wanted)

    def test_collision_tail(self):
        game = create_game()
        game.snake.direction = Vector2(1, 0)
        game.snake.body = [Vector2(5, 7), Vector2(5, 6), Vector2(6, 6), Vector2(6, 7), Vector2(6, 8)]
        game.snake.move_snake()
        game.check_collision()
        new_pos = game.snake.body
        wanted_pos = [Vector2(5, 7), Vector2(4, 7), Vector2(3, 7)]
        self.assertEqual(new_pos, wanted_pos)
