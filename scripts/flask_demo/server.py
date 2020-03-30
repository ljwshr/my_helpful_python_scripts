# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify, render_template


import json
from werkzeug.utils import redirect
from flask.helpers import url_for

import sqlite3
import time
from threading import Timer
 
app = Flask(__name__)

my_test_time = 1
global dic_data
dic_data = {}
def timedTask():
    '''
    第一个参数: 延迟多长时间执行任务(单位: 秒)
    第二个参数: 要执行的任务, 即函数
    第三个参数: 调用函数的参数(tuple)
    '''
    Timer(3600, test_read_sql_data, ()).start()
def test_read_sql_data():
    time_stamp_start = time.time() - 48*60*60
    print(time_stamp_start)
    print(time_stamp_start)
    conn = sqlite3.connect(r'/usr/local/src/test.db')
    print ("Opened database successfully")
    c = conn.cursor()
    results=c.execute('''select * from SPORTS_ACTIVITY where timestamp > ?
    ''',[time_stamp_start])
    global dic_data
    dic_data = {}
    for row in results: 
        dic_data[str(row[1])]= '\t昵称:'+str(row[3])+'\t步数:'+str(row[4])+'\t能量:'+str(row[5]) 
 
    
    print(dic_data)
#     json_data = []
#     for row in results:
#         result = {} 
#         result['时间'] = str(row[1]) 
#         result['昵称'] = str(row[3])   
#         result['步数'] = str(row[4])   
#         result['能量'] = str(row[5])   
# 
#         json_data.append(result)
#     print(json_data)
    conn.close()
    #return dic_data

@app.route('/start_read')
def start_read():

    #data_from_sql=test_read_sql_data()
    #dict = {'phy':50,'che':60,'maths':70}
    test_read_sql_data()
    return render_template('hello.html', result = dic_data)

@app.route('/')
def do_json():

    #data_from_sql=test_read_sql_data()
    #dict = {'phy':50,'che':60,'maths':70}
    return render_template('hello.html', result = dic_data)

 
if __name__ == '__main__':
    app.run(port=5000)
