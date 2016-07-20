import numpy as np
import pandas as pd


class myDBSCAN():
    # clusters = []
    cluster_number = 0

    class Cluster():
        # cluster_number = 0

        def __init__(self):
            self.cluster_id = myDBSCAN.cluster_number
            myDBSCAN.cluster_number += 1
            self.cluster_points = pd.DataFrame()
            print "cluster number is ", myDBSCAN.cluster_number

        def addPoint(self, point):
            # print "ppoint", point
            self.cluster_points = self.cluster_points.append(point)

    def __init__(self, eps, m_pts, metric="euclidian"):
        self.eps = eps
        self.m_pts = m_pts
        self.metric = metric  # not used in current version
        self.clusters = []
        self.cluster_number = 0

    def clusterize(self, input_data):
        self.data = input_data
        self.data_size = self.data.shape[0]
        # print self.data

        for x in xrange(0, self.data_size):
            if self.data.loc[x, 'visited'] == 'n':
                # print 'not visited'
                self.data.set_value(x, 'visited', 'y')
                # print self.data.loc[x, 'visited']
                neighbours_id = self.find_neighbours_id(x)
                # print "neigh \n", neighbours_id
                if (len(neighbours_id) < self.m_pts):
                    # print "?? noise??"
                    self.data.set_value(x, 'noise', 'y')
                else:
                    new_cluster = self.Cluster()
                    # myDBSCAN.cluster_number += 1
                    # print "new cluster??"
                    # print myDBSCAN.cluster_number
                    new_cluster = self.expandCluster(
                        self.data.iloc[x], new_cluster, neighbours_id)
                    self.clusters.append(new_cluster)
                    # print "got further??"  # last visited after
                    # print type(new_cluster)
        return self.clusters

    def find_neighbours_id(self, point_id):
        neighbours_id = []
        for check_point_id in xrange(0, self.data_size):
            if self.euclidian(self.data.iloc[point_id],
                              self.data.iloc[check_point_id]) < self.eps:
                neighbours_id.append(check_point_id)
        # print "ype of neighbours_id2", type(neighbours_id)
        return neighbours_id

    def euclidian(self, point1, point2):
        # print "tried euclidian", point1[1], point1[2], " ", point2[1], point2[2],
        # print (point1[1] - point2[1])**2 + (point1[2] - point2[2])**2
        return (point1[1] - point2[1])**2 + (point1[2] - point2[2])**2

    def expandCluster(self, point, cluster, neighbours_id):
        # print "point ", point
        cluster.addPoint(point)
        # print cluster.cluster_points.iloc[0]  # last visited
        point_next_id = 0
        while True:
            # print "point_next_id", point_next_id
            if self.data.loc[neighbours_id[point_next_id], 'visited'] == 'n':
                self.data.set_value(
                    neighbours_id[point_next_id], 'visited', 'y')
                neighbours_next_id = self.find_neighbours_id(
                    neighbours_id[point_next_id])
                if len(neighbours_next_id) >= self.m_pts:
                    neighbours_id.extend(neighbours_next_id)
            if self.belongToCluster(neighbours_id[point_next_id]) == 0:
                cluster.addPoint(self.data.iloc[neighbours_id[point_next_id]])
            point_next_id += 1
            if len(neighbours_id) == point_next_id:
                break
        return cluster

    def belongToCluster(self, point_rid):  # real id, not pd index
        belongs = 0
        for cl in xrange(0, self.cluster_number):
            for p in xrange(0, self.clusters[cl].shape[0]):
                if self.clusters[cl].loc[p, 'id'] == point_rid:
                    belongs = 1
                    break
                else:
                    pass
        return belongs

dots = []
for x in xrange(0, 3):
    for i in xrange(0, 3):
        if x == i:
            dots.append((x, x, i))  # tryout with np.rand(id)

for x in xrange(50, 53):
    for i in xrange(50, 53):
        if x == i:
            dots.append((x - 47, x, i))

pd.set_option('mode.chained_assignment', 'warn')
# test_data = pd.DataFrame(data=dots, columns=['id', 'x', 'y'])
# test_data = test_data.assign(visited=lambda x: 'n', noise=lambda x: 'n')
# print test_data
# db = myDBSCAN(eps=3, m_pts=1)
# clusters = db.clusterize(test_data)
# print db.cluster_number
# print clusters[1].cluster_points

# print db.eps

# dots = []

# print len(dots)

# dots = [1, 2, 465, 56786, 433412, 2323, 5]
# shmots = [-5, 90, 9999]
# i = 0
# while True:
#     print dots[i]
#     if dots[i] == 2323:
#         dots.extend(shmots)
#     i += 1

"""for the decision"""
# data = pd.read_csv("order201510-small.csv", header=None,
#                    usecols=[0, 3, 4], names=['id', 'x', 'y'],
#                    dtype={'id': np.int32})
# data = data.assign(visited=lambda x: 'n', noise=lambda x: 'n')
# db = myDBSCAN(eps=0.001, m_pts=4)
# clusters = db.clusterize(data)
# # print clusters
# print db.cluster_number
