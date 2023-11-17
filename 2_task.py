#  Задача
# Вывести на экран:
# - сумму всех элементов списка
# - среднее арифметическое всех элементов списка
# - максимальное значение списка
# - минимальное значение списка


def numbers(arr):
    summ=sum(arr)
    sr=sum(arr) / len(arr)
    print(f'Сумма:{summ}')
    print(f'Среднее арифметическое:{sr} ')
    print(f'Минимальное значение:{min(arr)} ')
    print(f'Максимальное значение: {max(arr)}')
    return summ,sr
first_arr=[]

  #  for i in range(10):
      #  num=int(input(f"Введите {i} элемент:"))
     #  first_arr.append(num)
  #  numbers(first_arr)

second_arr=[12,5,456,-15,64,54,-24]
numbers(second_arr)
res=numbers(second_arr)[0]
res1=numbers(second_arr)[1]
print(res)
print(res1)
