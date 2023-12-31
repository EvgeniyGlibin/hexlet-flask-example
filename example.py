from flask import Flask, request, redirect, flash, get_flashed_messages
from flask import render_template
import os
from validator import validate
import json

# Это callable WSGI-приложение
app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

# устанавливаем секретный ключ для работы с сессиями (Flash-сообщения)
app.secret_key = "secret_key"


@app.route('/')
def hello_world():
    print(request.headers)
    return f'Hello, World!'

@app.route('/html/')
def html():
    return render_template('index.html')

@app.route('/not_found')
def not_found():
    return 'Oops!', 404

@app.route('/courses/<course_id>/lessons/<lessons_id>')
def courses(course_id, lessons_id):
    return f'Courses id: {course_id}, Lessons id: {lessons_id}'

@app.route('/users/<id>')
def welcome_user(id):
    return render_template(
        '/users/show.html',
        name=id,
    )

users = [
    'mike', 'mishel', 'adel', 'keks', 'kamila'
]

@app.route('/users/new')
def users_new():
    user = {'name': '',
            'email': '',
            'city': ''}
    errors = {}

    return render_template(
        'users/new.html',
        user=user,
        errors=errors
    )


@app.post('/users')
def users_post():
    user = request.form.to_dict()
    errors = validate(user)
    if errors:
        render_template(
            '/users/new.html',
            user=user,
            errors=errors
        ), 422

    with open('data_users.json', 'w+', encoding="utf-8") as file:
        file.write(json.dumps(user))
    flash('User was added successful', 'success')  #  flash сообщение активируется, показано будеет на другой страничке

    return redirect('/users', code=302)


@app.route('/users')
def get_users():
    result = users
    search = request.args.get('term', '')
    if search:
        result = [user for user in users if search in user]
    # Извлечение flash-сообщений, которые установлены на предыдущем запросе
    messages = get_flashed_messages(with_categories=True)
    print(messages)
    return render_template(
        'users/index.html',
        users=result,
        search=search,
        messages=messages
    )
