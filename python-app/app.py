import os
from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def hello_world(hostname=None):
    myhost = os.uname()[1]
    appname = os.environ.get('APP_NAME', 'NoName')
    return render_template('index.html', hostname=myhost, appname=appname)
