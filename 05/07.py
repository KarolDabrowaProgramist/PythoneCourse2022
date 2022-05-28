

def is_card(number):
    if number.isdigit() and len(number) >= 13:
        return True
def is_visa(number):
    if len(number) in [13, 16] and number[0] == '4':
        return True
    else:
        return False
def is_mastercard(number):
    if len(number) == 16 and number[0] == '5':
        return True
    else:
        return False
def is_american(number):
    if len(number) == 15 and number.startswith(('24', '37')):
        return True
    else:
        return False
def main():
    number = input('Podaj nr karty kredytowej ->')
    print('Numer karty:', number)
    while True:
        if is_card(number):
            break
        else:
            print('To nie jest prawidłowy numer')
    if is_visa(number):
        print('To jest visa')
    elif is_mastercard(number):
        print('To jest Mastercard')
    elif is_american(number):
        print('To jest American Express')
    elif is_card(number):
        print('Zły numer')

main()

