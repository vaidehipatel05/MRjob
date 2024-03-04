"""#!/usr/bin/env python3

from mrjob.job import MRJob
from statistics import mean

class SentimentAnalysisReducer(MRJob):

    def get_sentiment_label(self, score):
        if score >= 0.05:
            return 'Positive'
        elif score <= -0.05:
            return 'Negative'
        else:
            return 'Neutral'

    def reducer(self, _, lines):
        for line in lines:
            comment_id, sentiment_score = line.strip().split('\t')
            # Check if comment ID is not "null" or "0"
            if comment_id != "null" and comment_id != "0":
                sentiment_score = float(sentiment_score)
                sentiment_label = self.get_sentiment_label(sentiment_score)
                yield comment_id, (sentiment_score, sentiment_label)

if __name__ == '__main__':
    SentimentAnalysisReducer.run()
"""



#!/usr/bin/env python3

import sys
from statistics import mean

class SAReducer:

    def get_sentiment_label(self, score):
        if score >= 0.05:
            return 'Positive'
        elif score <= -0.05:
            return 'Negative'
        else:
            return 'Neutral'

    def reducer(self):
        for line in sys.stdin:
            comment_id, sentiment_score = line.strip().split('\t')
            if comment_id != "null" and comment_id != "0":
                sentiment_score = float(sentiment_score)
                sentiment_label = self.get_sentiment_label(sentiment_score)
                yield comment_id, (sentiment_score, sentiment_label)

if __name__ == '__main__':
    reducer = SAReducer()
    reducer.reducer()
