from flask import Flask
from jinja2 import escape

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello world"

# @app.route("/name>")
# def user(name):
#     return f"Hello {name}"

if __name__ == "__main__":
    app.run()