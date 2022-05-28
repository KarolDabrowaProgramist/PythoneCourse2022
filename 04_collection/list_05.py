list = [
    ['Adam', 'Małysz', 'Sportowiec'],
    ['Robert', 'Lewandowski', 'Piłkarz'],
    ['Dorota', 'Wellman', 'Dziennikarka'],
    ['Krystyna', 'Janda', 'Aktorka']
]

for row in list:
    for id, value in enumerate(row):
        if id == 1:
            print(value, end=" | ")
        else:
            print(value, end=' ')
    print()


