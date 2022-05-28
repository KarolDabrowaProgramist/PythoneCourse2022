quote = 'Honesty is the first chapter in the book of wisdom.'

new_quote = quote.replace('wisdom','friendship')
print("1: Ilość znaków:", len(quote))
print("2:", quote[-7:-1:1])
print("3:", quote[:25:1])
print("4:", quote[-1::])
print("5:", quote[25::3])
print("6:", quote[::2])
print("7:", quote[::-1])
print('8:', new_quote)

