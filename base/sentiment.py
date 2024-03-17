import string
from nltk.sentiment.vader import SentimentIntensityAnalyzer


def getAnalysis(user_text):
    def analyzeSentiment(sentimentText):
        score = SentimentIntensityAnalyzer().polarity_scores(sentimentText)
        pos = score['pos']
        neg = score['neg']
        if pos < neg:
            print("1")
            return "Negative"
        elif pos > neg:
            print("2")
            return "Positive"
        else:
            print("3")
            return "Nutral"
    text = user_text
    textLower = text.lower()
    cleanText = textLower.translate(str.maketrans("", "", string.punctuation))
    return analyzeSentiment(cleanText)