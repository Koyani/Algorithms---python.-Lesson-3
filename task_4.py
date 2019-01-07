#task_4
#Определить, какое число в массиве встречается чаще всего.
from random import random
m = []
for n in range(0, 10):
    m.append(randint(-5, 5))
print(m)
num = m[0]
max_freq = 1
for i in range(len(m)):
    freq = 1
    for j in range(i+1,len(m)):
        if m[i] == m[j]:
            freq += 1
    if freq > max_freq:
        max_freq = freq
        num = m[i]
 
if max_freq > 1:
    print(f"Number {num} is presented {max_freq} in the array")
else:
    print("All element are unique")
