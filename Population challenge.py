def nb_year(p0, percent, aug, p):
    normal_percent = percent / 100
    year = 0
    while p0 < p:
        p0 = p0 + p0 * normal_percent + aug
        year += 1
    return print("It will need", year, "entire years.")


nb_year(1000, 2, 50, 1200)
nb_year(1500, 5, 100, 5000)
nb_year(1500000, 2.5, 10000, 2000000)
nb_year(1500000, 0.25, 1000, 2000000)