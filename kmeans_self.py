import math

def getDist(point,center):
    return math.sqrt((point[0]-center[0])**2 + (point[1]-center[1])**2)

def distributePoints(points,centers):
    map = {}
    for p_ind,point in enumerate(points):
        min_dist = float('inf')
        min_ind = 0
        for ind in range(len(centers)):
            dist = getDist(point,centers[ind])
            if(dist<min_dist):
                min_dist=dist
                min_ind = ind
        if(min_ind in map.keys()):
            map[min_ind].append(p_ind)
        else:
            map[min_ind] = [p_ind]
    return map

def mean_centers(clusters,data):
    centers=[]
    for i in clusters.keys():
        center=[]
        x=0
        y=0
        count=0
        for j in clusters[i]:
            x+=data[j][0]
            y+=data[j][1]
            count+=1
        if(count!=0):
            center.append(x/count)
            center.append(y/count)
        centers.append(center)
    return centers

if __name__ == '__main__':
    f = open('data/kmeansdata.txt')
    lines = f.readlines()
    data=[]
    for i in lines:
        data.append(list(map(float,i.split())))
    k = int(input("Enter number of clusters: "))
    centers = []
    for i in range(k):
        center = list(map(float,input("Enter a center: ").split()))
        centers.append(center)
    prev_centers=[]
    clusters = distributePoints(data,centers)
    while(prev_centers != centers):
        prev_centers = centers
        centers = mean_centers(clusters,data)
        clusters=distributePoints(data,centers)
    for i in clusters:
        print("Cluster ",i)
        for j in clusters[i]:
            print(data[j])
        print("---------------------")