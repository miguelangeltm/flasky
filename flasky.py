from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/hello", methods=["GET"])
def say_hello():
    return jsonify({"msg": "Hello, I'm Flasky"})

@app.route("/hello2", methods=["GET"])
def new_route():
    return jsonify({"msg": "This message was added 15 minutes after the first successful pipeline execution."})

@app.route("/hello3", methods=["GET"])
def new_route():
    return jsonify({"msg": "This message was added after the second successful jenkins pipeline execution."})


if __name__ == "__main__":
    # Please do not set debug=True in production
    app.run(host="0.0.0.0", port=5000, debug=True)