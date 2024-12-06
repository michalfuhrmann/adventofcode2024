obstacle = "#"
guard = "^"

def count_visited(array, rows, cols):
    count = 0
    for r in range(rows):
        for c in range(cols):
            if array[r][c] == 1:
                count += 1
    print(count)
def print_array(array, rows, cols):
    for r in range(rows):
        for c in range(cols):
            print(array[r][c], end="")
        print()
def next_move(r, c, rows, cols, lines, array):
    return r + move[0], c + move[1]
def simulate_movement(r, c, rows, cols, lines, array):
    movement_list = [(-1,0), (0, 1), (1, 0), (0, -1)]
    movement_idx = 0
    move = movement_list[movement_idx]

    while r < rows  and r>=0 and c < cols and c>=0:
        array[r][c] = 1

        if r + move[0] >= rows or r + move[0] < 0 or c + move[1] >= cols or c + move[1] < 0:
            break
        if  lines[r+move[0]][c+move[1]] == obstacle:
            move = movement_list[movement_idx % len(movement_list)]
            movement_idx+=1
            continue
        r,c  = r + move[0], c + move[1]
        # print_array(array, rows, cols)
        # print("----")
        # print("----")


def main():
    with open('in-test.txt', 'r') as f:
        lines = f.readlines()
        rows = len(lines)
        cols = len(lines[0].strip())
        r, c = (0, 0)
        for r in range(rows):
            for c in range(cols):
                if lines[r][c] == guard:
                    break
            if lines[r][c] == guard:
                break

        print(r, c)

    array = [[0 for i in range(cols)] for j in range(rows)]

    simulate_movement(r, c, rows, cols, lines, array)

    count_visited (array, rows, cols)


if __name__ == '__main__':
    main()
