from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.get('/')
def LoginPage():
    return render_template('login.html')


app.run(debug=True)
