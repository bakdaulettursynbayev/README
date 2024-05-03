import pygame  # Импортируем модуль Pygame для создания игры
import random  # Импортируем модуль random для генерации случайных чисел
import math  # Импортируем модуль math для математических операций

# Инициализация Pygame
pygame.init()

# Определение констант для игрового окна и цветов
SCREEN_WIDTH = 600  # Ширина игрового окна
SCREEN_HEIGHT = 600  # Высота игрового окна
BLACK = (0, 0, 0)  # Черный цвет
WHITE = (255, 255, 255)  # Белый цвет
RED = (255, 0, 0)  # Красный цвет
YELLOW = (255, 255, 0)  # Желтый цвет
BLUE = (0, 0, 255)  # Синий цвет
GREEN = (0, 255, 0)  # Зеленый цвет
PURPLE = (128, 0, 128)  # Фиолетовый цвет
TURQUOISE = (64, 224, 208)  # Бирюзовый цвет
PINK = (255, 192, 203)  # Розовый цвет
PACMAN_SIZE = 40  # Размер Пакмана
GHOST_SIZE = 30  # Размер привидений
SPEED = 6  # Скорость движения

# Создание игрового окна и задание заголовка
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # Создание окна
pygame.display.set_caption("YellowSquare")  # Установка заголовка окна

# Класс для создания объектов-противников (призраков)
class Ghost:
    def __init__(self, color, maze, pacman):  # Инициализация призрака
        self.maze = maze  # Лабиринт
        self.pacman = pacman  # Объект Пакмана
        self.color = color  # Цвет призрака
        self.reset()  # Сброс на начальное состояние

    def reset(self):  # Метод сброса призрака
        self.x = random.randint(1, len(self.maze[0]) - 2) * PACMAN_SIZE  # Случайная позиция по x
        self.y = random.randint(1, len(self.maze) - 2) * PACMAN_SIZE  # Случайная позиция по y
        self.dx = random.choice([-SPEED, SPEED])  # Случайное направление по x
        self.dy = random.choice([-SPEED, SPEED])  # Случайное направление по y
        self.directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]  # Направления движения

    def move(self):  # Метод движения призрака
        target_x, target_y = self.pacman.get_position()  # Получение позиции Пакмана
        dx = target_x - self.x  # Разница по x
        dy = target_y - self.y  # Разница по y
        distance = math.sqrt(dx ** 2 + dy ** 2)  # Расстояние до Пакмана
        if distance != 0:  # Если расстояние не нулевое
            self.dx = int((dx / distance) * SPEED)  # Вычисление нового направления по x
            self.dy = int((dy / distance) * SPEED)  # Вычисление нового направления по y

        next_x = self.x + self.dx  # Следующая позиция по x
        next_y = self.y + self.dy  # Следующая позиция по y
        if self.maze[int(next_y / PACMAN_SIZE)][int(next_x / PACMAN_SIZE)] == 0:  # Если следующая клетка свободна
            self.x = next_x  # Обновление позиции по x
            self.y = next_y  # Обновление позиции по y

    def draw(self):  # Метод отрисовки призрака
        pygame.draw.rect(screen, self.color, (self.x, self.y, GHOST_SIZE, GHOST_SIZE))  # Отрисовка прямоугольника

# Класс для создания объекта Пакмана
class Pacman:
    def __init__(self, x, y):  # Инициализация Пакмана
        self.x = x  # Позиция по x
        self.y = y  # Позиция по y
        self.eaten_dots = 0  # Количество съеденных точек

    def get_position(self):  # Получение позиции Пакмана
        return self.x, self.y  # Возвращение координат

    def move(self, dx, dy):  # Метод движения Пакмана
        next_x = self.x + dx  # Следующая позиция по x
        next_y = self.y + dy  # Следующая позиция по y
        if maze[int(next_y / PACMAN_SIZE)][int(next_x / PACMAN_SIZE)] == 0:  # Если следующая клетка свободна
            self.x = next_x  # Обновление позиции по x
            self.y = next_y  # Обновление позиции по y

    def eat_dot(self):  # Метод съедания точки
        self.eaten_dots += 1  # Увеличение количества съеденных точек

# Создание лабиринта (0 - пусто, 1 - стена)
maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

# Создание объектов-противников и Пакмана
pacman = Pacman(40, 40)  # Создание Пакмана
ghosts = [Ghost(PINK, maze, pacman), Ghost(RED, maze, pacman), Ghost(TURQUOISE, maze, pacman)]  # Создание призраков

# Создание белых квадратиков для Пакмана
dots = []  # Список с координатами белых квадратиков
for _ in range(5):  # Пять белых квадратиков
    dot_x = random.randint(0, len(maze[0]) - 1) * PACMAN_SIZE  # Случайная позиция по x
    dot_y = random.randint(0, len(maze) - 1) * PACMAN_SIZE  # Случайная позиция по y
    while maze[int(dot_y / PACMAN_SIZE)][int(dot_x / PACMAN_SIZE)] != 0:  # Проверка на столкновение с лабиринтом
        dot_x = random.randint(0, len(maze[0]) - 1) * PACMAN_SIZE  # Повторная генерация x
        dot_y = random.randint(0, len(maze) - 1) * PACMAN_SIZE  # Повторная генерация y
    dots.append((dot_x, dot_y))  # Добавление новой точки в список

# Основной игровой цикл
clock = pygame.time.Clock()  # Создание объекта для отслеживания времени
running = True  # Флаг для работы игрового цикла
game_over = False  # Флаг окончания игры
winner = False  # Флаг победы
restart = False  # Флаг перезапуска игры
paused = False  # Флаг паузы
font = pygame.font.Font(None, 36)  # Шрифт для текста

while running:  # Основной игровой цикл
    for event in pygame.event.get():  # Обработка событий
        if event.type == pygame.QUIT:  # Закрытие окна
            running = False  # Остановка игрового цикла
        elif event.type == pygame.KEYDOWN:  # Обработка нажатия клавиши
            if event.key == pygame.K_r:  # Если нажата клавиша R
                restart = True  # Установка флага перезапуска
            elif event.key == pygame.K_ESCAPE:  # Если нажата клавиша Esc
                paused = not paused  # Изменение состояния паузы
            elif event.key == pygame.K_SPACE:  # Если нажата клавиша Space
                paused = False  # Убрать паузу

    if not game_over and not winner:  # Если игра не окончена и не победа
        keys = pygame.key.get_pressed()  # Получение нажатых клавиш
        if keys[pygame.K_LEFT]:  # Если нажата клавиша влево
            pacman.move(-SPEED, 0)  # Движение влево
        if keys[pygame.K_RIGHT]:  # Если нажата клавиша вправо
            pacman.move(SPEED, 0)  # Движение вправо
        if keys[pygame.K_UP]:  # Если нажата клавиша вверх
            pacman.move(0, -SPEED)  # Движение вверх
        if keys[pygame.K_DOWN]:  # Если нажата клавиша вниз
            pacman.move(0, SPEED)  # Движение вниз

        # Обновление состояния игры только если игра не на паузе
        if not paused:
            # Проверка на столкновение Пакмана с белыми квадратиками
            eaten_dots = []  # Список съеденных точек
            for dot in dots:  # Перебор всех точек
                dot_rect = pygame.Rect(dot[0], dot[1], PACMAN_SIZE, PACMAN_SIZE)  # Создание прямоугольника точки
                pacman_rect = pygame.Rect(pacman.x, pacman.y, PACMAN_SIZE, PACMAN_SIZE)  # Прямоугольник Пакмана
                if dot_rect.colliderect(pacman_rect):  # Если произошло столкновение
                    eaten_dots.append(dot)  # Добавить точку в список съеденных
            for dot in eaten_dots:  # Перебор съеденных точек
                dots.remove(dot)  # Удаление точки из списка
                pacman.eat_dot()  # Увеличение количества съеденных точек

            if len(dots) == 0:  # Если все точки съедены
                winner = True  # Установка флага победы

            for ghost in ghosts:  # Перебор призраков
                ghost.move()  # Движение призрака

            pacman_rect = pygame.Rect(pacman.x, pacman.y, PACMAN_SIZE, PACMAN_SIZE)  # Прямоугольник Пакмана
            for ghost in ghosts:  # Перебор призраков
                ghost_rect = pygame.Rect(ghost.x, ghost.y, GHOST_SIZE, GHOST_SIZE)  # Прямоугольник призрака
                if pacman_rect.colliderect(ghost_rect):  # Если произошло столкновение с призраком
                    game_over = True  # Установка флага окончания игры

    screen.fill(BLACK)  # Заливка экрана черным цветом

    # Отрисовка лабиринта
    for y, row in enumerate(maze):  # Перебор строк лабиринта
        for x, cell in enumerate(row):  # Перебор клеток в строке
            if cell == 1:  # Если клетка стена
                pygame.draw.rect(screen, BLUE, (x * PACMAN_SIZE, y * PACMAN_SIZE, PACMAN_SIZE, PACMAN_SIZE))

    pygame.draw.rect(screen, YELLOW, (pacman.x, pacman.y, PACMAN_SIZE, PACMAN_SIZE))  # Отрисовка Пакмана

    for ghost in ghosts:  # Перебор призраков
        ghost.draw()  # Отрисовка призрака

    for dot in dots:  # Перебор всех точек
        pygame.draw.rect(screen, WHITE, (dot[0], dot[1], PACMAN_SIZE, PACMAN_SIZE))  # Отрисовка белых точек

    # Отображение текста в случае окончания игры или победы
    if game_over:  # Если игра окончена
        text = font.render("Game Over!", True, RED)  # Текст "Game Over!"
        text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))  # Центрирование текста
        screen.blit(text, text_rect)  # Отображение текста
        restart = True  # Установка флага перезапуска
    elif winner:  # Если игрок победил
        text = font.render("Winner!", True, GREEN)  # Текст "Winner!"
        text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))  # Центрирование текста
        screen.blit(text, text_rect)  # Отображение текста
        restart = True  # Установка флага перезапуска

    # При паузе выводим текст на экране
    if paused:  # Если игра на паузе
        pause_text = font.render("Press Space to resume", True, WHITE)  # Текст для паузы
        pause_text_rect = pause_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))  # Центрирование текста
        screen.blit(pause_text, pause_text_rect)  # Отображение текста паузы

    pygame.display.flip()  # Обновление экрана

    clock.tick(30)  # Ограничение FPS

    if restart:  # Если нужно перезапустить игру
        pygame.time.delay(2000)  # Задержка на 2 секунды

        for ghost in ghosts:  # Перезапуск призраков
            ghost.reset()  # Сброс призрака
        pacman.x = 40  # Установка начальной позиции Пакмана по x
        pacman.y = 40  # Установка начальной позиции Пакмана по y
        pacman.eaten_dots = 0  # Сброс количества съеденных точек
        dots.clear()  # Очистка списка точек

        # Создание новых белых квадратиков для Пакмана
        for _ in range(5):  # Пять новых точек
            dot_x = random.randint(0, len(maze[0]) - 1) * PACMAN_SIZE  # Случайная позиция по x
            dot_y = random.randint(0, len(maze) - 1) * PACMAN_SIZE  # Случайная позиция по y
            while maze[int(dot_y / PACMAN_SIZE)][int(dot_x / PACMAN_SIZE)] != 0:  # Проверка на столкновение
                dot_x = random.randint(0, len(maze[0]) - 1) * PACMAN_SIZE  # Повторная генерация x
                dot_y = random.randint(0, len(maze) - 1) * PACMAN_SIZE  # Повторная генерация y
            dots.append((dot_x, dot_y))  # Добавление новой точки в список

        game_over = False  # Сброс флага окончания игры
        winner = False  # Сброс флага победы
        restart = False  # Сброс флага перезапуска
        paused = False  # Сброс флага паузы

pygame.quit()  # Завершение работы Pygame
