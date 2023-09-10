#Задание 2
import math
def calculator(action):
    print("Введите 1 элемент: ")
    while True:
        first_variable=input()
        try:
            first_variable=float(first_variable)
            break
        except:
            print("Введенный элемент не является числом, введите элемент: ")
            first_variable=input()
    if action==6:
        return math.log(first_variable)
    print("Введите 2 элемент: ")
    while True:
        second_variable=input()
        try:
            second_variable=float(second_variable)
            break
        except:
            print("Введенный элемент не является числом, введите элемент: ")
            second_variable=input()
    if action==1:
        if int((first_variable+second_variable)*10)%10==0:
            return int(first_variable+second_variable)
        else:
            return first_variable+second_variable
    if action==2:
        if int((first_variable-second_variable)*10)%10==0:
            return int(first_variable-second_variable)
        else:
            return first_variable-second_variable
    if action==3:
        if int((first_variable/second_variable)*10)%10==0:
            return int(first_variable/second_variable)
        else:
            return first_variable/second_variable
    if action==4:
        if int((first_variable*second_variable)*10)%10==0:
            return int(first_variable*second_variable)
        else:
            return first_variable*second_variable
    if action==5:
        if int((first_variable**second_variable)*10)%10==0:
            return int(first_variable**second_variable)
        else:
            return first_variable**second_variable
    if action==7:
        first_variable*=10**second_variable
        first_variable=math.ceil(first_variable)
        return first_variable/10**second_variable
    if action==8:
        first_variable *= 10 ** second_variable
        first_variable = math.floor(first_variable)-1
        return first_variable / 10 ** second_variable
    else:
        print("Неизвестная команда")
        return 0
print("Список функций:"
          "\n1. Сложение"
          "\n2. Вычитание"
          "\n3. Деление"
          "\n4. Умножение"
          "\n5. Возведение в степень"
          "\n6. Логарифм"
          "\n7. Округление в большую сторону до N знака после запятой"
          "\n8. Округление в меньшую сторону до N знака после запятой")
print("Выберите желаемое действие:")
per=int(input())
print(calculator(per))
