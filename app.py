from flask import Flask, render_template, url_for
from templates.database import admin_session

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')



@app.route('/signup')
def admin():
    admin_session()
    return render_template('signup.html')



if __name__ == "__main__":
    app.debug = True
    app.run(debug=True)

 