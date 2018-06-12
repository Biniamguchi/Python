

from flask import Flask,render_template,redirect,session,request
import re
email_re = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
dob_re   = re.compile(r'^[0-9]')

app = Flask(__name__)
app.secret_key = "hideMe"

@app.route('/')
def index():
    return render_template('index.html',style="static/style.css")

@app.route('/success')
def success():
    return render_template('success.html',style="static/style.css")

@app.route('/process',methods=['POST'])
def process():
    isValid  = False
    count = 1

    for k in request.form:
        session[k] = ""
        v = request.form[k]

        if len(v) < 1:
            session[k] = "Please fill out this field"
            count -= 1
        elif k == "first" and not v.isalpha():
            session[k] = "Name must contain a-z characters."
            count -= 1
        elif k == "last" and not v.isalpha():
            session[k] = "Name must contain a-z characters."
            count -= 1
        elif k == "email" and not email_re.match(v):
            session[k] = "Invalid email address"
            count -= 1
        elif k == "pass" and request.form['confirm'] != v:
            session[k]         = "Passwords must match."
            session['confirm'] = "Passwords must match."
            count -= 2
        elif k == "dob":
            v = v.split('/')
            if len(v) < 3:
                session[k] = "Please use this format: mm/dd/yyyy"
                count -= 1
            else:   
                for i in v:
                    if not dob_re.match(i):
                        session[k] = "DoB must contain 0-9 characters."
                        count -= 1

                if int(v[0]) < 0 or int(v[0]) > 12:#Month
                    session[k] = "Enter a valid birth month."
                    count -= 1
                elif int(v[1]) < 0 or int(v[1]) > 32:#Day
                    session[k] = "Enter a valid birth day."
                    count -= 1
                elif int(v[2]) < 1900 or int(v[2]) > 2017: #Year
                    session[k] = "Enter a valid birth year."
                    count -= 1
        elif count == len(request.form):
            isValid = True

        count += 1

    if isValid:
        return render_template('success.html',style="static/style.css",first=request.form['first'],email=request.form['email'])
    else:
        return redirect('/')
    
app.run(debug=True) 