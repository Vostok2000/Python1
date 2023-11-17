#  Задача
# Вывести на экран сумму всех цифр заданного числа
# дано: 123 -> вывод: 6

def sum_digit(num):
    summ=0
    while num>0:
        summ += num % 10
        num=num//10
    return(summ)
data=int(input())
print(sum_digit(data))

# дано: 337 -> вывод: 13

