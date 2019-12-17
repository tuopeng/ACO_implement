from ACO_implement.ACO_implement import ants
import numpy as np
import math
import sys
import random

x = []
y = []
K = np.zeros((48,48))
ants = []
str = open("ant_data").readlines()
citycount = int(str[0])
# print(list(range(citycount)))
for i in range(1,citycount+1):
    strbuff = str[i].split()
    x.append(int(strbuff[1]))
    y.append(int(strbuff[2]))

for i in range(citycount):
    for j in range(citycount):
        K[i][j] = math.sqrt(pow(x[i]-x[j],2)+pow(y[i]-y[j],2))
        # print("strbuff",strbuff)
# print("x[-1]:",x[-1])
# print("x:",x)
# print(K[5])
# print(math.sqrt(pow(x[5]-x[8],2)+pow(y[5]-y[8],2)))
# print(len(x))
# print(K[8][5])

# print(sys.maxsize)
#
# print(np.zeros((10)))

# class people:
#     a = 1
#     b = 0
#     def emp(self):
#         people.a = np.zeros((10))
#         people.b = np.zeros((10))
#     def boss(self):
#         for i in range(len(people.a)):
#             people.a[i] = 2
#             people.bossw(self)
#
#     def bossw(self):
#         for i in range(len(people.b)):
#             people.b[i] = 2
#
#
# g = people()
# g.emp()
# g.boss()
# print(g.a)

# from ACO_implement import ACO
#
# aco = ACO.ACO()
# aco.init("ant_data",100)
# acc = 1
# for i in range(1,49):
#     acc *= i
# print("acc:",acc)

a = np.zeros((5,5))
b = []
b.append()





# import numpy as np
# a = np.array([[np.nan, np.nan, 1, 2], [np.inf, np.inf, 3, 4], [1, 1, 1, 1], [2, 2, 2, 2]])
# print (a)
# where_are_nan = np.isnan(a)
# where_are_inf = np.isinf(a)
# a[where_are_nan] = 0
# a[where_are_inf] = 0
# print (a)
# print (np.mean(a))