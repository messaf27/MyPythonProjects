# Урок 1. Знакомство с Python
# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

# weekDaysList = ['Пн','Вт','Ср','Чт','Пт','Сб','Вс']
weekDaysList = ('Пн','Вт','Ср','Чт','Пт','Сб','Вс')
dayNum = int(input('Введите номер дня недели: '))

if(dayNum < 5):
    print(f'Рабочий день ({weekDaysList[dayNum - 1]})')
else:
    print(f'Выходной день ({weekDaysList[dayNum - 1]})')