__author__ = 'Administrator'
from sys import stdout
import json
import math
import time
import threading
from spider_util.db_util import DbUtil
from ext_api.baidu_map_api.geo_coding import GeoCode
from spider_util.html_util import HtmlAnalyzeUtil
import os
class t(threading.Thread):
    count=0
    run_event=threading.Event()

    rlock=threading.RLock()
    def __init__(self):
        threading.Thread.__init__(self)
        self.do=True
        self.start()
    def run(self):
        while self.do:
            self.run_event.wait()
            time.sleep(0.2)
            self.rlock.acquire()
            t.count=t.count+1
            self.rlock.release()
    def stop(self):
        self.do=False
t1=t.count
t2=t.count
t3=t.count
t.run_event.set()
thread_array=[t() for i in range(1000)]
a_run=80
a_rep=40
t_count=0

while True:
    t3=t2
    t2=t1
    t1=t.count
    c=t1
    v=t1-t2
    a=t3-2*t2+t1
    print("c:%d,v:%d,a:%d"%(t1,t1-t2,t3-2*t2+t1),end=',')
    if a_run*a_rep<0:
        a_run=round(-0.7*a_run)
    elif a_run*a_rep>0:
        a_run=round(1.05*a_run)
    t.run_event.clear()
    print("a_run:%d,arr:%d"%(a_run,thread_array.__len__()))
    if a_run>0 and a_run<5:
        a_run=5
    if a_run>-5 and a_run<0:
        a_run=-5
    if a_run>0:
        for i in range(a_run):
            thread_array.append(t())
    elif a_run<0:
        for i in range(abs(-a_run)):
            thread_array.pop().stop()
    t.run_event.set()
    if a_run==0:
        t_count=t_count+1
    else:
        t_count=0
    time.sleep(1)
    a_rep=a

