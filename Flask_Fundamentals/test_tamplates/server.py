from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
  return render_template("user.html", phrase="hello", times=10)
app.run(debug=True)

 