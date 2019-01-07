#task_9
#Найти максимальный элемент среди минимальных элементов столбцов матрицы.
from random import random
x = 5
y = 4
m = []
for i in range(x):
    n = []
    for j in range(x):
        number = int(randint(0, 100))
        n.append(number)
        print(number, ' ',end='')
    m.append(n)
    print('')
 
maxx = -1
for j in range(x):
    minn = 10000
    for i in range(y):
        if m[i][j] < minn:
            minn = m[i][j]
    if minn > maxx:
        maxx = minn
print("Maximum among minimal: ", maxx)
