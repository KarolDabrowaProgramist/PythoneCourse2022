
def main():
    user_numb = int(input('Podaj liczbę ->'))
    print(check(user_numb))
def check(user_numb):
    if user_numb % 2 == 0:
        print('Liczba jest parzysta')
    else:
        print('Liczba nie jest parzysta')

main()