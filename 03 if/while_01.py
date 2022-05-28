fahr = 0
while fahr <= 200:
    celc = 5/9 * (fahr - 32)
    print(f'{fahr} st F -> {round(celc, 1)} st C')
    fahr += 20