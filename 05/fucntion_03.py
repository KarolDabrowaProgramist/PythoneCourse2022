# Nie korzystając z funkcji wbudowanej max(),
# napisz funkcję znajdującą maksymalną wartość z 3 liczb. maximum_of(a, b, c).

def min_of_two(wart1, wart2):
    return wart1 if wart1 < wart2 else wart2


def minimum_of_two(a, b, c):
    return min_of_two(c, min_of_two(a, b))


def main():
    result = minimum_of_two(90, 16, 44)
    print(result)

main()
