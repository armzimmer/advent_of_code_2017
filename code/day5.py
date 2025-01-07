import os, math, numpy as np

input_file = "/home/alex/Nextcloud (Kopie)/Documents_old/interestingtoread/advent_of_code/2017/input/\
day5_input.txt"

def main():
    with open(input_file, 'r') as file:
        jumps = []
        for line in file.readlines():
            jumps.append(int(line))

        print("file:", jumps)

        pose = 0
        cntr = 0

        # update pose, value+=1
        while pose >= 0 and pose < len(jumps):
            if jumps[pose] < 3: # and jumps[pose] > -3
                # part 1: only use the contents of this if-case
                new_pose = pose + jumps[pose]
                jumps[pose] += 1
            else:
                new_pose = pose + jumps[pose]
                jumps[pose] -= 1
            pose = new_pose
            cntr += 1
        
        print("after", cntr, "jumps we got out!")



if __name__ == "__main__":
    main()