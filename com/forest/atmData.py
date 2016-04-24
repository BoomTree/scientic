# -*- coding: utf-8 -*-
import data2one
import datetime
"""
Created on Tue Mar 22 12:38:20 2016

@author: Coco
"""

class atmData(object):
    def __init__(self,cityName=0,airPressureAve=0,airPressureMax=0,airPressureMin=0,temperatureAve=0,temperatureMax=0,temperatureMin=0,waterPressureAve=0,precipitation=0,windVelocityAve=0,windVelocityMax=0,hoursOfSunshine=0,dayType=0,powerConsume=0,detailNum='',year=0,month=0,day=0):
        self.cityName = cityName
        self.date = datetime.date(year,month,day)
#        print self.date
        self.airPressureAve = airPressureAve
        self.airPressureMax = airPressureMax
        self.airPressureMin = airPressureMin
        self.temperatureAve = temperatureAve
        self.temperatureMax = temperatureMax
        self.temperatureMin = temperatureMin
        self.waterPressureAve = waterPressureAve
        self.precipitation = precipitation
        self.windVelocityAve = windVelocityAve
        self.windVelocityMax = windVelocityMax
        self.hoursOfSunshine = hoursOfSunshine
        self.dayType = int(dayType)
        self.powerConsume = int(powerConsume * 10**4)
#        print self.powerConsume
        self.detailNum = detailNum
        self.oneData = {
            'airPressureAve':data2one.transform['airPressure'](airPressureAve),
            'airPressureMax':data2one.transform['airPressure'](airPressureMax),
            'airPressureMin':data2one.transform['airPressure'](airPressureMin),
            'temperatureAve':data2one.transform['temperature'](temperatureAve),   
            'temperatureMax':data2one.transform['temperature'](temperatureMax),   
            'temperatureMin':data2one.transform['temperature'](temperatureMin),
            'waterPressureAve':data2one.transform['waterPressure'](waterPressureAve),
            'precipitation':data2one.transform['precipitation'](precipitation),
            'windVelocityAve':data2one.transform['windVelocity'](windVelocityAve),
            'windVelocityMax':data2one.transform['windVelocity'](windVelocityMax),
            'hoursOfSunshine':data2one.transform['hoursOfSunshine'](hoursOfSunshine)
        }
        self.similarity = 0
    def printOne(self):
        print "%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f"%(self.oneData['airPressureAve'],self.oneData['airPressureMax'],self.oneData['airPressureMin'],self.oneData['temperatureAve'],self.oneData['temperatureMax'],self.oneData['temperatureMin'],self.oneData['waterPressureAve'],self.oneData['precipitation'],self.oneData['windVelocityAve'],self.oneData['windVelocityMax'],self.oneData['hoursOfSunshine'])
    def printDate(self):
        print "%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f"%(self.airPressureAve,self.airPressureMax,self.airPressureMin,self.temperatureAve,self.temperatureMax,self.temperatureMin,self.waterPressureAve,self.precipitation,self.windVelocityAve,self.windVelocityMax,self.hoursOfSunshine)
    def getList(self):
        return []