from logic import *
import pygame
import sys
from database import sqlite_create, sqlite_sort, sqlite_insert

def init_const():
    global mas, score
    mas = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
    ]
    empty = get_empty_list(mas)
    random.shuffle(empty)
    random_num1 = empty.pop()
    random_num2 = empty.pop()
    x1, y1 = get_index_from_number(random_num1)
    mas = insert_2_or_4(mas, x1, y1)
    x2, y2 = get_index_from_number(random_num2)
    mas = insert_2_or_4(mas, x2, y2)
    score = 0

# Константы цвета по RGB
COLOR_TEXT = (255, 137, 0)
COLORS = {
    0: (130, 130, 130),
    2: (255, 255, 255),
    4: (255, 255, 128),
    8: (255, 255, 0),
    16: (255, 235, 255),
    32: (255, 235, 128),
    64: (255, 235, 0),
    128: (155, 200, 200),
    256: (155, 135, 255),
    512: (155, 200, 200),
    1024: (255, 0, 255),
    2048: (0, 235, 255),
}
# Настройки игры
mas = None
score = None
init_const()
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (130, 130, 130)
RED = (255, 0, 0)

# Константы настроечных параметров
BLOCKS = 4
SIZE_BLOCK = 110
MARGIN = 10
WIDTH = BLOCKS * SIZE_BLOCK + (BLOCKS + 1) * MARGIN
HEIGTH = WIDTH + SIZE_BLOCK
TITLE_REC = pygame.Rect(0, 0, WIDTH, SIZE_BLOCK)
USERNAME = "Player"

delta = 0
(name1, point1), (name2, point2), (name3, point3) = sqlite_sort()

def draw_interface(score = None, delta = None):
    pygame.draw.rect(screen, WHITE, TITLE_REC)
    font = pygame.font.SysFont('stxingkai', 70)
    font_score = pygame.font.SysFont('sitkatext', 42)
    font_delta = pygame.font.SysFont('sitkatext', 24)
    font_statistic = pygame.font.SysFont('stxingkai', 20)

    text_score = font_score.render("Score: ", True, COLOR_TEXT)
    screen.blit(text_score, (20, 35))
    text_score_num = font_score.render(f"{score} ", True, COLOR_TEXT)
    screen.blit(text_score_num, (180, 35))

    if delta > 0:
        text_delta = font_delta.render(f"+{delta} ", True, COLOR_TEXT)
        screen.blit(text_delta, (175, 75))

    text_statistic_header = font_statistic.render(f"Статистика лучших игроков:", True, COLOR_TEXT)
    screen.blit(text_statistic_header, (255, 15))
    global name1, name2, name3, point1, point2, point3
    text_statistic1 = font_statistic.render(f"#1: {name1} : {point1}", True, COLOR_TEXT)
    screen.blit(text_statistic1, (300, 35))
    text_statistic2 = font_statistic.render(f"#2: {name2} : {point2}", True, COLOR_TEXT)
    screen.blit(text_statistic2, (300, 55))
    text_statistic3 = font_statistic.render(f"#3: {name3} : {point3}", True, COLOR_TEXT)
    screen.blit(text_statistic3, (300, 75))
    pretty_print(mas)
    for row in range(BLOCKS):
        for column in range(BLOCKS):
            value = mas[row][column]
            text = font.render(f'{value}', True, BLACK)
            w = column * SIZE_BLOCK + (column + 1) * MARGIN
            h = row * SIZE_BLOCK + (row + 1) * MARGIN + SIZE_BLOCK
            pygame.draw.rect(screen, COLORS[value], (w, h, SIZE_BLOCK, SIZE_BLOCK))
            if value != 0:
                font_w, font_h = text.get_size()
                text_x = w + (SIZE_BLOCK - font_w) / 2
                text_y = h + (SIZE_BLOCK - font_h) / 2
                screen.blit(text, (text_x, text_y))


# Картинка приветствия
def draw_intro():
    img2048 = pygame.image.load('picture.jpg')
    font = pygame.font.SysFont('stxingkai', 70)
    text_welcome = font.render("Welcome!", True, WHITE)
    name = "Player"
    insert_name = False
    while not insert_name:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.unicode.isalpha():
                    if name == "Player":
                        name = ""
                    name += event.unicode
                elif event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                elif event.key == pygame.K_RETURN:
                    if name and name != "Player":
                        global USERNAME
                        USERNAME = name
                        insert_name = True
                        break
        screen.fill(BLACK)
        text_name = font.render(name, True, WHITE)
        rect_name = text_name.get_rect()
        rect_name.center = screen.get_rect().center
        screen.blit(pygame.transform.scale(img2048, [300, 200]), [10, 10])
        screen.blit(text_welcome, (125, 220))
        screen.blit(text_name, rect_name)
        pygame.display.update()
    screen.fill(BLACK)

def compare_score(score, point):
    if score > point:
        compare_text = "вы установили рекорд!"
    else:
        compare_text = f"Рекорд: {point}"
    return compare_text

# Размер экрана
screen = pygame.display.set_mode((WIDTH, HEIGTH))
# Заголовок экрана
pygame.display.set_caption("GAME 2048")

def game_loop():
    global score, delta, mas

    draw_interface(score, delta)
    # Основной цикл программы

    while is_zero_in_mas(mas):
        for event in pygame.event.get():
            pygame.display.update()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                delta = 0
                if event.key == pygame.K_LEFT:
                    mas, delta = move_left(mas)
                elif event.key == pygame.K_RIGHT:
                    mas, delta = move_right(mas)
                elif event.key == pygame.K_UP:
                    mas, delta = move_up(mas)
                elif event.key == pygame.K_DOWN:
                    mas, delta = move_down(mas)
                score += delta
                empty = get_empty_list(mas)
                random.shuffle(empty)
                random_num = empty.pop()
                x, y = get_index_from_number(random_num)
                mas = insert_2_or_4(mas, x, y)
                draw_interface(score, delta)
                pygame.display.update()
    sqlite_create()
    sqlite_insert(score, USERNAME)



def draw_finish(score, USERNAME, point):
    global mas
    img2048 = pygame.image.load('finish_image.jpg')
    # Шрифты текста
    font = pygame.font.SysFont('stxingkai', 40)
    font_enter = pygame.font.SysFont('stxingkai', 25)
    finish = False
    # Основной цикл финишной отрисовки экрана
    insert_name = False
    while not insert_name:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    insert_name = True
                    finish = True
                    break
                elif event.key == pygame.K_SPACE: # рестарт
                    USERNAME = "Player"
                    insert_name = True
                    init_const()

        screen.fill(BLACK)

        comp_text = compare_score(score, point)
        # Устанавливаем текст
        text_compare = font.render(f"{comp_text}", True, WHITE)
        text_point = font.render(f"Вы набрали {score}", True, WHITE)
        text_finish = font.render("Game Over!", True, WHITE)
        text_name = font.render(f"Gamer : {USERNAME}", True, WHITE)
        text_enter = font_enter.render("Для выхода нажмите [Enter]", True, RED)

        # Прикрепляем к экрану наш текст
        screen.blit(pygame.transform.scale(img2048, [500, 200]), (0, 0))
        screen.blit(text_finish, (175, 210))
        screen.blit(text_name, (10, 245))
        screen.blit(text_compare, (10, 275))
        screen.blit(text_point, (10, 305))
        screen.blit(text_enter, (130, 500))

        # Обновляем экран
        pygame.display.update()
    screen.fill(BLACK)
    return finish

def main():
    finishgame = False
    pygame.init()
    while not finishgame:
        if USERNAME == "Player":
            draw_intro()
        game_loop()
        finishgame = draw_finish(score, USERNAME, point1)


if __name__ == '__main__':
    main()

