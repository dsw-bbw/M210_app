from pathlib import Path
from html import escape
from flask import Flask

app = Flask(__name__)
pfad = Path(__file__).parent / "data.txt"

@app.route("/")
def anzeigen():
    inhalt = pfad.read_text(encoding="utf-8")
    return f"""
    <html>
      <head><meta charset="utf-8"><title>data.txt</title></head>
      <body>
        <h1>Inhalt von data.txt</h1>
        <pre>{escape(inhalt)}</pre>
      </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)