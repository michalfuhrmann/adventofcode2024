
def swap_numbers(indexof,idx,numbers):
    temp = numbers[indexof]
    numbers[indexof] = numbers[idx]
    numbers[idx] = temp
    return numbers

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

        print(updates)

        to_return = []
        for numbers in updates:
            valid =True
            idx=0
            while idx != len(numbers):
                number = numbers[idx]
                if number in orderings :
                    print(f"processing number {number}")
                    for value in orderings[number]:
                        if value  in set(numbers[:idx]) :
                            indexof = numbers.index(value)
                            swap_numbers(indexof,idx,numbers)
                            print(numbers, idx, indexof,number)
                            valid =False
                            idx = min(idx,indexof)
                            print(f"setting index to {idx}")
                            continue
                idx+=1

            if not valid:
                to_return.append(numbers[int(len(numbers)/2)])


    print(orderings)
    print(updates)

    print(to_return)
    print(sum([int(i) for i in to_return]))
if __name__ == '__main__':
    main()
