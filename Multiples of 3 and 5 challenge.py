def solution(number):
    sum = 0
    h = 0
    if number is not None:
        for k in range(1, number):
            if k % 3 == 0 or k % 5 == 0:
                sum += k
                h += 1
    return print("The sum is", sum, "amount of numbers:", h)


solution(1)
#3 5 6 9 10 12 15! 18 20 21 24 25 27 30
