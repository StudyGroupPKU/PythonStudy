# -*- coding: UTF-8 -*-
from matplotlib import pyplot
from source_me_2 import genData
heights, weights, grades = genData()

#绘制箱形图
def drawBox(heights):
    #创建箱形图
    #第一个参数为待绘制的定量数据
    #第二个参数为数据的文字说明
    #pyplot.boxplot([heights], labels=['Heights'])
    pyplot.boxplot([heights])
    pyplot.title('Heights Of Male Students')
    pyplot.show()

drawBox(heights)


