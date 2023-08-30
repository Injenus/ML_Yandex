import matplotlib.pyplot as plt
from random import uniform
from math import cos, sin, pi


# Замените эти функции на ваши функции получения координат
def generate1():
    a = uniform(0, 1)
    b = uniform(0, 1)
    return (a * cos(2 * pi * b), a * sin(2 * pi * b))


def generate2():
    while True:
        x = uniform(-1, 1)
        y = uniform(-1, 1)
        if x ** 2 + y ** 2 > 1:
            continue
        return (x, y)


# Количество вызовов каждой функции
num_calls = 100

# Генерируем координаты и записываем их в файл
with open('coordinates.txt', 'w') as file:
    for _ in range(num_calls):
        coordinates1 = [generate1() for _ in range(1000)]
        coordinates2 = [generate2() for _ in range(1000)]

        coordinates1_flat = [coord for point in coordinates1 for coord in
                             point]
        coordinates2_flat = [coord for point in coordinates2 for coord in
                             point]

        coordinates1_line = " ".join(map(str, coordinates1_flat))
        coordinates2_line = " ".join(map(str, coordinates2_flat))

        file.write(coordinates1_line + "\n")
        file.write(coordinates2_line + "\n")

# Визуализация кода остается такой же, как в вашем примере
# ... (ваш код для визуализации)

plt.show()
