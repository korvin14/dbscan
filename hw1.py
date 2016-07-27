import numpy as np
# import pandas as pd
import time
import csv

# seems to not work on big set with some condition. debug.


class myDBSCAN():
    clusters_number = 0

    def __init__(self, eps, m_pts, metric="euclidianSquared"):
        self.eps = eps
        self.m_pts = m_pts
        self.clusters = []

    class Cluster():
        def __init__(self):
            self.points = {}
            print "cl # ", myDBSCAN.clusters_number
            myDBSCAN.clusters_number += 1

        # noise and visited is only for myDBSCAN.data. clustered points doesnt
        # need it
        def addPoint(self, id, x, y):
            xy = (x, y)  # tuple because we just need to store it
            # print "id {} x {} y {}".format(id, x, y)
            self.points[id] = xy

    def clusterize(self, input_data):
        self.data = input_data
        self.data_size = len(self.data)
        for x in xrange(0, self.data_size):
            if self.data[x][3] == 0:
                self.data[x][3] = 1
                neighbours_ids = self.find_neighbours_ids(x)
                if (len(neighbours_ids) < self.m_pts):
                    self.data[x][4] = 1
                else:
                    new_cluster = self.Cluster()
                    new_cluster = self.expandCluster(
                        self.data[x], new_cluster, neighbours_ids)
                    self.clusters.append(new_cluster)
        return self.clusters

    def find_neighbours_ids(self, pt_id):  # point number in table
        neighbours_ids = []
        for check_point_id in xrange(0, self.data_size):
            if self.euclidianSquared(self.data[pt_id],
                                     self.data[check_point_id]) < self.eps:
                neighbours_ids.append(check_point_id)
        return neighbours_ids

    def euclidianSquared(self, point1, point2):
        """Calculates distance without sqrt"""
        return (point1[1] - point2[1])**2 + (point1[2] - point2[2])**2

    def expandCluster(self, point, cluster, neighbours_ids):
        cluster.addPoint(point[0], point[1], point[2])
        for p_id, el in enumerate(neighbours_ids):
            # cuz of the enum - make every neighbs_id el[p_id]??
            if self.data[el][3] == 0:
                self.data[el][3] = 1
                el_neighbours_id = self.find_neighbours_ids(el)
                if len(el_neighbours_id) >= self.m_pts:
                    neighbours_ids.extend(el_neighbours_id)
            if self.belongToCluster(self.data[el][0]) == 0:
                add_point = self.data[el]
                cluster.addPoint(add_point[0], add_point[1], add_point[2])
        return cluster

    def belongToCluster(self, point_rid):  # real id, not self.data DF index
        belongs = 0
        if len(self.clusters) == 0:
            return 0  # doesnt matter that much. duplicate ids wont be added to dict inside cluster anyway
        for cl in self.clusters:
            if point_rid in cl.points:
                belongs = 1
                break
        return belongs


"""TEST BEGIN"""
dots = []
for x in xrange(0, 3):
    for i in xrange(0, 3):
        if x == i:
            dots.append([x, x, i, 0, 0])  # tryout with np.rand(id)
for x in xrange(50, 53):
    for i in xrange(50, 53):
        if x == i:
            dots.append([x - 47, x, i, 0, 0])
dots.append([145, 100, 100, 0, 0])
dots.append([146, 100, 100, 0, 0])

print dots

db = myDBSCAN(eps=3, m_pts=2)
clusters = db.clusterize(dots)
print "number of cluster overall - ", len(clusters)
cl_count = 0
for i in clusters:
    print "cluster #", cl_count
    print "points ", i.points
    cl_count += 1

"""REAL DATA"""
# print "start reading data"
# start = time.time()
# table = []
# with open("order201510-small.csv", "rb") as f:
#     lines = csv.reader(f, delimiter=',')
#     for one in lines:
#         table.append([int(one[0]), np.float64(
#             one[3]), np.float64(one[4]), 0, 0])
# print len(table)
# print table
# print "finished reading data in {}s".format(time.time() - start)

# start = time.time()
# db = myDBSCAN(eps=0.001, m_pts=4)
# print "ported data"
# clusters = db.clusterize(table)
# print db.clusters_number
# print "finished clustering in {} s".format(start - time.time())
