def calculator():
    again = "да"
    usd_rate = 75
    euro_rate = 80
    print("Добро пожаловать в деньгообменник!")
    while again.lower() == "да":
        try:
            cash = float(input("Введите сумму: "))
        except ValueError:
            print("Введите сумму числом, а не словами")
            continue
        while True:
            value = input("Выберите валюту (доллар/евро): ")
            if value == "доллар":
                money = round(cash / usd_rate, 2)
                print("Вы внесли", cash, "\nВаша сумма", money)
                break
            if value == "евро":
                money = round(cash / euro_rate, 2)
                print("Вы внесли", cash, "\nВаша сумма", money)
                break
            else:
                print("Введите именно указанные валюты, а никакие другие")
                continue
        again = input("Желаете перевести ещё одну сумму? (да/нет) ")


def main():
    calculator()


if __name__ == "__main__":
    main()
