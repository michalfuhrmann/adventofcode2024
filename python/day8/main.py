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

        for key in dict_antenns:
            print(key)
            combinations = itertools.combinations(dict_antenns[key], 2)
            for a1,a2 in combinations:
                diff = (a2[0]-a1[0], a2[1]-a1[1])
                antinode_1 = (a1[0] - diff[0], a1[1] - diff[1])
                antinode_2 = (a2[0] + diff[0], a2[1] + diff[1])
                if antinode_1[0] >= 0 and antinode_1[0] < rows and antinode_1[1] >= 0 and antinode_1[1] < cols:
                    antinodes_map[antinode_1[0]][antinode_1[1]] = '#'
                if antinode_2[0] >= 0 and antinode_2[0] < rows and antinode_2[1] >= 0 and antinode_2[1] < cols:
                    antinodes_map[antinode_2[0]][antinode_2[1]] = '#'

            sum=0
            for row in antinodes_map:
                for char in row:
                    if char == '#':
                        sum+=1
            print(sum)





if __name__ == '__main__':
    main()