#!/usr/bin/env python3

from mrjob.job import MRJob
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
import string
import re

class SAMapper(MRJob):

    def configure_args(self):
        super(SAMapper, self).configure_args()
        self.add_file_arg('--stopwords', help='Path to NLTK stopwords file')

    def mapper_init(self):
        self.sid = SentimentIntensityAnalyzer()
        self.stop_words = set(stopwords.words('english'))
        self.punctuation = set(string.punctuation)

        if self.options.stopwords:
            with open(self.options.stopwords, 'r') as f:
                custom_stopwords = set(f.read().splitlines())
                self.stop_words.update(custom_stopwords)

    def preprocess_comment(self, comment):
        tokens = re.findall(r'\b\w+\b', comment.lower())
        tokens = [token for token in tokens if token not in self.stop_words and token not in self.punctuation]
        return ' '.join(tokens)

    def get_sentiment_score(self, comment):
        return self.sid.polarity_scores(comment)['compound']

    def mapper(self, _, line):
        comment_id = hash(line)
        preprocessed_comment = self.preprocess_comment(line)
        sentiment_score = self.get_sentiment_score(preprocessed_comment)
        yield comment_id, sentiment_score

if __name__ == '__main__':
    SAMapper.run()
