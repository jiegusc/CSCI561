import random
def input_airplane():
    f = open('input0.txt', 'r')
    context = f.readlines()
    b = []
    for i in range(int(context[1])):
        a = context[i + 2].strip().split()
        b.append(a)
    plane = [[0 for i in range(5)] for j in range(int(context[1]))]
    for i in range(int(context[1])):
        for j in range(5):
            plane[i][j] = int(b[i][j])
    return plane

def input_LGT():
    f = open('input0.txt', 'r')
    a = f.readline().strip().split()
    b = [0, 0, 0]
    for i in range(3):
        b[i] = int(a[i])
    return b

def dictionary(plane):
    my_dict = {}
    for i in range(len(plane)):
        my_dict.update({i: [plane[i][0], plane[i][1], plane[i][2], plane[i][3], plane[i][4]]})
    return my_dict
def output(a):
    c = open('output.txt', 'w')
    for i in range(len(a[1])):
        c.write(str(a[1][i][0]) + " " + str(a[1][i][1])+"\n")
    c.close()

def create_random_output(plane):  # dictionary
    a = {}
    for i in range(len(plane)):
        f=random.randint(0, plane[i][0])
        d=random.randint(f+plane[i][1] + plane[i][2], f + plane[i][1] + plane[i][4])
        a[i] = [f,d]
    return a

def fitness(time_length, singpop, a, L, G, T):  # 0:L,1:G,2:T  a=time number b table length
    LGT = {}
    table_LGT = [[0 for i in range(time_length)] for j in range(3)]
    LGT[0] = (table_LGT[0])
    LGT[1] = (table_LGT[1])
    LGT[2] = (table_LGT[2])
    for i in range(len(singpop)):
        for t in range(singpop[i][0], singpop[i][0] + a[i][1]):
            LGT[0][t] += 1
        for t in range(singpop[i][0] + a[i][1], singpop[i][1]):
            LGT[1][t] += 1
        for t in range(singpop[i][1], singpop[i][1] + a[i][3]):
            LGT[2][t] += 1
    count = 0
    for i in LGT[0]:
        if i > L:
            count += 1
    for i in LGT[1]:
        if i > G:
            count += 1
    for i in LGT[2]:
        if i > T:
            count += 1
    return count
def population(plane, pop):
    Population = []
    for i in range(pop):
        Population.append(create_random_output(plane))
    return Population
def crossover(a, parent1, parent2):
    child = {}
    for i in range(len(a)):
        a = []
        b = parent1[1][i]
        c = parent2[1][i]
        a.append(b)
        a.append(c)
        child[i] = random.choice(a)
    return child
def main():
    a = dictionary(input_airplane())
    sum_time = []
    for i in range(len(a)):
        sum_time.append(a[i][0] + a[i][1] + a[i][2] + a[i][3] + a[i][4])
    IT = 100
    time_length = sorted(sum_time)[-1]
    pop = 200
    b = input_LGT()
    L = b[0]
    G = b[1]
    T = b[2]
    pop_p = [(fitness(time_length, g, a, L, G, T), g) for g in population(a, pop)]
    pop_p.sort()
    for i in range(IT):
        if pop_p[0][0] == 0:
            return pop_p[0]
        else:
            for i in range(int(pop / 2)):
                g = crossover(a, pop_p[i], pop_p[i + 1])
                pop_p.append((fitness(time_length, g, a, L, G, T), g))
            pop_p.sort()
            pop_p = pop_p[:pop]
    return pop_p[0]
a = main()
output(a)
print(a)


