from flask import Flask, render_template
app = Flask(__name__)
@app.route('/') 


def hello_world():
  return render_template('index.html', name="Ben")

@app.route("/projects")
def ninja():
    return render_template('projects.html')

@app.route('/about')
def dojo():
    return render_template('about.html')
app.run(debug=True)
