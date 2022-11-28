compnum = 50
number = int(input('Введите число '))
attempt = 1
while number > compnum :
    if number > compnum:
        print(number, 'больше 50')
        number = int(input('Введите еще одно число '))
        attempt += 1
    elif number == compnum:
        print('Well done you took ', attempt, 'attempts ')
while number < compnum:
    if number < compnum:
        print(number, 'меньше 50 ')
        number = int(input('Введите еще оно число '))
        attempt += 1
    elif number == compnum:
        attempt += 1
        print('Well done you took ', attempt, 'attempts ')
while number == compnum:
    if number == compnum:
        print('Wel done you took ', attempt , 'attempts ')
        break
