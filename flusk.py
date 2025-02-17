import flask

app = flask.Flask(__name__)

@app.route("/hello")
def hello():
    return "Hello world!"


## how ro run server

if __name__ == "__main__":
    app.run(debug=True)