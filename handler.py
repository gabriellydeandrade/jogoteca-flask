from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello_flask():
    return render_template("index.html")


app.run()
