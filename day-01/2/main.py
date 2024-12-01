if __name__ == "__main__":
    ls1 = []
    ls2 = []
    with open('../input.txt', 'r') as file:
        for line in file:
            sp = line.split()
            ls1.append(float(sp[0]))
            ls2.append(float(sp[1]))

    ls1 = list(tuple(ls1))

    d = dict.fromkeys(ls1, 0)

    for n in ls2:
        if d.get(n) != None:
            d[n] += 1
        
    total = 0

    for key, val in d.items():
        total += key * val

    print(total)

