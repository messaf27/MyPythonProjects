# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных индексах. Индексы вводятся одной строкой, через пробел.
# n = 3
# [-3, -2, -1, 0, 1, 2, 3]
# --> 0 2 3
# -3 * -1 * 0 = 0
# Вывод: 0

import os
clear = lambda: os.system('cls')
clear()

n = int(input('Введите число N: '))
nNeg = n * -1

numList = []

for i in range(nNeg, n + 1):
    numList.append(i)
    
print(numList)

indexList = list(map(int, input('Введите индексы через пробел: ').split()))
rMult = 0
rMultStr = ''
for i in indexList:
    rMult *= numList[i]
    print(rMult)
    if i > 1:
        rMultStr += ' * '
    rMultStr += str(numList[i])

# print(indexList)
print(rMultStr + ' = ' + str(rMult))
print(f'вывод: {rMult}')