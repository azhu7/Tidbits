from flask import redirect, render_template , session, url_for

from project.app import app
from project.forms import QueryForm


@app.route('/', methods=['GET', 'POST'])
def home():
    form = QueryForm()
    if form.validate_on_submit():
        session['query_result'] = form.query.data
        return redirect(url_for('.results'))
    return render_template('index.html', title='Search', form=form)


@app.route('/results/')
def results():
    return render_template('results.html', query_result=session['query_result'])
