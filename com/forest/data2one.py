# -*- coding: utf-8 -*-
import MySQLdb
from mmap import mmap,ACCESS_READ
"""
Created on Tue Mar 22 11:12:36 2016

@author: Coco
"""
cityName = 'shanwei'
year = 2007
data = "airPressureMax,airPressureMin,temperatureMax,temperatureMin,waterPressureMax,waterPressureMin,relativeHumidityMax,relativeHumidityMin,`20-20precipitationMax`,`20-20precipitationMin`,evaporationMax,evaporationMin,winVelocityMax,winVelocityMin,hoursOfSunshineMax,hoursOfSunshineMin"
airPressureAve,airPressureMax,airPressureMin,temperatureAve,temperatureMax,temperatureMin,,waterPressureAve,relativeHumidityAve,relativeHumidityMin,precipitation,smallEvaporation,largeEvaporation,windVelocityAve,windVelocityMax,windVelocityDirection,extremeWindVelocity,extremeWindVelocityDir,hoursOfSunshine




try:
    conn = MySQLdb.connect(host='localhost',user='ly',passwd='ly',port=3306,db='powerforest',charset='utf8')
    cur = conn.cursor()
    cur.execute("SELECT %s FROM `atmosphere_history_analyze` where year='%i' and cityName='%s' limit 1"%(data,year,cityName))
    r = cur.fetchone()
    one={
        'airPressureMax':r[0],
        'airPressureMin':r[1],
        'temperatureMax':r[2],
        'temperatureMin':r[3],
        'waterPressureMax':r[4],
        'waterPressureMin':r[5],
        'relativeHumidityMax':r[6],
        'relativeHumidityMin':r[7],
        'precipitationMax':r[8],
        'precipitationMin':r[9],
        'evaporationMax':r[10],
        'evaporationMin':r[11],
        'winVelocityMax':r[12],
        'winVelocityMin':r[13],
        'hoursOfSunshineMax':r[14],
        'hoursOfSunshineMin':r[15]
    }

except MySQLdb.Error,e:
    print e.args[0],":",e.args[1]


def _airPressure(date):
    return float((date-one['airPressureMin'])/(one['airPressureMax']-one['airPressureMin']))
def _temperature(date):
    return float((date-one['temperatureMin'])/(one['temperatureMax']-one['temperatureMin']))
def _waterPressure(date):
    return float((date-one['waterPressureMin'])/(one['waterPressureMax']-one['waterPressureMin']))
def _precipitation(date):
    return float((date-one['precipitationMin'])/(one['precipitationMax']-one['precipitationMin']))
def _windVelocity(date):
    return float((date-one['winVelocityMin'])/(one['winVelocityMax']-one['winVelocityMin']))
def _hoursOfSunshine(date):
    return float((date-one['hoursOfSunshineMin'])/(one['hoursOfSunshineMax']-one['hoursOfSunshineMin']))
    
transform = {
    'airPressure':_airPressure,
    'temperature':_temperature,
    'waterPressure':_waterPressure,
    'precipitation':_precipitation,
    'windVelocity':_windVelocity,
    'hoursOfSunshine':_hoursOfSunshine
}
