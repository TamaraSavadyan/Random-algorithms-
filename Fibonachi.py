# n = int(input())
# s = []
# a = k = 0
# b = 1
# while s[:k] != s[k:] or k < 1:
#    s += [a % n]
#    k = len(s) / 2
#    a, b = b, a + b
# print(k)

n = int(input("Enter № "))
numbersOfFibonachi = [1, 1]
remainders = [1, 1]
for i in range(0, n - 2):
    k = numbersOfFibonachi[i] + numbersOfFibonachi[i + 1]
    numbersOfFibonachi.append(k)
    remainders.append(k % 4)
print(numbersOfFibonachi)
print(remainders)
