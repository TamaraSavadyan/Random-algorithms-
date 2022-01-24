import account  # модули

# hello
name = input("Enter your name: ")
print("Hi,", name)
# расчёт факториала
again = "yes"
while again.lower() == "yes":
    try:
        number = int(input("Enter your number and I'll calculate factorial: "))
    except ValueError:
        print("NUMBER, not word")
        continue
    factorial = 1
    for i in range(1, number + 1):
        factorial *= i
        i += 1
    print("Your number:", number, "\nit's factorial:", factorial)
    again = input("Do you want to continue? Type yes or no: ")
# кортежи
countries = (
    ("Germany", 80.2, (("Berlin", 3.326), ("Hamburg", 1.718))),
    ("France", 66, (("Paris", 2.2), ("Marsel", 1.6)))
)

for country in countries:
    countryName, countryPopulation, cities = country
    print("\nCountry: {}  population: {}".format(countryName, countryPopulation))
    for city in cities:
        cityName, cityPopulation = city
        print("City: {}  population: {}".format(cityName, cityPopulation))
# модули
account.calculator()
