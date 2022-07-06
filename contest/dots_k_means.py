'''
- Создать датасет
- Написать алгоритм (скопировать частично)
- Написать функции в алгоритме
- Запустить 3 раза и выбрать лучший результат
---
m строк по
n точек
---
- Создание датасета:
    - Открыть файл
    - Сгенерировать точки рандомным способом с помощью обоих алгоритмов в задании (200 точек)
    - Сохранить в файл
    -- Формат данных тот же, что и в задании - строки с пробелами

- Алгоритм:
    - Цикл (3 раза)
        - Выбираем две рандомные строки из датасета - это будут два кластера
        - Считаем для каждой строки ближайшее расстояние до кластера (выход - массив m x 1, содержащий значения
          кластера для каждой точки)
        - Сохраняем промежуточный результат
        - Цикл:
            - Считаем среднее от точек в каждом кластере, обновляем координаты
            - Считаем для каждой строки ближайшее расстрояние до нового кластера
            - Если новый промежуточный результат не отличается от прошлого, цикл разрывается
            - Если нет, сохраняем промежуточный результат
        - Выводим точность сравнения, сохраняем вместе с координатами кластеров
    - Выбираем лучшую точность и пишем в отдельный файл координаты лучших кластеров

- Программа для загрузки:
    - Часть функции по экстракции данных
    - Весь алгоритм
'''
import copy
import random
import math


# Dots generators
def generate1():
    a = random.uniform(0, 1)
    b = random.uniform(0, 1)
    return a * math.cos(2 * math.pi * b), a * math.sin(2 * math.pi * b)


def generate2():
    while True:
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x ** 2 + y ** 2 > 1:
            continue
        return x, y


# Создание датасета
def create_dataset(m, n):
    xf = open('x_dots', 'w')
    yf = open('y_dots', 'w')

    for i in range(m):
        r = random.choice([0, 1])
        for j in range(n):
            if r == 0:
                x, y = generate1()
            else:
                x, y = generate2()
            xf.write(str(x) + ' ' + str(y) + ' ')
        yf.write(str(r) + ' ')
        xf.write('\n')

    xf.close()
    yf.close()


def extract_data(m):
    x_data = []

    xf = open('x_dots', 'r')
    for i in range(m):
        stroka = list(map(float, xf.readline().split()))
        x_data.append(stroka)
    xf.close()

    yf = open('y_dots', 'r')
    y_data = list(map(int, yf.readline().split()))
    yf.close()

    return x_data, y_data


def avg_vector_len(row):
  dim = len(row)
  res = 0
  x = row[0:dim:2]
  y = row[1:dim+1:2]
  for n in range(len(x)):
    res += (x[n]**2 + y[n]**2)**(1/2)
  return res/dim


def data_restructorization(x_data):
    new_data = []
    for m in range(len(x_data)):
        new_data.append(avg_vector_len(x_data[m]))
    return new_data


def get_clusters(ex, x_data):
    clusters = [x_data[0], x_data[ex//2]]
    return clusters


def data_distribution(x_data, clusters, k, ex, dim):
    labels = []
    for m in range(ex):
        min_distance = float('inf')
        suitable_cluster = -1
        for q in range(k):
            distance = 0
            for n in range(dim):
                distance += (x_data[m][n] - clusters[q][n])**2
            distance = distance**(1/2)
            if distance < min_distance:
                suitable_cluster = q
                min_distance = distance
        labels.append(suitable_cluster)
    return labels


def update_clusters(x_data, labels, k, ex, dim):
    newclusters = [[] for i in range(k)]
    for q in range(k):
        sum = 0
        num = 0
        for n in range(dim):
            for m in range(ex):
                if labels[m] == q:
                    sum += x_data[m][n]
                    num += 1
            newclusters[q].append(sum/num)
    return newclusters


# Algorithm
def clusterization(x_data, k):
    ex = len(x_data)
    dim = len(x_data[0])

    preclusters = get_clusters(ex, x_data)

    while 1:
        labels = data_distribution(x_data, preclusters, k, ex, dim)
        clusters = update_clusters(x_data, labels, k, ex, dim)
        if preclusters == clusters:
            break
        preclusters = clusters.copy()
    return labels


"""def get_data():
    dataset = []
    for i in range(100):
        dataset.append(list(map(float, input().split())))
    return dataset"""

# BODY
# Creating dataset
# необходимые общие переменные
m = 100     # количество строк в датасете
n = 1000    # количество точек в строке
k = 2       # количество кластеров

create_dataset(m, n)
x_data, y_data = extract_data(m)

#x_data = data_restructorization(x_data)
#x_data = get_data()
labels = clusterization(x_data, k)

"""
for i in range(len(labels)):
    print(labels[i])
    """
right = [int(labels[i] == y_data[i]) for i in range(m)]
print(right)
accuracy = sum(right)/len(right)
print(accuracy)
'''
Код работает, но с количеством итераций точность не растет
Вывод: данным методом разделить выборку нельзя
'''
