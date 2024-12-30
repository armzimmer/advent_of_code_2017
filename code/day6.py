import os, math, numpy as np

input_file = "/home/alex/Nextcloud (Kopie)/Documents_old/interestingtoread/advent_of_code/2017/input/\
day6_input.txt"

def main():
    storage = np.array(input().split('\t'), dtype=np.int64)

    print(func(storage))


def func(storage):
    storage_past = []
    cntr = 0
    found = False
    found_i = 0
    
    while True:
        storage_past.append(tuple(storage))
        # # part 1
        # for i in range(len(storage_past) - 1):
        #     if storage_past[i] == storage_past[-1]:
        #         return cntr
        for i in range(len(storage_past) - 1):
            if not found:
                if storage_past[i] == storage_past[-1]:
                    found = True
                    found_i = len(storage_past) - 1
            else:
                if i <= found_i:
                    continue
                if storage_past[found_i] == storage_past[-1]:
                    return cntr


        if found:
            cntr += 1
        
        max_idx = np.argmax(storage)
        max = storage[max_idx]
        storage[max_idx] = 0

        end_idx = max_idx+1+max
        storage[max_idx+1 : end_idx] += 1

        while end_idx >= len(storage):
            end_idx -= len(storage)
            storage[0 : end_idx] += 1
        print(storage)





if __name__ == "__main__":
    main()