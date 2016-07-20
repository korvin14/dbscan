# import numpy as np
import pandas as pd


class myDBSCAN():
    clusters = []
    cluster_number = 0

    class Cluster():

        def __init__(self):
            self.cluster_id = myDBSCAN.cluster_number
            myDBSCAN.cluster_number += 1
            self.cluster_points = pd.DataFrame()

        def addPoint(self, point):
            self.cluster_points = self.cluster_points.append(point)

    def __init__(self, eps, m_pts, metric="euclidian"):
        self.eps = eps
        self.m_pts = m_pts
        self.metric = metric  # not used in current version

    def clusterize(self, input_data):
        self.data = input_data
        self.data_size = self.data.shape[0]
        for x in xrange(0, self.data_size):
            if self.data.loc[x, 'visited'] == 'n':
                self.data.set_value(x, 'visited', 'y')
                neighbours_id = self.find_neighbours_id(x)
                if len(neighbours_id) < self.m_pts:
                    self.data.set_value(x, 'noise', 'y')
                else:
                    new_cluster = self.Cluster()
                    new_cluster = self.expandCluster(
                        self.data.iloc[x], new_cluster, neighbours_id)
                    # myDBSCAN.clusters = myDBSCAN.clusters.append(new_cluster)
        # return myDBSCAN.clusters

    def find_neighbours_id(self, point_id):
        neighbours_id = []
        for check_point_id in xrange(0, self.data_size):
            if self.euclidian(self.data.iloc[point_id],
                              self.data.iloc[check_point_id]) < self.eps:
                neighbours_id = neighbours_id.append(check_point_id)
        return neighbours_id

    def euclidian(self, point1, point2):
        return (point1[1] - point2[1])**2 + (point1[2] - point2[2])**2

    def expandCluster(self, point, cluster, neighbours_id):
        cluster.addPoint(point)
        point_next_id = 0
        while True:
            if self.data.loc[neighbours_id[point_next_id], 'visited'] == 'n':
                self.data.set_value(
                    neighbours_id[point_next_id], 'visited', 'y')
                neighbours_next_id = self.find_neighbours(
                    neighbours_id[point_next_id])
                if len(neighbours_next_id) >= self.m_pts:
                    neighbours_id.extend(neighbours_next_id)
            if self.belongToCluster(neighbours_id[point_next_id]) == 0:
                cluster.addPoint(self.data.iloc[neighbours_id[point_next_id]])
        point_next_id += 1
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
for x in xrange(0, 20):
    for i in xrange(0, 20):
        if x == i:
            dots.append((x, x, i))  # tryout with np.rand(id)

for x in xrange(50, 70):
    for i in xrange(50, 70):
        if x == i:
            dots.append((x - 30, x, i))

test_data = pd.DataFrame(data=dots, columns=['id', 'x', 'y'])
test_data = test_data.assign(visited=lambda x: 'n', noise=lambda x: 'n')
print test_data
db = myDBSCAN(eps=1, m_pts=5)
clusters = db.clusterize(test_data)
print clusters.cluster_number


# dots = [1, 2, 465, 56786, 433412, 2323, 5]
# shmots = [-5, 90, 9999]
# i = 0
# while True:
#     print dots[i]
#     if dots[i] == 2323:
#         dots.extend(shmots)
#     i += 1
