a = float(input("Введите стартовое значение ряда\n"))
b = float(input("Введите конечное значение ряда\n"))
c = int(input("Введите точность\n"))
# устанавливаем для b необходимую точность

b = round(b, c)
sum = 0
n = 1
counter = 0


while sum + a < b:
    # Подсчитывем сумму последовательности вместе с членом последовательности
    sum += 1 / (n * n)
    n += 1
    # Считаем число итераций
    counter += 1
    
if sum + a >= b:
    print("Число итераций равно:", counter)