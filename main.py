"""
1. Сумма чисел
2. Разность чисел
3. Произведение чисел
4. Частное чисел (деление)
5. Замена чисел (позволяет ввести новые числа для манипуляций)
0. Выход
"""

print('привіт друже я калькулятор :-)')
while True:
    v = input('вкажіть операцію: \n 1 Додавання \n 2 Віднімання \n 3 Множення \n 4 Розподіл \n 0 Вихід \n')

    if (v != '1') and (v != '2') and (v != '3')  and (v != '4') and (v != '0') and (v != None) :
        print('T_T Операция вказана не вірно!')
        quit()

    v = int(v)

    if v == 0:
        print('До побачення!')
        quit()

    x = int (input('Вкажіть число X: '))
    y = int (input('Вкажіть число Y: '))

    while (v == 4) and (y == 0):
       y = int(input(':-0   На 0 неможливе розподіл, ведіть інше число: '))


    if v == 1:
        r = x + y
        t = 'Додавання'
    if v == 2:
        r = x - y
        t = 'Віднімання'
    if v == 3:
        r = x * y
        t = 'Множення'
    if v == 4:
        r = float(x / y)
        t = 'Розподіл'
    print ('Результат обчислення: ', t,' = ', r)
    x = ''
    y = ''
   # still standing :-)