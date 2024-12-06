
def is_x_mas(r, c, rows, cols, lines):
    if lines[r][c] != "A":
        return False
    mas1= lines[r-1][c-1]+lines[r+1][c+1]
    mas2= lines[r-1][c+1]+lines[r+1][c-1]


    return   all([mas in ['MS',"SM"] for mas in [mas1,mas2]])


def main():
    with open('in.txt', 'r') as f:
        lines = [line.strip() for line in f.readlines()]
        rows = len(lines)
        cols = len(lines[0].strip())
        found = 0

        for r in range(1,rows-1):
            for c in range(1,cols-1):
                if is_x_mas(r, c, rows, cols, lines):
                    found += 1

        print(found)


if __name__ == '__main__':
    main()
