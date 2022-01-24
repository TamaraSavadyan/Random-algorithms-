def find_prime(integers):
    numbers = []
    num = 0
    prime = 0
    for i in range(0, len(integers)):
        if integers[i] < 0:
            for j in range(integers[i] - 1, 0):
                if integers[i] % j == 0:
                    num += 1
        else:
            for j in range(1, integers[i] + 1):
                if integers[i] % j == 0:
                    num += 1
        numbers.insert(i, num)
        num = 0
    for k in range(0, len(numbers)):
        if numbers[k] <= 2:
            number_prime = integers[k]
            prime += 1
        else:
            number_normal = integers[k]
            num += 1
    if num > prime:
        return print(number_prime, "\t", numbers)
    else:
        return print(number_normal, "\t", numbers)


def find_outlier(integers):
    numbers = []
    even = 0
    odd = 0
    for i in range(0, len(integers)):
        if integers[i] % 2 == 0:
            numbers.append(1)
        else:
            numbers.append(0)
    for j in range(0, len(numbers)):
        if numbers[j] == 1:
            even += 1
            answer_even = integers[j]
        else:
            odd += 1
            answer_odd = integers[j]
    if even > odd:
        return print(answer_odd, "\t", numbers)
    else:
        return print(answer_even, "\t", numbers)


integers = [78, 48, 6, 24, -67, 90, 1052, 1710, 906, 124568, 4, 324, 506]
integers1 = [7, 3, 17, 19, 11, 13, 23, -160, 123127, 79, 61, 4567, 1]
find_prime(integers)
find_outlier(integers1)
# t = 1
# while t == 1:
#     try:
#         number = int(input("Enter your number "))
#     except ValueError:
#         print("Incorrect")
#         continue
#     numb_list = []
#     numb = 0
#     for j in range(1, number + 1):
#         if number % j == 0:
#             numb += 1
#             print(j)
#     if numb > 2:
#         print("Number is even")
#     else:
#         print("Number is odd")
#     t = input("Again? (1)/(2) ")
