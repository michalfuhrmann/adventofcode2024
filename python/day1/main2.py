def main():
    with open('in.txt', 'r') as f:
        lines = f.readlines()
        l1 = []
        l2 = []
        for line in lines:
            indexes = line.split()
            l1.append(indexes[0])
            l2.append(indexes[1])
        occurences = {}
        for el in l2:
            if el not in occurences:
                occurences[el] = 0
            occurences[el] += 1

        sum=0
        for el in l1:
            if el not in occurences:
                factor= 0
            else:
                factor = int(occurences[el])
            sum += factor*int(el)
        print(sum)

if __name__ == '__main__':
    main()
