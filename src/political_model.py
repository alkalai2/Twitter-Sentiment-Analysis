import csv
from twokenizer import tokenize
import nltk

# the created sentiment model and candidate matcher
from sentiment_model import SentimentModel
import candidate_matcher

# *********** USAGE **************
#    note: make sure to use in src/ folder
#
#         Python 2.7.5 (default, Mar  9 2014, 22:15:05)
#         [GCC 4.2.1 Compatible Apple LLVM 5.0 (clang-500.0.68)] on darwin
#         Type "help", "copyright", "credits" or "license" for more information.
#         >>> from political_model import PoliticalModel
#         >>> model = PoliticalModel()
#          training sentiment model ...
#         >>> model.view("Obama is a terrorist")
#         {'Candidate': 2, 'Sentiment': 1, 'View': 'Republican'}
#         >>> view = model.view("McCain should be leading this country")
#         >>> view
#         {'Candidate': 1, 'Sentiment': 2, 'View': 'Republican'}
#         >>> view['Candidate']
#         1
#         >>> view['Sentiment']
#         2
#         >>> view['View']
#         'Republican'

class PoliticalModel:
    """
        The PoliticalModel class will combine the outputs of SentimentModel classifaction
        and candidate matching to produce Political views

            Sentiment:    +    Candidate:      ->   Political View:

            Positive            Obama               Democrat
            Negative            McCain              Democrat
            Positive            McCain              Republican
            Negative            Obama               Republican

            Mixed                                   Undecided
            Other                                   Undecided
                                Both                Undecided
                                Neither             Undecided
    """

    def __init__(self):

        # create sentiment model from dataset
        self.sentiment_model = SentimentModel()
        self.sentiment_model.create_classifier()
        #print 'model created'

    def view(self, tweet):
        """
            get political view
        """

        # get sentiment from sentiment_model
        # 1 = negative , 2 = positive , 3 = mixed, 4 = other
        sentiment = int(self.sentiment_model.classify(tweet))

        # 0 = neither  ,  1 = McCain   , 2 = Obama , 3 = both
        candidate = candidate_matcher.match_candidate(tweet)

        view = 'Could not determine'
        if(sentiment > 2 or candidate == 0 or candidate == 3):
            view = 'Undecided'
        else:
            if(sentiment==1):
                if(candidate == 1):
                    view = 'Democrat'
                if(candidate == 2):
                    view = 'Republican'

            if(sentiment==2):
                if(candidate == 1):
                    view = 'Republican'
                if(candidate == 2):
                    view = 'Democrat'

        # return a report of sentiment, candidate, and view
        report = {}
        report['Sentiment'] = sentiment
        report['Candidate'] = candidate
        report['View'] = view

        # output is of the following : {'Sentiment' : 1, 'Candidate' : 2, 'View' : 'Republican' }
        return report
