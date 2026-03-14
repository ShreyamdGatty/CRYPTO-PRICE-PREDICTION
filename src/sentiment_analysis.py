from textblob import TextBlob
import pandas as pd

def sentiment_analysis(news_list):

    sentiments = []

    for news in news_list:

        polarity = TextBlob(news).sentiment.polarity
        sentiments.append(polarity)

    return pd.DataFrame({
        "news":news_list,
        "sentiment":sentiments
    })
