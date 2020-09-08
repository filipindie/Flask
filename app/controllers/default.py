#Aqui ficam as rotas das páginas
from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user
from app import app, lm
from app.models.tables import db

from app.models.tables import Users
from app.models.forms import LoginForm


@lm.user_loader
def load_user(id):
    return Users.select().where(Users.id==id).first()

@app.route("/index")
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=['GET', "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = Users.select().where(Users.username == form.username.data).first()
        # print(user.password)
        # print(form.password)
        if user and user.password == form.password.data:
            login_user(user)
            flash("Logged in.")
            return redirect(url_for("index"))
            # print(form.username.data)
            # print(form.password.data)
        else:
            flash("Invalid login.")
    
    return  render_template('login.html', form=form)

@app.route("/logout")
def logout():
    logout_user()
    flash("Logged out")
    return redirect(url_for("index"))



# essa parte pode ter funcionalidade de criar usuário
# @app.route("/teste/<info>")
# @app.route("/teste", defaults={"info": None})
# def teste(info):
#     i = Users.create(username='emily', name='Emily Costa', password='1234', email='emily@gmail.com')
#     # i = Users.delete().where(Users.name== 'hig').execute()
#     i.save()
#     return "ok"

