"""Views for Tidbits."""

import logging
import tweepy

from flask import redirect, render_template, session, url_for

from project.app import app
from project.forms import QueryForm
import project.api_config # if error, read the docstring in api_config_example


@app.route('/', methods=['GET', 'POST'])
def home():
    """Home page."""
    twitter_config = project.api_config.TWITTER_CONFIG
    try:
        auth = tweepy.OAuthHandler(twitter_config['consumer_key'], twitter_config['consumer_secret'])
        auth.set_access_token(twitter_config['access_token'], twitter_config['access_token_secret'])

        api = tweepy.API(auth)
    except:
        print "Authentification failed"
    search = api.search(q='hitler', lang='en', count='100', tweet_mode='extended')
    for item in search:
        print item.full_text
        print item.display_text_range
        print "--------------"

    form = QueryForm()
    if form.validate_on_submit():
        session['query_result'] = form.query.data
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
