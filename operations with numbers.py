import math

print("Hello!")
while True:
    try:
        number = int(input("Enter your number "))
    except ValueError:
        print("Incorrect")
        continue
    a = input("Посчитать факториал (1) или квадрат числа (2)? ")
    if a == "1":
        print("Your factorial ", math.factorial(number))
    else:
        print("Your degree ", pow(number, 2))
    b = input("Anything else? (yes)/(no) ")
    if b == "no":
        break
