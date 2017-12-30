# coding=utf-8

# 系统模块:
from flask import Flask, request, render_template, redirect, session
import MySQLdb as mysql
import json


conn= mysql.connect(    # 连接MySQL
        host='localhost',
        port = 9036,
        user='root',
        passwd='888888',
        db ='reboot12',
        unix_socket = '/tmp/mysql9036.sock',
        )

cur = conn.cursor()
conn.autocommit(True)
# cur.execute("select * from flask_user")   # 测试连接库
# print(cur.fetchall())

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('idc_index.html')

## app: idc
# 显示idc地域分布
@app.route('/idc_list')
def idc_list():
    cur.execute('select * from idc_list')
    res = cur.fetchall()
    return json.dumps(res)

# 添加idc page.
@app.route('/add_idc',methods=['post'])
def addidc():
    idc_name = request.form.get('name')
    sql = 'insert into idc_list(name) values("%s")' %(idc_name)
    print(sql)
    cur.execute(sql)
    # conn.commit()
    return 'ok'


## app：pc
@app.route('/pc')
def pc():
    return render_template('pc.html')

@ app.route('/pclist')
def pclist():
    # update-btn
    id = request.args.get('id') # 获取浏览器传参: id;获取单条信息
    sql = 'select * from pc'
    if id:
        sql += ' where id=%s' %(id)
    cur.execute(sql)
    res = cur.fetchall() # 获取数据
    print(res)
    return json.dumps(res)

# 添加服务器信息
@app.route('/addpc',methods=['post'])
def addpc():
    ip = request.form.get('ip')
    mem = request.form.get('mem')
    idc_id = request.form.get('idc_id')
    create_time = request.form.get('create_time')
    sql = 'insert into pc(ip,mem,idc_id,create_time) values("%s",%s,%s,"%s")' %(ip,mem,idc_id,create_time)
    print('*'*100)
    print(sql)
    cur.execute(sql)
    return 'ok'

# 删除服务器信息
@app.route('/delpc',methods=['post'])
def delpc():
    id = request.form.get('id')
    if not id:
        return 'error'
    sql = 'delete from pc where id=%s' %(id)
    print(sql)
    cur.execute(sql)
    return 'ok'

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=999,debug=True)
