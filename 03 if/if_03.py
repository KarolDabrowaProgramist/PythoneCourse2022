opinion1 = float(input('W skali od 0 do 10 oceń głównego bohatera książki ->'))
opinion2 = float(input('W skali od 0 do 10 oceń fabułę książki ->'))
opinion3 = float(input('W skali od 0 do 10 opisz czy warto było przeczytać książkę ->'))

result = (opinion1 + opinion2 + opinion3) / 3
if result > 7:
    print('Bardzo dobry')
elif result >= 5:
    print('Przeciętna')
elif result <= 5:
    print('Nie warta uwagi')
