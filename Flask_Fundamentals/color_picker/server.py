from flask import Flask,request,render_template,redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',r="2",g="3",b="45")

@app.route('/submit',methods=['POST'])
def submit():
    r = request.form['r']
    g = request.form['g']
    b = request.form['b']

    r = int(r)
    g = int(g)
    b = int(b)

    if r < 0 or r > 255:
        r = 255
    if g  < 0 or g > 255:
        g = 255
    if b < 0 or b > 255:
        b = 255

    r = str(r)
    g = str(g)
    b = str(b)

    return render_template('index.html',r=r,g=g,b=b)
app.run(debug=True)