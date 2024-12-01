if __name__ == "__main__":
    ls1 = []
    ls2 = []
    with open('../input.txt', 'r') as file:
        for line in file:
            sp = line.split()
            ls1.append(float(sp[0]))
            ls2.append(float(sp[1]))

    ls1.sort()
    ls2.sort()

    dis = 0

    for i, _ in enumerate(ls1):
        dis += abs(ls1[i] - ls2[i])

    print(dis)
