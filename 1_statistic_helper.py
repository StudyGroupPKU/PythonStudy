# -*- coding: UTF-8 -*-
import numpy as np
#from scipy.stats import mode
import scipy.stats

data = [1,2,3]
#print(data)
#print(type(data))

data_np = np.array([1,2,3])
#print(data_np)
#print(type(data_np))

data_np_ran_int = np.random.randint(0, 10, size = 10)
#print(type(data_np_ran_int))
#print(data_np_ran_int)

data_np_ran = np.random.normal(0,4, size = 10)
#print(type(data_np_ran))
#print(data_np_ran)

mean = np.mean(data_np_ran)
median = np.median(data_np_ran)
#print "mean value of data_np_ran :", mean
#print "median value of data_np_ran :",median


#极差（PTP）、方差（Variance）、标准差（STD）、变异系数（CV）偏差程度（z-分数: z-score）
PTP = np.ptp(data_np_ran)  # MAX_value - MIN_value
VAR = np.var(data_np_ran)
STD = np.var(data_np_ran)
CV = mean/STD
for i in range(data_np_ran.size):
    Z_SCORE = (data_np_ran[i]-mean) / STD
#    print(Z_SCORE)
#print(data_np_ran)
#print(PTP)
#print(VAR)
#print(STD)
#print(CV)


# 相关程度: 协方差（COV）和相关系数（CORRCOEF）
data_np_ran1 = np.random.normal(0,4, size = 10)
data_np_ran2 = np.random.normal(0,4, size = 10)
#print(data_np_ran1)
#print(data_np_ran2)
data_ran = np.append(data_np_ran1, data_np_ran2)
#print(data_ran.shape)
COV = np.cov(data, bias=1)  #参数bias=1表示结果需要除以N，否则只计算了分子部分
#print(COV)

data_ran = data_ran.reshape(2,10)
#print(data_ran.shape)
#print(data_ran)
COV = np.cov(data, bias=1)  #参数bias=1表示结果需要除以N，否则只计算了分子部分
#print(COV)

CORRCOEF = np.corrcoef(data_ran)  #corrcoef = COV / (STD1*STD2)
#print(CORRCOEF)





