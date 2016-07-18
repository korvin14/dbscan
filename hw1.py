import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN


# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def euclidean(self, point):
#         return (self.x - point.x)**2 + (self.y - point.y)**2

def euclidian(point1, point2):
    return (point1.x - point2.x)**2 + (point1.y - point2.y)**2


class Cluster(object):
    def __init__(self):
        self.cl_id = 0

    def __init__(self, cl_id, cl_pts):
        self.cl_id = cl_id
        self.cl_pts = cl_pts

    def addPoint(self, p_id, p_x, p_y, p_type):
        pass


class myDBSCAN():
    def __init__(self, eps, mPts):
        self.eps = eps
        self.mPts = mPts

    # def clusterize():
    #     pass

    # def get


# pd.options.display.memory_usage = True #for >1.16
data = pd.read_csv("order201510-small.csv",
                   header=None, usecols=[0, 3, 4], names=['id', 'x', 'y'], dtype={'id': np.int32})
# , dtype={'id': np.int64, 'x': np.float.64, 'y': np.float.64}
# data.id = data.id.astype('int64')

print "head:"
print data.head()

# print "seprate"
# kekid, kekx, keky = data.iloc[1]
# # dont gorget to output as int
# print "kekid is {}; kekx is {}; while keky is {}".format(kekid, kekx, keky)

# print "real separate"
# print data.iloc[1][1], data.iloc[1][2]


# db = DBSCAN(eps=0.001, min_samples=4).fit(data)
# clusters = db.labels_
# number_clusters = len(set(clusters)) - (41 if -1 in clusters else 0)
# print number_clusters

print euclidian(data.iloc[1], data.iloc[1])
