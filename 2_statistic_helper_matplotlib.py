# -*- coding: UTF-8 -*-
# https://www.cnblogs.com/jasonfreak/p/5441512.html
from matplotlib import pyplot
from source_me_2 import genData
heights, weights, grades = genData()

#绘制柱状图
def drawBar(grades):
    xticks = ['A', 'B', 'C', 'D', 'E']
    gradeGroup = {}
    #对每一类成绩进行频数统计
    for grade in grades:
        gradeGroup[grade] = gradeGroup.get(grade, 0) + 1
    #创建柱状图
    #第一个参数为柱的横坐标
    #第二个参数为柱的高度
    #参数align为柱的对齐方式，以第一个参数为参考标准
    pyplot.bar(range(5), [gradeGroup.get(xtick, 0) for xtick in xticks], align='center')

    #设置柱的文字说明
    #第一个参数为文字说明的横坐标
    #第二个参数为文字说明的内容
    pyplot.xticks(range(5), xticks)

    #设置横坐标的文字说明
    pyplot.xlabel('Grade')
    #设置纵坐标的文字说明
    pyplot.ylabel('Frequency')
    #设置标题
    pyplot.title('Grades Of Male Students')
    #绘图
    pyplot.show()

drawBar(grades)
