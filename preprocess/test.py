# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 10:53:22 2016

@author: Coco
"""
import MySQLdb
from mmap import mmap
import datetime

dt = datetime.datetime(2007,4,1)
print dt

dt = dt+datetime.timedelta(0,15*60)
print dt

try:
    conn = MySQLdb.connect(host='localhost',user='ly',passwd='ly',port=3306,db='powerforest',charset='utf8')
    cur = conn.cursor()
    cur.execute("SELECT "+
            	"MAX(ah.airPressureMax) as airPressureMax,"+
            	"MIN(ah.airPressureMin) as airPressureMin,"+
            	"MAX(ah.temperatureMax) as temperatureMax,"+
            	"MIN(ah.temperatureMin) as temperatureMin,"+
            	"MAX(ah.waterPressureAve) as waterPressureMax,"+
            	"MIN(ah.waterPressureAve) as waterPressureMin,"+
            	"MAX(ah.`20-20precipitation`) as `20-20precipitationMax`,"+
            	"MAX(ah.smallEvaporation) as smallEvaporationMax,"+
            	"MIN(ah.smallEvaporation) as smallEvaporationMin,"+
            	"MAX(ah.largeEvaporation) as largeEvaporationMax,"+
            	"MIN(ah.largeEvaporation) as largeEvaporationMin,"+
            	"MAX(ah.windVelocityMax) as windVelocityMax,"+
            	"MAX(ah.hoursOfSunshine) as hoursOfSunshineMax,"+
            	"MIN(ah.hoursOfSunshine) as hoursOfSunshineMin"+
             " FROM "+
            	"atmosphere_history ah"+
             " where cityname='"+cityName+"'")
    result = cur.fetchone();
    print result
except MySQLdb.Error,e:
    print e.args[0],":",e.args[1]