m = float(input('Podaj wagę w kg ->'))
w = float(input ('Podaj swój wzrost w m2 ->'))
# 25,0–29,9: nadwaga
# 30,0–34,9: otyłość I stopnia
# 18,5–24,9: waga prawidłowa
# 16,0 – 16,9: wychudzenie
bmi = m / w ** 2

print("Twoje BMI wynosi:", round(bmi, 2))

if bmi > 29.9 and bmi < 34.9:
    print('Nadwaga!')
if bmi > 34.9:
    print('OTYŁOŚĆ!')
if bmi >= 18.5 and bmi <= 24.9:
    print('waga prawidłowa!')
if bmi < 16.9:
    print('Wychudzenie!')

def your_bmi(calculate):
    m = float(input('Podaj wagę w kg ->'))
    w = float(input('Podaj swój wzrost w m2 ->'))
    bmi = m / w ** 2
    return your_bmi(calculate)