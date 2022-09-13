from flask import Flask,render_template,request,session
import mysql.connector
import os

app = Flask(__name__)

conn=mysql.connector.connect(host="localhost",user="root",password="",database="gym")
cursor= conn.cursor()

#Home 
@app.route('/')
def login():
    return render_template('admin.html')

#if Logged_in
@app.route('/login_validation',methods=['post'])
def login_validation():
    username= request.form.get('username')
    password = request.form.get('password')
    cursor.execute("""select * from aa where username like '{}' and password like '{}'""".format(username,password))
    us= cursor.fetchall()
    if len(us)>0:
        return render_template('index.html')
    else:
        return render_template('admin.html',info = 'Invalid User')

@app.route('/index',methods=['post','get'])
def Add():
    return render_template('index.html')

@app.route('/add_user',methods=['post','get'])
def add_users():
    return render_template('register.html')
        
#add member
@app.route('/addbb',methods=['post'])
def add_user():
    gymid=request.form.get('gymid')
    name= request.form.get('name')
    your_plain=request.form.get('your_plain')
    contact_number=request.form.get('contact_number')
    aadharcard_number=request.form.get('aadharcard_number')
    age=request.form.get('age')
    membership=request.form.get('membership')
    #password=request.form.get('upassword')
    cursor.execute("insert into bb(gymid,name,your_plain,contact_number,aadharcard_number,age,membership) values('{}','{}','{}','{}','{}','{}','{}')".format(gymid,name,your_plain,contact_number,aadharcard_number,age,membership))
    conn.commit()
    return render_template("register.html")

#all user detail show
@app.route("/alluser")
def alldata():
    cursor.execute("select * from bb")
    data=cursor.fetchall()
    return render_template("alldata.html",elist=data)

#Delete Employee
@app.route('/delete',methods=['post','get'])
def delete():
    return render_template('curd.html')
 
@app.route("/delete_user",methods=['post'])
def delete_user():
    name=request.form.get('name')
    cursor.execute("""delete from bb where name like '{}'""".format(name))
    conn.commit()
    return render_template('index.html')

@app.route('/update',methods=['post','get'])
def update():
    return render_template('update.html')

@app.route("/updatebb", methods=["POST"])
def update_bb():
    gymid = request.form["gymid"]
    name = request.form["name"]
    your_plain = request.form["your_plain"]
    contact_number = request.form["contact_number"]
    aadharcard_number = request.form["aadharcard_number"]
    age = request.form["age"]
    membership = request.form["membership"]
    cursor.execute("update bb set name='{}',your_plain='{}',contact_number='{}',aadharcard_number='{}',age={},membership='{}' where gymid = {}".format(name,your_plain,contact_number,aadharcard_number,age,membership,gymid))
    return render_template('index.html')

    #Run App
if __name__=="__main__":
  app.run(debug=True)
