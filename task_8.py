#task_8
#Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк. 
#Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки. 
#В конце следует вывести полученную матрицу.

x = 5
y = 4
n = []
for i in range(y):
    m = []
    summ = 0
    print(f"{i} line")
    for j in range(x-1):
        a = int(input("Enter a number: "))
        summ += a
        m.append(a)
    m.append(summ)
    n.append(m)
for i in n:
    print(i)

