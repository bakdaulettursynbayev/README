import pygame
import time
import random

pygame.init()

# Определение цветов
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Размеры экрана
dis_width = 1200
dis_height = 800

# Размер блока
block_size = 10

# Создание окна
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Xenzia')

# Настройка часов для контроля скорости игры
clock = pygame.time.Clock()

# Размер блока змейки и скорость
snake_block = 20
snake_speed = 15

# Создание шрифта для вывода сообщений
font_style = pygame.font.SysFont(None, 70)


def our_snake(snake_block, snake_list):
    """Функция для отображения змейки на экране."""
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])


def message(msg, color):
    """Функция для вывода сообщения на экран."""
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])


def your_score(score):
    """Функция для отображения счета на экране."""
    value = font_style.render("Score:" + str(score), True, black)
    dis.blit(value, [0, 0])


def gameLoop():
    """Основной игровой цикл."""
    game_over = False
    game_close = False

    # Начальные координаты змейки
    x1 = dis_width / 2
    y1 = dis_height / 2

    # Изменение координат при движении змейки
    x1_change = 0
    y1_change = 0

    # Список координат тела змейки и длина змейки
    snake_List = []
    Length_of_snake = 1

    # Начальные координаты еды
    foodx = round(random.randrange(0, dis_width - snake_block) / 20.0) * 20.0
    foody = round(random.randrange(0, dis_height - snake_block) / 20.0) * 20.0

    score = 0  # Инициализация счета

    while not game_over:

        while game_close == True:
            # Отображение сообщения о поражении и кнопки Restart? Yes/No
            dis.fill(black)
            message("You Lost:( Restart? Y-Yes or N-No", white)
            your_score(score)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_y:
                        gameLoop()  # Перезапуск игры
                    if event.key == pygame.K_n:
                        game_over = True  # Завершение игры

        for event in pygame.event.get():
            # Обработка событий
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                # Изменение направления движения змейки при нажатии клавиш
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        # Проверка на столкновение с границами экрана
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(white)

        # Проверка на выход за границы
        if x1 >= dis_width:
            x1 = 0
        elif x1 < 0:
            x1 = dis_width - snake_block
        if y1 >= dis_height:
            y1 = 0
        elif y1 < 0:
            y1 = dis_height - snake_block


        # Отображение еды
        pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])

        # Добавление новой головы змейки
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)

        # Удаление лишних блоков змейки
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        # Проверка на столкновение с собой
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        # Отображение змейки
        our_snake(snake_block, snake_List)

        # Отображение счета
        your_score(score)

        pygame.display.update()

        # Обработка съедания еды
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 20.0) * 20.0
            foody = round(random.randrange(0, dis_height - snake_block) / 20.0) * 20.0
            Length_of_snake += 1
            score += 1  # Увеличение счета при съедании еды


        # Ограничение скорости змейки
        clock.tick(snake_speed)

    pygame.quit()
    quit()


gameLoop()