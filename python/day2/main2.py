def main():
    with open('in.txt', 'r') as f:
        lines = f.readlines()

    count = 0
    for line in lines:
        levels = [int(i) for i in line.split()]

        if is_level_ok(count, levels):
            count += 1
        else:
            for i in range(0, len(levels)):
                levels_bad = list(levels)
                levels_bad.pop(i)
                if is_level_ok(count, levels_bad):
                    print("done with dampener")
                    count += 1
                    break
    print(count)


def is_level_ok(count, levels):
    prev = levels[0]
    ordering = 0
    level_count = 1
    for level in levels[1:]:
        if ordering == 0:
            if level > prev and level <= prev + 3:
                ordering = 1
                level_count += 1
            elif level < prev and level >= prev - 3:
                ordering = -1
                level_count += 1
            else:
                break
        elif ordering == 1 and level > prev and level <= prev + 3:
            level_count += 1
        elif ordering == -1 and level < prev and level >= prev - 3:
            level_count += 1
        else:
            break
        if level_count == len(levels):
            count += 1
            print(levels)
            return True
        prev = level
    return False


if __name__ == '__main__':
    main()