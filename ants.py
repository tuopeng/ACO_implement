import numpy as np
import random
import math


class ant:
    Tour = 0
    unvisitedcity = 0
    tourlength = 0
    citys = 0
    count = 0
    def RandomSelectCity(self,citycount):
        ant.citys = citycount
        ant.tourlength = 0
        ant.Tour = np.zeros((citycount+1),int)
        ant.unvisitedcity = np.ones((citycount))

        for i in np.arange(citycount):
            ant.Tour[i] = -1
        firstcity = random.randint(0,citycount-1)
        ant.unvisitedcity[firstcity] = 0 #0表示已经访问过
        ant.Tour[0] = firstcity #起始城市

    def SelectNextCity(self,index,tao,distance):
        p = np.zeros((ant.citys))  #citys
        x = 0
        alpha = 1.0
        beta = 2.0
        sum = 0
        currentcity = ant.Tour[index-1]
              # print("curr",ant.Tour)
        # print(ant.unvisitedcity)
        for i in range(ant.citys):
            # print(ant.unvisitedcity[i])
            if ant.unvisitedcity[i] == 1:
                sum += (math.pow(tao[currentcity][i], alpha) * math.pow(1.0/distance[currentcity][i], beta))
        #        计算每个城市被选中的概率
        for i in range(ant.citys):
            if ant.unvisitedcity[i] == 0:
                p[i] = 0.0
            else:
                p[i] = (math.pow(tao[currentcity][i], alpha) * math.pow(1.0/distance[currentcity][i], beta))/sum
        selectp = random.random()
#       轮盘赌选择一个城市
        sumselect = 0.0
        selectcity = -1
        for i in  range(ant.citys):
            sumselect += p[i]
            # print("i",i,"sumselect",sumselect)
            if sumselect >= selectp:
                selectcity = i
                break

        if selectcity == -1:
            print('')
        ant.Tour[index] = selectcity
        # print("selectcity",selectcity)
        ant.unvisitedcity[selectcity] = 0
        # print(ant.Tour)

#         计算蚂蚁获得的路径的长度
#         distance 全局的距离矩阵信息
    def CalTourLength(self,distance):
        ant.Tour[ant.citys] = ant.Tour[0]
        for i in range(ant.citys):
            ant.tourlength += distance[int(ant.Tour[i])][int(ant.Tour[i+1])]
































