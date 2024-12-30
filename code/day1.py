input_file = "/home/alex/Nextcloud (Kopie)/Documents_old/interestingtoread/advent_of_code/2017/input/\
day1_input.txt"

def main():
    # data = input()
    with open(input_file, 'r') as file:
        data = file.read().rstrip()
    # print(data)

    res = 0

    # # part 1
    # for i in range(len(data)):
    #     if data[i] == data[(i+1) % len(data)]:
    #         res += int(data[i])

    # part 2
    for i in range(len(data)):
        if data[i] == data[(i+len(data)//2) % len(data)]:
            res += int(data[i])
    
    print(res)



if __name__ == "__main__":
    main()