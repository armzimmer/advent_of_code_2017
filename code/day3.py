import os, math, numpy as np

input_file = "/home/alex/Nextcloud (Kopie)/Documents_old/interestingtoread/advent_of_code/2017/input/\
day2_input.txt"

def main():
    try:
        goal = int(input())
    except ValueError:
        print("Please enter an integer.")

    num, net, y, x, sidelen, center_coord = build_net_until(goal)
                

    # print(data)


    # for i in range(len(data)):
    #     if data[i] == data[(i+len(data)//2) % len(data)]:
    #         res += int(data[i])
    
    print(net)

    # part 1
    # # return distance to center
    # res = abs(y-center_coord)+abs(x-center_coord)
    # print("distance to center: " + str(res))

    # part 2
    print("the first value bigger than", str(goal), "is:", str(num))

def build_net_until(goal):
    sidelen = math.ceil(math.sqrt(goal)) + 2
    center_coord = (sidelen - 1) // 2
    net = np.zeros(shape=(sidelen, sidelen), dtype=np.int64)

    net[center_coord, center_coord] = 1

    x = y = center_coord
    direction = 0 # 0=right, 1=up, 2=left, 3=down
    num_steps_in_direction = 1.0
    num_steps_current = 0
    change = True
    for num_temp in range(goal):
        start_x = x
        start_y = y
        # part 1
        # num = num_temp+1
        num = np.sum(net[max(0,y-1):min(sidelen-1,y+1)+1, max(0,x-1):min(sidelen-1,x+1)+1])
        net[y,x] = num
        
        num_steps_current += 1

        if num > goal:
            break

        # update pos
        if change:
            change = False
            direction = (direction+1) % 4
        
        if direction == 0:
            x+=1
        if direction == 1:
            y+=1
        if direction == 2:
            x-=1
        if direction == 3:
            y-=1
        
        # num steps in direction: 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6
        # set change=True after num of steps above

        if num_steps_current == math.floor(num_steps_in_direction):
            change = True
            num_steps_current = 0
            num_steps_in_direction += 0.5

    return num, net, start_y, start_x, sidelen, center_coord



if __name__ == "__main__":
    main()