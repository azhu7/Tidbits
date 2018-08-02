"""Views for Tidbits."""

import logging

from flask import redirect, render_template, session, url_for

from project.app import app
from project.forms import QueryForm
from project.query import Query


@app.route('/', methods=['GET', 'POST'])
def home():
    """Home page."""
    # query_instance = Query()
    form = QueryForm()
    if form.validate_on_submit():
        session['query_result'] = form.query.data
        # print query_instance.twitter_search(session['query_result'])
        logging.debug('User queried:|%s|', session['query_result'])
        return redirect(url_for('.results'))
    return render_template('index.html', title='Search', form=form)


@app.route('/results/')
def results():
    """Results page."""
    query_result = session.get('query_result', default=None)
    if not query_result:
        logging.error('No query result stored. Navigating to home page.')
        return redirect(url_for('.home'))
    return render_template('results.html', query_result=query_result)
