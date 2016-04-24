# -*- coding: utf-8 -*-
import datetime
import functools
"""
Created on Thu Mar 24 10:13:45 2016

@author: Coco
"""

def log(arg):
    if hasattr(arg,'__call__'):
        @functools.wraps(arg)
        def wrapper(*args,**kw):
            print 'call %s()'%arg.__name__
            return arg(*args,**kw)
        return wrapper
    else:
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args,**kw):
                print '%s %s()'%(arg,func.__name__)
                return func(*args,**kw)
            return wrapper
        return decorator
        
@log("calling this:")
def nowdate(msg):
    print msg,datetime.datetime.now().date()
    
@log
def nowtime(msg):
    print msg,datetime.datetime.now().time()
 
nowdate("current date:")
nowtime("current time:")

#print type(nowtime)
#print hasattr(nowtime,'__call__')





