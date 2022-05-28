set_1 = (1, 3, 5, 7, 9)
set_2 = (0, 2, 4, 6, 8)
tuple_3 = (set_1[::2] + set_2[1::2])
koniec = list(tuple_3)
print(koniec)

result_set = set(koniec)
print(result_set)