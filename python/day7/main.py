
def operation (a,b,operator):
    if operator == "+":
        return a+b
    if operator == "*":
        return a*b
    if operator == "||":
        return  int(str(a) + str(b))
OPERATIONS= ["+","*", "||"]
def main():
    sum=0
    with open('in.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            result =int(line.split(":")[0].strip())
            values = [n.strip() for n in line.split(":")[1:]]
            valuess_split = [int(n) for n in values[0].split(" ")]
            print(result, valuess_split)

            idx =1
            prev_results = [valuess_split[0]]
            while idx < len(valuess_split):
                new_results = []
                current = valuess_split[idx]
                for operator in OPERATIONS:
                    for prev in prev_results:
                        new_results.append(operation(prev,current,operator))
                idx+=1
                prev_results = new_results

            for computed_resukt in prev_results:
                if computed_resukt == result:
                    sum+=computed_resukt
                    break

            print(sum)





if __name__ == '__main__':
    main()