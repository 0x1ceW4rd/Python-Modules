def ft_count_harvest_iterative():
    countto = int(input("Days until harvest: "))
    r = range(1, countto)
    for n in r:
        print(f"Day {n}")
    print(f"Day {countto}")
    print("Harvest time!")
