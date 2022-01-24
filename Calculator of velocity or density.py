import math
import random

Amplitudes_bottom = []
Amplitudes_multiple = []

sum_bottom = 0
sum_multiple = 0

comparator = []
k = 100
length = 10
for h in range(0, k):
    for j in range(0, length):
        Amplitudes_bottom.append(random.random())
        Amplitudes_multiple.append(random.random())

    Amplitudes_bottom.sort()
    Amplitudes_multiple.sort()
    Peak_bottom = Amplitudes_bottom[-1]
    Peak_multiple = Amplitudes_multiple[-1]

    for i in range(0, len(Amplitudes_bottom)):
        sum_bottom += math.pow(Amplitudes_bottom[i], 2)
    RMS_bottom = math.sqrt(sum_bottom / len(Amplitudes_bottom))

    for i in range(0, len(Amplitudes_multiple)):
        sum_multiple += math.pow(Amplitudes_multiple[i], 2)
    RMS_multiple = math.sqrt(sum_multiple / len(Amplitudes_multiple))

    # print("Amplitudes_multiple", Amplitudes_multiple, "Amplitudes_bottom", Amplitudes_bottom)
    # print(RMS_multiple, RMS_bottom, Peak_multiple, Peak_bottom)
    # print(RMS_multiple/RMS_bottom, "\t", Peak_multiple/Peak_bottom)

    if RMS_multiple / RMS_bottom > Peak_multiple / Peak_bottom:
        compare = 4  # print(4)  #
    else:
        compare = 5  # print("\t", 5)  #
    comparator.append(compare)
count_1 = 0
count_2 = 0
for i in range(0, len(comparator)):
    if comparator[i] % 4 == 0:
        count_1 += 1
    else:
        count_2 += 1

print("RMS:", count_1, "Peak:", count_2)
# def calculate(V1, p1, p2):
#     # maK = (v2p2-v1p1)/(v2p2 + v1p1)1
#     return V2
# V1 = 1500
# V2 = 0
# p1 = 1
# p2 = 2
