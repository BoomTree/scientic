# -*- coding: utf-8 -*-
import MySQLdb
from mmap import mmap,ACCESS_READ
from atmData import atmData
"""
Created on Wed Mar 23 12:59:37 2016

@author: Coco
"""
date = '2007-2-1'
cityName = 'shanwei'
try:
    conn = MySQLdb.connect(host='localhost',user='ly',passwd='ly',port=3306,db='powerforest',charset='utf8')
    cur = conn.cursor()
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
                	"ah.cityName = '%s' AND ah.date='%s' limit 1"%(cityName,date))

    atmResult = cur.fetchone()
    tomorrowAtm = atmData(atmResult[0],atmResult[1],atmResult[2],atmResult[3],atmResult[4],atmResult[5],atmResult[6],atmResult[7],atmResult[8],atmResult[9],atmResult[10],atmResult[11],atmResult[12],atmResult[13],atmResult[14],atmResult[15],atmResult[16],atmResult[17])
except MySQLdb.Error,e:
    print e.args[0],":",e.args[1]