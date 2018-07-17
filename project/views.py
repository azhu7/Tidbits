from flask import render_template, redirect, session, url_for

from project.app import app
from project.forms import QueryForm

import logging


@app.route('/', methods=['GET', 'POST'])
def home():
    form = QueryForm()
    if form.validate_on_submit():
        session['query_result'] = form.query.data
        logging.debug('User queried:|{}|'.format(session['query_result']))
        return redirect(url_for('.results'))
    return render_template('index.html', title='Search', form=form)


@app.route('/results/')
def results():
    query_result = session.get('query_result', default=None)
    if not query_result:
        logging.error('No query result stored. Navigating to home page.')
        return redirect(url_for('.home'))
    return render_template('results.html', query_result=query_result)
