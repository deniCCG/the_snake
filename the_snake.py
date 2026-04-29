from random import choice, randint

import pygame

# Константы для размеров поля и сетки:
SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE

# Направления движения:
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Цвет фона - черный:
BOARD_BACKGROUND_COLOR = (0, 0, 0)

# Цвет границы ячейки
BORDER_COLOR = (93, 216, 228)

# Цвет яблока
APPLE_COLOR = (255, 0, 0)

# Цвет змейки
SNAKE_COLOR = (0, 255, 0)

# Скорость движения змейки:
SPEED = 20

# Настройка игрового окна:
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

# Заголовок окна игрового поля:
pygame.display.set_caption('Змейка')

# Настройка времени:
clock = pygame.time.Clock()


# Тут опишите все классы игры.
class GameObject:
    """
    Базовый класс, от которого наследуются все объекты.
    Содержит общие атрибуты
    """
    def init(self, position = None, bodycolor=None):

        """
        Конструктор базового игрового объекта
        Аргументы position (координаты), body_color(цвет)
        """

    if position is None:
        self.position = (320, 240)
    else:
        self.position = position

    def draw(self, surface):
        """
        Абстрактный метод для отрисовки объекта на экране.
        Аргумент surface (поверхность на которой рисуем)
        """
        pass


class Apple(GameObject):
    """
    Класс Apple Наследуется от GameObject
    Появляется в случайном месте поля
    """

    super().init(position=None, body_color=APPLE_COLOR)

    self.randomize_position(self):
    """
    Устанавливает случайные координаты для яблока
    """
    max_x = 640 - 20
    max_y = 480 - 20

    x.random.randrage(0, max_x + 1, 20)
    y.random.randrage(0, max_x + 1, 20)

    self.position = (x,y)

    def draw(self,surface):
        """
        Отрисовывает яблоко на игровом поле
        """

        rect = pygame.Rect(
            self.position[0],
            self.position[1],
            20,
            20,
        )

        pygame.draw.rect(surface, self.body_color, rect)

def main():
    # Инициализация PyGame:
    pygame.init()
    # Тут нужно создать экземпляры классов.
    ...import random
import sys
import pygame as pg

# Константы для игры
GRID_WIDTH = 20
GRID_HEIGHT = 20
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BOARD_BACKGROUND_COLOR = (30, 30, 30)
LIGHT_GRAY = (200, 200, 200)
BLACK = (0, 0, 0)
DARK_GREEN = (0, 100, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
INFO_AREA_WIDTH = 400

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

MOVEMENT_KEYS = {
    pg.K_w: UP,
    pg.K_s: DOWN,
    pg.K_a: LEFT,
    pg.K_d: RIGHT,
    pg.K_UP: UP,
    pg.K_DOWN: DOWN,
    pg.K_LEFT: LEFT,
    pg.K_RIGHT: RIGHT,
}

INSTRUCTION_TEXT = [
    "Score: {}",
    "Use arrows or WASD to move",
    "Avoid bombs",
    "Eat apples to grow"
]

FONT = None  # будет инициализирован в main

score = 0
frame_delay = 100
apples_eaten = 0


class GameObject:
    def init(self, color):
        self.color = color

    def draw_cell(self, position):
        cell_size = 20
        x, y = position
        pg.draw.rect(
            screen,
            self.color,
            pg.Rect(x * cell_size, y * cell_size, cell_size, cell_size)
        )


class Snake(GameObject):
    """Наследуемый класс змейки"""

    def init(self):
        super().init(DARK_GREEN)
        mid_x = GRID_WIDTH // 2
        mid_y = GRID_HEIGHT // 2
        self.positions = [(mid_x, mid_y)]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.grow = False

    def move(self):
        """Инициализация движения"""
        head_x, head_y = self.positions[0]
        dx, dy = self.direction
        new_head = ((head_x + dx) % GRID_WIDTH, (head_y + dy) % GRID_HEIGHT)

        if new_head in self.positions[4:]:
            game_over("self")
            return False

        self.positions.insert(0, new_head)
        if not self.grow:
            self.positions.pop()
        else:
            self.grow = False
        return True

    # while True:
    #     clock.tick(SPEED)

        # Тут опишите основную логику игры.
        # ...


if __name__ == '__main__':
    main()


# Метод draw класса Apple
# def draw(self):
#     rect = pygame.Rect(self.position, (GRID_SIZE, GRID_SIZE))
#     pygame.draw.rect(screen, self.body_color, rect)
#     pygame.draw.rect(screen, BORDER_COLOR, rect, 1)

# # Метод draw класса Snake
# def draw(self):
#     for position in self.positions[:-1]:
#         rect = (pygame.Rect(position, (GRID_SIZE, GRID_SIZE)))
#         pygame.draw.rect(screen, self.body_color, rect)
#         pygame.draw.rect(screen, BORDER_COLOR, rect, 1)

#     # Отрисовка головы змейки
#     head_rect = pygame.Rect(self.positions[0], (GRID_SIZE, GRID_SIZE))
#     pygame.draw.rect(screen, self.body_color, head_rect)
#     pygame.draw.rect(screen, BORDER_COLOR, head_rect, 1)

#     # Затирание последнего сегмента
#     if self.last:
#         last_rect = pygame.Rect(self.last, (GRID_SIZE, GRID_SIZE))
#         pygame.draw.rect(screen, BOARD_BACKGROUND_COLOR, last_rect)

# Функция обработки действий пользователя
# def handle_keys(game_object):
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             raise SystemExit
#         elif event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_UP and game_object.direction != DOWN:
#                 game_object.next_direction = UP
#             elif event.key == pygame.K_DOWN and game_object.direction != UP:
#                 game_object.next_direction = DOWN
#             elif event.key == pygame.K_LEFT and game_object.direction != RIGHT:
#                 game_object.next_direction = LEFT
#             elif event.key == pygame.K_RIGHT and game_object.direction != LEFT:
#                 game_object.next_direction = RIGHT

# Метод обновления направления после нажатия на кнопку
# def update_direction(self):
#     if self.next_direction:
#         self.direction = self.next_direction
#         self.next_direction = None
