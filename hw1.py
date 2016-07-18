import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def euclidean(point):
        return (self.x - point.x)**2 + (self.y - point.y)**2

# class Cluster():
#     def __init__(self, ):
#         self. = arg


# class Cluster():
#         def __init__(self, Point ):
#             self.arg = arg

# pd.options.display.memory_usage = True
data = pd.read_csv("order201510-small.csv",
                   header=None, usecols=[0, 3, 4], names=['id', 'x', 'y'], dtype={'id': np.int32})
# , dtype={'id': np.int64, 'x': np.float.64, 'y': np.float.64}
# data.id = data.id.astype('int64')

print "head:"
print data.head()

print "index"
print data.index

print "describe"
print data.describe()

print "trying to print first n samples"
print data[0:1]

print "some info"
print data.info()

print "seprate"
kekid, kekx, keky = data.iloc[1]
# dont gorget to output as int
print "kekid is {}; kekx is {}; while keky is {}".format(kekid, kekx, keky)

print "real separate"
print data.iloc[1][1], data.iloc[1][2]


# db = DBSCAN(eps=0.001, min_samples=4).fit(data)
# clusters = db.labels_
# number_clusters = len(set(clusters)) - (1 if -1 in clusters else 0)
# print number_clusters
