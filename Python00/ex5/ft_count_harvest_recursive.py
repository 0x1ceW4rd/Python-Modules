def ft_count_harvest_recursive():
    countto = int(input("Days until harvest: "))
    ft_count_days(1, countto)


def ft_count_days(day, countto):
    if day == countto:
        print(f"Day {day}")
        print("Harvest time!")
        return
    print(f"Day {day}")
    ft_count_days(day + 1, countto)
