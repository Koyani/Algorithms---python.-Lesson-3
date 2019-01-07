#task_5
#В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
m = [-9, 8, -8, 0, 5, 4, -4, -4]
if m[i] < 0:
    max = m[i]
for i in range(len(m)):
    if m[i] < 0 and m[i] > max:
        max = m[i]
for i in range(len(m)):        
    if m[i] == max:
        print(f"Maximum value of all negative elements in array is {max} and its index is {i}")  
