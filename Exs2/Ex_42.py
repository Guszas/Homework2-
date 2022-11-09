note = str(input('Введите обозначение ноты '))
octave = int(input('Введите номер нотации октавы'))
if note == 'C':
    frequency = 263.63
elif note == 'E':
    frequency = 329.63
elif note == 'F':
    frequency = 349.23
elif note == 'G':
    frequency = 392.00
elif note == 'A':
    frequency = 440.00
elif note == 'B':
    frequency = 493.88
frequency = frequency / 2 ** (4 - octave)
print(frequency)