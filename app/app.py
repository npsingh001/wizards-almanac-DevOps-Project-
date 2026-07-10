from flask import Flask

app = Flask(__name__)

with open("VERSION") as f:
    VERSION = f.read().strip()


@app.route("/")
def home():
    return f"Welcome to the Wizard's Almanac (v{VERSION})"


@app.route("/version")
def version():
    return VERSION


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)