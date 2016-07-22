import numpy as np
import pandas as pd


class myDBSCAN():
    clusters_number = 0

    def __init__(self, eps, m_pts, metric="euclidian"):
        self.eps = eps
        self.m_pts = m_pts
        self.clusters = []
        # self.clusters_number = 0  # dont think i need since len??

    class Cluster():
        def __init__(self):
            self.points = {}
            print "cluster # ", myDBSCAN.clusters_number
            myDBSCAN.clusters_number += 1

        # noise and visited is only for DF. all in clusters doesnt follow it
        def addPoint(self, id, x, y):
            xy = (x, y)  # tuple because we just need to store it
            self.points[id] = xy
            print "added p ", id

    def clusterize(self, input_data):
        self.data = input_data
        del input_data
        self.data_size = self.data.shape[0]
        for x in xrange(0, self.data_size):
            if self.data.loc[x, 'visited'] == 'n':
                self.data.set_value(x, 'visited', 'y')
                neighbours_id = self.find_neighbours_id(x)
                print "neighbours id: ", neighbours_id
                if (len(neighbours_id) < self.m_pts):
                    self.data.set_value(x, 'noise', 'y')
                else:
                    new_cluster = self.Cluster()
                    new_cluster = self.expandCluster(
                        self.data.iloc[x], new_cluster, neighbours_id)
                    # print "cluster :\n", new_cluster.points
                    self.clusters.append(new_cluster)
        return self.clusters

    def find_neighbours_id(self, pd_id):
        neighbours_id = []
        for check_point_id in xrange(0, self.data_size):
            if self.euclidian(self.data.iloc[pd_id],
                              self.data.iloc[check_point_id]) < self.eps:
                neighbours_id.append(check_point_id)
        return neighbours_id

    def euclidian(self, point1, point2):
        return (point1[1] - point2[1])**2 + (point1[2] - point2[2])**2

    def expandCluster(self, point, cluster, neighbours_id):
        cluster.addPoint(point[0], point[1], point[2])
        print "neighbours_id", neighbours_id
        print "nighb 0 ", neighbours_id[0]
        for p_id, el in enumerate(neighbours_id):
            if self.data.loc[neighbours_id[p_id], 'visited'] == 'n':
                self.data.loc[neighbours_id[p_id], 'visited'] = 'y'
                p_neighbours_id = self.find_neighbours_id(neighbours_id[p_id])
                if len(p_neighbours_id) >= self.m_pts:
                    neighbours_id.extend(p_neighbours_id)
            if self.belongToCluster(neighbours_id[p_id]) == 0:
                add_point = self.data.iloc[neighbours_id[p_id]]
                cluster.addPoint(add_point[0], add_point[1], add_point[2])
        return cluster

    def belongToCluster(self, point_rid):  # real id, not pd index
        belongs = 0
        if len(self.clusters) == 0:
            return 0  # doesnt matter that much. duplicate ids wont be added to dict inside cluster anyway
        for cl in xrange(0, self.cluster_number):
            if point_rid in self.clusters[cl].cluster_points:
                belongs = 1
                break
        return belongs


"""TEST BEGIN"""
dots = []
for x in xrange(0, 3):
    for i in xrange(0, 3):
        if x == i:
            dots.append((x, x, i))  # tryout with np.rand(id)

tochki = [(999, 999, 999), (9999, 9999, 9999), (12, 3, 6)]
# print "dots \n", dots
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

# print "clusters number is", db.cluster_number
# print "cluster ", db.cluster_number - 1
# print clusters[0].cluster_points
# print "cluster ", db.cluster_number
# print clusters[1].cluster_points
"""TEST END"""
