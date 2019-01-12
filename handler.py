from flask import Flask, render_template, request, redirect, session, flash, url_for

from game import Game

app = Flask(__name__)
app.secret_key = "flask"

mario = Game(name='Super Mario', category='Classic', console='SNES')
zelda = Game(name='The Legend Of Zelda', category='RPG', console='WII')

games: list = [mario, zelda]


@app.route("/")
def index():
    return render_template("index.html", page_name='Jogos', games=games)


@app.route("/new_game")
def new_game():
    if session["is_logged"]:
        return render_template("new_game.html", page_name="Novo Jogo")
    return redirect(url_for(endpoint="login", new_page=url_for(endpoint="new_game")))


@app.route("/save_game", methods=['POST'])
def save_game():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']

    new_game = Game(name=nome, category=categoria, console=console)
    games.append(new_game)

    return redirect(url_for(endpoint="index"))


@app.route("/login")
def login():
    new_page: str = request.args.get("new_page")
    return render_template("login.html", page_name="Login", new_page=new_page)


@app.route("/logout")
def logout():
    session["is_logged"] = None
    flash("Nenhum usuário logado!")
    return redirect(url_for(endpoint="index"))


@app.route("/auth", methods=['POST'])
def auth():
    default = "mestra"
    session["is_logged"] = request.form["senha"]
    if default == session["is_logged"]:
        flash(f"{request.form['usuario']} logado com sucesso")
        return redirect(request.form['new_page'])
    else:
        flash("Tente novamente!")
        return redirect(url_for(endpoint="login"))


app.run(debug=True)
