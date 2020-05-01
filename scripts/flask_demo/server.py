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
json_data = []

def test_read_sql_data():
    time_stamp_start = time.time() - 4*24*60*60
    print(time_stamp_start)
    print(time_stamp_start)
    #conn = sqlite3.connect(r'test.db')
    conn = sqlite3.connect(r'/usr/local/src/test.db')
    print ("Opened database successfully")
    c = conn.cursor()
    results=c.execute('''select * from SPORTS_ACTIVITY where timestamp > ?
    ''',[time_stamp_start])
    conn.close()

    global json_data
    for row in results:
        result = {}
        result['Time'] = str(row[1][5:])
        result['nickname'] = str(row[3])
        result['step'] = str(row[4])
        result['cal'] = str(row[5])

        json_data.append(result)
    print(json_data)

    #return dic_data
test_read_sql_data()

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
