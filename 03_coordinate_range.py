# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

number = int(input('Введите номер четверти: '))

if number == 1:
    print(f'У {number} четверти диапазон координат: х = (0; + бесконечность), y = (0; + бесконечность)')
elif number == 2:
    print(f'У {number} четверти диапазон координат: х = (- бесконечность; 0), y = (0; + бесконечность)')
elif number == 3:
    print(f'У {number} четверти диапазон координат: х = (- бесконечность; 0), y = (- бесконечность; 0)')
elif number == 4:
    print(f'У {number} четверти диапазон координат: х = (0; + бесконечность), y = (- бесконечность; 0)')
else:
    print('Необходимо ввести число от 1 до 4')