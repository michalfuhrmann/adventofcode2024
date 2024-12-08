import itertools

from pandas._libs.parsers import defaultdict

def main():
    sum=0
    with open('in.txt', 'r') as f:
        lines = f.readlines()
        rows = len(lines)
        cols = len(lines[0].strip())
        antinodes_map = [['_' for _ in range(cols)] for _ in range(rows)]
        print(antinodes_map)
        dict_antenns= defaultdict(list)
        for col_i in range(0, cols):
            for row_i in range(0, rows):
                char = lines[row_i][col_i]
                if char.isalnum():
                    dict_antenns[char].append((row_i,col_i))
                    antinodes_map[row_i][col_i] = char

        for key in dict_antenns:
            print(key)
            combinations = itertools.combinations(dict_antenns[key], 2)
            for a1,a2 in combinations:

                    (x1, y1), (x2, y2) = a1, a2
                    a = (y2 - y1) / (x2 - x1)
                    b = y1 - a * x1
                    for x in range(rows):
                        y = round(a * x + b,4)
                        if y.is_integer() and 0 <= y < cols:
                            antinodes_map[int(x)][ int(y)] = '#'

                    for y in range(cols):
                        if a != 0:
                            x =round( (y - b) / a,4)
                            if x.is_integer() and 0 <= x < rows:
                                antinodes_map[int(x)][ int(y)] = '#'

            sum=0
            for row in antinodes_map:
                print(row)
                for char in row:
                    if char == '#':
                        sum+=1
            print(sum)





if __name__ == '__main__':
    main()