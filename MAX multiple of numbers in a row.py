print("Welcome to Aplle Company!\n")
print("Enter your list of numbers\n")
print("When you're done pls enter N\n")
numbers = list()
item = ""
while item.strip().lower() != "n":
    item = input()  # num = item.split(" ")
    try:
        numbers = list(map(float, item.split(" ")))  # numbers.append(map(float, num))
    except ValueError:
        print("Incorrect")
# numbers = [12, 32, 45, 67, -123, 1, -2, 43, -45, 100]
if numbers:
    numbers.sort()
    First_Two_Numbers_Multiple_And_One_Last = numbers[0] * numbers[1] * numbers[-1]
    Last_Three_Numbers_Multiple = numbers[-1] * numbers[-2] * numbers[-3]

    if First_Two_Numbers_Multiple_And_One_Last > Last_Three_Numbers_Multiple:
        print("Your numbers:", numbers[0], numbers[1], numbers[-1], "And your MAX multiple is:",
              First_Two_Numbers_Multiple_And_One_Last)
    else:
        print("Your numbers:", numbers[-1], numbers[-2], numbers[-3], "And your MAX multiple is:",
              Last_Three_Numbers_Multiple)
else:
    print("You didn't give me numbers :(")
