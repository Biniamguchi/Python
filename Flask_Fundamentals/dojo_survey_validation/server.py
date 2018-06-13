from flask import Flask,render_template,request,redirect,flash,session

app = Flask(__name__)
app.secret_key = "hideMe"
style = "static/style.css"

@app.route("/")
def index():
	return render_template("index.html",style=style)

@app.route("/process",methods=["POST"])
def process():
	for i in request.form:
		if len(request.form[i]) < 1:
			flash("Please fill in all fields.")
			return redirect('/')
		if i == "com" and len(request.form[i]) > 120:
			flash('Comment must be less than 120 characters.')
			return redirect('/')
		session[i] = request.form[i]

	return render_template("results.html",style="static/style.css")
app.run()