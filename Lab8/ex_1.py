import random  # Импорт модуля random для генерации случайных чисел.
import time  # Импорт модуля time для работы со временем.

import pygame  # Импорт библиотеки Pygame для создания игр.
import sys  # Импорт модуля sys для работы с системными функциями.
from pygame.locals import *  # Импорт различных констант и функций из Pygame.

pygame.init()  # Инициализация Pygame.

# Определение основных констант и переменных игры.
FPS = 60  # Частота кадров в секунду.
FramePerSec = pygame.time.Clock()  # Создание объекта Clock для управления FPS.

BLUE = (0, 0, 255)  # Цвета в формате RGB.
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SCREEN_WIDTH = 400  # Ширина игрового экрана.
SCREEN_HEIGHT = 600 # Высота игрового экрана
SPEED = 5  # Скорость движения объектов.
SCORE = 0  # Очки игрока.
COIN_SCORE = 0  # Очки за сбор монет.

# Создание шрифтов для отображения текста.
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, WHITE)

# Загрузка фонового изображения.
background = pygame.image.load("/Users/bakdaulettursunbaev/Desktop/README/Lab8/media/AnimatedStreet.png")

# Создание окна игры.
DISPLAYSURF = pygame.display.set_mode((400, 600))
pygame.display.set_caption("Game")

# Определение классов игровых объектов.

# Класс врага (противника).
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("/Users/bakdaulettursunbaev/Desktop/README/Lab8/media/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(20, SCREEN_WIDTH - 20), 0)

    def move(self):  # Метод для движения врага.
        global SCORE  # Используется для изменения глобальной переменной.
        self.rect.move_ip(0, SPEED)  # Перемещение вниз на SPEED пикселей.
        if self.rect.top > 600:  # Если враг выходит за границы экрана.
            SCORE += 1  # Увеличиваем счет игрока.
            self.rect.top = 0  # Перемещаем врага вверх экрана.
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)  # Генерируем новое положение.

# Класс игрока.
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("/Users/bakdaulettursunbaev/Desktop/README/Lab8/media/Car.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):  # Метод для движения игрока.
        pressed_keys = pygame.key.get_pressed()  # Получаем нажатые клавиши.

        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)  # Движение влево.
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)  # Движение вправо.

    def collect_coin(self, coins):  # Метод для сбора монет.
        collisions = pygame.sprite.spritecollide(self, coins, True)  # Проверка столкновения с монетой.
        for coin in collisions:
            return True  # Если столкновение произошло, возвращаем True.
        return False  # Если нет столкновения, возвращаем False.

# Класс монеты.
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("/Users/bakdaulettursunbaev/Desktop/README/Lab8/media/Coin.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):  # Метод для движения монеты.
        self.rect.move_ip(0, SPEED)  # Перемещение монеты вниз.
        if self.rect.top > 600:  # Если монета выходит за границы экрана.
            self.rect.top = 0  # Перемещаем монету вверх экрана.
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)  # Генерируем новое положение.

# Создание экземпляров игровых объектов.
P1 = Player()
E1 = Enemy()
C1 = Coin()

# Группировка объектов.
enemies = pygame.sprite.Group()
enemies.add(E1)
coins = pygame.sprite.Group()
coins.add(C1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)

# Установка события для увеличения скорости.
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

# Основной игровой цикл.
while True:
    for event in pygame.event.get():  # Обработка событий.
        if event.type == INC_SPEED:  # Если событие - увеличение скорости.
            SPEED += 0.5  # Увеличиваем скорость.
        if event.type == QUIT:  # Если событие - выход из игры.
            pygame.quit()  # Завершаем Pygame.
            sys.exit()  # Завершаем программу.

    # Отрисовка фона и текстовых элементов.
    DISPLAYSURF.blit(background, (0, 0))  # Отображение фонового изображения.
    scores = font_small.render(str(SCORE), True, BLACK)  # Отображение счета.
    coin_scores = font_small.render(str(COIN_SCORE), True, BLACK)  # Отображение очков за монеты.
    DISPLAYSURF.blit(scores, (10, 10))  # Отображение счета в верхнем левом углу.
    DISPLAYSURF.blit(coin_scores, (375, 10))  # Отображение очков за монеты в верхнем правом углу.

    # Обработка движения и столкновений объектов.
    for entity in all_sprites:  # Для каждого объекта в группе.
        DISPLAYSURF.blit(entity.image, entity.rect)  # Отображаем его изображение на экране.
        entity.move()  # Вызываем метод движения объекта.

    # Проверка на сбор монеты и столкновение с врагом.
    if P1.collect_coin(coins):  # Если игрок собирает монету.
        COIN_SCORE += 1  # Увеличиваем очки за монеты.
        new_coin = Coin()  # Создаем новую монету.
        coins.add(new_coin)  # Добавляем ее в группу монет.
        all_sprites.add(new_coin)  # Добавляем в общую группу объектов.

    if pygame.sprite.spritecollideany(P1, enemies):  # Если произошло столкновение с врагом.
        pygame.mixer.Sound('media/crash.wav').play()  # Воспроизводим звук столкновения.
        time.sleep(0.5)  # Пауза для эффекта столкновения.

        DISPLAYSURF.fill(BLUE)  # Заливка экрана синим цветом.
        DISPLAYSURF.blit(game_over, (30, 250))  # Отображение текста "Game Over".

        pygame.display.update()  # Обновление экрана.
        for entity in all_sprites:  # Для каждого объекта в общей группе.
            entity.kill()  # Удаляем объекты.
        time.sleep(2)  # Пауза перед выходом.
        pygame.quit()  # Завершаем Pygame.
        sys.exit()  # Завершаем программу.

    pygame.display.update()  # Обновление экрана.
    FramePerSec.tick(FPS)  # Управление частотой кадров.
