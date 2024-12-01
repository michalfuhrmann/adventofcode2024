def main():
    with open('in.txt', 'r') as f:
        lines = f.readlines()
        l1 = []
        l2 = []
        for line in lines:
            indexes = line.split()
            l1.append(indexes[0])
            l2.append(indexes[1])
        l1 =list(sorted(l1))
        l2=list(sorted(l2))
        sum =0

        for i in range(len(l1)):
            smaller=min(l1[i],l2[i])
            larger=max(l1[i],l2[i])
            sum+=int(larger)-int(smaller)
        print(sum)


if __name__ == '__main__':
    main()
