from flask import Flask, render_template

from game import Game

app = Flask(__name__)


@app.route("/")
def hello_flask():

    mario = Game(name='Super Mario', category='Classic', console='SNES')
    zelda = Game(name='The Legend Of Zelda', category='RPG', console='WII')

    games: list = [mario, zelda]
    return render_template("index.html", page_name='Jogos', games=games)


app.run()
