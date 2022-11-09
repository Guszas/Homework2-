estimate = str(input('Enter a letter grade '))
if estimate == 'A+' or estimate == 'A':
    print(4.0)
elif estimate == 'A-':
    print(3.7)
elif estimate == 'B+':
    print(3.3)
elif estimate == 'B':
    print(3.0)
elif estimate == 'B-':
    print(2.7)
elif estimate == 'C+':
    print(2.3)
elif estimate == 'C':
    print(2.0)
elif estimate == 'C-':
    print(1.7)
elif estimate == 'D+':
    print(1.3)
elif estimate == 'D':
    print(1.0)
elif estimate == 'F':
    print(0)
else:
    print('Error ')
