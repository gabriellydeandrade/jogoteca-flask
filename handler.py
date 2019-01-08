from flask import Flask, render_template, request, redirect

from game import Game

app = Flask(__name__)

mario = Game(name='Super Mario', category='Classic', console='SNES')
zelda = Game(name='The Legend Of Zelda', category='RPG', console='WII')

games: list = [mario, zelda]


@app.route("/")
def index():
    return render_template("index.html", page_name='Jogos', games=games)


@app.route("/new_game")
def new_game():
    return render_template("new_game.html", page_name="Novo Jogo")


@app.route("/save_game", methods=['POST'])
def save_game():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']

    new_game = Game(name=nome, category=categoria, console=console)
    games.append(new_game)

    return redirect("/")


app.run(debug=True)
