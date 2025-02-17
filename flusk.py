import flask

app = flask.Flask(__name__)

@app.route('/hello')
def hello():
    return flask.jsonify({"msg" : "Hello world!"})

@app.route('/about', methods=["POST", "PUT", "GET"])
def about():
    return flask.jsonify({"namaste":"it is me"})


## how ro run server

if __name__ == "__main__":
    app.run(debug=True)