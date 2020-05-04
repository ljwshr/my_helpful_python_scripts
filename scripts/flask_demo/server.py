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
json_data_origin = []
json_data = []
# TODO: read it from the file or database
user_data = {
                                       
'70462837'	:'【兰芷】命运主宰与轮回大帝' ,
'48453706'	:'远方'                       ,
'17815165'	:'李立婷'                     ,
'69587650'	:'呼吁'                       ,
'75588850'	:'【兰芷】Maggie'             ,
'102319081'	:'Jessie'                     ,
'67660219'	:'鹿鹿爸Fod'                  ,
'42480091'	:'【兰芷】雒萌'               ,
'39870157'	:'【兰芷】安行'               ,
'23969590'	:'Study makes me happy'       ,
'83616130'	:'〔兰芷〕夕颜  '             ,
'82158259'	:'【兰芷】Eavan Xia✨  '       ,
'72608065'	:'[兰芷]cynesley'             ,
'29196715'	:'^倚楼听风雨、'              ,
'78491047'	:'【兰芷】帅雷雷'             ,
'161773374'	:'Crystal !'                  ,
'57234706'	:'【兰芷】Zxy '             ,
'7921282'	    :'【兰芷】crq '               ,
'34175866'	:'酒到微醺即是德 '            ,
'36762616'	:'【兰芷】青衫 '              ,
'220726641'	:'【兰芷】Alex 仔仔'          ,
'55450399'	:'wuxin23458 '                ,
'39949603'	:'【兰芷】寒天星尘-烛曦 '     ,
'40407376'	:'Joseph周 '                  ,
'64440148'	:'剑舞 '                      ,
'40192615'	:'【兰芷】Acer.Liong '        ,
'31476937'	:'【兰芷】云中雁'             ,
'45375580'	:'Coco'                       ,
'26632609'	:'【兰芷】徒手捏小强的大侠 '  ,
'47849527'	:'【兰芷】小小书童 '          ,
'82593688'	:'为梦想启航 '                ,
'65925154'	:'【兰芷】小小慧'             ,
'21877246'	:'【兰芷】慕瑶丶'             ,
'68367382'	:'【兰芷】青 '                ,
'56592592'	:'【兰芷】简思'               ,
'111299536'	:'西蓝花(⁎⁍̴̛ᴗ⁍̴̛⁎) '              ,
'24335650'	:'熊猫盼盼盼盼盼盼盼 '        ,
'93857404'	:'【兰芷 】扶苏   '           ,
'220638220'	:'草山   '                    ,
'51642805'	:'【兰芷】清风藏袖 '          ,
'45252271'	:'玫瑰 '                      ,
'32296228'	:'失意扬扬'                   ,
'56382307'	:'兰芷lily '                  ,
'81503974'	:'【兰芷】将琴代语 '          ,
'47463988'	:'【兰芷】静以幽，正以治。'   ,
'214909393'	:'瓶盖儿一毛钱'               ,
'82776226'	:'【兰芷】澧澧  '             ,
'31951624'	:'小清梅づ'                   ,
'36846991'	:'【兰芷】爱学习的鬼'
                 

}

# def read_participants():
#     global user_data
#     user_data = []
#     with open(r'participants.txt',"r") as f:    #设置文件对象
#         user_data_t = f.readlines()
#         for t in user_data_t:
#             t=t.strip();#用来删除字符串两端的空白字符。
#             t=t.strip("\n");
#             print("this is from the txt file")
#             print(t)
#             user_data.append(t)
    
#read_participants()
print(user_data)
 
def get_data_time():
    now_hour=int(time.strftime("%H", time.localtime()))
    now_minute=int(time.strftime("%M", time.localtime()))
    result = {}
    result['Time'] = str(now_hour)
    result['nickname'] = str(now_minute)
    result['step'] = "5000"
    result['cal'] = "None"
    #print(result)
    json_data.append(result)

get_data_time()

def test_read_sql_data():
    now_time = int(time.time())
    today_begin_time = now_time - (now_time- time.timezone)%86400
    time_stamp_start = today_begin_time - 3*24*60*60 # 3天前0时的时间戳
    print(time_stamp_start)
    #conn = sqlite3.connect(r'test.db')
    conn = sqlite3.connect(r'/usr/local/src/test.db')
    print ("Opened database successfully")
    c = conn.cursor()
    results=c.execute('''select * from SPORTS_ACTIVITY where timestamp > ?
    ''',[time_stamp_start])

    global json_data_origin
    for row in results:
        result = {}
        result['Stamp'] = str(row[0])
        result['Time'] = str(row[1][5:])
        result['ID'] = str(row[2])
        result['nickname'] = str(row[3])
        result['step'] = str(row[4])
        result['cal'] = str(row[5])

        json_data_origin.append(result)
    #print(json_data_origin)
    conn.close()
    #return dic_data
test_read_sql_data()
def transfer_origin_json_data_to_json_data(start_time:int,end_time:int):

    temp_circle = []
    for row in json_data_origin:
        
        if (int(row['Stamp']) >= start_time) and (int(row['Stamp']) <= end_time):
            result = {}
            result['ID'] =  None # clear the ID
            #result.pop('ID')
            result['Time'] = row['Time']
            result['nickname'] = row['nickname']
            result['step'] = row['step']
            result['cal'] = row['cal']
            json_data.append(result)
            # ID and temp_circle are secure, use internal
            result['ID'] = row['ID']
            temp_circle.append(result)
            #result['ID'] =  None # clear the ID
            
    #print("This is the first handle")
    #print(json_data)
    for id in user_data.keys():
        found_flag = False
        for ID_list in temp_circle:
            if ID_list['ID'] == id:
                found_flag = True
                break

        if found_flag is False:
            result = {}
            result['Time'] = ""
            result['nickname'] = user_data[id]
            result['step'] = "None"
            result['cal'] = "None"
            #print(result)
            json_data.append(result)
    # The last one line to tell apart the
    result = {}
    result['Time'] = "2020"
    result['nickname'] = 'End'
    result['step'] = "5000"
    result['cal'] = "180"
    #print(result)
    json_data.append(result)

def recursive_get_data_day_by_day():
    now_time = int(time.time())
    today_begin_time = now_time - (now_time- time.timezone)%86400
    time_stamp_3days = today_begin_time - 3*24*60*60 # 3天前0时的时间戳
    time_stamp_2days = today_begin_time - 2*24*60*60 # 2天前0时的时间戳
    time_stamp_1days = today_begin_time - 1*24*60*60 # 3天前0时的时间戳
    #transfer_origin_json_data_to_json_data(time_stamp_3days,time_stamp_2days)
    transfer_origin_json_data_to_json_data(time_stamp_2days,time_stamp_1days)
    transfer_origin_json_data_to_json_data(time_stamp_1days,today_begin_time)
    transfer_origin_json_data_to_json_data(today_begin_time,now_time)

recursive_get_data_day_by_day()
print("This is the reuslt of json data")
print(json_data)

@app.route('/start')
def start_read():
    test_read_sql_data()
    return render_template('hello.html', result = dic_data)

@app.route('/yd_data')
def return_yundong_data():
    #test_read_sql_data()
    #return render_template('hello.html', result = dic_data)
    
    print("This is from function return_yundong_data")
    return jsonify(json_data)

@app.route('/yd')
def show_yundong():

    print("This is from function show_yundong")
    return render_template('yun_dong.html')

@app.route('/')
def do_json():
    #test_read_sql_data()
    #return render_template('hello.html', result = dic_data)
    
    print("This is from function do_json")
    return jsonify(json_data)
 
if __name__ == '__main__':
    app.config['JSON_AS_ASCII'] = False
    app.run(port=5000)
