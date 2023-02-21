import random
def input_airplane():
    f = open('input4.txt', 'r')
    context = f.readlines()
    b = []
    for i in range(int(context[1])):
        a = context[i + 2].strip().split()
        b.append(a)
    plane = [[0 for _ in range(5)] for _ in range(int(context[1]))]
    for i in range(int(context[1])):
        for j in range(5):
            plane[i][j] = int(b[i][j])
    return plane

def input_LGT():
    f = open('input4.txt', 'r')
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

# randomly choiced landing time and taking off time as a set stored in a dict.
def create_random_output(plane):  # dictionary
    a = {}
    for i in range(len(plane)):
        # f : landing time
        f=random.randint(0, plane[i][0])
        # d : taking off time
        d=random.randint(f+plane[i][1] + plane[i][2], f + plane[i][1] + plane[i][4])
        a[i] = [f,d]
    return a

# calculate the score of the gene
def fitness(time_length, singpop, a, L, G, T):  # 0:L,1:G,2:T  a=time number b table length
    LGT = {}
    table_LGT = [[0 for _ in range(time_length)] for _ in range(3)]
    LGT[0] = (table_LGT[0])
    LGT[1] = (table_LGT[1])
    LGT[2] = (table_LGT[2])
    for i in range(len(singpop)):
        # landing time
        for t in range(singpop[i][0], singpop[i][0] + a[i][1]):
            LGT[0][t] += 1
        # the time at the gate
        for t in range(singpop[i][0] + a[i][1], singpop[i][1]):
            LGT[1][t] += 1
        # the taking off time
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

# crossover each plane's landing and taking off time.
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

if __name__ == '__main__':
    # a : dict of all planes
    planes_dict = dictionary(input_airplane())
    sum_time = []
    for i in range(len(planes_dict)):
        sum_time.append(planes_dict[i][0] + planes_dict[i][1] + planes_dict[i][2] + planes_dict[i][3] + planes_dict[i][4])
    #iteratoin number
    IT = 100
    time_length = sorted(sum_time)[-1]

    # randomly picked # ; as genes #
    pop = 200
    b = input_LGT()
    # number of plane landing at the same time
    L = b[0]
    # gate number
    G = b[1]
    # number of plane taking off at the same time
    T = b[2]
    # pop_p is a combination of a score value and the return result. if the score is 0, then return the result.
    pop_p = [(fitness(time_length, g, planes_dict, L, G, T), g) for g in population(planes_dict, pop)]
    pop_p.sort(key=lambda x:x[0])

    for i in range(IT):
        if pop_p[0][0] == 0:
            output(pop_p[0])
            break
        else:
            for i in range(int(pop / 2)):
                # g is the result set.
                g = crossover(planes_dict, pop_p[i], pop_p[i + 1])
                pop_p.append((fitness(time_length, g, planes_dict, L, G, T), g))
                new_gene = create_random_output(planes_dict)
                pop_p.append((fitness(time_length, new_gene, planes_dict, L, G, T), new_gene))
            pop_p.sort(key=lambda x:x[0])
            pop_p = pop_p[:pop]
    print(pop_p[0])
    output(pop_p[0])



