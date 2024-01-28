from contextlib import _RedirectStream
from flask import Flask, render_template, url_for,request,jsonify
import mysql.connector as mysql
from templates.database import admin_session,auth_admin

app = Flask(__name__)

db = mysql.connect(host="localhost",user="root",password="",database="college")
command_handler = db.cursor(buffered=True)

@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/login')
def login():
    return render_template('loginchoose.html')


@app.route('/student', methods=['GET', 'POST'])
def student():
    if request.method == "POST":
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
        query_vals = (studentname,Class,Address,parentsnumber,Parentsname)
        command_handler.execute("INSERT INTO users(S_name,Class,Address,Parentsnumber,Parentsname) VALUES (%s,%s,%s,%s,%s)",query_vals)
        db.commit()
    
    return render_template('student.html')

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        username = request.form.get['username']
        print(username)
        password = request.form.get['password']
        print(password)
        if username == "admin" and password == "password":
            session['logged_in'] = True
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM users")
            users = cursor.fetchall()
            return render_template('index.html', users=users)
        else:
            return render_template('login.html', error='Invalid username or password.')
    return render_template('login.html')
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           # print("Delete Existing Student Account")
           # username = input(str("Student username : "))
           # query_vals = (username)
           # command_handler.execute("DELETE FROM users WHERE username = %s ",query_vals)
           # db.commit()
           # if command_handler.rowcount < 1:
           #     print("User not found")
           # else:
           #    print(username + " has been deleted")
            
    #return render_template('admin.html')

















@app.route('/teacher', methods=['GET', 'POST'])
def teacher():
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

 