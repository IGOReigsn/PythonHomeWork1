"""Задача 2: Найдите сумму цифр трехзначного числа.

*Пример:*

123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0) |"""
    
num=input("Введите трехзначное число:")
if 99<int(num)<1000: #только положительные (для упрощения своей жизни)
     sum=0
     for i in num: 
        sum=sum+int(i)
     print("Сумма цифр равна: ", sum) 

else:  
    print("Некорректное значение: число не трехзначное")
    

    