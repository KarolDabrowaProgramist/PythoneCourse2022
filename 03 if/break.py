sum_grades = 0
for i in range(3):
    subject = input("Przedmiot szkolny: ", )
    grade = int(input(f"Podaj ocenę z {subject} -> "))
    print(f'Ocena z {subject} to {grade}')
    sum_grades += grade
print('Twoja średnia ocen z 3 przedmiotów to ->', {round(sum_grades/3, 2)})
