import ants
import numpy as np
import math
import sys

class ACO:
    # 定义蚂蚁群
    ants = []
    antcount = 0 # 蚂蚁数量
    distance  = 0 #城市之间的距离
    tao = 0 #信息素矩阵
    citycount = 0 #城市数量
    besttour = 0 #求解的最佳路径
    bestlength = 0 #求解最优解的长度
    def __init__(self,filename,antnum):
        ACO.antcount = antnum
        #读取数据
        x = []
        y = []
        z = []
        str = open(filename).readlines()
        ACO.citycount = int(str[0])
        for i in range(1,ACO.citycount+1):
            strbuff = str[i].split()
            x.append(int(strbuff[1]))
            y.append(int(strbuff[2]))
#        计算距离矩阵，计算的是点之间的距离
        ACO.distance = np.zeros((ACO.citycount,ACO.citycount))
        for i in range(ACO.citycount):
            for j in range(ACO.citycount):
                ACO.distance[i][j] = math.sqrt(pow(x[i]-x[j],2)+pow(y[i]-y[j],2))
#         初始化信息矩阵
        ACO.tao = np.zeros((ACO.citycount,ACO.citycount))
        for i in range(ACO.citycount):
            for j in range(ACO.citycount):
                ACO.tao[i][j] = 0.1
        ACO.bestlength = sys.maxsize #最优路径长度
        ACO.besttour = np.zeros((ACO.citycount)) #最优路径
#         随机放置蚂蚁
#         for i in range(ACO.antcount):
#             ACO.ants.append(ants.ant())
#             ACO.ants[i].RandomSelectCity(ACO.citycount)
    """
    跟新信息素矩阵
    """
    def UpdateTao(self):
        rou = 0.5
        # 信息素挥发
        for i in range(ACO.citycount):
            for j in range(ACO.citycount):
                ACO.tao[i][j] = ACO.tao[i][j] *(1-rou)
        # 信息素更新
        for i in range(ACO.citycount):
            for j in range(ACO.citycount):
                ACO.tao[int(ACO.ants[i].Tour[j])][ACO.ants[i].Tour[j+1]]  += 1.0/ACO.ants[i].tourlength

        """
        ACO的运行过程
        maxgen ACO的最多次循环次数
        """
    def run(self,maxgen):
        # 每只蚂蚁移动的过程
        for runtimes in range(maxgen):
            # 随机放置蚂蚁
            for i in range(ACO.antcount):
                ACO.ants.append(ants.ant())
                ACO.ants[i].RandomSelectCity(ACO.citycount)
                for j in range(1,ACO.citycount):
                    ACO.ants[i].SelectNextCity(j,ACO.tao,ACO.distance)
                # 计算蚂蚁获得的路径的长度
                ACO.ants[i].CalTourLength(ACO.distance)
                if ACO.ants[i].tourlength < ACO.bestlength:
#                     保留最优路径
                    ACO.bestlength = ACO.ants[i].tourlength
                    print("第",runtimes+1,"次,发现解",ACO.bestlength)
                    for j in range(0,ACO.citycount):
                        ACO.besttour[j] = ACO.ants[i].Tour[j]
            ACO.UpdateTao(self)
            for i in range(ACO.antcount):
                ACO.ants[i].RandomSelectCity(ACO.citycount)

    """输出运行结果"""
    def ReportResult(self):
        print("最优路径长度是",ACO.bestlength)
        print("最优路径为：",ACO.besttour+1)
        # for i in range(len(ACO.besttour)):
        #     if i != len(ACO.besttour)-1:
        #         print(ACO.besttour[i],",")
        #     else:
        #         print(ACO.besttour[i])











# 车辆整体的分布热力图
# 需要调度的车辆热力图
# 调动区域的热力图
# 局部调度散点图
# 调度顺序图


