

numbers = (1, 2, 3, 5, 8, 9, 12321)
num = numbers
num = input('Podaj losową liczbę ->')
flag = False

for i, v in enumerate(num):
    if int(num) == v:
        print('mam to', i)
    flag = True
    break
if not flag:
    print('Nie ma')

