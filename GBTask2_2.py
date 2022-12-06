# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def fact(n):
    f = 1
    for i in range(n):
        f *= i+1
    return f

number = int(input('Введите число: '))

mResults = []
mActions = []

res = 1
rString = ''
for i in range(number):
    res *= i + 1
    
    if i == 1:
        rString += str(i)
    else:
       rString += '*'+str(i)
       
    mActions.append(rString)
    mResults.append(res)

print(f'N = {number} тогда {mResults} {mActions}')


    