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
    return jsonify({"confirm":data[0],"import_case":data[1],"heal":data[2],"dead":data[3],"suspect":data[4],"heal_rate":data[5],"dead_rate":data[6]})


@app.route("/time")
def get_time():
    return utils.get_time()

@app.route("/l1")
def get_l1_data():
    data = utils.get_l1_data()
    day,confirm,import_case,heal,dead = [],[],[],[],[]
    for a,b,c,d,e in data[7:]:
        day.append(a.strftime("%m-%d")) #a是datatime类型
        confirm.append(b)
        import_case.append(c)
        heal.append(d)
        dead.append(e)
    return jsonify({"day":day,"confirm": confirm, "import_case": import_case, "heal": heal, "dead": dead})

@app.route("/r1")
def get_r1_data():
    data = utils.get_r1_data()
    day, confirm_add, dead_add = [],[],[]
    for a,b,c in data[5:]:
        day.append(a.strftime("%m-%d")) #a是datatime类型
        confirm_add.append(b)
        dead_add.append(c)
    return jsonify({"day": day, "confirm_add": confirm_add, "dead_add": dead_add})


if __name__ == '__main__':
    app.run()
