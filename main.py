# функция input()
print("Введите значение а: ")
a = int(input())
# print(a)

# if используется для того, чтобы в алгоритме можно было иметь несколько сценариев исполнения логики
# в засимости от значения переменных.

# if a <= 5:
#    print("мало")
# else:
#    print("много")

# логические операторы - нужны для сравнения значений
#print("Введите значение b:")
#b = int(input())

# print(a<b)      # а меньше, чем b?
# print(a>b)      # а больше, чем b?
# print(a <= b)       # а меньше, чем b, значение b включительно
# print(a >= b)       # а больше, чем b, значение b включительно
# print(a == b)   # а ровно b?

# print(a & b) # а и b
# print(a | b) # а или b

print("a:", a)
#print("b:", b)


# if (a == 5) | (b == 2):
#    print("мало")
# else:
#    print("много")

# ДЗ: Написать код, который будет выводить на экран значение "Код красный" если темпиратура
#     ниже 0 или выше +50. Во всех иных случаях будет выведео значение "Код синий".

if a < 0:
    print("Код красный")
elif a > 50:
    print("Код красный")
else:
    print("Код синий")




#fruits = ["apple", "banana", "cherry"]
#for x in fruits:
 ##  break
 # print(x)