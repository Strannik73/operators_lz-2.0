input_data = open('input.txt', 'r') # откпрываем для чтения (литера 'r')файл и кладем в него преременную
output_data = open('output.txt', 'w')
data = input_data.read() # читаем в другую переменную соднержимое всего файла
data = data.split()
#разбиваем строку в список = с использованием команды сплит(по умолчанию разделитель - пробел)
#-----------------------------------------------------------------------

a = int(data[0])#переменной а присваиваем значение первого элемента списка - результат первого стрелка


for i in range(2 , 25001):
    if a%i==0 and a!=i: 
         output_data.write(str('N')) 
         break
else: output_data.write(str('Y'))
  
if a==1: output_data.write(str('N'))

#-----------------------------------------------------------------------
# откпрываем для чтения (литера 'w')файл и кладем в него преременную
#записываем перменную и не забываем преобразовать его в строку(иначе будет ошибка)


#не забываем закрыть ранее открытые файлы
input_data.close()
output_data.close()