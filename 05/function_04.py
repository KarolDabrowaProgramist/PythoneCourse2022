#▹ Napisz funkcję, która sprawdzi, czy liczba występuje w podanym przez użytkownika zakresie.
#Powinna zwrócić komunikat: “tak, liczba x znajduje się w zadanym zakresie”, “nie, liczba x jest z poza zakresu”.

def main():
    user_numbers = (8, 90, 7, 1, 8, 9)
    print(check(user_numbers))

def check(number, user_numbers):
    if number in user_numbers:
      return 'liczba w zbiorze'
    else:
      return 'brak liczby w zbiorze'

#def check(user_numbers):
#    x = 7
#    for numb in user_numbers:
#        if numb == x:
#            print("Liczba znajduje się w zbiorze")
#       elif numb != x:
#            print('Nie znajduje się')

main()

