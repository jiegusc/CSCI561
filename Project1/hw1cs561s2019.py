import copy
#open file, create a board
def get_initial_board():
    f = open('input1.txt', 'r')
    context = f.readlines()
    table = [[0 for i in range(int(context[0]))] for j in range(int(context[0]))]
    for i in range(int(context[0])):
     for j in range(int(context[0])):
            table[i][j] = int(context[i+1][j])
    return table

def possible_coordinates(table,a):
    l = []
    for i in range(a):
        for j in range(a):
            if table[i][j] == 0:
                l.append((i, j))
    return l
def score(table,a):
    score_m = 0
    score_o = 0
    for i in range(a):
        for j in range(a):
            if (table[i][j] == 1 )or (table[i][j] ==4 )or(table[i][j] ==6) :
                score_m += 1
            if (table[i][j] == 2) or (table[i][j]==5 )or (table[i][j]==6):
                score_o +=1
    return score_m-score_o
def terminal_test(table,a):
    e=possible_coordinates(table,a)
    if e==[]:
        return True
    else:
        return False

def result_Max(table,c):
    table[c[0]][c[1]]=1

def result_Min(table, c):
    table[c[0]][c[1]] = 2

def state(table,a):
    for i in range(a):
        for j in range(a):
            if table[i][j] == 1:
                stop_left_up = True
                stop_up = True
                stop_right_up = True
                stop_left = True
                stop_right = True
                stop_left_down = True
                stop_down = True
                stop_right_down = True
                for beam in range(3):
                    if (0 <= i - 1 - beam < a) and (0 <= j - 1 - beam < a) and stop_left_up:
                        if table[i - 1 - beam][j - 1 - beam] == 0:
                            table[i - 1 - beam][j - 1 - beam] = 4
                        if table[i - 1 - beam][j - 1 - beam] == 5:
                            table[i - 1 - beam][j - 1 - beam] = 6
                        if table[i - 1 - beam][j - 1 - beam] == 3:
                            stop_left_up = False
                    if (0 <= i - 1 - beam < a) and (0 <= j < a) and stop_up:
                        if table[i - 1 - beam][j] == 0:
                            table[i - 1 - beam][j] = 4
                        if table[i - 1 - beam][j] == 5:
                            table[i - 1 - beam][j] = 6
                        if table[i - 1 - beam][j] == 3:
                            stop_up = False
                    if (0 <= i - 1 - beam < a) and (
                            0 <= j + 1 + beam < a) and stop_right_up:
                        if table[i - 1 - beam][j + 1 + beam] == 0:
                            table[i - 1 - beam][j + 1 + beam] = 4
                        if table[i - 1 - beam][j + 1 + beam] == 5:
                            table[i - 1 - beam][j + 1 + beam] = 6
                        if table[i - 1 - beam][j + 1 + beam] == 3:
                            stop_right_up = False
                    if (0 <= i < a) and (0 <= j - 1 - beam < a) and stop_left:
                        if table[i][j - 1 - beam] == 0:
                            table[i][j - 1 - beam] = 4
                        if table[i][j - 1 - beam] == 5:
                            table[i][j - 1 - beam] = 6
                        if table[i][j - 1 - beam] == 3:
                            stop_left = False
                    if (0 <= i < a) and (0 <= j + 1 + beam < a) and stop_right:
                        if table[i][j + 1 + beam] == 0:
                            table[i][j + 1 + beam] = 4
                        if table[i][j + 1 + beam] == 5:
                            table[i][j + 1 + beam] = 6
                        if table[i][j + 1 + beam] == 3:
                            stop_right = False
                    if (0 <= i + 1 + beam < a) and (
                            0 <= j - 1 - beam < a) and stop_left_down:
                        if table[i + 1 + beam][j - 1 - beam] == 0:
                            table[i + 1 + beam][j - 1 - beam] = 4
                        if table[i + 1 + beam][j - 1 - beam] == 5:
                            table[i + 1 + beam][j - 1 - beam] = 6
                        if table[i + 1 + beam][j - 1 - beam] == 3:
                            stop_left_down = False
                    if (0 <= i + 1 + beam < a) and (0 <= j < a) and stop_down:
                        if table[i + 1 + beam][j] == 0:
                            table[i + 1 + beam][j] = 4
                        if table[i + 1 + beam][j] == 5:
                            table[i + 1 + beam][j] = 6
                        if table[i + 1 + beam][j] == 3:
                            stop_down = False
                    if (0 <= i + 1 + beam < a) and (
                            0 <= j + 1 + beam < a) and stop_right_down:
                        if table[i + 1 + beam][j + 1 + beam] == 0:
                            table[i + 1 + beam][j + 1 + beam] = 4
                        if table[i + 1 + beam][j + 1 + beam] == 5:
                            table[i + 1 + beam][j + 1 + beam] = 6
                        if table[i + 1 + beam][j + 1 + beam] == 3:
                            stop_right_down = False
            if table[i][j] == 2:
                stop_left_up = True
                stop_up = True
                stop_right_up = True
                stop_left = True
                stop_right = True
                stop_left_down = True
                stop_down = True
                stop_right_down = True
                for beam in range(3):
                    if (0 <= i - 1 - beam < a) and (0 <= j - 1 - beam < a) and stop_left_up:
                        if table[i - 1 - beam][j - 1 - beam] == 0:
                            table[i - 1 - beam][j - 1 - beam] = 5
                        if table[i - 1 - beam][j - 1 - beam] == 4:
                            table[i - 1 - beam][j - 1 - beam] = 6
                        if table[i - 1 - beam][j - 1 - beam] == 3:
                            stop_left_up = False
                    if (0 <= i - 1 - beam < a) and (0 <= j < a) and stop_up:
                        if table[i - 1 - beam][j] == 0:
                            table[i - 1 - beam][j] = 5
                        if table[i - 1 - beam][j] == 4:
                            table[i - 1 - beam][j] = 6
                        if table[i - 1 - beam][j] == 3:
                            stop_up = False
                    if (0 <= i - 1 - beam < a) and (
                            0 <= j + 1 + beam < a) and stop_right_up:
                        if table[i - 1 - beam][j + 1 + beam] == 0:
                            table[i - 1 - beam][j + 1 + beam] = 5
                        if table[i - 1 - beam][j + 1 + beam] == 4:
                            table[i - 1 - beam][j + 1 + beam] = 6
                        if table[i - 1 - beam][j + 1 + beam] == 3:
                            stop_right_up = False
                    if (0 <= i < a) and (0 <= j - 1 - beam < a) and stop_left:
                        if table[i][j - 1 - beam] == 0:
                            table[i][j - 1 - beam] = 5
                        if table[i][j - 1 - beam] == 4:
                            table[i][j - 1 - beam] = 6
                        if table[i][j - 1 - beam] == 3:
                            stop_left = False
                    if (0 <= i < a) and (0 <= j + 1 + beam < a) and stop_right:
                        if table[i][j + 1 + beam] == 0:
                            table[i][j + 1 + beam] = 5
                        if table[i][j + 1 + beam] == 4:
                            table[i][j + 1 + beam] = 6
                        if table[i][j + 1 + beam] == 3:
                            stop_right = False
                    if (0 <= i + 1 + beam < a) and (
                            0 <= j - 1 - beam < a) and stop_left_down:
                        if table[i + 1 + beam][j - 1 - beam] == 0:
                            table[i + 1 + beam][j - 1 - beam] = 5
                        if table[i + 1 + beam][j - 1 - beam] == 4:
                            table[i + 1 + beam][j - 1 - beam] = 6
                        if table[i + 1 + beam][j - 1 - beam] == 3:
                            stop_left_down = False
                    if (0 <= i + 1 + beam <a) and (0 <= j < a) and stop_down:
                        if table[i + 1 + beam][j] == 0:
                            table[i + 1 + beam][j] = 5
                        if table[i + 1 + beam][j] == 4:
                            table[i + 1 + beam][j] = 6
                        if table[i + 1 + beam][j] == 3:
                            stop_down = False
                    if (0 <= i + 1 + beam < a) and (
                            0 <= j + 1 + beam < a) and stop_right_down:
                        if table[i + 1 + beam][j + 1 + beam] == 0:
                            table[i + 1 + beam][j + 1 + beam] = 5
                        if table[i + 1 + beam][j + 1 + beam] == 4:
                            table[i + 1 + beam][j + 1 + beam] = 6
                        if table[i + 1 + beam][j + 1 + beam] == 3:
                            stop_right_down = False
    return table

def Min_Value(table,x,y,a,depth):
    if terminal_test(table,a)==True or depth==0:
        return score(table,a)
    v=99
    for item in (possible_coordinates(table,a)):
        # create_state=state(table,a)
        new_state=copy.deepcopy(table)
        result_Min(new_state,item)
        value=Max_Value(state(new_state,a),x,y,a,depth-1)
        v=min(v,value)
        if v<=x:
            return v
        y=min(y,v)
        # v=min(v,Max_Value(state(result_Min(state(table,a),item),a),a))
    return v
def Max_Value(table,x,y,a,depth):
    if terminal_test(table,a)==True or depth==0:
        return score(table,a)
    v=-99
    for item in (possible_coordinates(table,a)):
         # create_state = state(table,a)
         new_state = copy.deepcopy(table)
         result_Max(new_state,item)
         value = Min_Value(state(new_state,a),x,y,a,depth-1)
         v = max(v,value)
         if v>=y:
             return v
         x=max(x,v)
         # v=max(v,Min_Value(state(result_Max(state(table,a),item),a),a))
    return v
def Minimax_decision(table,x,y,a,depth):
    v=-99
    for item in (possible_coordinates(table,a)):
        current_table=copy.deepcopy(table)
        result_Max(current_table,item)
        value=Min_Value(state(current_table,a),x,y,a,depth-1)
        # value=Min_Value(state(result_Max(state(table,a),item),a),a)
        if value>v:
            v=value
            b=item
    return b

def main():
    x=-99999
    y=99999
    depth=4
    a=len(get_initial_board())
    table=state(get_initial_board(),a)
    coor_best=Minimax_decision(table,x,y,a,depth)
    return coor_best

item=main()
c=open('output.txt','w')
c.write(str(item[0])+' '+str(item[1]))
c.close()

