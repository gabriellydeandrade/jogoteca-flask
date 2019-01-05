from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello_flask():
    games: list = ['Super Mario', 'The Legend Of Zelda', 'Tetris']
    return render_template("index.html", page_name='Jogos', games=games)


app.run()
