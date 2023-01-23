# ЗАДАЧА 1

# Задайте список из вещественных чисел и найдите разницу между макс и мин значениеями дробной части

text = [1.1,1.2,3.1,4,10.01]
text2 = []
for i in range(len(text)):
    if text[i] % 1 !=0:
        text2.append(text[i])
text3 = [round(text2[i] % 1, 2)
for i in range(len(text2))]
print(f"{text3} -> {max(text3) - min(text3)}")

# ЗАДАЧА 1.1

text = [1.1,1.2,3.1,4,10.01]
text2 = list(map(float, text))
text3 = [round(i % 1, 2) for i in text2 if i % 1 != 0]
print(max(text3) - min(text3))

# ЗАДАЧА 2

# Задайте список из нескольких чисел. и найти сумму элементов стоящих на нечетных позициях
 
# text = [1,2,3,65,100]
# sum = 0 
# for i in range(0, len(text), 2):
#     sum += text[i]
# print(f"{text} -> sum = {sum}")

# ЗАДАЧА 2.1

text = [1,2,3,65,100]
def Full_Sum(ls, count=0):
    if count == 0:
        return sum(ls[0::2])
    else:
        return sum(ls[0:len(text):2])

text = Full_Sum(list(map(int, text)))
print(text)

# ФИБОНАЧИ

# ЗАДАЧА 3

num = int(input())
def fibonacci(n):
	
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
for i in range(num):
    print(fibonacci(i))

# ЗАДАЧА 3.1

def fibonacci(count):
    res = [0, 1]
    any(map(lambda _: res.append(sum(res[-2:])), range(2, count)))
    return res[-10:count]

print(fibonacci(10))