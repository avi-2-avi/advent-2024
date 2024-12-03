if __name__ == "__main__":
    counter = 0
    with open('../input.txt', 'r') as file:
        for line in file:
            valid = True
            ls = []
            sp = line.split()

            for i in sp:
                ls.append(float(i))

            isPos = 1 if ls[1] >= ls[0] else -1

            for i, _ in enumerate(ls):
                if i > 0:
                    op = isPos*(ls[i] - ls[i - 1])
                    if op < 1 or op > 3:
                        valid = False

            if valid != False:
                counter += 1 

    print(counter)
