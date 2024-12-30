import os, math, numpy as np

input_file = "/home/alex/Nextcloud (Kopie)/Documents_old/interestingtoread/advent_of_code/2017/input/\
day4_input.txt"

def main():

    data = input()
    if data == "file":
        valid = invalid = 0
        with open(input_file, 'r') as file:
            for line in file.readlines():
                data_sub = (line.strip().split(' '))
                if test_validity(data_sub):
                    valid += 1
                else:
                    invalid += 1
    else:
        data = data.strip().split(' ')
        valid = test_validity(data)

    print("validity:", valid)

def test_validity(inp):
    for i_word in range(len(inp)):
        for i_rest_word in range(len(inp) - i_word - 1):
            # # part 1
            # if inp[i_word] == inp[i_word + i_rest_word + 1]:
            #     return False
            
            # part 2
            if sorted(inp[i_word])== sorted(inp[i_word + i_rest_word + 1]):
                return False
    return True

if __name__ == "__main__":
    main()