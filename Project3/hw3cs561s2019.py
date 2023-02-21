import copy
import time


start=time.time()
def get_possible_index(table, rs):
    poss_list = []
    for i in range(len(table)):
        for j in range(len(table)):
            if table[i][j] == rs:
                poss_list.append([i, j])
    return poss_list


def get_utility_table(table, poss_list, p, rs, gamma, e):
    while True:
        table_current = copy.deepcopy(table)
        delta = 0
        for i in poss_list:
            table[i[0]][i[1]] = rs + gamma * max(utility_action_right(table, i[0], i[1], p),
                                                 utility_action_up(table, i[0], i[1], p),
                                                 utility_action_down(table, i[0], i[1], p),
                                                 utility_action_left(table, i[0], i[1], p))
            if abs(table[i[0]][i[1]] - table_current[i[0]][i[1]]) > delta:
                delta = abs(table[i[0]][i[1]] - table_current[i[0]][i[1]])
            print(table)
        if delta < e * (1 - gamma)/gamma:
            return table_current

def utility_action_up(table, x, y, p):  # table and one coordinate
    if x - 1 < 0:
        return (1 - p)/2 * table[x][y] + (1 - p)/2 * table[x][y] + table[x][y] * p
    if (x - 1 >= 0) and (y - 1 < 0):  # first column
        if table[x - 1][y] == "N" and table[x - 1][y + 1] != "N":
            return table[x][y] * (p + (1 - p)/2) + (1 - p)/2 * table[x - 1][y + 1]
        if table[x - 1][y] == "N" and table[x - 1][y + 1] == "N":
            return (1 - p)/2 * table[x][y] + (1 - p)/2 * table[x][y] + table[x][y] * p
        if table[x - 1][y] != "N" and table[x - 1][y + 1] == "N":
            return (1 - p) * table[x][y] + table[x - 1][y] * p
        else:
            return (1 - p)/2 * table[x][y] + table[x - 1][y] * p + (1 - p)/2 * table[x - 1][y + 1]
    if (x - 1 >= 0) and (y + 1 == len(table)):  # last column
        if table[x - 1][y] == "N" and table[x - 1][y - 1] != "N":
            return table[x][y] * (p + (1 - p)/2) + (1 - p)/2 * table[x - 1][y - 1]
        if table[x - 1][y] == "N" and table[x - 1][y - 1] == "N":
            return (1 - p)/2 * table[x][y] + (1 - p)/2 * table[x][y] + table[x][y] * p
        if table[x - 1][y] != "N" and table[x - 1][y - 1] == "N":
            return (1 - p) * table[x][y] + table[x - 1][y] * p
        else:
            return (1 - p)/2 * table[x][y] + table[x - 1][y] * p + (1 - p)/2 * table[x - 1][y - 1]
    if (x - 1 >= 0) and (0 <= y - 1 and y + 1 < len(table)):  # columns in middle
        if table[x - 1][y - 1] == "N" and table[x - 1][y] == "N" and table[x - 1][y + 1] == "N":
            return (1 - p)/2 * table[x][y] + (1 - p)/2 * table[x][y] + table[x][y] * p
        if table[x - 1][y - 1] != "N" and table[x - 1][y] == "N" and table[x - 1][y + 1] == "N":
            return table[x - 1][y - 1] * (1 - p)/2 + table[x][y] * (p + (1 - p)/2)
        if table[x - 1][y - 1] != "N" and table[x - 1][y] != "N" and table[x - 1][y + 1] == "N":
            return table[x - 1][y - 1] * (1 - p)/2 + table[x - 1][y] * p + table[x][y] * (1 - p)/2
        if table[x - 1][y - 1] != "N" and table[x - 1][y] == "N" and table[x - 1][y + 1] != "N":
            return (1 - p)/2 * table[x - 1][y - 1] + (1 - p)/2 * table[x - 1][y + 1] + table[x][y] * p
        if table[x - 1][y - 1] == "N" and table[x - 1][y] != "N" and table[x - 1][y + 1] == "N":
            return table[x - 1][y] * p + table[x][y] * (1 - p)
        if table[x - 1][y - 1] == "N" and table[x - 1][y] == "N" and table[x - 1][y + 1] != "N":
            return (p + (1 - p)/2) * table[x][y] + table[x - 1][y + 1] * (1 - p)/2
        if table[x - 1][y - 1] == "N" and table[x - 1][y] != "N" and table[x - 1][y + 1] != "N":
            return table[x][y] * (1 - p)/2 + table[x - 1][y] * p + table[x - 1][y + 1] * (1 - p)/2
        else:
            return (1 - p)/2 * table[x - 1][y - 1] + table[x - 1][y] * p + (1 - p)/2 * table[x - 1][y + 1]


def utility_action_down(table, x, y, p):
    if x + 1 == len(table):
        return (1 - p)/2 * table[x][y] + (1 - p)/2 * table[x][y] + table[x][y] * p
    if (x + 1 < len(table)) and (y - 1 < 0):  # first column
        if table[x + 1][y] == "N" and table[x + 1][y + 1] == "N":
            return (1 - p)/2 * table[x][y] + (1 - p)/2 * table[x][y] + table[x][y] * p
        if table[x + 1][y] != "N" and table[x + 1][y + 1] == "N":
            return table[x + 1][y] * p + table[x][y] * (1 - p)
        if table[x + 1][y] == "N" and table[x + 1][y + 1] != "N":
            return (p + (1 - p)/2) * table[x][y] + (1 - p)/2 * table[x + 1][y + 1]
        else:
            return (1 - p)/2 * table[x][y] + table[x + 1][y] * p + (1 - p)/2 * table[x + 1][y + 1]
    if (x + 1 < len(table)) and (y + 1 == len(table)):  # last column
        if table[x + 1][y] == "N" and table[x + 1][y - 1] == "N":
            return (1 - p)/2 * table[x][y] + (1 - p)/2 * table[x][y] + table[x][y] * p
        if table[x + 1][y] != "N" and table[x + 1][y - 1] == "N":
            return table[x + 1][y] * p + table[x][y] * (1 - p)
        if table[x + 1][y] == "N" and table[x + 1][y - 1] != "N":
            return table[x][y] * (p + (1 - p)/2) + table[x + 1][y - 1] * (1 - p)/2
        else:
            return (1 - p)/2 * table[x][y] + table[x + 1][y] * p + (1 - p)/2 * table[x + 1][y - 1]
    if (x + 1 < len(table)) and (0 <= y - 1 and y + 1 < len(table)):  # middle columns
        if table[x + 1][y - 1] == "N" and table[x + 1][y] == "N" and table[x + 1][y + 1] == "N":
            return (1 - p)/2 * table[x][y] + (1 - p)/2 * table[x][y] + table[x][y] * p
        if table[x + 1][y - 1] != "N" and table[x + 1][y] == "N" and table[x + 1][y + 1] == "N":
            return (p + (1 - p)/2) * table[x][y] + (1 - p)/2 * table[x + 1][y - 1]
        if table[x + 1][y - 1] != "N" and table[x + 1][y] != "N" and table[x + 1][y + 1] == "N":
            return (1 - p)/2 * table[x + 1][y - 1] + table[x + 1][y] * p + (1 - p)/2 * table[x][y]
        if table[x + 1][y - 1] != "N" and table[x + 1][y] == "N" and table[x + 1][y + 1] != "N":
            return (1 - p)/2 * table[x + 1][y - 1] + (1 - p)/2 * table[x + 1][y + 1] + table[x][y] * p
        if table[x + 1][y - 1] == "N" and table[x + 1][y] != "N" and table[x + 1][y + 1] == "N":
            return (1 - p) * table[x][y] + table[x + 1][y] * p
        if table[x + 1][y - 1] == "N" and table[x + 1][y] == "N" and table[x + 1][y + 1] != "N":
            return (p + (1 - p)/2) * table[x][y] + (1 - p)/2 * table[x + 1][y + 1]
        if table[x + 1][y - 1] == "N" and table[x + 1][y] != "N" and table[x + 1][y + 1] != "N":
            return (1 - p)/2 * table[x][y] + table[x + 1][y] * p + (1 - p)/2 * table[x + 1][y + 1]
        else:
            return (1 - p)/2 * table[x + 1][y - 1] + table[x + 1][y] * p + (1 - p)/2 * table[x + 1][y + 1]


def utility_action_left(table, x, y, p):
    if y - 1 < 0:
        return (1 - p)/2 * table[x][y] + (1 - p)/2 * table[x][y] + table[x][y] * p
    if (y - 1 >= 0) and (x - 1 < 0):  # first row
        if table[x][y - 1] == "N" and table[x + 1][y - 1] == "N":
            return (1 - p)/2 * table[x][y] + (1 - p)/2 * table[x][y] + table[x][y] * p
        if table[x][y - 1] != "N" and table[x + 1][y - 1] == "N":
            return p * table[x][y - 1] + (1 - p) * table[x][y]
        if table[x][y - 1] == "N" and table[x + 1][y - 1] != "N":
            return (p + (1 - p)/2) * table[x][y] + (1 - p)/2 * table[x + 1][y - 1]
        else:
            return table[x][y - 1] * p + table[x + 1][y - 1] * (1 - p)/2 + table[x][y] * (1 - p)/2
    if (y - 1 >= 0) and (x + 1 == len(table)):  # last row
        if table[x - 1][y - 1] == "N" and table[x][y - 1] == "N":
            return (1 - p)/2 * table[x][y] + (1 - p)/2 * table[x][y] + table[x][y] * p
        if table[x - 1][y - 1] != "N" and table[x][y - 1] == "N":
            return (p + (1 - p)/2) * table[x][y] + table[x - 1][y - 1] * (1 - p)/2
        if table[x - 1][y - 1] == "N" and table[x][y - 1] != "N":
            return (1 - p) * table[x][y] + p * table[x][y - 1]
        else:
            return (1 - p)/2 * table[x][y] + p * table[x][y - 1] + (1 - p)/2 * table[x - 1][y - 1]
    if (y - 1 >= 0) and (0 <= x - 1 and x + 1 <= len(table)):  # middle columns
        if table[x - 1][y - 1] == "N" and table[x][y - 1] == "N" and table[x + 1][y - 1] == "N":
            return (1 - p)/2 * table[x][y] + (1 - p)/2 * table[x][y] + table[x][y] * p
        if table[x - 1][y - 1] != "N" and table[x][y - 1] == "N" and table[x + 1][y - 1] == "N":
            return (p + (1 - p)/2) * table[x][y] + (1 - p)/2 * table[x - 1][y - 1]
        if table[x - 1][y - 1] != "N" and table[x][y - 1] != "N" and table[x + 1][y - 1] == "N":
            return (1 - p)/2 * table[x - 1][y - 1] + table[x][y - 1] * p + (1 - p)/2 * table[x][y]
        if table[x - 1][y - 1] != "N" and table[x][y - 1] == "N" and table[x + 1][y - 1] != "N":
            return (1 - p)/2 * table[x - 1][y - 1] + (1 - p)/2 * table[x + 1][y - 1] + table[x][y] * p
        if table[x - 1][y - 1] == "N" and table[x][y - 1] != "N" and table[x + 1][y - 1] == "N":
            return (1 - p) * table[x][y] + table[x][y - 1] * p
        if table[x - 1][y - 1] == "N" and table[x][y - 1] == "N" and table[x + 1][y - 1] != "N":
            return (p + (1 - p)/2) * table[x][y] + (1 - p)/2 * table[x + 1][y - 1]
        if table[x - 1][y - 1] == "N" and table[x][y - 1] != "N" and table[x + 1][y - 1] != "N":
            return (1 - p)/2 * table[x][y] + table[x][y - 1] * p + (1 - p)/2 * table[x + 1][y - 1]
        else:
            return table[x - 1][y - 1] * (1 - p)/2 + table[x][y - 1] * p + (1 - p)/2 * table[x + 1][y - 1]


def utility_action_right(table, x, y, p):
    if y + 1 == len(table):
        return (1 - p)/2 * table[x][y] + (1 - p)/2 * table[x][y] + table[x][y] * p
    if (y + 1 < len(table)) and (x - 1 < 0):  # first row
        if table[x][y + 1] == "N" and table[x + 1][y + 1] == "N":
            return (1 - p)/2 * table[x][y] + (1 - p)/2 * table[x][y] + table[x][y] * p
        if table[x][y + 1] != "N" and table[x + 1][y + 1] == "N":
            return p * table[x][y + 1] + (1 - p) * table[x][y]
        if table[x][y + 1] == "N" and table[x + 1][y + 1] != "N":
            return (p + (1 - p)/2) * table[x][y] + (1 - p)/2 * table[x + 1][y + 1]
        else:
            return (1 - p)/2 * table[x][y] + table[x][y + 1] * p + (1 - p)/2 * table[x + 1][y + 1]
    if (y + 1 < len(table)) and (x + 1 == len(table)):  # last row
        if table[x - 1][y + 1] == "N" and table[x][y + 1] == "N":
            return (1 - p)/2 * table[x][y] + (1 - p)/2 * table[x][y] + table[x][y] * p
        if table[x - 1][y + 1] != "N" and table[x][y + 1] == "N":
            return (p + (1 - p) / 2) * table[x][y] + table[x - 1][y + 1] * (1 - p) / 2
        if table[x - 1][y + 1] == "N" and table[x][y + 1] != "N":
            return (1 - p) * table[x][y] + p * table[x][y + 1]
        else:
            return (1 - p)/2 * table[x][y] + table[x][y + 1] * p + table[x - 1][y + 1] * (1 - p)/2
    if (y + 1 < len(table)) and (0 <= x - 1 and x + 1 < len(table)):  # middle rows
        if table[x - 1][y + 1] == "N" and table[x][y + 1] == "N" and table[x + 1][y + 1] == "N":
            return (1 - p)/2 * table[x][y] + (1 - p)/2 * table[x][y] + table[x][y] * p
        if table[x - 1][y + 1] != "N" and table[x][y + 1] == "N" and table[x + 1][y + 1] == "N":
            return (p + (1 - p)/2) * table[x][y] + (1 - p)/2 * table[x - 1][y + 1]
        if table[x - 1][y + 1] != "N" and table[x][y + 1] != "N" and table[x + 1][y + 1] == "N":
            return (1 - p)/2 * table[x - 1][y + 1] + table[x][y + 1] * p + (1 - p)/2 * table[x][y]
        if table[x - 1][y + 1] != "N" and table[x][y + 1] == "N" and table[x + 1][y + 1] != "N":
            return (1 - p)/2 * table[x - 1][y + 1] + (1 - p)/2 * table[x + 1][y + 1] + table[x][y] * p
        if table[x - 1][y + 1] == "N" and table[x][y + 1] != "N" and table[x + 1][y + 1] == "N":
            return (1 - p) * table[x][y] + table[x][y + 1] * p
        if table[x - 1][y + 1] == "N" and table[x][y + 1] == "N" and table[x + 1][y + 1] != "N":
            return (p + (1 - p)/2) * table[x][y] + (1 - p)/2 * table[x + 1][y + 1]
        if table[x - 1][y + 1] == "N" and table[x][y + 1] != "N" and table[x + 1][y + 1] != "N":
            return (1 - p)/2 * table[x][y] + table[x][y + 1] * p + (1 - p)/2 * table[x + 1][y + 1]
        else:
            return (1 - p)/2 * table[x - 1][y + 1] + table[x][y + 1] * p + (1 - p)/2 * table[x + 1][y + 1]


def direction(table, x, y, p):
    dir_list = list()
    dir_list.append((utility_action_left(table, x, y, p), "L"))
    dir_list.append((utility_action_down(table, x, y, p), "D"))
    dir_list.append((utility_action_up(table, x, y, p), "U"))
    dir_list.append((utility_action_right(table, x, y, p), "R"))
    return sorted(dir_list)


def output(table):
    c = open('output.txt', 'w')
    for i in range(len(table)):
        for j in range(len(table) - 1):
            c.write(str(table[i][j]) + ",")
        c.write(str(table[i][len(table) - 1]) + "\n")
    c.close()


def main():
    e = 0.01
    f = open('input0.txt', 'r')
    context = f.readlines()
    wall = []
    wall_num = int(context[1])
    for i in range(wall_num):
        b = context[2 + i].strip().split(',')
        wall.append(b)
    exi = []
    exi_num = int(context[2 + wall_num])
    for i in range(exi_num):
        c = context[3 + wall_num + i].strip().split(',')
        exi.append(c)
    #initial value in each cell
    rs = float(context[-2])
    # probability to transform
    p = float(context[-3])
    # penal param
    gamma = float(context[-1])
    get_initial_table = list()
    for i in range(int(context[0])):
        get_initial_table.append([float(rs)] * int(context[0]))
    for i in range(wall_num):
        get_initial_table[int(wall[i][0]) - 1][int(wall[i][1]) - 1] = "N"
    for i in range(exi_num):
        get_initial_table[int(exi[i][0]) - 1][int(exi[i][1]) - 1] = float(exi[i][2])
    table = copy.copy(get_initial_table)
    print(table)
    # possible position to move
    poss_list = get_possible_index(table, rs)
    final_table = get_utility_table(table, poss_list, p, rs, gamma, e)
    output_table = []
    for i in range(int(context[0])):
        output_table.append(["0"]*int(context[0]))
    for i in poss_list:
        output_table[i[0]][i[1]] = direction(final_table, i[0], i[1], p)[3][1]
        print(direction(final_table, i[0], i[1], p))

    for i in range(wall_num):
        output_table[int(wall[i][0]) - 1][int(wall[i][1]) - 1] = "N"
    for i in range(exi_num):
        output_table[int(exi[i][0]) - 1][int(exi[i][1]) - 1] = "E"

    return output_table


output(main())
end=time.time()
print(end-start)

