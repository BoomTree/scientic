# -*- coding: utf-8 -*-
import MySQLdb
from mmap import mmap,ACCESS_READ
from atmData import atmData
"""
Created on Tue Mar 22 10:55:34 2016
获得气象参数、电力负荷的数据，并封装在atmData对象中，用作公公调用
@author: Coco
"""
cityName = 'shanwei'
startDate = '2007-01-01'
endDate = '2007-01-31'

atms = []
try:
    conn = MySQLdb.connect(host='localhost',user='ly',passwd='ly',port=3306,db='powerforest',charset='utf8')
    cur = conn.cursor()
    
#    获得历史日的数据
    cur.execute("SELECT "+
                	"ah.cityName,"+
                	"ah.airPressureAve,"+
                	"ah.airPressureMax,"+
                	"ah.airPressureMin,"+
                	"ah.temperatureAve,"+
                	"ah.temperatureMax,"+
                	"ah.temperatureMin,"+
                	"ah.waterPressureAve,"+
                	"ah.`20-20precipitation`,"+
                	"ah.windVelocityAve,"+
                	"ah.windVelocityMax,"+
                	"ah.hoursOfSunshine,"+
                	"sh.daytype,"+
                	"sh.powerConsume,"+
                	"sh.detailNum,"+
                	"sh.year,"+
                	"sh.month,"+
                	"sh.day "+
                "FROM "+
                	"atmosphere_history ah "+
                "INNER JOIN "+
                	"sw_history sh ON ah.date = sh.date and ah.cityName = sh.cityName "+
                "WHERE "+
                	"ah.cityName = '%s' AND ah.date >= '%s' AND ah.date <= '%s' order by ah.date"%(cityName,startDate,endDate))

    atmResult = cur.fetchall()
    for index in range(len(atmResult)):
        atms.append(atmData(atmResult[index][0],atmResult[index][1],atmResult[index][2],atmResult[index][3],atmResult[index][4],atmResult[index][5],atmResult[index][6],atmResult[index][7],atmResult[index][8],atmResult[index][9],atmResult[index][10],atmResult[index][11],atmResult[index][12],atmResult[index][13],atmResult[index][14],atmResult[index][15],atmResult[index][16],atmResult[index][17]))
    
    
except MySQLdb.Error,e:
    print e.args[0],":",e.args[1]

#print atms