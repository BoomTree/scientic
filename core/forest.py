# -*- coding: utf-8 -*-
"""
Created on Mon Apr 04 16:51:04 2016

@author: Coco
"""

import entity,utiles,db
from datetime import datetime,timedelta
from math import sqrt


from sklearn.svm import SVC

Stage = utiles.enum(INIT=0,SETDATA=1,NORMALIZE=2,SIMILARITY=3)


def _normalizationMetaData():
    res = db.select("SELECT\
                    	MAX(ah.airPressureMax) as airPressureMax,\
                    	MIN(ah.airPressureMin) as airPressureMin,\
                    	MAX(ah.temperatureMax) as temperatureMax,\
                    	MIN(ah.temperatureMin) as temperatureMin,\
                    	MAX(ah.waterPressureAve) as waterPressureMax,\
                    	MIN(ah.waterPressureAve) as waterPressureMin,\
                    	MAX(ah.relativeHumidityAve) as relativeHumidityMax,\
                    	MIN(ah.relativeHumidityMin) as relativeHumidityMin,\
                    	MAX(ah.precipitation) as precipitationMax,\
                    	MIN(ah.precipitation) as precipitationMin,\
                    	MAX(ah.smallEvaporation) as smallEvaporationMax,\
                    	MIN(ah.smallEvaporation) as smallEvaporationMin,\
                    	MAX(ah.largeEvaporation) as largeEvaporationMax,\
                    	MIN(ah.largeEvaporation) as largeEvaporationMin,\
                    	(CASE WHEN MAX(ah.windVelocityMax)>MAX(ah.extremeWindVelocity) THEN MAX(ah.windVelocityMax) ELSE MAX(ah.extremeWindVelocity) END) as windVelocityMax,\
                    	(CASE WHEN MIN(ah.windVelocityAve)<MIN(ah.extremeWindVelocity) THEN MIN(ah.windVelocityAve) ELSE MIN(ah.extremeWindVelocity) END) as windVelocityMin,\
                    	MAX(ah.hoursOfSunshine) as hoursOfSunshineMax,\
                    	MIN(ah.hoursOfSunshine) as hoursOfSunshineMin\
                     FROM\
                    	atmosphere_history ah\
                    where\
                    	ah.cityName = 'shanwei';")
    res = res[0]
    for key in res.iterkeys():
        res[key] = int(res[key])
    return res

md = _normalizationMetaData()
normalize = {
    'airPressure':lambda airPressure : float((airPressure-md['airPressureMin']))/(md['airPressureMax']-md['airPressureMin']),
    'temperature':lambda temperature : float((temperature-md['temperatureMin']))/(md['temperatureMax']-md['temperatureMin']),
    'waterPressure':lambda waterPressure : float((waterPressure-md['waterPressureMin']))/(md['waterPressureMax']-md['waterPressureMin']),
    'relativeHumidity':lambda relativeHumidity : float((relativeHumidity-md['relativeHumidityMin']))/(md['relativeHumidityMax']-md['relativeHumidityMin']),
    'precipitation':lambda precipitation : float((precipitation-md['precipitationMin']))/(md['precipitationMax']-md['precipitationMin']),
#    'smallEvaporation':lambda smallEvaporation : float((smallEvaporation-md['smallEvaporationMin']))/(md['smallEvaporationMax']-md['smallEvaporationMin']),
    'largeEvaporationMax':lambda largeEvaporationMax : float((largeEvaporationMax-md['largeEvaporationMin']))/(md['largeEvaporationMax']-md['largeEvaporationMin']),
    'windVelocity':lambda windVelocity : float((windVelocity-md['windVelocityMin']))/(md['windVelocityMax']-md['windVelocityMin']),
    'hoursOfSunshine':lambda hoursOfSunshine : float((hoursOfSunshine-md['hoursOfSunshineMin']))/(md['hoursOfSunshineMax']-md['hoursOfSunshineMin']),
    'windVelocityDir':lambda windVelocityDir : float((windVelocityDir-1))/(16-1)
}

def normalizeAP(ap):
    oneData = {}
    oneData['airPressureAve'] = normalize['airPressure'](ap.airPressureAve)
    oneData['airPressureMax'] = normalize['airPressure'](ap.airPressureMax)
    oneData['airPressureMin'] = normalize['airPressure'](ap.airPressureMin)
    oneData['temperatureAve'] = normalize['temperature'](ap.temperatureAve)
    oneData['temperatureMax'] = normalize['temperature'](ap.temperatureMax)
    oneData['temperatureMin'] = normalize['temperature'](ap.temperatureMin)
    oneData['waterPressureAve'] = normalize['waterPressure'](ap.waterPressureAve)
    oneData['relativeHumidityAve'] = normalize['relativeHumidity'](ap.relativeHumidityAve)
    oneData['relativeHumidityMin'] = normalize['relativeHumidity'](ap.relativeHumidityMin)
    oneData['precipitation'] = normalize['precipitation'](ap.precipitation)
#    oneData['smallEvaporation'] = normalize['smallEvaporation'](ap.smallEvaporation)
    oneData['largeEvaporation'] = normalize['largeEvaporationMax'](ap.largeEvaporation)
    oneData['windVelocityAve'] = normalize['windVelocity'](ap.windVelocityAve)
    oneData['windVelocityMax'] = normalize['windVelocity'](ap.windVelocityMax)
    oneData['extremeWindVelocity'] = normalize['windVelocity'](ap.extremeWindVelocity)
    oneData['hoursOfSunshine'] = normalize['hoursOfSunshine'](ap.hoursOfSunshine)
    oneData['windVelocityDirection'] = normalize['windVelocityDir'](ap.windVelocityDirection)
    oneData['extremeWindVelocityDir'] = normalize['windVelocityDir'](ap.extremeWindVelocityDir)
    
    #设置日期类型变量
    oneData['Monday'] = 0
    oneData['Tuesday'] = 0
    oneData['Wednesday'] = 0
    oneData['Thursday'] = 0
    oneData['Friday'] = 0
    oneData['Saturday'] = 0
    oneData['Sunday'] = 0
    if ap.daytype==0:
        oneData['Monday'] = 1
    if ap.daytype==1:
        oneData['Tuesday'] = 1
    if ap.daytype==2:
        oneData['Wednesday'] = 1
    if ap.daytype==3:
        oneData['Thursday'] = 1
    if ap.daytype==4:
        oneData['Friday'] = 1
    if ap.daytype==5:
        oneData['Saturday'] = 1
    if ap.daytype==6:
        oneData['Sunday'] = 1
    ap.oneData = oneData

    
normalizeList = {'min-max标准化':normalizeAP}

def _countRelevancy():
    '''
    用于计算缺省的相关度，默认会赋值给relevancy全局变量
    '''
    data = db.select("select ah.airPressureAve,ah.airPressureMax,ah.airPressureMin,ah.temperatureAve,ah.temperatureMax,ah.temperatureMin,ah.waterPressureAve,ah.relativeHumidityAve,ah.relativeHumidityMin,ah.precipitation,ah.smallEvaporation,ah.largeEvaporation,ah.windVelocityAve,ah.windVelocityMax,ah.windVelocityDirection,ah.extremeWindVelocity,ah.extremeWindVelocityDir,ah.hoursOfSunshine,sh.daytype,sh.powerConsume from atmosphere_history ah INNER JOIN sw_history sh on ah.date = sh.date where sh.detailNum=96 ORDER BY ah.date") 
    powerConsumes = []
    atm = {}
    rel = {}
        
    
    for row in data:
        powerConsumes.append(float(row['powerConsume']))
        row.pop('powerConsume')
    for key in data[0].iterkeys():
        atm[key] = []
        rel[key] = 0
    for row in data:
        for key,val in row.iteritems():
            atm[key].append(int(val))
    for key in rel.iterkeys():
        rel[key] = utiles.sim_pearson(atm[key],powerConsumes)

    # 计算前七天的相关度
    # rel['oneday'] = utiles.sim_pearson(powerConsumes[1:],powerConsumes[0:len(powerConsumes)-1])
    # rel['twoday'] = utiles.sim_pearson(powerConsumes[2:],powerConsumes[0:len(powerConsumes)-2])
    # rel['threeday'] = utiles.sim_pearson(powerConsumes[3:],powerConsumes[0:len(powerConsumes)-3])
    # rel['fourday'] = utiles.sim_pearson(powerConsumes[4:],powerConsumes[0:len(powerConsumes)-4])
    # rel['fiveday'] = utiles.sim_pearson(powerConsumes[5:],powerConsumes[0:len(powerConsumes)-5])
    # rel['sixday'] = utiles.sim_pearson(powerConsumes[6:],powerConsumes[0:len(powerConsumes)-6])
    # rel['sevenday'] = utiles.sim_pearson(powerConsumes[7:],powerConsumes[0:len(powerConsumes)-7])

    return rel
relevancy = _countRelevancy()
print
relevancyList = {'威尔逊算法（全年数据）':relevancy}

def calculateSimilarity(early,predict,rel=relevancy,minRel=0.2):
    '''
    用于计算两个dict的相似度
    
    参数：
    early(dict)        :    历史日的气象数据
    predict(dict)      :    待预测日的气象数据
    rel(dict)          :    相关度系数
    minRel(int)        :    最小相关系数
    '''
    sum = 0
    for key in rel.iterkeys():
        if abs(rel[key])>minRel:
            sum += abs(rel[key]) * (1-early[key]+predict[key])**2
    return sqrt(sum)

similarityList = {'欧几里得距离':calculateSimilarity}

def APCompareSimilarity(a,b):
    '''
    用于AP对象的基于_similarity的比较
    
    参数:
    a(AP)    :    需要比较的AP对象1
    b(AP)    :    需要比较的AP对象2
    
    '''
    if a._similarity < b._similarity:
        return -1
    return 1

predictModel = {'支持向量机':SVC()}

class BaseForest(object):
    '''
    电力负荷预测核心类
    
    参数：
    stage(int)                  :    进行的阶段 INIT=0,PREPARE=1,PREDICTING=2,PREDICTED=3
    rel(list)                   :    特征量和电力负荷的皮尔逊相关系数列表  默认为relevancy
    minRel (float)              :    过滤相关性小的特征量 默认0.2
    source(list(AP))            :    历史气象、电力负荷数据
    forest(list(AP))            :    待预测的气象数据
    expect(list)                :    用于测试，待预测日真实电力负荷
    predictPC(list)             ：   预测值
    countNum(int)               :    相似度筛选数量
    
    similarityList(list(list(int))): 历史日的气象数据值（经过归一化，二维数组，数值）
    similarityPCList(list(int)) :    历史日的电力负荷
    forestList(list((list(int))):    待预测日的气象数据值（经过归一化，二维数组，数值）
    keyList(list(string))       :    similarityList、forestList是数组，数值没有下表，通过keyList和他们的数值表示内容一一对应
    similarity(list(list(AP)))  :    待预测日与历史日气象的相似度列表，第一个list长度等于forest，第二个list为切片长度等于source，切片后等于countNum
    similarityValue(list[list[int]]):similarity的具体相似值
    doSimilarity(method)        :    相似度计算函数
    predictModel(object)        :    智能预测的方法，有SVM等
    predictWithForestData(bool) :    是否利用预测得到的电力负荷值，进行后面的预测
    evaluation(list)            :    计算expect和predictPC的误差
    基本使用
    bf = forest.BaseForest()
    bf.setData(40,"2007-04-04",4)    
    '''
    def __init__(self):

        self.stage = Stage.INIT
        self.rel = relevancy
        self.normalize = normalizeAP
        self.minRel = 0.6
        self.source = []
        self.forest = []
        self.expect = []
        self.predictPC = []
        self.countNum = 20
        
        #以下用于预测
        self.similarityList = []
        self.forestList = []
        self.keyList = []
        self.similarity = []
        self.similarityValue = []
        self.doSimilarity = calculateSimilarity
        self.predictModel = SVC()
        self.predictWithForestData = False
        self.evaluation = []
    
    def setData(self,sourceNum,startDate,forestNum):
        '''
        参数：
        sourceNum(int)       :    历史日的天数
        startDate(str)       :    需要预测的日期（格式：'2007-4-5'）
        forestNum(str)       :    需要预测的天数，包含startDate向后数forestNum天
        
        
        '''
        
        d = datetime.strptime(startDate,"%Y-%m-%d")
        #计算历史日的第一天的日期
        preDate = (d+timedelta(-sourceNum)).strftime("%Y-%m-%d")
        #计算待预测日的最后一天的日期
        endDate = (d+timedelta(forestNum-1)).strftime("%Y-%m-%d")
        #从数据库获取历史日 元数据 sourceDates(list(dict))
        sourceDates = db.select("select ah.*,sh.daytype,sh.detailNum,sh.powerConsume from atmosphere_history ah INNER JOIN sw_history sh on ah.date = sh.date where ah.date>=? and ah.date<? and sh.detailNum=96 ORDER BY ah.date",preDate,startDate)
        #从数据库获取待预测日 元数据 forestDates(list(dict))        
        forestDates = db.select("select ah.*,sh.daytype,sh.detailNum,sh.powerConsume from atmosphere_history ah INNER JOIN sw_history sh on ah.date = sh.date where ah.date>=? and ah.date<=? and sh.detailNum=96 ORDER BY ah.date",startDate,endDate)
        
        
        
        utiles.clearList(self.source)
        utiles.clearList(self.expect)
        utiles.clearList(self.forest)
        #1 将历史日元数据转化为 AP 对象
        #2 赋值到source
        for one in sourceDates:
            for key in one.iterkeys():
                if key=='powerConsume':
                    one[key] = float('%5.6f'%one[key])
                    continue
                elif (key=='date' or key=='cityName'):
                    continue
                one[key] = int(one[key])
            ap = entity.AP(**one)
            
            self.source.append(ap)
        
        #1 将待预测日元数据转化为 AP 对象
        #2 赋值到forest
        for one in forestDates:
            for key in one.iterkeys():
                if key=='powerConsume':
                    one[key] = float('%5.6f'%one[key])
                    self.expect.append(one[key])
                    continue
                elif (key=='date' or key=='cityName'):
                    continue
                one[key] = int(one[key])
            ap = entity.AP(**one)
            self.forest.append(ap)
        
        self.stage = Stage.SETDATA

    def normalizeData(self):
        if self.stage != Stage.SETDATA:
            print '未设置数据'
        for i in range(len(self.forest)):
            self.normalize(self.forest[i])
        for i in range(len(self.source)):
            self.normalize(self.source[i])
        self.stage = Stage.NORMALIZE
    
    def countSimilarity(self):
        if self.stage != Stage.NORMALIZE:
            print '数据没有进行归一化'
        #1 计算每个待预测日的气象情况 与 所有历史日的相似度  
        #2 分别排序每个待预测日的相似度情况，并切片countNum的数量
        utiles.clearList(self.similarity)
        utiles.clearList(self.similarityValue)
#        for one in self.forest:
#            sim = []
#            for sor in self.source:
#                sor._similarity = self.doSimilarity(sor.oneData,one.oneData,self.rel,self.minRel)
#                sim.append(sor)
#            if self.predictWithForestData:
#                for fo in self.forest:
#                    if fo == one:
#                        break
#                    fo._similarity = self.doSimilarity(fo.oneData,one.oneData,self.rel,self.minRel)
#                    sim.append(fo)
#            sim.sort(reverse=True,cmp=APCompareSimilarity)
#            sim = sim[0:self.countNum]
#            self.similarity.append(sim)
#            
#            simValue = [s._similarity for s in sim]
#            self.similarityValue.append(simValue)
        for i in range(len(self.forest)):
            sim = []
            for sor in self.source:
                sor._similarity = self.doSimilarity(sor.oneData,self.forest[i].oneData,self.rel,self.minRel)
                sim.append(sor)
            if self.predictWithForestData==True:
                j = 0
                while j < i:
                    self.forest[j]._similarity = self.doSimilarity(self.forest[j].oneData,self.forest[i].oneData,self.rel,self.minRel)
                    sim.append(self.forest[j])
                    j += 1
            sim.sort(reverse=True,cmp=APCompareSimilarity)
            sim = sim[0:self.countNum]
            self.similarity.append(sim)
            
            simValue = [s._similarity for s in sim]
            self.similarityValue.append(simValue)
        
        self.keyList = self.forest[0].oneData.keys()
        print len(self.keyList)
        index=len(self.keyList)-1
        while index>=0:
            if self.rel.has_key(self.keyList[index]) and abs(self.rel[self.keyList[index]])<self.minRel:
                self.keyList.remove(self.keyList[index])
            index -= 1
        
        print self.keyList


        utiles.clearList(self.similarityList)
#        for sim in self.similarity:
#            simList = []
#            for one in sim:
#                data = []
#                for key in self.keyList:
#                    data.append(one.oneData[key])
#                simList.append(data)
#            self.similarityList.append(simList)
        for i in range(len(self.similarity)):
            simList = []
            for j in range(len(self.similarity[i])):
                data = []
                for key in self.keyList:
                    data.append(self.similarity[i][j].oneData[key])
                simList.append(data)
            self.similarityList.append(simList)
        
        utiles.clearList(self.forestList)
        for fl in self.forest:
            data = []
            for key in self.keyList:
                data.append(fl.oneData[key])
            self.forestList.append(data)
        
        self.stage = Stage.SIMILARITY
    
    def predict(self):
        if self.stage != Stage.SIMILARITY:
            print '没有计算相似度'
        import numpy as np
        
        utiles.clearList(self.predictPC)
        utiles.clearList(self.evaluation)
        for i in range(len(self.forest)):
            similarityPCList = []
            for sim in self.similarity[i]:
                similarityPCList.append(int(sim.powerConsume*100000))
            similarity_X = np.array(self.similarityList[i])
            similarity_y = np.array(similarityPCList)
#            print similarity_y
            predictModel = SVC()
            predictModel.fit(similarity_X, similarity_y)
            
            forest_X = np.array(self.forestList[i])
            forest_X = forest_X.reshape(1,-1)
            predicted = predictModel.predict(forest_X)
            
            self.forest[i].powerConsume = float(predicted[0]/100000.0)
            self.predictPC.append(float(predicted[0]/100000.0))
        
        for i in range(len(self.expect)):
            self.evaluation.append((self.expect[i]-self.predictPC[i])/self.expect[i])
