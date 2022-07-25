data = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]

def rules():
    print("")
    print("Игра 'Креcтики-Нолики'")
    print("Правила:")
    print("Два игрока (X и 0) по очереди делают свой ход")
    print("В консоль вводится 2 числовых значения через пробел")
    print("Первое значение номер строки")
    print("Второе значение номер столбца")
    print("Формат ввода: '0 2'")
    print("Удачи!")

def game_field():
    print("")
    print("  0 1 2")
    for i in range(len(data)):
        print(str(i), *data[i])

def check_error():
    while True:
        print("")
        value = input(f"     Игрок {player} делает свой ход: ").split()
        if len(value) != 2:
            print("")
            print("Ошибка: Введите ДВА числовых значения!")
            continue
        x, y = value
        if not (x.isdigit()) or not (y.isdigit()):
            print("")
            print("Ошибка: Введите 2 ЧИСЛОВЫХ значения!")
            continue
        x, y = int(x), int(y)
        if x < 0 or x > 2 or y < 0 or y > 2:
            print("")
            print("Ошибка: Значения находятся за приделами поля!")
            continue
        if data[x][y] != "-":
            print("")
            print("Ошибка: Клетка уже занята!")
            continue
        return x, y

def check_win():
    win_list = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for line in win_list:
        v = []
        for place in line:
            v.append(data[place[0]][place[1]])
        if v == [player, player, player]:
            game_field()
            print("")
            print(f"Выиграл игрок {player}!")
            return True
    return False

rules()
count = 0
while True:
    if count == 9:
        game_field()
        print("")
        print("Ничья!")
        break
    if count %2 == 0:
        player = 'X'
    else:
        player = '0'
    game_field()
    x, y = check_error()
    data[x][y] = player
    if check_win():
        break
    count += 1