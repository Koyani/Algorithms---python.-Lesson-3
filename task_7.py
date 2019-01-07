#task_7
#В одномерном массиве целых чисел определить два наименьших элемента. 
#Они могут быть как равны между собой (оба являться минимальными), так и различаться.
m = [-9, 8, -8, 0, 5, 4, -4, -4]
minn = m[0]
for i in range(len(m)):
    if m[i] < minn:
        minn = m[i]
for i in range(len(m)):        
    if m[i] == minn:
        min_i = i
m.remove(minn)
print(f"First minimal number: {minn}")
minn = m[0]
for i in range(len(m)):
    if m[i] < minn:
        minn = m[i]
for i in range(len(m)):        
    if m[i] == minn:
        min_i = i  
print(f"Second minimal number: {minn}")

