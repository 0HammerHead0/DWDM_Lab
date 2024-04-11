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

min_sup = 2


def getCount(c,data):
    map = {}
    for i in c:
        for j in data:
            if set(i).issubset(j[1]):
                i_ = tuple(i)
                if i_ in map.keys():
                    map[i_]+=1
                else:
                    map[i_]=1
    return map

def getL(c,min_sup,data):
    l=[]
    map = getCount(c,data)
    for i in map.keys():
        if(map[i]>=min_sup):
            l.append(i)
    return l

def genC(l):
    c=[]
    for i in range(len(l)-1):
        for j in range(i+1,len(l)):
            if(l[i][:-1] == l[j][:-1]):
                temp=list(l[i])
                temp.append(l[j][-1])
                c.append(tuple(temp
                    ))
                # print((list(l[i]).append((l[j][-1]))))
    return c
def apriori(data,min_sup):
    c=[]
    l=[]
    for i in data:
        for j in i[1]:
            if( j not in c):
                c.append(j)
    c.sort()
    temp = []
    for i in c:
        temp.append([i])
    c=temp
    while(c!=[]):
        l.append(getL(c,min_sup,data))
        c=genC(l[-1])
    for i in (l[:-1]):
        print(i)

apriori(data,min_sup)