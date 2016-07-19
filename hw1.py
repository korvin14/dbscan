import numpy as np
import pandas as pd
# import matplotlib.pyplot as plt
# from sklearn.cluster import DBSCAN


# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def euclidean(self, point):
#         return (self.x - point.x)**2 + (self.y - point.y)**2

class Cluster(object):
    cluster_number = 0

    def __init__(self):  # do i need this crap?
        self.cl_id = 0

    def __init__(self, cl_id, cl_pts):  # change the params
        self.cl_id = cl_id
        self.cl_pts = cl_pts

    def addPoint(self, p_id, p_x, p_y, p_visited):  # change the params
        pass


class myDBSCAN():
    def __init__(self, eps, m_pts, metric="euclidian"):
        self.eps = eps
        self.m_pts = m_pts
        self.metric = metric

    def clusterize(self, input_data):
        self.data = input_data
        del input_data
        self.data_size = self.data.shape[0]
        for x in xrange(0, self.data_size):
            if self.data.iloc[x][3] == 'y':
                pass
            self.data.iloc[x][3] = 'y'
            neighbours = self.find_neighbours(self.data.iloc[x])

    def euclidian(point1, point2):
        return (point1.x[0] - point2.x[0])**2 + (point1.y[0] - point2.y[0])**2

    def find_neighbours(self, point):
        neighbours = pd.DataFrame()
        for x in xrange(0, self.data_size):
            if point.id[0] != self.data.id[x] and self.euclidian(point, self.data.iloc[x]) < self.eps:
                neighbours = neighbours.append(self.data.iloc[x])
        return neighbours

data = pd.read_csv("order201510-small.csv", header=None,
                   usecols=[0, 3, 4], names=['id', 'x', 'y'], dtype={'id': np.int32})
new_data = data.assign(visited=lambda x: 'n', noise=lambda x: 'n')


print "head:"
print new_data.head()
print new_data.shape[0]
print new_data.iloc[0]
print new_data.iloc[1]
print new_data.iloc[2]

print "_____"
print new_data.id[0]
print new_data.x[0]
print new_data.y[0]

d1 = new_data.head(10)
print d1

df = pd.DataFrame()
print df.empty
df = df.append(d1.iloc[1])
print df

for x in xrange(1, 10):
    if x % 2 == 0:
        pass
    else:
        print x
# print euclidian(data.iloc[1], data.iloc[1])


"""scikit check"""
# print "scikit check"
# data should be just 3 and 4th column with noheader. and that's it
# db = DBSCAN(eps=0.001, min_samples=4).fit(data)
# clusters = db.labels_
# number_clusters = len(set(clusters)) - (1 if -1 in clusters else 0)
# print number_clusters
