poem = """Szybko, zbudź się, szybko, wstawaj
Szybko, szybko, stygnie kawa
Szybko, zęby myj i ręce"""
poem = poem.replace(',',' ')
poem = poem.lower()
tab = poem.split()
print(tab)

words_counter = {}

for word in tab:
    if word in words_counter:
        words_counter[word] += 1
    else:
        words_counter[word] = 1

for k, v in words_counter.items():
    print(f'- {k} : {v}')