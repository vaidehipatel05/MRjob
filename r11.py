#!/usr/bin/env python3
"""r11.py"""

from mrjob.job import MRJob

def classify_sentiment(score):
    if score >= 0.05:
        return 'Positive'
    elif score <= -0.05:
        return 'Negative'
    else:
        return 'Neutral'

class SentimentAnalysisReducer(MRJob):
    def reducer(self, comment_id, scores):
        total_sentiment_score = 0
        comment_count = 0

        for score_str in scores:
            comment_id_str, score = score_str.split('\t')
            total_sentiment_score += float(score) 
            comment_count += 1

        average_sentiment_score = total_sentiment_score / comment_count
        sentiment = classify_sentiment(average_sentiment_score)
        yield comment_id, (average_sentiment_score, sentiment)


if __name__ == '__main__':
    SentimentAnalysisReducer.run()
