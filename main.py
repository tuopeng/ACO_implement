import ACO

aco = ACO.ACO("ant_data",1000)
# aco.init("ant_data",1000)
#点数量为50，蚂蚁数量
aco.run(200)

aco.ReportResult()



