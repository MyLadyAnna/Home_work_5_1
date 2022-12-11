# Напишите программу для проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

for x in range(2):      #набор 0,1
    for y in range(2):
        for z in range(2):
            if not(x or y or z) == (not x and not y and not z):
                print(f'Для х = {x}, y = {y} и z = {z} утверждение истинно')
            else:
                print(f'Для х = {x}, y = {y} и z = {z} утверждение ложно')