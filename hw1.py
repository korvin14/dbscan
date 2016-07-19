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

class myDBSCAN():
    clusters = []
    cluster_number = 0

    def __init__(self, eps, m_pts, metric="euclidian"):
        self.eps = eps
        self.m_pts = m_pts
        self.metric = metric

    class Cluster():

        def __init__(self):  # do i need this crap?
            self.cl_id = myDBSCAN.cluster_number  # do i need this crap?
            myDBSCAN.cluster_number += 1  # do i need this crap?
            self.cluster_points = pd.DataFrame()

        def addPoint(self, point):
            # if : # CHECK IF WE ALREADY HAVE POINT WITH THIS ID
            self.cluster_points = self.cluster_points.append(point)
            # else:
            #     pass

    def clusterize(self, input_data):
        self.data = input_data
        del input_data
        self.data_size = self.data.shape[0]
        for x in xrange(0, self.data_size):
            if self.data.iloc[x][3] == 'y':
                pass  # not dummy
            self.data.iloc[x][3] = 'y'
            neighbours = self.find_neighbours(self.data.iloc[x])
            if neighbours.shape[0] < self.m_pts:
                self.data.noise[x] = 'y'
            else:
                new_cluster = self.Cluster()
                # new_cluster.cluster_number += 1
                new_cluster.expandCluster(self.data.iloc[x], neighbours)
                myDBSCAN.clusters = myDBSCAN.clusters.append(new_cluster)
        return myDBSCAN.clusters

    def expandCluster(self, point, neighbours):
        self.Cluster.addPoint(point)
        point_next = 0
        while neighbours.iloc[point_next]:
            if neighbours.visited[point_next] == 'n':
                neighbours.visited[point_next] = 'y'
                neighbours_next = self.find_neighbours(
                    neighbours.iloc[point_next])
                if neighbours_next.shape[0] >= self.m_pts:
                    neighbours = neighbours.append(neighbours_next)
            # if  # func with cluster belonging
            point_next += 1

    def belongToCluster(self, point):
        belongs = 0
        for x in xrange(0, 10):
            pass
        return belongs

    def euclidian(point1, point2):
        return (point1.x[0] - point2.x[0])**2 + (point1.y[0] - point2.y[0])**2

    def find_neighbours(self, point):
        neighbours = pd.DataFrame()
        for x in xrange(0, self.data_size):
            if self.euclidian(point, self.data.iloc[x]) < self.eps:
                neighbours = neighbours.append(self.data.iloc[x])
        return neighbours

data = pd.read_csv("order201510-small.csv", header=None,
                   usecols=[0, 3, 4], names=['id', 'x', 'y'],
                   dtype={'id': np.int32})
new_data = data.assign(visited=lambda x: 'n', noise=lambda x: 'n')


print "head:"
print new_data.head()
print new_data.shape[0]
# print new_data.iloc[0]
# print new_data.iloc[1]
# print new_data.iloc[2]

# print "_____"
# print new_data.id[0]
# print new_data.x[0]
# print new_data.y[0]

d1 = new_data.head(10)
for x in xrange(0, d1.shape[0]):
    print x
    if x == 10:
        d1 = d1.append(new_data.head(11, 20))

print "anpother version:"


# # print d1

# df = pd.DataFrame()
# print df.empty
# df = df.append(d1.iloc[1])
# # print df

for x in xrange(0, 10):
    print "sdf", x
# print euclidian(data.iloc[1], data.iloc[1])


"""scikit check"""
# print "scikit check"
# data should be just 3 and 4th column with noheader. and that's it
# db = DBSCAN(eps=0.001, min_samples=4).fit(data)
# clusters = db.labels_
# number_clusters = len(set(clusters)) - (1 if -1 in clusters else 0)
# print number_clusters
