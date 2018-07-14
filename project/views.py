from flask import render_template, redirect, url_for

from project.app import app, freezer
from project.forms import QueryForm


@freezer.register_generator
def url_generator():
    yield 'results', {'query_result': 'hello'}
    yield 'results', {'query_result': 'test'}


@app.route('/', methods=['GET', 'POST'])
def home():
    form = QueryForm()
    if form.validate_on_submit():
        return redirect(url_for('.results', query_result=form.query.data))
    return render_template('index.html', title='Search', form=form)


@app.route('/results/<string:query_result>/')
def results(query_result):
    return render_template('results.html', query_result=query_result)
