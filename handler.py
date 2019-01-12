from flask import Flask, render_template, request, redirect, session, flash, url_for

from game import Game
from user import User

app = Flask(__name__)
app.secret_key = "flask"

mario = Game(name='Super Mario', category='Classic', console='SNES')
zelda = Game(name='The Legend Of Zelda', category='RPG', console='WII')

games: list = [mario, zelda]

user1 = User("gaby", "Gabrielly", "123")
user2 = User("maciel", "Gabriel", "lol")

users: dict = {
    user1.id: user1,
    user2.id: user2
}


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


def user_exists(user: str) -> bool:
    return user in users


def validate_password(user: User, password_given: str) -> None:
    if password_given == user.password:
        session["is_logged"] = password_given


@app.route("/auth", methods=['POST'])
def auth():
    user = request.form["user"]
    if user_exists(user=user):
        validate_password(user=users[user], password_given=request.form["password"])

        if session["is_logged"]:
            flash(f"{users[user].name} logado com sucesso")
            return redirect(request.form['new_page'])

    flash("Tente novamente!")
    return redirect(url_for(endpoint="login"))


app.run(debug=True)
