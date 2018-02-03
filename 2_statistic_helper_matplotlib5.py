# -*- coding: UTF-8 -*-
from matplotlib import pyplot
from source_me_2 import genData
heights, weights, grades = genData()

#绘制散点图
def drawScatter(heights, weights):
    #创建散点图
    #第一个参数为点的横坐标
    #第二个参数为点的纵坐标
    pyplot.scatter(heights, weights)
    pyplot.xlabel('Heights')
    pyplot.ylabel('Weights')
    pyplot.title('Heights & Weights Of Male Students')
    pyplot.show()

drawScatter(heights, weights)
