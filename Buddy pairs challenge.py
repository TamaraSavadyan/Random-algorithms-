# def buddy(start, limit):
#     s = 0
#     body = []
#     mass = list(range(start, limit + 1))
#     for j in range(0, len(mass)):
#         body[j] = True
#     return body  # "Nothing"


start = int(input("Start: "))
limit = int(input("Limit: "))
divisors = []
sum_n = 0
sum_m = 0
mass = 0
massive = list(range(start, limit + 1))
for k in range(0, len(massive)):
    for i in range(1, massive[k]):
        if massive[k] % i == 0:
            sum_n += i
    divisors.append(sum_n)
    sum_n = 0
for j in range(0, len(divisors)):
    divided = divisors[j] - 1
    for i in range(1, divided):
        if divided % i == 0:
            sum_m += i
    if massive[j] == sum_m - 1:
        bud1 = divided
        bud2 = massive[j]
        buddy = "Buddies"
        break
    else:
        buddy = "Nothing"
if buddy == "Buddies":
    print(bud2, bud1)
else:
    print("Nothing")

# Divisors of 48 are: 1, 2, 3, 4, 6, 8, 12, 16, 24 --> sum: 76 = 75 + 1
# Divisors of 75 are: 1, 3, 5, 15, 25 --> sum: 49 = 48 + 1
# start = int(input("Start: "))
# limit = int(input("Limit: "))
# divisors_num = []
# divisors_sum = []
# sum_n = 0
# massive = list(range(start, limit + 1))
# for k in range(0, len(massive)):
#     for i in range(1, massive[k]):
#         if massive[k] % i == 0:
#             divisors_num.append(i)
#             sum_n += i
#     divisors_sum.append(sum_n)
#     sum_n = 0
# for j in range(0, len(divisors_sum)):
#     for i in range(0, len(divisors_num[i])):
#         if divisors_sum[j] - 1 == divisors_num[i]:
#             buddy = "Buddies"
#             a = divisors_sum[j] - 1
#             b = divisors_num[i]
# print(buddy, "(", a, b, ")")
# print(divisors_sum, "\n", divisors_num)
