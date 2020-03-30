#!/bin/sh

PROCESS=`ps -ef|grep gunicorn|grep -v grep|grep -v PPID|awk '{ print $2}'`
for i in $PROCESS
do
  echo "Kill the $1 process [ $i ]"
  kill -9 $i
done

python3 /usr/local/src/Activity-Presider/沁心运动/bin/main.py

cd /usr/local/src/p3env/flask_demo/

/usr/local/src/p3env/p3env/bin/python3 /usr/local/src/p3env/p3env/bin/gunicorn -w 1 -t 30 -b 0.0.0.0:5000 server:app