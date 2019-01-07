#task_5
#В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
m = [-9, 8, -8, 0, 5, 4, -4, -4]
maxx = m[0]
for i in range(len(m)):
    if m[i] <0 and m[i] > maxx:
        maxx = m[i]
for i in range(len(m)):        
    if m[i] == maxx:
        print(f"Maximum value of all negative elements in array is {maxx} and its index is {i}")  
