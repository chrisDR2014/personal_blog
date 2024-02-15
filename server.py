from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
app.config['SECRET_KEY'] = '71231239124'
Bootstrap5(app)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False, port=8001)