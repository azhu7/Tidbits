"""Flask app setup."""

import logging

from flask import Flask, redirect, render_template, session, url_for
from project.forms import QueryForm
from project.query import Query


def create_app(config):
    """Initialize Flask app and its endpoints."""
    app = Flask(__name__)
    app.config.from_object(config)

    @app.route('/', methods=['GET', 'POST'])
    def home():  # pylint: disable=unused-variable
        """Home page."""
        form = QueryForm()
        if form.validate_on_submit():
            session['query_result'] = form.query.data
            logging.debug('User queried:|%s|', session['query_result'])
            return redirect(url_for('.results'))
        return render_template('index.html', title='Search', form=form)

    @app.route('/results/')
    def results():  # pylint: disable=unused-variable
        """Results page."""
        query_result = session.get('query_result', default=None)
        if not query_result:
            logging.error('No query result stored. Navigating to home page.')
            return redirect(url_for('.home'))
        return render_template('results.html', query_result=query_result)

    return app
