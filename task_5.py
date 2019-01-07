#task_5
#В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
from random import random
m = []
for n in range(0, 10):
    m.append(randint(-100, 100))
print(m)
if m[i] < 0:
    maxx = m[i]
for i in range(len(m)):
    if (m[i] < 0) and (m[i] > maxx):
        maxx = m[i]
        print(maxx)
for i in range(len(m)):        
    if m[i] == maxx:
print(f"Maximum value of all negative elements in array is {maxx} and its index is {i}") 
