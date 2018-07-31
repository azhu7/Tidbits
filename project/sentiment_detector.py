"""Sentiment detector for Tidbits:
Utilizes the Google Cloud Platform Natural Language Processing API.
"""
from collections import namedtuple

"""tuple containing sentiment score (pos/neg/neutral rating) and magnitude,
as defined by the GCP NLP API.
"""
SentimentScore = namedtuple('SentimentScore', ['score', 'magnitude'])


def detect_sentence_sentiment(sentence):
    """Performs sentiment analysis on a sentence.

    TODO(jason): depending on how we pull data, we can send one request per document and get
    sentiment scores for each sentence within. In that case we can return a list of
    SentimentScore objects, one per sentence.

    :param sentence: String[] of words composing a sentence
    :return: SentimentScore object with scores for the entire sentence
    """
    return SentimentScore(1.0, 1.0)


def detect_entity_sentiment(sentence):
    """Performs entity sentiment analysis on a sentence.
    Entity sentiment analysis extracts entities (nouns and proper nouns), and detects sentiment
    for each occurrence of each entity.

    :param sentence: String[] of words composing a sentence
    :return: map of entity_name -> SentimentScore[] containing
                one score object per occurrence of the entity
    """
    return {"": [SentimentScore(1.0, 1.0)]}
