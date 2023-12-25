from flask import Flask, render_template
import requests

api_get_url = "http://srv1.logi.li:6490/message/9"
response = requests.get(api_get_url)
res = response.json()

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template('index.html', res=res)
