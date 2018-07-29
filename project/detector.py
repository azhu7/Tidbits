"""
Sentiment detector for Tidbits:
Utilizes the Google Cloud Platform Natural Language Processing API.
"""


class SentimentScore:
    """
    Score object containing a valence (pos/neg/neutral) score on a scale of [-1.0, 1.0],
    and a magnitude score on a scale of [0.0, inf) - as defined by the GCP NLP API.

    Note that a neutral sentence will have near 0.0 score and magnitude,
    while a mixed sentence will average to near 0.0 score but have greater magnitude.
    """
    def __init__(self, score, magnitude):
        self.score = score
        self.magnitude = magnitude


def detect_sentence_sentiment(sentence):
    """
    Take a list of words, treats it as a sentence and performs sentiment analysis on it.

    TODO: depending on how we pull data, we can send one request per document and get
    sentiment scores for each sentence within. In that case we can return a list of
    SentimentScore objects, one per sentence.

    :param sentence: String[] of words composing a sentence
    :return: SentimentScore object with scores for the entire sentence
    """
    return SentimentScore(1.0, 1.0)


def detect_entity_sentiment(sentence):
    """
    Take a list of words, treats it as a sentence and performs entity sentiment analysis on it.
    Entity sentiment analysis extracts entities (nouns and proper nouns), and detects sentiment
    for each occurrence of each entity.

    :param sentence: String[] of words composing a sentence
    :return: map of entity_name -> SentimentScore[] containing
                one score object per occurrence of the entity
    """
    return {"": [SentimentScore(1.0, 1.0)]}
