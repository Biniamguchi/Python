from flask import Flask, render_template, request, redirect
app = Flask(__name__)
@app.route('/')
def show_user_profile():
    return render_template("index.html")

@app.route('/ninjas')
def display():    
    return render_template("ninjas.html")

@app.route('/dojos/new')
def view_form():
    return render_template("dojos.html")

@app.route('/dojos', methods=['POST'])
def getDojos():
    print request.form
    name = request.form['name']
    return redirect('/ninjas')

app.run(debug=True)