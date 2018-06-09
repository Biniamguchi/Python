from flask import Flask,request,redirect,flash,session,render_template
app = Flask(__name__)
app.secret_key = "hideme"



@app.route("/")
def index():
    if "counter" not in session:
        session["counter"] =0

    else:
        session["counter"] += 2
    return render_template("index.html", counter = session["counter"])

@app.route("/counter", methods=["POST"])
def button():
    return redirect("/")

@app.route("/reset", methods=["POST"])
def reset():
    session["counter"] =-1
    return redirect("/")
app.run(debug=True)
