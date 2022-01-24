from tkinter import *

root = Tk()
root.title("Графическая программа на Python")
root.geometry("600x500")
# root.mainloop()

import matplotlib.pyplot as plt

NumberOfSubwayCars = [9, 7, 5, 12, 10, 10, 11, 1, 8, 8, 9, 7, 8, 9, 7, 8, 5, 8, 8, 8, 8, 7, 7]
NumberOfSubwayCars.sort()
a = len(NumberOfSubwayCars)
Intervals = []
Counts = dict()
Plot = []
SubPlot = []
for i in range(0, 15):
    Intervals.append(i)
    Plot.append(0)
    if 2 < i < 13:
        SubPlot.append(8)
        continue
    SubPlot.append(0)
for i in NumberOfSubwayCars:
    Counts.setdefault(i, NumberOfSubwayCars.count(i))
for key in Counts.keys():
    Plot[key] = Counts[key]
fig, ax = plt.subplots()
ax.set_title("Гистограмма распределения количества вагонов")
ax.set_xlabel("Количество вагонов")
ax.set_ylabel("Количество ответов")
ax.set_xticks(Intervals)
ax.fill(Intervals, SubPlot, color='#ffe7af', label='Область 3-х сигм\nσ = 2.21\nδ = 4.88')
ax.hist(NumberOfSubwayCars, bins=Intervals, align='left', color='#3888ff', label='Гистограмма')
ax.plot(Plot, color='#000', label='График')
ax.legend(loc=2)
plt.show()

