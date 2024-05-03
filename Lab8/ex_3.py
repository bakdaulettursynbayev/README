import pygame

pygame.init()  # Инициализация Pygame.

# Определение частоты кадров и размеров окна
fps = 60  # Частота кадров в секунду.
timer = pygame.time.Clock()  # Создание объекта для отслеживания времени.
WIDTH = 800  # Ширина окна.
HEIGHT = 600  # Высота окна.
active_figure = 0  # Текущая выбранная фигура (0 - круг, 1 - прямоугольник).
active_color = 'white'  # Текущий выбранный цвет.

# Создание окна и названия приложения
screen = pygame.display.set_mode([WIDTH, HEIGHT])  # Создание окна с заданными размерами.
pygame.display.set_caption("Paint")  # Установка названия окна.
painting = []  # Список для хранения нарисованных элементов.

def draw_menu(color):
    # Отрисовка меню с выбором кистей и цветов
    pygame.draw.rect(screen, 'gray', [0, 0, WIDTH, 70])  # Отрисовка верхней панели меню.
    pygame.draw.line(screen, 'black', (0, 70), (WIDTH, 70), 3)  # Отрисовка разделительной линии.

    # Создание кнопок для выбора кистей
    circle_brush = [pygame.draw.rect(screen, 'white', [10, 10, 50, 50]), 0]
    pygame.draw.circle(screen, 'black', (35, 35), 20)  # Кнопка для круглой кисти.
    pygame.draw.circle(screen, 'white', (35, 35), 18)

    rect_brush = [pygame.draw.rect(screen, 'white', [70, 10, 50, 50]), 1]
    pygame.draw.rect(screen, 'black', [76.5, 26, 37, 20], 2)  # Кнопка для квадратной кисти.

    brush_list = [circle_brush, rect_brush]

    # Создание палитры цветов
    pygame.draw.circle(screen, color, (400, 35), 30)  # Круглый выбранный цвет.
    pygame.draw.circle(screen, 'dark gray', (400, 35), 30, 3)  # Обводка выбранного цвета.

    eraser = pygame.image.load("/Users/bakdaulettursunbaev/Desktop/README/Lab8/media/Eraser.png")  # Изображение ластика.
    eraser_rect = eraser.get_rect(topleft=(WIDTH - 190, 10))  # Позиция и размеры ластика.
    eraser_rect.width = eraser_rect.height = 35
    screen.blit(eraser, [WIDTH - 190, 10, 25, 25])  # Отображение изображения ластика на экране.

    # Определение прямоугольников для различных цветов
    blue = pygame.draw.rect(screen, (0, 0, 255), [WIDTH - 35, 10, 25, 25])
    red = pygame.draw.rect(screen, (255, 0, 0), [WIDTH - 35, 35, 25, 25])
    green = pygame.draw.rect(screen, (0, 255, 0), [WIDTH - 60, 10, 25, 25])
    yellow = pygame.draw.rect(screen, (255, 255, 0), [WIDTH - 60, 35, 25, 25])
    teal = pygame.draw.rect(screen, (0, 255, 255), [WIDTH - 85, 35, 25, 25])
    purple = pygame.draw.rect(screen, (255, 0, 255), [WIDTH - 85, 10, 25, 25])
    black = pygame.draw.rect(screen, (0, 0, 0), [WIDTH - 110, 10, 25, 25])
    color_rect = [blue, red, green, yellow, teal, purple, black, eraser_rect]  # Список прямоугольников для цветов.
    rgb_list = [(0, 0, 255), (255, 0, 0), (0, 255, 0), (255, 255, 0),
                (0, 255, 255), (255, 0, 255), (0, 0, 0), (255, 255, 255)]  # Список RGB цветов.

    return brush_list, color_rect, rgb_list  # Возвращение созданных элементов меню.

def draw_painting(paints):
    # Отображение нарисованных элементов на экране
    for color, pos, figure in paints:
        if color == (255, 255, 255):
            pygame.draw.rect(screen, color, [pos[0] - 15, pos[1] - 15, 37, 20])  # Отображение прямоугольника для ластика.
        else:
            if figure == 0:
                pygame.draw.circle(screen, color, pos, 20, 2)  # Отображение круга с рамкой.
            elif figure == 1:
                pygame.draw.rect(screen, color, [pos[0] - 15, pos[1] - 15, 37, 20], 2)  # Отображение прямоугольника с рамкой.

run = True
while run:
    timer.tick(fps)  # Ограничение частоты кадров.

    screen.fill("white")  # Заполнение экрана белым цветом.

    # Получение текущих позиции и действий мыши
    mouse = pygame.mouse.get_pos()
    left_click = pygame.mouse.get_pressed()[0]

    # Отрисовка меню и выбор цвета/кисти
    brushes, colors, rgbs = draw_menu(active_color)

    # Если нажата левая кнопка мыши и курсор находится в области рисования, добавляем элемент в список рисования
    if left_click and mouse[1] > 85:
        painting.append((active_color, mouse, active_figure))

    draw_painting(painting)  # Отображение элементов рисования на экране.

    # Отображение выбранного инструмента (кисти/ластика)
    if mouse[1] > 85:
        if active_color == (255, 255, 255):  # Если выбран ластик, рисуем прямоугольник для ластика.
            pygame.draw.rect(screen, active_color, [mouse[0] - 20, mouse[1] - 20, 40, 40])
        else:
            if active_figure == 0:  # Если выбрана кисть, рисуем круг или прямоугольник в зависимости от выбора.
                pygame.draw.circle(screen, active_color, mouse, 20, 2)
            elif active_figure == 1:
                pygame.draw.rect(screen, active_color, [mouse[0] - 20, mouse[1] - 10, 40, 20], 2)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Завершение программы при закрытии окна.
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(colors)):  # Проверка нажатий на палитре цветов.
                if colors[i].collidepoint(event.pos):
                    active_color = rgbs[i]  # Установка активного цвета.

            for i in brushes:  # Проверка нажатий на кнопки кистей.
                if i[0].collidepoint(event.pos):
                    active_figure = i[1]  # Установка активной кисти.

    pygame.display.flip()  # Обновление экрана.

pygame.quit()  # Завершение работы Pygame при выходе из программы.