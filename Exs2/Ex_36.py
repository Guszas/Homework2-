age = int(input("Введите возраст человека "))
if age <= 22 and age >= 0:
    print(age / 10.5)
elif age > 22:
    print(2 + (age - 22) / 4)
else:
    print("Ошибка ")
