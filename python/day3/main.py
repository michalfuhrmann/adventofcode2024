import re

mul_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"


def search_section(text, start, end):
    matches = re.findall(mul_pattern, text[start:end])
    mul_sum = 0
    for d1, d2 in matches:
        mul_sum += int(d1) * int(d2)
    return mul_sum

def main():
    with open('in.txt', 'r') as f:
        lines = f.readlines()
        text = "".join(lines)
        enable_op = "do()"
        disable_op = "don't()"

        sum = 0
        mul_enabled = True
        last_section_start =0
        for i in range(0, len(text)):
            if mul_enabled:
                if i+len(disable_op)< len(text) and text[i: i+len(disable_op)] == disable_op:
                    mul_enabled = False
                    sum += search_section(text, last_section_start, i)
                    last_section_start= i
            else:
                if i+len(enable_op)< len(text) and text[i: i+len(enable_op)] == enable_op:
                    mul_enabled = True
                    last_section_start = i

        if mul_enabled:
            sum += search_section(text, last_section_start, len(text))

        print(sum)



if __name__ == '__main__':
    main()
