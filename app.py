from flask import Flask, session, redirect, request, render_template
from flask_sqlalchemy import *
from models.User import User
from sqlalchemy import *
import dotenv
import os
from sqlalchemy.orm import sessionmaker


app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Добавьте секретный ключ для работы с сессиями
dotenv.load_dotenv()


app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_URL')
engine = create_engine('sqlite:///hakaton.db')

@app.route('/reg')
def register():
    return render_template("register.html")


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

    Session = sessionmaker(bind=engine)
    session_db = Session()

    accounts = session_db.execute(select(User)).scalars().all()

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

    Session = sessionmaker(bind=engine)
    session = Session()

    accounts = session.execute(select(User)).scalars().all()

    if double_password == password:
        for acc in accounts:
            if acc.login == login:
                return "Такой Логин уже существует."

        new_user = User(login=login, password=password, username=username)  # Создаем нового пользователя

        session.add(new_user)  # Добавляем его в сессию
        session.commit()  # Сохраняем изменения в базе данных
        return redirect('/')
    else:
        return "Пароли не сходятся, попробуйте снова."

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

