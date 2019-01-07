#task_3
#В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
from random import random
m = []
for n in range(0, 10):
    m.append(randint(-100, 100))
print(m)
max = m[i]
min = m[i]
for i in range(len(m)):
    if m[i] > max:
        max = m[i]
    if m[i] < min:
        min = m[i]
for i in range(len(m)):
    if m[i] == max:
        max_i = i
    if m[i] == min:
        min_i = i
m[max_i] = min
m[min_i] = max
print(m)
