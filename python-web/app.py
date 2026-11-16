from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def hallo():
    name = request.args.get("name")
    return f"<h1>Hallo {name}!</h1>"


if __name__ == "__main__":
    app.run()