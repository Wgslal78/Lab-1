#Задание 3
print("Введите число: ")
variable=int(input())
def fibonachurs(per):
    if per==0:
        return 0
    if per==1:
        return 1
    return fibonachurs(per-1)+fibonachurs(per-2)
for i in range(variable+5):
    if fibonachurs(i)==variable:
        print("Введенное число является числом фибоначи")
        break
    elif fibonachurs(i)>variable:
        print("Введенное число не является числом фибоначи")
        break