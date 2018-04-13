from flask import Flask
from flask import render_template
from flask import request
from mymodules.vsearch import search_for_letters

webapp_title = 'Welcome to search4letters on the web!'

app = Flask(__name__)


@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    results = str(search_for_letters(phrase, letters))
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
