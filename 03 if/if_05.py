password = input('Podaj hasło:')

if len(password) < 8:
    print('Hasło niepoprawne. Hasło jest za krótkie!')
if password.isalnum() and (password.isdigit() or password.isalpha()):
    print('Hasło powinno zawierać cyfry i litery')
if password.isalnum() and password.islower():
    print('Hasło zawiera tylko małe litery, powinno zawierać conajmniej 1 dużą literę')
if password.isalnum() and password.isupper():
    print('Hasło zawiera tylko duże litery, powinno zawierać conajmniej 1 małą literę')
