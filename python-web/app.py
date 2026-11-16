from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hallo():
    name = request.args.get("name", "Welt")
    return f"<h1>Hallo {name}!</h1>"

app.run(host="0.0.0.0", port=5000)