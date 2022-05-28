days = {'Jan': 31, 'Feb': 28, 'Mar': 31, 'Apr': 30, 'May': 31, 'Jun': 30, 'Jul': 31, 'Aug': 31, 'Sept': 30}
month = days.values()

print(list(set(month)))

for row in set(month):
    print(row)