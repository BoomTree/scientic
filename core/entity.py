# -*- coding: utf-8 -*-
"""
Created on Mon Apr 04 15:48:30 2016

@author: Coco
"""
import orm
#powerConsume,daytype,airPressureAve,airPressureMax,airPressureMin,temperatureAve,temperatureMax,temperatureMin,,waterPressureAve,relativeHumidityAve,relativeHumidityMin,precipitation,smallEvaporation,largeEvaporation,windVelocityAve,windVelocityMax,windVelocityDirection,extremeWindVelocity,extremeWindVelocityDir,hoursOfSunshine
order = ['date','cityName','year','month','day','daytype','detailNum','powerConsume','airPressureAve','airPressureMax','airPressureMin','temperatureAve','temperatureMax','temperatureMin','waterPressureAve','relativeHumidityAve','relativeHumidityMin','precipitation','smallEvaporation','largeEvaporation','windVelocityAve','windVelocityMax','windVelocityDirection','extremeWindVelocity','extremeWindVelocityDir','hoursOfSunshine']
fieldDescription = {
    'airPressureAve':'平均气压',
    'airPressureMax':'日最高气压',
    'airPressureMin':'日最低气压',
    'temperatureAve':'平均气温',
    'temperatureMax':'日最高气温',
    'temperatureMin':'日最低气温',
    'waterPressureAve':'平均水汽压',
    'relativeHumidityAve':'平均相对湿度',
    'relativeHumidityMin':'最小相对湿度',
    'precipitation':'20-20时降水量',
    'smallEvaporation':'小型蒸发量',
    'largeEvaporation':'大型蒸发量',
    'windVelocityAve':'平均风速',
    'windVelocityMax':'最大风速',
    'windVelocityDirection':'最大风速的风向',
    'extremeWindVelocity':'极大风速',
    'extremeWindVelocityDir':'极大风速的风向',
    'hoursOfSunshine':'日照时数',
    'cityName':'城市',
    'powerConsume':'电力负荷',
    'daytype':'星期',
    'detailNum':'数据数量',
    'date':'日期',
    'year':'年',
    'month':'月',
    'day':'日'
}

#print [fieldDescription.get(value).decode('utf-8') for value in order]
class Atmosphere(orm.Model):
    ast_his_id = orm.IntegerField(primary_key=True,updatable=False)
    cityName = orm.StringField()
    station_id = orm.StringField()
    date = orm.DateField()
    year = orm.IntegerField()
    month = orm.IntegerField()
    day = orm.IntegerField()
    airPressureAve = orm.IntegerField()
    airPressureMax = orm.IntegerField()
    airPressureMin = orm.IntegerField()
    temperatureAve = orm.IntegerField()
    temperatureMax = orm.IntegerField()
    temperatureMin = orm.IntegerField()
    waterPressureAve = orm.IntegerField()
    relativeHumidityAve = orm.IntegerField()
    relativeHumidityMin = orm.IntegerField()
    precipitation = orm.IntegerField()
    smallEvaporation = orm.IntegerField()
    largeEvaporation = orm.IntegerField()
    windVelocityAve = orm.IntegerField()
    windVelocityMax = orm.IntegerField()
    windVelocityDirection = orm.IntegerField()
    extremeWindVelocity = orm.IntegerField()
    extremeWindVelocityDir = orm.IntegerField()
    hoursOfSunshine = orm.IntegerField()

class PowerConsume(orm.Model):
    his_id = orm.IntegerField(primary_key=True,updatable=False)
    cityName = orm.StringField()
    powerConsume = orm.FloatField()
    date = orm.DateField()
    year = orm.IntegerField()
    month = orm.IntegerField()
    day = orm.IntegerField()
    daytype = orm.StringField()
    detailNum = orm.IntegerField()
    def __init__(self,**kw):
        super(PowerConsume,self).__init__(**kw)
        self['powerConsumeInt'] = int(self['powerConsume'] * 10**4)

class AP(Atmosphere,PowerConsume):
    his_id = orm.IntegerField(primary_key=True,updatable=False)
    
    def getAtmDict(self):
        return {'powerConsume':self.powerConsume,'daytype':self.daytype,'airPressureAve':self.airPressureAve,\
        'airPressureMax':self.airPressureMax,'airPressureMin':self.airPressureMin,'temperatureAve':self.temperatureAve,\
        'temperatureMax':self.temperatureMax,'temperatureMin':self.temperatureMin,'waterPressureAve':self.waterPressureAve,\
        'relativeHumidityAve':self.relativeHumidityAve,'relativeHumidityMin':self.relativeHumidityMin,'precipitation':self.precipitation,\
        'smallEvaporation':self.smallEvaporation,'largeEvaporation':self.largeEvaporation,'windVelocityAve':self.windVelocityAve,'windVelocityMax':self.windVelocityMax,\
        'extremeWindVelocity':self.extremeWindVelocity,\
        'hoursOfSunshine':self.hoursOfSunshine}
    def getAtmNorDict(self):
        return {'powerConsume':self.oneData['powerConsume'],'daytype':self.oneData['daytype'],'airPressureAve':self.oneData['airPressureAve'],\
        'airPressureMax':self.oneData['airPressureMax'],'airPressureMin':self.oneData['airPressureMin'],'temperatureAve':self.oneData['temperatureAve'],\
        'temperatureMax':self.oneData['temperatureMax'],'temperatureMin':self.oneData['temperatureMin'],'waterPressureAve':self.oneData['waterPressureAve'],\
        'relativeHumidityAve':self.oneData['relativeHumidityAve'],'relativeHumidityMin':self.oneData['relativeHumidityMin'],'precipitation':self.oneData['precipitation'],\
        'smallEvaporation':self.oneData['smallEvaporation'],'largeEvaporation':self.oneData['largeEvaporation'],'windVelocityAve':self.oneData['windVelocityAve'],'windVelocityMax':self.oneData['windVelocityMax'],\
        'extremeWindVelocity':self.oneData['extremeWindVelocity'],'hoursOfSunshine':self.oneData['hoursOfSunshine']
        }