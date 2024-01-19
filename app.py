from flask import Flask, render_template, url_for


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')




@app.route('/signup')
def admin():
    return render_template('signup.html')


if __name__ == "__main__":
    app.debug = True
    app.run(debug=True)

 