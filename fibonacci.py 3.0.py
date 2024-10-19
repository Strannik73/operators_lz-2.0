input_data = open('input.txt', 'r')
output_data = open('output.txt', 'w')

n = input_data.readline()
#----------------------------------------------------------------------------------

f1 = 0
f2 = 1
# Выводим значения двух первых членов последовательности через запятую
output_data.write(str(f1))
output_data.write(", ")
output_data.write(str(f2))
output_data.write(", ")


for i in range(2, int(n) + 1):
    # Переприсваеваем n-ому и n+1-ому члену значения n+1-ого и n+2-ого
    f1, f2 = f2, f1 + f2
    # Выводим в файл новое значение переменной f2 (она сейчас равна n+2-ому члену)
    output_data.write(str(f2))
    if i != (int(n)):
        output_data.write(", ")
#--------------------------------------------------------------------------------------------
input_data.close()
output_data.close()