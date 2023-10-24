from flask import Flask, request
from flask import render_template

# Это callable WSGI-приложение
app = Flask(__name__)

@app.route('/')
def hello_world():
    print(request.headers)
    return f'Hello, World!'

@app.route('/json/')
def json():
    return {'json': 42}

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



@app.route('/users')
def get_users():
    result = users
    search = request.args.get('term', '')
    if search:
        result = [user for user in users if search in user]

    return render_template(
        'users/index.html',
        users=result,
        search=search,
    )


# def filter_name(user, search):
#     return user.lower().startswith(search.lower())

