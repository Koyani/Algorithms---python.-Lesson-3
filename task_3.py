#task_3
#В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
from random import random
m = []
for n in range(0, 10):
    m.append(randint(-100, 100))
print(m)
maxx = m[i]
minn = m[i]
for i in range(len(m)):
    if m[i] > maxx:
        maxx = m[i]
    if m[i] < minn:
        minn = m[i]
for i in range(len(m)):
    if m[i] == maxx:
        max_i = i
    if m[i] == minn:
        min_i = i
m[max_i] = minn
m[min_i] = maxx
print(m)
