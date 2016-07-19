import numpy as np
import pandas as pd
# import matplotlib.pyplot as plt
# from sklearn.cluster import DBSCAN


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
            if self.belongToCluster(neighbours.iloc[point_next]) == 0:
                self.Cluster.addPoint(neighbours.iloc[point_next])
            point_next += 1

    def belongToCluster(self, point):
        belongs = 0
        for cl in xrange(0, myDBSCAN.number_clusters):
            for p in xrange(0, self.clusters.shape[0]):
                if self.clusters[cl].id[p] == point.id[0]:
                    belongs = 1
                    break
                else:
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

__main__
data = pd.read_csv("order201510-small.csv", header=None,
                   usecols=[0, 3, 4], names=['id', 'x', 'y'],
                   dtype={'id': np.int32})
new_data = data.assign(visited=lambda x: 'n', noise=lambda x: 'n')

# d1 = d1.sort_values(['id'], ascending=[True])  # mb need sorting
