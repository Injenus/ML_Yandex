import numpy as np

def calculate_average_distance(points):
    total_distance = 0
    num_pairs = 0

    for i in range(0, len(points), 2):
        x1, y1 = points[i], points[i + 1]
        for j in range(i + 2, len(points), 2):
            x2, y2 = points[j], points[j + 1]
            total_distance += np.linalg.norm(np.array([x1, y1]) - np.array([x2, y2]))
            num_pairs += 1

    return total_distance / num_pairs

# Чтение данных из файла
with open('coordinates.txt', 'r') as f:
    lines = f.readlines()

# Вычисление средних расстояний и запись в файл
with open('output.txt', 'w') as f:
    for line in lines:
        points = list(map(float, line.strip().split()))
        avg_distance = calculate_average_distance(points)
        f.write(f'{avg_distance}\n')
