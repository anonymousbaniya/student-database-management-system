from contextlib import _RedirectStream
from flask import Flask, render_template, url_for,request,jsonify
import mysql.connector as mysql
from templates.database import admin_session,auth_admin

app = Flask(__name__)

db = mysql.connect(host="localhost",user="root",password="",database="college")
command_handler = db.cursor(buffered=True)

@app.route('/')
def index():
    return render_template('homepage.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
   

   
    return render_template('loginchoose.html')


@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print(username)
        print(password)
        if username == "admin" and password == "password":
            admin_session()  
            
    return render_template('admin.html')


@app.route('/student', methods=['GET', 'POST'])
def student():
    if request.method == "POST":
        Rollno = request.form.get("Rollno")
        print("Rollno " , Rollno)
        studentname = request.form.get("S_Name")
        print("studentname" ,studentname)
        Class = request.form.get("Class")
        print("class " , Class)
        Address = request.form.get("Address")
        print("address " , Address)
        parentsnumber = request.form.get("parentsNumber")
        print("parents number " , parentsnumber)
        Parentsname = request.form.get("parentsName")
        print("parentsname " , Parentsname)
        query_vals = (Rollno,studentname,Class,Address,parentsnumber,Parentsname)
        command_handler.execute("INSERT INTO users(Rollno,S_name,Class,Address,Parentsnumber,Parentsname) VALUES (%s,%s,%s,%s,%s,%s)",query_vals)
        db.commit()
    
    return render_template('student.html')

@app.route('/teacher', methods=['GET', 'POST'])
def teacher_info():
        if request.method == "POST":
            username = request.form.get("username")
            password = request.form.get("password")
            print("Username: " + username)
            print("Password: " + password)
            query_vals = (username,password)
            command_handler.execute("INSERT INTO users (username,password,privilage) VALUES (%s,%s,'teacher')",query_vals)
            db.commit()


        return render_template('teacherlogin.html')



if __name__ == "__main__":
    app.debug = True
    app.run(debug=True)

 