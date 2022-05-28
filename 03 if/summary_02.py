text = input('Podaj dowolny tekst ->')
#sposób z string slicing
print('->', text[::2])
#sposób z pętlą
for i, letter in enumerate(text):
    if i % 2 == 0:
        print(letter)


