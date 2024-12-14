import itertools

from pandas._libs.parsers import defaultdict
def append ( number,length):
    result = []
    for i in range(length):
        result+=[str(number)]
    return result
def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
    return arr

def main():
    sum=0
    with open('in.txt', 'r') as f:
        line = f.read()
        print(line)
        id =0
        output_raw = []
        isFile=True
        for c in line.strip():
            if isFile:
                size=int(c)
                output_raw+=append(id,size)
                id+=1
                isFile=False
            else:
                size=int(c)
                output_raw+=append(".",size)
                isFile=True

        print("".join(output_raw))

        space_index=0
        file_index=len(output_raw)-1
        while space_index<file_index:
            if not output_raw[file_index].isdigit():
                file_index-=1
            if output_raw[space_index]!=".":
                space_index+=1
            if output_raw[file_index].isdigit() and output_raw[space_index]==".":
                swap(output_raw,file_index,space_index)



        print("".join(output_raw))
        sum+=0
        for i in range(len(output_raw)):
            if output_raw[i].isdigit():
                sum+=int(output_raw[i])*i

        print(sum)



if __name__ == '__main__':
    main()