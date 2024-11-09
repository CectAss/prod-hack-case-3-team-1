from flask import Flask, session, redirect, request, render_template
from flask_sqlalchemy import *
from models.User import User
from sqlalchemy import *
import dotenv
import os


app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Добавьте секретный ключ для работы с сессиями
dotenv.load_dotenv()


app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_URL')
db = SQLAlchemy(app)

@app.route('/reg')
def register():
    return render_template("register.html")

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')


@app.route('/')
def index():
    if session.get('auth') == True:
        return render_template("index.html")
    else:
        return render_template("info.html")

#@app.route('/api/count_journeys/<int:user_id>')

@app.route('/login')
def log():
    return render_template("login.html")


@app.route('/login', methods=['POST'])
def login():
    login = request.form['login']
    password = request.form['password']
    accounts = db.session.execute(db.select(User)).scalars().all()

    for acc in accounts:
        if login == acc.login and password == str(acc.password):
            session['auth'] = True
            return redirect('/')

    return redirect('/login')

@app.route('/reg', methods=['POST'])
def reg():
    login = request.form['login']  # Изменено для получения логина
    password = request.form['password']
    double_password = request.form['double_password']
    username = request.form['name']

    accounts = db.session.execute(db.select(User)).scalars().all()

    if double_password == password:
        for acc in accounts:
            if acc.login == login:
                return "Такой Логин уже существует."

        new_user = User(login=login, password=password, username=username)  # Создаем нового пользователя

        db.session.add(new_user)  # Добавляем его в сессию
        db.session.commit()  # Сохраняем изменения в базе данных
        return redirect('/')
    else:
        return "Пароли не сходятся, попробуйте снова."


if __name__ == '__main__':
    app.run(debug=True)