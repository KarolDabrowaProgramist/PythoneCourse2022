#
#used_fuel = 6.2
#distance = 120
#price_fuel = 5.04
#
#cost_of_journey = ((used_fuel * distance) / 100) * price_fuel
#print("Koszt wyprawy wynosi: ", round(cost_of_journey,2), 'zł')

used_fuel = float(input("Spalanie paliwa ->"))
distance = float(input('Przejechana odległość[km] ->'))
fuel_price = float(input('Aktualna cena paliwa[zł] ->'))
cost_of_journey = used_fuel * distance * fuel_price / 100
print('Koszt wycieczki to:', round(cost_of_journey,2), 'zł')