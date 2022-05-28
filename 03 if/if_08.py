n1 = int(input("Podaj pierwszą liczbę ->"))
n2 = int(input("Podaj drugą liczbę ->"))
n3 = int(input('Podaj trzecią liczbę ->'))

list = []

if n1 > n2 and n1 > n3:
    list.insert(1, n1)
    list.insert(2, n2)
    list.insert(3, n3)
    print(list)
elif n2 > n1 and n1 > n3:
    list.insert(1, n2)
    list.insert(2, n1)
    list.insert(3, n3)
    print(list)
elif n3 > n1 and n2 > n1:
    list.insert(1, n3)
    list.insert(2, n2)
    list.insert(3, n1)
    print(list)
