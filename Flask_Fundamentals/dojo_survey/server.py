from flask import Flask,render_template,request,redirect

app = Flask(__name__)
# app.secret_key = "hideMe"
style = "static/style.css"

@app.route("/")
def index():
	return render_template("index.html",style="static/style.css")

@app.route("/result",methods=["POST"])
def process():

	return render_template("results.html",name = request.form['name'], 
		language = request.form['language'],
		location = request.form['location'],
		comment = request.form['comment'],
		style="static/style.css")
app.run(debug=True)