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


def extract_dataset(m):
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


def get_dataset():
    dataset = []
    for i in range(100):
        dataset.append(list(map(float, input().split())))
    return dataset


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

import random
import math

# BODY
m = 100
n = 1000

create_dataset(m, n)
x_data, y_data = extract_dataset(m)

res_data = data_restructorization(x_data)

maxvalue = max(res_data)
minvalue = min(res_data)

print(res_data, minvalue, maxvalue)

avgval = (maxvalue + minvalue)/2

labels = []
for i in range(m):
    if res_data[i] <= avgval:
        labels.append(0)
        print(0)
    else:
        labels.append(1)
        print(1)
print(labels == y_data)

