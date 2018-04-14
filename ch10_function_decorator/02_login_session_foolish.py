from flask import Flask
from flask import session


def check_logged_in() -> bool:
    if 'logged_in' in session:
        return True
    return False


app = Flask(__name__)

app.secret_key = 'I am your father!'


@app.route('/')
def hello() -> str:
    return 'Hello from the simple webapp.'


@app.route('/login')
def do_login() -> str:
    session['logged_in'] = True
    return 'You are now logged in'


@app.route('/logout')
def do_logout() -> str:
    del session['logged_in']
    return 'You are no longer logged in'


@app.route('/status')
def check_status() -> str:
    if 'logged_in' in session:
        return 'You are currently logged in.'
    return 'You are NOT logged in.'


@app.route('/page1')
def page1() -> str:
    if not check_logged_in():
        return 'You are NOT logged in.'
    return 'This is page 1.'


@app.route('/page2')
def page2() -> str:
    if not check_logged_in():
        return 'You are NOT logged in.'
    return 'This is page 2.'


@app.route('/page3')
def page3() -> str:
    if not check_logged_in():
        return 'You are NOT logged in.'
    return 'This is page 3.'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
