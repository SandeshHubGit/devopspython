import flask

app = flask.Flask(__name__)

# @app.route('/hello')
# def hello():
#     return flask.jsonify({"msg" : "Hello world!"})

# @app.route('/about', methods=["POST", "PUT", "GET"])
# def about():
#     return flask.jsonify({"namaste":"it is me"})

# @app.route('/userdata', methods=["POST"])
# def take_from_user():
#     data = flask.request.get_json()
#     print(data)
#     return "take_from_user"


@app.route('/userdatatype', methods=["POST"])
def take_from_user_type():
    data = flask.request.get_json()
    print(data)
    print(type(data))
    print(data["name"])
    print(type(data['name']))
    return data["name"]

## how ro run server

if __name__ == "__main__":
    app.run(debug=True)