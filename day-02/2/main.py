if __name__ == "__main__":
    counter = 0
    lsc = []
    with open('../input.txt', 'r') as file:
        for line in file:
            ls = list(map(int, line.split()))
            print(ls)
            valid = False

            for j in range(len(ls)):
                sp = ls[:j] + ls[j+1:]
                in_ord = (sp==sorted(sp) or sp==sorted(sp, reverse=True))
                fine = True

                for i in range(len(sp) - 1):
                    op = abs(sp[i] - sp[i + 1])
                    if op < 1 or op > 3:
                        fine = False

                if fine and in_ord:
                    print("Hello")
                    valid = True

            if valid:
                counter += 1

    print(counter)
