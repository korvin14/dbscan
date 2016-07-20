import numpy as np
import pandas as pd


class myDBSCAN():
    clusters = []
    cluster_number = 0

    def __init__(self, eps, m_pts, metric="euclidian"):
        self.eps = eps
        self.m_pts = m_pts
        self.metric = metric  # not used in current version

    class Cluster():

        def __init__(self):
            self.cl_id = myDBSCAN.cluster_number
            myDBSCAN.cluster_number += 1
            self.cluster_points = pd.DataFrame()

        def addPoint(self, point):
            # if : # CHECK IF WE ALREADY HAVE POINT WITH THIS ID??
            self.cluster_points = self.cluster_points.append(point)
            # else:
            #     pass

    def clusterize(self, input_data):
        self.data = input_data
        # del input_data  # needed??
        self.data_size = self.data.shape[0]
        for x in xrange(0, self.data_size):
            if self.data.loc[x, 'visited'] == 'y':
                pass  # not dummy
            self.data.set_value(x, 'visited', 'y')
            neighbours = self.find_neighbours(self.data.iloc[x])
            if neighbours.shape[0] < self.m_pts:
                self.data.noise[x] = 'y'
            else:
                new_cluster = self.Cluster()
                self.expandCluster(self.data.iloc[x], new_cluster, neighbours)
                myDBSCAN.clusters = myDBSCAN.clusters.append(new_cluster)
        return myDBSCAN.clusters

    def expandCluster(self, point, cluster, neighbours):
        cluster.addPoint(point)
        point_next = 0
        while neighbours.iloc[point_next]:
            if neighbours.visited[point_next] == 'n':
                neighbours.visited[point_next] = 'y'
                self.data.visited[point_next] = 'y'  # kostyl'
                neighbours_next = self.find_neighbours(
                    neighbours.iloc[point_next])
                if neighbours_next.shape[0] >= self.m_pts:
                    neighbours = neighbours.append(neighbours_next)
            if self.belongToCluster(neighbours.iloc[point_next]) == 0:
                cluster.addPoint(neighbours.iloc[point_next])
            point_next += 1

    def euclidian(self, point1, point2):
        return (point1[1] - point2[1])**2 + (point1[2] - point2[2])**2

    def find_neighbours(self, point):
        neighbours = pd.DataFrame()
        for x in xrange(0, self.data_size):
            if self.euclidian(point, self.data.iloc[x]) < self.eps:
                neighbours = neighbours.append(self.data.iloc[x])
        return neighbours

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

pd.set_option('mode.chained_assignment', 'warn')
data = pd.read_csv("order201510-small.csv", header=None,
                   usecols=[0, 3, 4], names=['id', 'x', 'y'],
                   dtype={'id': np.int32})
upd_data = data.assign(visited=lambda x: 'n', noise=lambda x: 'n')

# db = myDBSCAN(eps=0.001, m_pts=4)
# d1 = d1.sort_values(['id'], ascending=[True])  # mb need sorting
# clusters = db.clusterize(upd_data)
# print clusters

print upd_data.head(10)
upd_data.set_value(0, 'visited', 'y')  # updates without making new ref
print "set value"
print upd_data.head(10)

dots = []
for x in xrange(0, 20):
    for i in xrange(0, 20):
        if x == i:
            dots.append((x, x, i))  # tryout with np.rand(id)
# print dots

# dots2 = []
for x in xrange(50, 70):
    for i in xrange(50, 70):
        if x == i:
            dots.append((x - 30, x, i))
# print dots

test_data = pd.DataFrame(data=dots, columns=['id', 'x', 'y'])
test_data = test_data.assign(visited=lambda x: 'n', noise=lambda x: 'n')
print test_data
db = myDBSCAN(eps=1, m_pts=5)
# clusters = db.clusterize(upd_data)
# print clusters.cluster_number
print test_data.loc[15, 'visited']
