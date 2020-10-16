from flask import Flask
from flask import request as re
from flask import render_template
from flask import jsonify
from jieba.analyse import extract_tags
import string
import utils

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("main.html")

@app.route("/c1")
def get_c1_data():
    data = utils.get_c1_data()
    return jsonify({"confirm":data[0],"suspect":data[1],"heal":data[2],"dead":data[3],"heal_rate":data[4],"dead_rate":data[5]})


@app.route("/time")
def get_time():
    return utils.get_time()


if __name__ == '__main__':
    app.run()
