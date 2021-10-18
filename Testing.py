import unittest

from Snake import Snake, Apple, Game


class SnakeTest(unittest.TestCase):

    def test_snake_move(self):
        snake = Snake()
        direction = snake.direction
        start_pos = snake.body.copy()
        snake.move_snake()
        start_pos = start_pos[-1:] + start_pos[:-1]
        start_pos[0] = start_pos[1] + direction
        moved = [snake.body[i] == start_pos[i] for i in range(len(start_pos))]
        self.assertTrue(all(moved))

    def test_apple_spawn(self):
        times = 1
        while times < 1000:
            apple = Apple()
            x = apple.x
            y = apple.y
            result = (x + 1) * (y + 1)
            self.assertLessEqual(result, 256)
            times += 1

    def test_overlap(self):
        pass


