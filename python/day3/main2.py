import re

def main():
    with open('in.txt', 'r') as f:
        lines = f.readlines()

        pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
        sum=0
        for line in lines:
            matches = re.findall(pattern, line)
            for d1,d2 in matches:
                sum+=int(d1)*int(d2)

        print(sum)


if __name__ == '__main__':
    main()
