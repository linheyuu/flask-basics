from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chickens")
def chickens():
    return render_template("chickens.html")

@app.route("/pandas")
def pandas():
    return render_template("pandas.html")


if __name__ == "__main__":
    app.run(debug=True)
