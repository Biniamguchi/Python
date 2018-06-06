from flask import Flask,render_template, request, redirect

app= Flask(__name__)

@app.route('/')
def Ninjas():
  return 'No Ninjas Here!'

@app.route("/ninja")
def ninja():

    displayAll = True

    return render_template("ninja.html", displayAll=displayAll)

@app.route('/ninja/<color>')
def getColor(color):

    displayAll = False

    return render_template('ninja.html', displayAll=displayAll, color=color)

app.run(debug=True)
