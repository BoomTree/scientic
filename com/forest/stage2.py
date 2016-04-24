# -*- coding: utf-8 -*-
import stage1
import tomorrowAtm
from math import sqrt
from copy import deepcopy
from atmWeight import atmWeight
"""
Created on Wed Mar 23 12:43:25 2016
计算相似度：方式一  （依此类推，stage3为方式二）
后面考虑用接口，方便扩展
计算相似度所用的atms对象均从stage1深度拷贝atms
需要预测的天气数据，从tomorrowAtm.py获得——tomorrowAtm
@author: Coco
"""
atms = deepcopy(stage1.atms)
tomAtm = deepcopy(tomorrowAtm.tomorrowAtm)

#for index in range(len(atms)):
#    atms[index].printOne()
#    atms[index].printDate()
    
def calculateSimilarity(his,tom):
    his_keys = his.oneData.keys()
    sum = 0
    for index in his_keys:
        sum += atmWeight[index] * (1-his.oneData[index]+tom.oneData[index])**2
    similarity = sqrt(sum)
    his.similarity = similarity
#    !!!calculate similarity and asign similarity!!!
for index in range(len(atms)):
    calculateSimilarity(atms[index],tomAtm)
#for index in range(len(atms)):
#    print atms[index].similarity
    
#    !!!sort atms by similarity !!!
atms.sort(key=lambda atmData:atmData.similarity,reverse=True)
#print '-------------------------'
#for index in range(len(atms)):
#    print atms[index].similarity
atmsList = []
for atm in atms:
    atmsList.append([atm.oneData['airPressureAve'],atm.oneData['airPressureMax'],atm.oneData['airPressureMin'],atm.oneData['temperatureAve'],atm.oneData['temperatureMax'],atm.oneData['temperatureMin'],atm.oneData['waterPressureAve'],atm.oneData['precipitation'],atm.oneData['windVelocityAve'],atm.oneData['windVelocityMax'],atm.oneData['hoursOfSunshine'],atm.dayType,atm.powerConsume])
#print atmsList[0]
#for num in atmsList[0]:
#    print type(num)
tomorrowAtmList = [tomAtm.oneData['airPressureAve'],tomAtm.oneData['airPressureMax'],tomAtm.oneData['airPressureMin'],tomAtm.oneData['temperatureAve'],tomAtm.oneData['temperatureMax'],tomAtm.oneData['temperatureMin'],tomAtm.oneData['waterPressureAve'],tomAtm.oneData['precipitation'],tomAtm.oneData['windVelocityAve'],tomAtm.oneData['windVelocityMax'],tomAtm.oneData['hoursOfSunshine'],tomAtm.dayType,tomAtm.powerConsume]