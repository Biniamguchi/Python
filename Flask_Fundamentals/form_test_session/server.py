from flask import Flask,render_template,request,redirect,session

app = Flask(__name__)
app.secret_key = "NOCOOKIES4U" # cant use session / cookies without a key.

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/users',methods=['POST'])
def newUser():
    session['name'] = request.form['name']
    session['email'] = request.form['email']

    return redirect("/show")

@app.route('/show')
def show_user():
    #You could set session vars in the html directly or pass them as args to be rendered.
    return render_template('user.html')

app.run(debug=True)