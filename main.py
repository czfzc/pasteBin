# -*- coding: utf-8 -*
import MySQLdb
db = MySQLdb.connect("127.0.0.1","root","4c82z3f69","mifan",charset="utf8")
#db = MySQLdb.connect("mifanblog.cn","sq_pqrod64777","uvf8103","sq_pqrod64777",charset="utf8")
cursor=db.cursor()

from flask import Flask , url_for,request,render_template,make_response,redirect
import time
import random
app = Flask(__name__)

@app.route("/")
def gets():
    return render_template("index.html")

@app.route('/paste_<id>')
def hello(id):
    sql="select * from pastebin where user=%s;"%(id)
    cursor.execute(sql)
    list=cursor.fetchone()
    if list!=None:
        return render_template("paste.html",title=list[0],subtitle=list[5]+" "+list[3],content=list[1])
    else:
        return render_template("index.html")

@app.route("/submitter",methods=['POST','GET'])
def forms():
    if(request.method == 'POST'):
        ran=random.randint(100000,999999)
        atime=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime());
        sql="insert into pastebin values('%s','%s','%s','%s','%s','%s','%s')"%\
            (request.form['title'],request.form['content'],request.form['pass'], \
             request.form['timevalue']+request.form['time'],str(ran),atime,'1');
        print sql
        cursor.execute(sql)
        db.commit()
        return redirect("paste_"+str(ran).decode("utf8"))

#unfinished functions


def cacu(max,num,add):
    if (num+add)/max != 0:
        return (num+add)%max
    else:
        return num+add


def compare(one,two):
    if int(one[0:4]+one[5:7]+one[8:10]+one[11:13]+one[14:16]+one[17:19])< \
            int(two[0:4] + two[5:7] + two[8:10] + two[11:13] + two[14:16] + two[17:19]):
        return True
    else:
        return False