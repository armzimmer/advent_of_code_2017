import os, math, numpy as np

input_file = "/home/alex/Nextcloud (Kopie)/Documents_old/interestingtoread/advent_of_code/2017/input/\
day7_input.txt"

def main():
    with open(input_file, 'r') as file:
        lines = file.readlines()
        balanced = True

        for line_no, line in enumerate(lines):
            if "->" in line:
                balanced = check_balanced(line_no, lines)[0]
                if not balanced:
                    return


def check_balanced(line_no, lines):
    weight_old_prog = get_prog_weight(line_no, lines)
    leaf_programs = get_leaf_programs(line_no, lines)
    leaf_programs_balance_vals = [] # make sure all the leaf programs have the same balance, collect in here
    if leaf_programs == []:
        return True, weight_old_prog
    
    for leaf_prog in leaf_programs:
        balanced, balance_val = check_balanced(get_line_no(leaf_prog, lines), lines)
        if not balanced:
            return False, -1
        leaf_programs_balance_vals.append(balance_val)
    different_values = list(set(leaf_programs_balance_vals))
    if len(different_values) == 1: # all programs have the same weight, so balanced
        print("balanced :)")
        print("line: ", lines[line_no].replace('\n', ''))
        print(leaf_programs_balance_vals, "\n")
        return True, len(leaf_programs) * different_values[0] + weight_old_prog
    else:
        print("NOT balanced :(")
        print("line: ", lines[line_no].replace('\n', ''))
        print(leaf_programs_balance_vals, "\n")
        return False, -1



# def get_depth(line_no, lines):
#     new_programs = get_right_side(line_no, lines) # returns list of programs
#     for program in new_programs:
#         program_line_no = find_line_no(program, lines)
#         d = get_depth(program_line_no, lines) # where to add recursive depth (+1)?
#         return d+1
#     return 0

def get_prog_weight(line_no, lines):
    line = lines[line_no]
    weight = int(line.replace('(', '').replace(')', '').split()[1])
    return weight


def get_line_no(program_name, lines):
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