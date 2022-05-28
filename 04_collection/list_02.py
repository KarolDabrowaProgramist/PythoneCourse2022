numb = (input("Podaj 10 wybranych liczb po przecinku ->"))
numb = numb.replace(',', ' ')
list = (numb)

for each in list:
    if (each % 2) == 0:
        print('fajowo')
