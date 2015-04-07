import csv
from twokenizer import tokenize
import nltk

# the created sentiment model and candidate matcher
from sentiment_model import SentimentModel
from candidate_matcher import match_candidate

# Comment for pedro 
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
        candidate = match_candidate(tweet)

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

        print 'Sentiment: ' + repr(sentiment)
        print 'Candidate: ' + repr(candidate)
        print 'View: ' + view
        #return view
