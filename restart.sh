#!/bin/bash
kill -9 `cat /var/run/gunicorn.pid`
sleep 1
/data/venv/bin/python3.6 /data/venv/bin/gunicorn -c /data/venv/StarsL.cn/gunicorn.conf vmaig_blog.wsgi --reload
sleep 1
ps -ef|grep gunicorn
