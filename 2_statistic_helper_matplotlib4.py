# -*- coding: UTF-8 -*-
from matplotlib import pyplot
from source_me_2 import genData
heights, weights, grades = genData()

#绘制累积曲线
def drawCumulativeHist(heights):
    #创建累积曲线
    #第一个参数为待绘制的定量数据
    #第二个参数为划分的区间个数
    #normed参数为是否无量纲化
    #histtype参数为'step'，绘制阶梯状的曲线
    #cumulative参数为是否累积
    pyplot.hist(heights, 20, normed=True, histtype='step', cumulative=True)
    pyplot.xlabel('Heights')
    pyplot.ylabel('Frequency')
    pyplot.title('Heights Of Male Students')
    pyplot.show()

drawCumulativeHist(heights)
