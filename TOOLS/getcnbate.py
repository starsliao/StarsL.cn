#!/data/venv/bin/python3.6
# -*- coding: UTF-8 -*-
import MySQLdb
import datetime
import feedparser
import random

d = feedparser.parse('https://rss.cnbeta.com/')
now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
conn=MySQLdb.connect(host='127.0.0.1',user='starsliao',passwd='wefw$jh37@4S',db='starsl.cn',port=3306, charset='utf8mb4')
cur=conn.cursor()
for i in range(15):
    num = random.randint(0,3)
    txt = d['entries'][i]['title']
    url = d['entries'][i]['id']
    if 'cnbeta.com' in url:
        insert_sql = f"INSERT INTO `starsl.cn`.blog_news(title, summary, news_from, url, create_time, pub_time) VALUES ('{txt}', '', {num}, '{url}', '{now}', '{now}')"
#    print(insert_sql)
        cur.execute(insert_sql)
conn.commit()
cur.close()
conn.close()
