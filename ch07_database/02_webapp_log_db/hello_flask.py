from flask import Flask
from flask import render_template
from flask import request
import mysql.connector
from mymodules.vsearch import search_for_letters

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

webapp_title = 'Welcome to search4letters on the web!'


def log_request(req: 'flask_request', res: str) -> None:
    dbconn = mysql.connector.connect(**dbconfig)
    dbcursor = dbconn.cursor()

    dbcursor.execute(
        log_insert_query,
        (
            req.form['phrase'],
            req.form['letters'],
            req.remote_addr,
            req.user_agent.browser,
            res,
        )
    )
    dbconn.commit()

    dbcursor.close()
    dbconn.close()


app = Flask(__name__)


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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
