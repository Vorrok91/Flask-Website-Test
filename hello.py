from flask import Flask
from markupsafe import escape
from flask import url_for

app = Flask(__name__)

"""
@app.route('/')
def index():
    return 'This is the Index Page!'

@app.route('/hello')
def hello():
    return 'Hello, World'
"""

"""
@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'
"""

"""
@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'
"""

@app.route('/')
def index():
    return 'index'

@app.route('/login')
def login():
    return 'login'

@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'

with app.test_request_context():
    print('http://127.0.0.1:5000' + url_for('index'))
    print('http://127.0.0.1:5000' + url_for('login'))
    print('http://127.0.0.1:5000' + url_for('login', next='/'))
    print('http://127.0.0.1:5000' + url_for('profile', username='John Doe'))