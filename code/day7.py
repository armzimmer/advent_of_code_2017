import os, math, numpy as np

input_file = "/home/alex/Nextcloud (Kopie)/Documents_old/interestingtoread/advent_of_code/2017/input/\
day7_input.txt"

def main():
    # part 1 (part 2 in file day7_part2.py)
    with open(input_file, 'r') as file:
        lines = file.readlines()
        max_depth = 0
        max_value_line = 0

        for line_no, line in enumerate(lines):
            if "->" in line:
                depth = get_depth(line_no, lines)
                if max_depth < depth:
                    max_depth = depth
                    max_value_line = line_no
        
        print("bottom program is called:", lines[max_value_line].split()[0])

def get_depth(line_no, lines):
    leaf_programs = get_leaf_programs(line_no, lines) # returns list of programs
    for program in leaf_programs:
        program_line_no = find_line_no(program, lines)
        d = get_depth(program_line_no, lines) # where to add recursive depth (+1)?
        return d+1
    return 0

def find_line_no(program_name, lines):
    for line_no, line in enumerate(lines):
        local_name = line.split()[0]
        if local_name == program_name:
            return line_no
    return program_name + " couldnt be found!"

def get_leaf_programs(line_no, lines):
    line = lines[line_no]
    leaf_programs = line.replace(',', '').replace('\n', '').split()[3:]
    return leaf_programs # a.split() = ['sxijke', '(987)', '->', 'dlzlo,', 'jlsxjq,', 'jmazezm']




if __name__ == "__main__":
    main()