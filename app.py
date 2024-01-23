from contextlib import _RedirectStream
from flask import Flask, render_template, url_for,request,jsonify
import mysql.connector as mysql
from templates.database import admin_session,auth_admin

app = Flask(__name__)

db = mysql.connect(host="localhost",user="root",password="",database="college")
command_handler = db.cursor(buffered=True)

@app.route('/')
def index():
    print(request)
    return render_template('homepage.html')

@app.route('/login')
def login():
   
    return render_template('loginchoose.html')


@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == "admin" and password == "password":
            admin_session()  
            
    return render_template('admin.html')


@app.route('/student')
def student_info():
    
         return render_template('student.html')

@app.route('/teacher')
def teacher_info():
    
        return render_template('teacherlogin.html')



if __name__ == "__main__":
    app.debug = True
    app.run(debug=True)

 