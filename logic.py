import random
COLOR_TEXT = (255, 137, 0)

def pretty_print(mass: list):
    print("-" * 7)
    for i in mass:
        print(*i)
    print("-" * 7)

def get_number_index(i,j : int):
    return i * 4 + j + 1

def get_index_from_number(num):
    num -= 1
    x, y = num // 4, num % 4
    return x, y

def insert_2_or_4(mas, x, y):
    if random.random() <= 0.75:
        mas[x][y] = 2
    else:
        mas[x][y] = 4
    return mas

def get_empty_list(mass : list):
    empty_list = []
    for i in range(4):
        for j in range(4):
            if mass[i][j] == 0:
                num = get_number_index(i, j)
                empty_list.append(num)
    return empty_list



def is_zero_in_mas(mas):
    for row in mas:
        if 0 in row:
            return True
    return False

def move_left(mas):
    delta = 0
    for row in mas:
        while 0 in row:
            row.remove(0)
        while len(row) != 4:
            row.append(0)
    for i in range(4):
        for j in range(3):
            if mas[i][j] == mas[i][j+1] and mas[i][j] != 0:
                mas[i][j] *= 2
                delta += mas[i][j]
                mas[i].pop(j+1)
                mas[i].append(0)
    return mas, delta

def move_right(mas):
    delta = 0
    for row in mas:
        while 0 in row:
            row.remove(0)
        while len(row) != 4:
            row.insert(0,0)
    for i in range(4):
        for j in range(3, 0, -1):
            if mas[i][j] == mas[i][j-1] and mas[i][j] != 0:
                mas[i][j] *= 2
                delta += mas[i][j]
                mas[i].pop(j-1)
                mas[i].insert(0, 0)
    return mas, delta

def reverse_mas(mas):
    temp_mass = [[] for i in range(4)]
    for i in range(4):
        for j in range(4):
            temp_mass[i].append(mas[j][i])
    return temp_mass

def move_up(mas):
    temp_mass = reverse_mas(mas)
    delta = 0
    for row in temp_mass:
        while 0 in row:
            row.remove(0)
        while len(row) != 4:
            row.append(0)
    for i in range(4):
        for j in range(3):
            if temp_mass[i][j] == temp_mass[i][j+1] and temp_mass[i][j] != 0:
                temp_mass[i][j] *= 2
                delta += temp_mass[i][j]
                temp_mass[i].pop(j+1)
                temp_mass[i].append(0)

    mas = reverse_mas(temp_mass)
    return mas, delta

def move_down(mas):
    temp_mass = reverse_mas(mas)
    delta = 0
    for row in temp_mass:
        while 0 in row:
            row.remove(0)
        while len(row) != 4:
            row.insert(0,0)
    for i in range(4):
        for j in range(3, 0, -1):
            if temp_mass[i][j] == temp_mass[i][j-1] and temp_mass[i][j] != 0:
                temp_mass[i][j] *= 2
                delta += temp_mass[i][j]
                temp_mass[i].pop(j-1)
                temp_mass[i].insert(0, 0)
    mas = reverse_mas(temp_mass)
    return mas, delta



