import itertools

from pandas._libs.parsers import defaultdict


def append(number, length):
    result = []
    for i in range(length):
        result += [str(number)]
    return result


def swap(arr, i, j, size_of_digit=1):
    for k in range(size_of_digit):
        temp = arr[i + k]
        arr[i + k] = arr[j + k]
        arr[j + k] = temp
    return arr


def main():
    sum = 0
    with open('in.txt', 'r') as f:
        line = f.read().strip()
        print(line)
        id = 0
        output_raw = []
        isFile = True
        for c in line.strip():
            if isFile:
                size = int(c)
                output_raw += append(id, size)
                id += 1
                isFile = False
            else:
                size = int(c)
                output_raw += append(".", size)
                isFile = True

        print("".join(output_raw))

        space_index = 0
        file_index = len(output_raw) - 1
        size_of_digit = 0
        size_of_space = 0
        current_digit = None

        while file_index >= 0:
            size_of_digit = 0
            size_of_space = 0
            space_index = 0
            if not  output_raw[file_index].isdigit():
                file_index -=1
                continue
            if current_digit is None:
                current_digit = output_raw[file_index]
            else:
                current_digit = new_digit

            while output_raw[file_index].isdigit() and output_raw[file_index] == current_digit:
                # size_of_digit += len(str(current_digit))
                size_of_digit += 1
                file_index -= 1

            new_digit = output_raw[file_index]


            if current_digit and current_digit.isdigit():
                while space_index <= file_index:
                    if not output_raw[space_index].isdigit():
                        size_of_space += 1
                    else:
                        size_of_space=0
                    space_index += 1

                    if size_of_space >= size_of_digit:
                        swap(output_raw, file_index + 1, space_index - size_of_space , size_of_digit)
                        size_of_digit = 0
                        size_of_space = 0
                        break


            # print(f"{space_index} {file_index} ")


        print("".join(output_raw))
        sum += 0
        for i in range(len(output_raw)):
            if output_raw[i].isdigit():
                sum += int(output_raw[i]) * i

        print(sum)


if __name__ == '__main__':
    main()
