import pygame  # Импортируем библиотеку Pygame для создания игры
import random  # Импортируем модуль random для генерации случайных чисел

pygame.init()  # Инициализация Pygame.

# Определение размеров и частоты кадров
W, H = 1200, 800  # Ширина и высота окна.
FPS = 60  # Частота кадров в секунду.

# Создание окна и настройка параметров
screen = pygame.display.set_mode((W, H), pygame.RESIZABLE)  # Создание окна с возможностью изменения размера.
clock = pygame.time.Clock()  # Создание объекта для отслеживания времени.
done = False  # Флаг для завершения игры.
bg = (0, 0, 0)  # Цвет фона (черный).

# Настройка параметров платформы и мяча
paddleW = 150  # Ширина платформы.
paddleH = 25  # Высота платформы.
paddleSpeed = 20  # Скорость движения платформы.
paddle = pygame.Rect(W // 2 - paddleW // 2, H - paddleH - 30, paddleW, paddleH)  # Создание прямоугольника для платформы.

ballRadius = 20  # Радиус мяча.
ballSpeed = 6  # Скорость движения мяча.
ball_rect = int(ballRadius * 2 ** 0.5)  # Размеры прямоугольника, в который вписан мяч.
ball = pygame.Rect(random.randrange(ball_rect, W - ball_rect), H // 2, ball_rect, ball_rect)  # Создание прямоугольника для мяча.
dx, dy = 1, -1  # Направление движения мяча по осям x и y.

# Параметры игры и текстовые элементы
game_score = 0  # Счет игры.
game_score_fonts = pygame.font.SysFont('comicsansms', 40)  # Шрифт для текста счета.
game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (0, 0, 0))  # Текст счета.
game_score_rect = game_score_text.get_rect()  # Прямоугольник для размещения текста счета.
game_score_rect.center = (210, 20)  # Позиция текста счета.

# Звуковые эффекты
collision_sound = pygame.mixer.Sound("/Users/bakdaulettursunbaev/Desktop/README/Lab8/media/catch.mp3")  # Звук при столкновении.

# Периодические интервалы и изменения
time_elapsed = 0  # Время, прошедшее с начала игры.
speed_increase_interval = 1000  # Интервал увеличения скорости мяча.
speed_increase_amount = 0.2  # Увеличение скорости мяча.
shrink_paddle_interval = 5000  # Интервал уменьшения платформы.
shrink_paddle_amount = 10  # Уменьшение платформы.

# Функция для обнаружения столкновений
def detect_collision(dx, dy, ball, rect):
    # Определение различных сценариев столкновений и изменение направления мяча
    if dx > 0:
        delta_x = ball.right - rect.left
    else:
        delta_x = rect.right - ball.left
    if dy > 0:
        delta_y = ball.bottom - rect.top
    else:
        delta_y = rect.bottom - ball.top

    if abs(delta_x - delta_y) < 10:
        dx, dy = -dx, -dy
    if delta_x > delta_y:
        dy = -dy
    elif delta_y > delta_x:
        dx = -dx
    return dx, dy

# Генерация списка блоков и их цветов
block_list = [pygame.Rect(10 + 120 * i, 50 + 70 * j, 100, 50) for i in range(10) for j in range(4)]  # Создание блоков.
color_list = [(random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)) for i in range(10) for j in range(4)]  # Цвета блоков.

# Создание неразрушаемых блоков
unbreakable_block_list = []  # Список неразрушаемых блоков.
for _ in range(5):
    random_index = random.randint(0, len(block_list) - 1)
    unbreakable_block_list.append(block_list.pop(random_index))  # Удаление блоков из основного списка и добавление в неразрушаемые.
unbreakable_color_list = [(0, 0, 255) for _ in range(len(unbreakable_block_list))]  # Цвет неразрушаемых блоков.

# Создание бонусных блоков с различными эффектами
bonus_brick_types = {
    "longer_paddle": {"color": (0, 255, 0), "perk": "paddle", "message": "Longer paddle!"},
    "increase_speed": {"color": (255, 165, 0), "perk": "speed", "message": "Speed Up!"},
}

bonus_brick_list = []
for _ in range(5):
    random_index = random.randint(0, len(block_list) - 1)
    bonus_brick_type = random.choice(list(bonus_brick_types.keys()))
    bonus_brick_list.append((block_list.pop(random_index), bonus_brick_type))

# Создание текстовых элементов для победы и поражения
losefont = pygame.font.SysFont('comicsansms', 40)
losetext = losefont.render('Game Over', True, (255, 255, 255))
losetextRect = losetext.get_rect()
losetextRect.center = (W // 2, H // 2)

winfont = pygame.font.SysFont('comicsansms', 40)
wintext = losefont.render('You win yay', True, (0, 0, 0))
wintextRect = wintext.get_rect()
wintextRect.center = (W // 2, H // 2)

message_font = pygame.font.SysFont('comicsansms', 40)
last_message = ""
last_message_rect = None

# Основной игровой цикл
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(bg)  # Заполнение экрана цветом фона.

    # Отрисовка блоков и элементов на экране
    [pygame.draw.rect(screen, color_list[color], block) for color, block in enumerate(block_list)]  # Отрисовка основных блоков.
    [pygame.draw.rect(screen, (0, 0, 255), block) for block in unbreakable_block_list]  # Отрисовка неразрушаемых блоков.

    pygame.draw.rect(screen, pygame.Color(255, 255, 255), paddle)  # Отрисовка платформы.
    pygame.draw.circle(screen, pygame.Color(255, 0, 0), ball.center, ballRadius)  # Отрисовка мяча.

    ball.x += ballSpeed * dx  # Изменение положения мяча по оси x.
    ball.y += ballSpeed * dy  # Изменение положения мяча по оси y.

    # Обработка столкновений и изменение направления мяча
    if ball.centerx < ballRadius or ball.centerx > W - ballRadius:
        dx = -dx
    if ball.centery < ballRadius + 50:
        dy = -dy
    if ball.colliderect(paddle) and dy > 0:
        dx, dy = detect_collision(dx, dy, ball, paddle)

    hitIndex = ball.collidelist(block_list)

    if hitIndex != -1:
        hitRect = block_list.pop(hitIndex)
        hitColor = color_list.pop(hitIndex)
        dx, dy = detect_collision(dx, dy, ball, hitRect)
        game_score += 1
        collision_sound.play()

    # Обработка столкновений с неразрушаемыми блоками
    for i, unbreakable_block in enumerate(unbreakable_block_list):
        if ball.colliderect(unbreakable_block):
            dx, dy = detect_collision(dx, dy, ball, unbreakable_block)

    # Обработка бонусных блоков
    for block, bonus_type in bonus_brick_list:
        pygame.draw.rect(screen, bonus_brick_types[bonus_type]["color"], block)

    for i, (bonus_brick, bonus_type) in enumerate(bonus_brick_list):
        if ball.colliderect(bonus_brick):
            if bonus_brick_types[bonus_type]["perk"] == "life":
                pass
            elif bonus_brick_types[bonus_type]["perk"] == "speed":
                ballSpeed += 1

            last_message = bonus_brick_types[bonus_type]["message"]
            last_message_surface = message_font.render(last_message, True, (255, 255, 255))
            last_message_rect = last_message_surface.get_rect(topright=(W - 10, -5))

            del bonus_brick_list[i]
            break

    if last_message:
        screen.blit(last_message_surface, last_message_rect)

    # Отображение текущего счета игры
    game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (255, 255, 255))
    screen.blit(game_score_text, game_score_rect)

    # Проверка условий поражения или победы
    if ball.bottom > H:
        screen.fill((0, 0, 0))
        screen.blit(losetext, losetextRect)
    elif not len(block_list):
        screen.fill((255, 255, 255))
        screen.blit(wintext, wintextRect)

    # Увеличение скорости и уменьшение размера платформы с течением времени
    time_elapsed += clock.get_rawtime()
    if time_elapsed >= speed_increase_interval:
        ballSpeed += speed_increase_amount
        time_elapsed = 0

    if time_elapsed >= shrink_paddle_interval:
        paddleW -= shrink_paddle_amount
        if paddleW < 50:
            paddleW = 50
        paddle.width = paddleW
        time_elapsed = 0

    # Управление платформой
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and paddle.left > 0:
        paddle.left -= paddleSpeed
    if key[pygame.K_RIGHT] and paddle.right < W:
        paddle.right += paddleSpeed

    pygame.display.flip()  # Обновление экрана.
    clock.tick(FPS)  # Управление частотой кадров.