# -*- coding: utf-8 -*-
import MySQLdb
from mmap import mmap,ACCESS_READ  
from xlrd import open_workbook,xldate,xldate_as_tuple
import datetime
"""
Created on Wed Mar 16 23:26:34 2016

@author: Coco
"""

try:
    conn = MySQLdb.connect(host='localhost',user='ly',passwd='ly',port=3306,db='powerforest',charset='utf8')
    cur = conn.cursor()
    count = cur.execute('select * from sw_history_detail')
#    print 'there has %s rows record' % count
    result = cur.fetchone()
#    print result
    
    
#   !!!!!!!重要!!!!!!!!!
#   !!!!!切换城市!!!!!!!
    cityname = 'shanwei'
#    cityname = 'shenzhen'
    
    wb = open_workbook('../'+cityname+'.xlsx')
    table = wb.sheets()[0]
    nrows = table.nrows
    for row in range(1,nrows):
#    for row in range(1,4):
        row_value = table.row_values(row)
        dt = xldate.xldate_as_datetime(row_value[0], 0)
        dt_formate = dt.strftime('%Y-%m-%d %H:%M:%S')
        t_formate = dt.strftime('%H:%M:%S')
        year = dt.year
        month = dt.month
        day = dt.day
        daytype = dt.weekday()
        time = dt.time()
        power = row_value[1]
#        print dt,daytype,power,dt_formate,t_formate
        cur.execute("insert into sw_history_detail(cityName,datetime,daytype,time,power_consume,year,month,day) values('%s','%s','%s','%s',%f,%i,%i,%i)"%(cityname,dt_formate,daytype,t_formate,power,year,month,day))
#        print "insert into sz_history(datetime,daytype,time,power_consume) values('%s',%i,'%s',%d)" % (dt_formate,daytype,t_formate,power)
#        time = xldate_as_tuple(table.cell(row,0).value, 0) 
#    print 'ID: %s info %s' % result
    conn.commit()
    cur.close()
    conn.close()
except MySQLdb.Error,e:
    print e.args[0],":",e.args[1]