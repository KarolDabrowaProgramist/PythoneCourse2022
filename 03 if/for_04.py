n = int(input('Podaj liczbę nie mniejszą niż 0, a nie większą niż 8 ->'))
s = 1
for i in range(2, n+1):
    s *= i
    print(s)