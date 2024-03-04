#!/usr/bin/env python3
"""m11.py"""

from mrjob.job import MRJob
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
import string
import re


sid = SentimentIntensityAnalyzer()
stop_words = set(stopwords.words('english'))

def preprocess_comment(comment):
    tokens = re.findall(r'\b\w+\b', comment.lower())
    tokens = [token for token in tokens if token not in stop_words and token not in string.punctuation]
    preprocessed_comment = ' '.join(tokens)
    return preprocessed_comment

def get_sentiment_score(comment):
    scores = sid.polarity_scores(comment)
    return scores['compound']

class SentimentAnalysisMapper(MRJob):
    def mapper(self, _, line):
        parts = line.strip().split(',', 1)
        if len(parts) == 2:
            comment_id, comment = parts
            preprocessed_comment = preprocess_comment(comment)
            sentiment_score = get_sentiment_score(preprocessed_comment)
            yield comment_id, sentiment_score

if __name__ == '__main__':
    SentimentAnalysisMapper.run()
