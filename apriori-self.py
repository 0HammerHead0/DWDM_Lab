data = [
        ['T100',['I1','I2','I5']],
        ['T200',['I2','I4']],
        ['T300',['I2','I3']],
        ['T400',['I1','I2','I4']],
        ['T500',['I1','I3']],
        ['T600',['I2','I3']],
        ['T700',['I1','I3']],
        ['T800',['I1','I2','I3','I5']],
        ['T900',['I1','I2','I3']]
    ]
data2= [
    ['T100',['M','O','N','K','E','Y']],
    ['T200',['D','O','N','K','E','Y']],
    ['T300',['M','A','K','E']],
    ['T400',['M','U','C','K','Y']],
    ['T500',['C','O','K','I','E']]
]




def getCount(c,data):
    count = {}
    for i in data:
        for j in c:
            if set(j).issubset(i[1]):
                j_tuple = tuple(j)  # Convert list to tuple
                if j_tuple in count:
                    count[j_tuple] += 1
                else:
                    count[j_tuple] = 1
    return count

def getL(c,min_sup,data):
    count = getCount(c,data)
    # print(count)
    l = []
    for i in count:
        if count[i] >= min_sup:
            l.append(i)
    return l

def generateC(l):
    c = []
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            if l[i][:-1] == l[j][:-1] and l[i][-1] != l[j][-1]:
                new_itemset = l[i] + (l[j][-1],)  # Convert string to single-element tuple
                c.append(new_itemset)
    return c


def apriori(data,min_sup = 2):
    c=[]
    l=[]
    c1=[]
    for i in data:
        for j in i[1]:
            if j not in c1:
                c1.append(j)
    c1.sort()
    temp=[]
    for i in c1:
        temp.append([i])
    c.append(temp)
    # print(c[-1])
    while(c[-1] != []):
        l.append(getL(c[-1],min_sup,data))
        # print(l)
        c.append(generateC(l[-1]))
        # print(c)
    return l

print(apriori(data2,min_sup=2))