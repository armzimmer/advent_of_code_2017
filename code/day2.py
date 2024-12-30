import os, math

input_file = "/home/alex/Nextcloud (Kopie)/Documents_old/interestingtoread/advent_of_code/2017/input/\
day2_input.txt"

def main():
    res = 0
    data = input()
    if data == "file":
        data = []
        with open(input_file, 'r') as file:
            # read two-dim input with tabs
            for line in file.readlines():
                data_sub = (line.strip().split('\t'))
                data_sub = [float(x) for x in data_sub]
                data.append(data_sub)

                # part 1
                res += max(data_sub) - min(data_sub)

                # part 2
                for i in range(len(data_sub) - 1):
                    for j in range(len(data_sub) - i - 1):
                        diff1 = data_sub[i] / data_sub[i+j+1]
                        diff2 = data_sub[i+j+1] / data_sub[i]
                        if diff1 == math.floor(diff1):
                            res += diff1
                        if diff2 == math.floor(diff2):
                            res += diff2
                

    # print(data)


    # for i in range(len(data)):
    #     if data[i] == data[(i+len(data)//2) % len(data)]:
    #         res += int(data[i])
    
    print(res)



if __name__ == "__main__":
    main()