from flask import Flask,render_template,redirect,request

turtles = [
    {
        "name":"Raphael",
        "color":"red",
        "img":"raphael.jpg"
    },

    {
        "name":"Leonardo",
        "color":"blue",
        "img":"leonardo.jpg"
    },

    {
        "name":"Michelangelo",
        "color":"orange",
        "img":"michelangelo.jpg"
    },

    {
        "name":"Donatello",
        "color":"purple",
        "img":"donatello.jpg"
    }
]

def formatInfo(ind):
    return turtles[ind]['name']+" "+turtles[ind]['color']+" "+turtles[ind]['img']

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',style="static/style.css",js="static/main.js")

@app.route('/turtles/<ind>',methods=['GET'])
def getInfo(ind):
    return formatInfo(int(ind))

app.run(debug=True)