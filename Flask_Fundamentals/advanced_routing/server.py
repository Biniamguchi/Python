
from flask import Flask, render_template, request, redirect
app = Flask(__name__)
@app.route('/users/<jay>')
def show_user_profile(jay):
    print jay
    return render_template("user.html")
app.run(debug=True)