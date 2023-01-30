
# Вычислить число c заданной точностью d
# Пример:
# - при d = 0.001, π = 3.141   

#       Ввод: 0.01
#       Вывод: 3.14

#       Ввод: 0.001
#       Вывод: 3.141
import os

def calc_pi(eps=1.0e-5):
    s=0
    d=1
    sgn=1
    while True:
        a=4/d
        s=s+sgn*a
        if a<eps:
            return s
        sgn=-sgn
        d=d+2
 
def div_calc(num):
    count = 0;
    while num != 1:
       num = num * 10
       count += 1
    return count

def toFixed(num, digits=0):
    return f"{num:.{digits}f}"

clear = lambda: os.system('cls')
clear()

d = float(input('Введите число точности: '))
p = calc_pi()
digNum = div_calc(d)

# print(f'd = {d}')
# print(f'p = {p}')
# print(f'divNum = {divNum}')

print(toFixed(p, digNum))