from flask import render_template, flash, redirect, url_for, request

from project.app import app
from project.forms import QueryForm


@app.route('/', methods=['GET', 'POST'])
def home():
    form = QueryForm()
    if form.validate_on_submit():
        response = form.query.data
        return redirect(url_for('.results', response=response))
    return render_template('index.html', title='Search', form=form)


@app.route('/results')
def results():
    response = request.args['response']
    return render_template('results.html', response=response)
