import numpy as np
import pandas as pd


"""TEST BEGIN"""
dots = []
for x in xrange(0, 3):
    for i in xrange(0, 3):
        if x == i:
            dots.append((x, x, i))  # tryout with np.rand(id)
# print "dots \n", dots
# for x in xrange(50, 53):
#     for i in xrange(50, 53):
#         if x == i:
#             dots.append((x - 47, x, i))

pd.set_option('mode.chained_assignment', 'warn')
test_data = pd.DataFrame(data=dots, columns=['id', 'x', 'y'])
test_data = test_data.assign(visited=lambda x: 'n', noise=lambda x: 'n')
print test_data
# db = myDBSCAN(eps=3, m_pts=2)
# clusters = db.clusterize(test_data)
# print "clusters number is", db.cluster_number
# print "cluster ", db.cluster_number - 1
# print clusters[0].cluster_points
# print "cluster ", db.cluster_number
# print clusters[1].cluster_points
"""TEST END"""
