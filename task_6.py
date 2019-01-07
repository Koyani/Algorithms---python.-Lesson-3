#task_6
#В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. 
#Сами минимальный и максимальный элементы в сумму не включать.
from random import random
m = []
for n in range(0, 10):
    m.append(randint(-100, 100))
print(m)
min = m[i]
max = m[i]
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
summ = 0
if max_i > min_i:
    m_slice = m[min_i+1:max_i]
    print(m_slice)
    for x in m_slice:
        summ = summ + x
else:
    m_slice = m[max_i+1:min_i]
    print(m_slice)
    for x in m_slice:
        summ = summ + x
print("Summ is: ", summ)

