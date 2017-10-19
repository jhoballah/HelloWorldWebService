from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/api/hello/<name>", methods=['GET'])
def hello(name):

    return "Hello World %s" % name


@app.route("/api/data/", methods=['GET'])
def data():

    a = {"temp": [20, 30, 40]}
    b = {"time": [10, 20, 30]}
    c = {"unit": "s"}

    data_dict = [a, b, c]

    return jsonify(data_dict)


@app.route("/api/add", methods=['POST'])
def add_data():

    a = request.json

    c = a['a'] + a['b']

    return "Your sum is my command: %d" % c

    # c = sum(a.values())
    #
    # print(c)
    # return "Sum was {}".format(c)