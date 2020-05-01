# -*- coding=utf-8 -*-
import sqlite3
from collections import OrderedDict
import datetime
import time
import json


def connect_sqlite3():
    conn = sqlite3.connect('test.db')
    print ("Opened database successfully")
    c = conn.cursor()
    c.execute('''CREATE TABLE SPORTS_ACTIVITY
           (timestamp INT PRIMARY KEY     NOT NULL,
           datetime           TEXT    NOT NULL,
           user_id            INT     NOT NULL,
           nickname          TEXT     NOT NULL,
           step        INT,
           calo        INT,
           TEMP         TEXT);''')
    print ("Table created successfully")
    conn.commit()
    conn.close()

    
def insert_data(origin_data):
    print(origin_data)
    tem_timestamp = 0
    tem_datetime = ''
    tem_user_id = 0
    tem_nickname = ''
    tem_step = 0
    tem_calo = 0
    tem_TEMP = 0
    conn = sqlite3.connect(r'E:\git_projects\my_helpful_python_scripts\scripts\test.db')
    print ("Opened database successfully")
    c = conn.cursor()
    
    for k, v in origin_data.items():
        print(k)
        for k1, v1 in v.items():
            if(k1 == "nickname"):
                tem_nickname = v1
            elif(k1 == "time"):
                tem_datetime = v1
                un_time = time.mktime(v1.timetuple())
                print(un_time)
                tem_timestamp = un_time
            elif(k1 == "user_id"):
                tem_user_id = v1
            elif(k1 == "step"):
                tem_step = v1
            elif(k1 == "calo"):
                tem_calo = v1
                
                sql = ''' insert or ignore into SPORTS_ACTIVITY
                  (timestamp, datetime, user_id, nickname, step, calo, TEMP)
                  values
                  (:timestamp, :datetime, :user_id,:nickname, :step, :calo, :TEMP)'''
                c.execute(sql, {'timestamp':tem_timestamp, 'datetime':tem_datetime, 'user_id':tem_user_id, 'nickname':tem_nickname, 'step':tem_step, 'calo':tem_calo, 'TEMP':tem_TEMP})
                print ("Insert one message")
    conn.commit()
    conn.close()


def test_order_dict():
    data_parent = OrderedDict()
    data = OrderedDict()
    data['user_id'] = 45337477
    data['nickname'] = '兰芷'
    data['time'] = datetime.datetime(2020, 3, 29, 10, 4, 35)
    data['step'] = 7995
    data['calo'] = None
    data['result'] = None
    
    data_parent[45337477] = data
    
    data1 = OrderedDict()
    data1['user_id'] = 45337478
    data1['nickname'] = '【兰芷】大阳1'
    data1['time'] = datetime.datetime(2021, 3, 29, 10, 4, 34)
    data1['step'] = 7996
    data1['calo'] = 180
    data1['result'] = None
    
    data_parent[45337478] = data1
    
    # print(data)
    print(data_parent)
    return data_parent

def test_read_sql_data():
    time_stamp_start = time.time() - 48*60*60
    print(time_stamp_start)
    print(time_stamp_start)
    conn = sqlite3.connect('test.db')
    print ("Opened database successfully")
    c = conn.cursor()
    results=c.execute('''select * from SPORTS_ACTIVITY where timestamp > ?
    ''',[time_stamp_start])
    
    json_data = []
    for row in results:
        result = {} 
        result['时间'] = row[1]  
        result['昵称'] = str(row[3])   
        result['步数'] = str(row[4])   
        result['能量'] = str(row[5])   

        json_data.append(result)
    print(json_data)
    conn.close()
    #return json_data


if __name__ == '__main__':
#     connect_sqlite3()
#     origin_data = test_order_dict()
#     insert_data(origin_data)
    test_read_sql_data()
    pass
