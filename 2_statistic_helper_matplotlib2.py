# -*- coding: UTF-8 -*-
from matplotlib import pyplot
from source_me_2 import genData
heights, weights, grades = genData()

#绘制饼形图
def drawPie(grades):
    labels = ['A', 'B', 'C', 'D', 'E']
    gradeGroup = {}
    for grade in grades:
        gradeGroup[grade] = gradeGroup.get(grade, 0) + 1
    #创建饼形图
    #第一个参数为扇形的面积
    #labels参数为扇形的说明文字
    #autopct参数为扇形占比的显示格式
    pyplot.pie([gradeGroup.get(label, 0) for label in labels], labels=labels, autopct='%1.1f%%')
    pyplot.title('Grades Of Male Students')
    pyplot.show()

drawPie(grades)
