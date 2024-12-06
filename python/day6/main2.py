obstacle = "#"
guard = "^"
def replacer(s, newstring, index, nofail=False):
    if not nofail and index not in range(len(s)):
        raise ValueError("index outside given string")

    if index < 0:
        return newstring + s
    if index > len(s):
        return s + newstring

    return s[:index] + newstring + s[index + 1:]
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
def simulate_movement(r, c, rows, cols, lines):
    movement_list = [(-1,0), (0, 1), (1, 0), (0, -1)]
    movement_idx = 0
    move = movement_list[movement_idx]
    loop=False
    turns_done= 0
    old_turns_positions = set()

    while r < rows  and r>=0 and c < cols and c>=0:

        new_move_r = r + move[0]
        new_move_c = c + move[1]
        if new_move_r >= rows or new_move_r < 0 or new_move_c >= cols or new_move_c < 0:
            loop=False
            break
        if  lines[new_move_r][new_move_c] == obstacle:
            move = movement_list[movement_idx % len(movement_list)]
            movement_idx+=1
            if (new_move_r, new_move_c) not in old_turns_positions:
                turns_done=0
            if (new_move_r,new_move_c) in old_turns_positions and turns_done==4:
                loop=True
                break
            else:
                turns_done+=1
                old_turns_positions.add((new_move_r,new_move_c))
            continue
        r,c  = new_move_r, new_move_c

    return loop
def main():
    with open('in.txt', 'r') as f:
        lines = f.readlines()
        rows = len(lines)
        cols = len(lines[0].strip())
        r_a, c_a = (0, 0)
        for r_a in range(rows):
            for c_a in range(cols):
                if lines[r_a][c_a] == guard:
                    break
            if lines[r_a][c_a] == guard:
                break

        print(r_a, c_a)
    loops_count =0
    for r in range(rows):
        for c in range(cols):
            lines_with_sim= lines.copy()
            if lines_with_sim[r][c] != obstacle   and lines_with_sim[r][c] != guard:
                lines_with_sim[r]=replacer(lines_with_sim[r],obstacle,c)
                if simulate_movement(r_a, c_a, rows, cols, lines_with_sim):
                    loops_count+=1

    print(loops_count)





if __name__ == '__main__':
    main()
