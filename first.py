#Задание 1
print("Выберите тип данных: "
      "\n1--------------- число"
      "\n2--------------- строка"
      "\n3--------------- список")
per=int(input())
if per==1:
    print("\nВведите 1 число: ")
    variable=int(input())
    print("\nВведите 2 число: ")
    variable1=int(input())
    print("\nПять математических действий "
          "\n1. Сложение ",variable+variable1,
          "\n2. Вычитание ",variable-variable1,
          "\n3. Деление без остатка ",variable//variable1,
          "\n4. Деление по модулю ",variable%variable1,
          "\n5. Возведение в степень ",variable**variable1)
elif per==2:
    print("\nВведите 1 слово: ")
    string=input()
    print("\nВведите 2 слово: ")
    string1=input()
    print("\n1. Верхний регистр для всех букв в строке ",string.upper(),"\t",string1.upper(),
          "\n2. Нижний регистр для всех букв в строке ",string.lower(),"\t",string1.lower(),
          "\n3. Конкатенация строк ",string+string1,
          "\n4. Сравнение строк ",string==string1,
          "\n5. Длина строк ",len(string),"\t",len(string1))
elif  per==3:
    arr=list()
    print("\nВведите числа добавляемые в список: "
          "\n число--'0' означает конец списка")
    variable=int(input())
    while variable!=0:
        arr.append(variable)
        variable=int(input())
    print("\n1. Колличество элементов в списке ",len(arr),
          "\n\n2. Последний элемент в списке ",arr[-1])
    arr.reverse()
    print("\n3. Развернутый список ",arr)
    arr.sort()
    print("\n4. Сортировка по возростанию ",arr)
    arr.clear()
    print("\n5. Очистка списка",arr)
else:
    print("Неизвестная команда")

