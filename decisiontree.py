import numpy as np
import pandas as pd
from collections import Counter
data = {
    'outlook': ['sunny', 'sunny', 'overcast', 'rain', 'rain', 'rain', 'overcast', 'sunny', 'sunny', 'rain', 'sunny', 'overcast', 'overcast', 'rain'],
    'temperature': ['hot', 'hot', 'hot', 'mild', 'cool', 'cool', 'cool', 'mild', 'cool', 'mild', 'mild', 'hot', 'hot', 'mild'],
    'humidity': ['high', 'high', 'high', 'high', 'normal', 'normal', 'normal', 'high', 'normal', 'normal', 'normal', 'high', 'normal', 'high'],
    'wind': ['weak', 'strong', 'weak', 'weak', 'weak', 'strong', 'strong', 'weak', 'weak', 'weak', 'strong', 'strong', 'weak', 'strong'],
    'answer': ['no', 'no', 'yes', 'yes', 'yes', 'no', 'yes', 'no', 'yes', 'yes', 'yes', 'yes', 'yes', 'no']
}

def getEntropy(data):
    unique_values = set(data)
    ans = 0
    for i in unique_values:
        ans-= data.count(i)/len(data) * np.log2(data.count(i)/len(data))
    return ans

def getInfoForAttribute(data,attr,target):
    unique_values = set(data[attr])
    uniq_target = set(data[target])
    info = 0
    map={}
    for i in unique_values:
        map[i]={}
        for j in uniq_target:
            map[i][j]=0
    for i in range(len(data[attr])):
        map[data[attr][i]][data[target][i]]+=1
    for i in map.keys():
        target_total=0
        for j in map[i].keys():
            target_total+=map[i][j]
        for j in map[i].keys():
            if(map[i][j]!=0):
                info -= target_total/len(data[attr]) * map[i][j]*np.log2(map[i][j]/target_total)/target_total
    return info

def getGain(data,attr,target):
    return getEntropy(data[target]) - getInfoForAttribute(data,attr,target)

def getBestAttr(data,target):
    gainArr = {attr: getGain(data,attr,target) for attr in data.keys() if attr!=target}
    return max(gainArr, key=gainArr.get)

def ID3(data,attrs,target):
    if len(set(data[target])) == 1:
        return data[target][0]
    best_attr = getBestAttr(data,target)
    tree = {best_attr:{}}
    rem_attr = [x for x in attrs if x!=best_attr]
    for value in set(data[best_attr]):
        subset={}
        for row in range(len(data[best_attr])):
            if(data[best_attr][row]==value):
                for attr in rem_attr:
                    if(attr in subset.keys()):
                        subset[attr].append(data[attr][row])
                    else:
                        subset[attr]=[data[attr][row]]
        tree[best_attr][value] = ID3(subset, rem_attr, target)
    return tree



attrs = ['outlook', 'temperature', 'humidity', 'wind','answer']
target = 'answer'
print(ID3(data,attrs,target))
