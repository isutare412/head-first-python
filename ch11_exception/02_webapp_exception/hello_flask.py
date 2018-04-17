from flask import Flask
from flask import render_template
from flask import request
from flask import session
from mymodules.vsearch import search_for_letters
from mymodules.DBcm import UseDatabase
from mymodules.DBcm import DBError
from mymodules.checker import check_logged_in

'''READ mymodules.DBcm
exceptions are raised
'''

dbconfig = {
    'host': '127.0.0.1',
    'user': 'vsearch',
    'password': 'vsearchpassword',
    'database': 'vsearchlogDB',
}

log_insert_query = (
    'INSERT INTO log '
    '(phrase, letters, ip, browser_string, results) '
    'values '
    '(%s, %s, %s, %s, %s)'
)

log_select_query = (
    'SELECT '
    'ts, phrase, letters, ip, browser_string, results '
    'FROM log'
)

webapp_title = 'Welcome to search4letters on the web!'

table_headers = (
    'Time stamp',
    'Phrase',
    'Letters',
    'IP address',
    'Browser',
    'Results',
)


def log_request(req: 'flask_request', res: str) -> None:
    '''Log details of the web request and the results'''
    try:
        with UseDatabase(**dbconfig) as cursor:
            cursor.execute(
                log_insert_query,
                (
                    req.form['phrase'],
                    req.form['letters'],
                    req.remote_addr,
                    req.user_agent.browser,
                    res,
                ),
            )
    except DBError as err:
        print('DB Error: {}'.format(str(err)))
    except Exception as err:
        print('Unhandled Error: {}'.format(str(err)))


app = Flask(__name__)
app.secret_key = "I'm your father!"


@app.route('/login')
def do_login() -> str:
    session['logged_in'] = True
    return 'You are now logged in.'


@app.route('/logout')
def do_logout() -> str:
    del session['logged_in']
    return 'You are now logged out.'


@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    results = str(search_for_letters(phrase, letters))
    log_request(request, results)

    return render_template(
        'results.html',
        the_title=webapp_title,
        the_phrase=phrase,
        the_letters=letters,
        the_results=results,
    )


@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template(
        'entry.html',
        the_title=webapp_title,
    )


@app.route('/viewlog')
@check_logged_in
def view_logs() -> 'html':
    try:
        with UseDatabase(**dbconfig) as cursor:
            cursor.execute(log_select_query)
            log_rows = cursor.fetchall()

        return render_template(
            'viewlog.html',
            the_title='View Log',
            row_titles=table_headers,
            log_data=log_rows,
        )
    except DBError as err:
        print('DB Error: {}'.format(str(err)))
    except Exception as err:
        print('Unhandled Error: {}'.format(str(err)))
    return 'Error occured... dig logs.'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
