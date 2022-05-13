
sentence = input('Podaj przykład Palindromu ->')

print('Czy twoje zdanie jest Palindromem?', (sentence[::1] == sentence[-1::-1]))