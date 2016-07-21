import numpy as np
import pandas as pd

# loosing data in expand cluster.


class myDBSCAN():

    class Cluster():

        def __init__(self, cluster_id):
            self.cluster_id = cluster_id
            self.cluster_points = pd.DataFrame()
            print "cluster number is ", self.cluster_id

        def addPoint(self, point):
            # while:
                # pass
            self.cluster_points = self.cluster_points.append(point)
            print "addpoint", self.cluster_points
            return

    def __init__(self, eps, m_pts, metric="euclidian"):
        self.eps = eps
        self.m_pts = m_pts
        self.metric = metric  # not used in current version
        self.clusters = []
        self.cluster_number = 0

    def clusterize(self, input_data):
        self.data = input_data
        self.data_size = self.data.shape[0]

        for x in xrange(0, self.data_size):
            print "clusterize p", self.data.loc[x, 'id']
            if self.data.loc[x, 'visited'] == 'n':
                self.data.set_value(x, 'visited', 'y')
                neighbours_id = self.find_neighbours_id(x)
                if (len(neighbours_id) < self.m_pts):
                    self.data.set_value(x, 'noise', 'y')
                else:
                    new_cluster = self.Cluster(self.cluster_number)
                    self.cluster_number += 1
                    new_cluster = self.expandCluster(
                        self.data.iloc[x], new_cluster, neighbours_id)
                    self.clusters.append(new_cluster)
        return self.clusters

    def find_neighbours_id(self, point_id):
        neighbours_id = []
        for check_point_id in xrange(0, self.data_size):
            if self.euclidian(self.data.iloc[point_id],
                              self.data.iloc[check_point_id]) < self.eps:
                neighbours_id.append(check_point_id)
        return neighbours_id

    def euclidian(self, point1, point2):
        return (point1[1] - point2[1])**2 + (point1[2] - point2[2])**2

    def expandCluster(self, point, cluster, neighbours_id):
        cluster.addPoint(point)
        point_next_id = 0
        while True:
            if self.data.loc[neighbours_id[point_next_id], 'visited'] == 'n':
                print "data loc", self.data.loc[neighbours_id[point_next_id], 'id']
                self.data.set_value(
                    neighbours_id[point_next_id], 'visited', 'y')
                neighbours_next_id = self.find_neighbours_id(
                    neighbours_id[point_next_id])
                if len(neighbours_next_id) >= self.m_pts:
                    neighbours_id.extend(neighbours_next_id)
                    print "nei ids", neighbours_next_id
                    print "nei_id", neighbours_id
            if self.belongToCluster(neighbours_id[point_next_id]) == 0:
                print "neigh_id", neighbours_id[point_next_id]
                cluster.addPoint(self.data.iloc[neighbours_id[point_next_id]])
            point_next_id += 1
            if len(neighbours_id) == point_next_id:
                print "point id in break", point_next_id
                print "len before break", len(neighbours_id)
                break
        print "cluster in expand\n", cluster.cluster_points
        return cluster

    def belongToCluster(self, point_rid):  # real id, not pd index
        # print "belongs 0"
        belongs = 0
        # print "cl number ", self.cluster_number
        print "shape ", len(self.clusters)
        if len(self.clusters) == 0:
            return 1
        for cl in xrange(0, self.cluster_number):
            for p in xrange(0, self.clusters[cl].cluster_points.shape[0]):
                print "cl - {}, p - {}".format(cl, p)
                if self.clusters[cl].cluster_points.loc[p, 'id'] == point_rid:
                    belongs = 1
                    break
                else:
                    pass
        return belongs

"""TEST BEGIN"""
dots = []
for x in xrange(0, 3):
    for i in xrange(0, 3):
        if x == i:
            dots.append((x, x, i))  # tryout with np.rand(id)
print "dots \n", dots
# for x in xrange(50, 53):
#     for i in xrange(50, 53):
#         if x == i:
#             dots.append((x - 47, x, i))

pd.set_option('mode.chained_assignment', 'warn')
test_data = pd.DataFrame(data=dots, columns=['id', 'x', 'y'])
test_data = test_data.assign(visited=lambda x: 'n', noise=lambda x: 'n')
print test_data
db = myDBSCAN(eps=3, m_pts=2)
clusters = db.clusterize(test_data)
print "clusters number is", db.cluster_number
print "cluster ", db.cluster_number - 1
print clusters[0].cluster_points
# print "cluster ", db.cluster_number
# print clusters[1].cluster_points
"""TEST END"""


"""FOR THE ANSWER"""
# data = pd.read_csv("order201510-small.csv", header=None,
#                    usecols=[0, 3, 4], names=['id', 'x', 'y'],
#                    dtype={'id': np.int32})
# data = data.assign(visited=lambda x: 'n', noise=lambda x: 'n')
# db = myDBSCAN(eps=0.001, m_pts=4)
# clusters = db.clusterize(data)
# # print clusters
# print db.cluster_number
