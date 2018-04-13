from flask import Flask
from flask import render_template
from flask import request
from flask import escape
from mymodules.vsearch import search_for_letters

webapp_title = 'Welcome to search4letters on the web!'
log_name = 'vsearch.log'


# leave log to file
def log_request(req: 'flask_request', res: str) -> None:
    with open(log_name, 'a') as log:
        print(
            req.form,
            req.remote_addr,
            req.user_agent,
            res,
            sep='|',
            file=log,
        )


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


# view logs before
@app.route('/viewlog')
def view_logs() -> 'html':
    formatted = []
    with open(log_name) as log:
        for line in log:
            formatted.append([])
            for data in line.split('|'):
                formatted[-1].append(escape(data.rstrip()))
    headers = ('Form Data', 'Remote_addr', 'User_agent', 'Results')
    return render_template(
        'viewlog.html',
        the_title='View Log',
        row_titles=headers,
        log_data=formatted,
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
