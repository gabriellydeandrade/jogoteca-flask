from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_flask():
    return '<h1>Hello Flask!</h1>'


app.run()
