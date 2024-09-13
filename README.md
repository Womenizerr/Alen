import random,math
try:
    magisters_input = print(f'Введите имена участников соревнования')
    first_player = input(f'Введите имя 1-го участника')
    print(f'{first_player} - это первый участник соревнований')
    second_player = input(f'Введите имя 2-го участника')
    print(f'{second_player} - это второй участник соревнований')
    print(f'Игра началась!')
    print(f'Испытание для {first_player}:')
    points1_1 = random.randint (3,10)
    points1_2 = random.randint(30,50)
    points1_3 = random.randint(3,10)
    way_1 = input(f'Ваш игрок проходил полосу препятствий?')
    honesty_1 = input(f'Играл ли этот игрок честно?')
    total_points1 = points1_1 + points1_2 + points1_3
    print(f'Испытание 1 - Дуэль: за дуэль он получил {points1_1} очков')
    print(f'Испытание 2 - Загадка: за эту загадку он получил {points1_2} очков')
    print(f'Испытание 3 - Испытание на ловкость: за свою ловкость он получил {points1_3} очков')
    print(f'Итого очков для {first_player} будет: {total_points1}')
    print(f'Испытание для {second_player}:')
    points2_1 = random.randint(3, 10)
    points2_2 = random.randint(30, 50)
    points2_3 = random.randint(3, 10)
    way_2 = input(f'Ваш игрок проходил полосу препятствий?')
    honesty_2 = input(f'Играл ли этот игрок честно?')
    total_points2 = points2_1 + points2_2 + points2_3
    print(f'Испытание 1 - Дуэль: за дуэль он получил {points2_1} очков')
    print(f'Испытание 2 - Загадка: за эту загадку он получил {points2_2} очков')
    print(f'Испытание 3 - Испытание на ловкость: за свою ловкость он получил{points2_3} очков')
    print(f'Итого очков для {second_player} будет: {total_points2}')
    if total_points1 > total_points2:
        print(f'Победил {first_player} с разницей {total_points1} очками')
    elif total_points2 > total_points1:
        print(f'Победил {second_player} с разницей {total_points2} очками')
    else:
        print(f'Ничья, оба игроков набрали {total_points1} очков')
        if honesty_1 == 'да':
            total_points1 += 40
        else:
            print(f'Доп.баллов начисленно не будет')
            if honesty_2 == 'да':
                total_points2 += 40
            else:
                print(f'Доп.баллов начисленно не будет')
                if way_1 == 'да':
                    total_points1 += 40
                else:
                    print(f'Доп.баллы за полосу препятствий начисленны не будут')
                    if way_2 == 'да':
                        total_points2 += 40
                    else:
                        print(f'Доп.баллы за полосу препятствий начисленны не будут')
except ValueError:
    print(f'Некоректный ввод данных')

