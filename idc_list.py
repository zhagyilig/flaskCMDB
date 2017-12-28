# coding=utf-8

# 系统模块:
from flask import Flask, request, render_template, redirect, session
import MySQLdb as mysql
import json

# 自定义模块

conn= mysql.connect(    # 连接MySQL
        host='localhost',
        port = 9036,
        user='root',
        passwd='888888',
        db ='reboot12',
        unix_socket = '/tmp/mysql9036.sock',
        )

cur = conn.cursor()
# conn.autocommit(True)
# cur.execute("select * from flask_user")   # 测试连接库
# print(cur.fetchall())

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('idc_index.html')

@app.route('/idc_list')
def idc_list():
    cur.execute('select * from idc_list')
    res = cur.fetchall()
    return json.dumps(res)

@app.route('/add_idc',methods=['post'])
def addidc():
    idc_name = request.form.get('name')
    sql = 'insert into idc_list(name) values("%s")' %(idc_name)
    print(sql)
    cur.execute(sql)
    conn.commit()
    return 'ok'

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=999,debug=True)
