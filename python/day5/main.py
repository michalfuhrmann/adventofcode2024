def main():
    with open('in.txt', 'r') as f:
        lines = f.readlines()
        orderings = {}
        updates = []
        for line in lines:
            if "|" in line:
                k,v = line.split("|")
                if k.strip() in orderings:
                    orderings[k.strip()] = list(sorted(orderings[k.strip()] + [v.strip()]))
                else:
                    orderings[k.strip()] = [v.strip()]
            else:
                if "," in line:
                    updates.append([k.strip() for k in line.split(",")])

        to_return = []
        for numbers in updates:
            valid =True
            for idx,number in enumerate(numbers):
                if number in orderings :
                    for value in orderings[number]:
                        if value  in set(numbers[:idx]) :
                            valid =False
                            break
            if valid:
                to_return.append(numbers[int(len(numbers)/2)])


    print(orderings)
    print(updates)

    print(to_return)
    print(sum([int(i) for i in to_return]))
if __name__ == '__main__':
    main()
