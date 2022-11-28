name = str(input('Введите имя '))
print(name, 'has been invited ')
quests = 1
answer = str(
    input('Хотите пригласить кого-то еще у/п'))
while answer == 'y':
    if answer == 'Y':
        new_name = str(input('Введите еще одно имя '))
    quests += 1
    print(new_name, 'has been invited')
    answer = str(input('Хотите пригласть кого-то еще у/п'))
else:
    print('number of quests', quests)
