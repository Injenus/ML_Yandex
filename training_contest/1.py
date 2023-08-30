import numpy as np
from scipy.spatial.ripley import ripleys_k


def determine_point_distribution(points):
    results = []

    for row in points:
        reshaped_row = row.reshape(-1,
                                   2)  # Преобразование строки в массив пар точек
        r, Kobs, Lexp, Kexp = ripleys_k(reshaped_row, np.max(reshaped_row))

        if Kobs / Kexp > 1.2:  # Произвольный порог для определения сконцентрированности
            results.append("Сконцентрированы")
        else:
            results.append("Равномерно распределены")

    return results


# Загрузка данных из файла (пример)
lines = np.loadtxt("coordinates.txt")

# Генерация случайных данных для примера
# np.random.seed(42)
# lines = np.random.rand(100, 2000)  # 100 строк, 2000 столбцов (1000 пар точек)

# Определение распределения точек для каждой строки
results = determine_point_distribution(lines)

for i, result in enumerate(results):
    print(f"Строка {i + 1}: {result}")
