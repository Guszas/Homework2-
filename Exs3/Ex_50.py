number = int(input('Ввeдите чисто от 10 до 20 '))
while number < 10 :
    if number < 10 :
        print('Too low ')
        number = int(input('Введите другое число '))
while number > 20 :
    if number > 20 :
        print(' Too hight ')
        number = int(input('Введите другео число '))
else:
    print('Thank you ')