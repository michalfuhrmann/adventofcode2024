import re

XMAS_CHARS = ["X", "M", "A", "S"]


directions = [
        (0, 1),
        (0, -1),
        (1, 0),  
        (-1, 0),
        (1, 1),
        (1, -1),
        (-1, 1),
        (-1, -1)
    ]
word = "XMAS"
word_len = len(word)


def is_valid(r, c, direction,rows,cols,lines):
    dr, dc = direction
    for i in range(word_len):
        next_row = r + dr * i
        next_col = c + dc * i
        if next_row < 0 or next_col < 0 or next_row >= rows or next_col >= cols or lines[next_row][next_col] != word[i]:
            return False
    return True


def main():
    with open('in.txt', 'r') as f:
        lines = f.readlines()
        rows = len(lines)
        cols = len(lines[0].strip())
        found = 0
        for col_i in range(0, cols):
            for row_i in range(0, rows):
                for direction in directions:
                    if is_valid(row_i, col_i, direction,rows,cols,lines):
                        found += 1

        print(found)


if __name__ == '__main__':
    main()
