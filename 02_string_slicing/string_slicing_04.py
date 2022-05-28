
title = input('Podaj tytuł książki ->')
surname = input('Podaj nazwisko autora ->')
pages = (input('Podaj ilość stron ->'))

print('Tytuł ->', str.capitalize(title))
print('Autor ->', str.capitalize(surname))
print('Liczba stron ->', pages)
print('Czy tytuł zawiera tylko litery?', str.isalpha(title))
print('Czy nazwisko zawiera tylko litery?', str.isalpha(surname))
print('Czy liczba stron składa się tylko z liczb?', str.isnumeric(pages))

print(str.split(sep=',', self='10', maxsplit=+ 1))
