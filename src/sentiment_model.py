import csv
from twokenizer import tokenize
import nltk
"""
  playing around w machine learning

  http://www.laurentluce.com/posts/twitter-sentiment-analysis-using-python-and-nltk/

"""

class SentimentModel:
    """
        Sentiment model to provide basic sentiment classification for tweets
    """


    # helper functions
    def get_words_in_tweets(self, tweets):
        all_words = []
        for (words, sentiment) in tweets:
            all_words.extend(words)
        return all_words

    def get_word_features(self, wordlist):
        wordlist = nltk.FreqDist(wordlist)
        self.word_features = wordlist.keys()
        #print word_features
        return self.word_features

    def extract_features(self, document):
        document_words = set(document)
        features = {}

        for word in self.word_features:
            features['contains(%s)' % word ] = (word in document_words)
        return features


    # separates content words from hashtags, retweets, emojis
    # also removes words < 3 chars long

    def tokenize_words(self, string):
        # twokenize tokenizer
        tokens = tokenize(string)
        output = []
        for t in tokens:
            if(t[0].isalpha() and len(t)>2):
                output.append(t.lower())
        return output

    def create_classifier(self):
        with open('../Data/working_data.csv', 'rU') as data:
            reader = csv.reader(data, delimiter=',')


            tweets = []
            training = []
            for k, row in enumerate(reader):
                # pick a few tweets randomly
                sentiment = ''
                if(k > 1):
                    #if(int(row[6]) < 3):
                        #words.append(tokenize_words(row[2]))
                    # if(int(row[6]) == 1):
                    #     sentiment = 'negative'
                    # if(int(row[6]) == 2):
                    #     sentiment = 'positive'
                    # if(int(row[6]) == 3):
                    #     sentiment = 'mixed'
                    # if(int(row[6]) == 4):
                    #     sentiment = 'other'

                    #create dict of content, ranking#1
                    tweets.append((self.tokenize_words(row[2]), row[6]))

                #
                # if(k%201==2):
                #     if(int(row[6]) < 3):
                #
                #         tokens = tokenize(row[2])
                #         for t in tokens:
                #             if(t[0].isalpha() and len(t)>2):
                #                 words.append(t.lower())
                #         if(int(row[6]) == 1):
                #             sentiment = 'negative'
                #         if(int(row[6]) == 2):
                #             sentiment = 'positive'

                        #create dict of content, ranking#1
                        # training.append((words, sentiment))
            print ' training sentiment model ...'
            self.word_features = self.get_word_features(self.get_words_in_tweets(tweets))
            self.training_set = nltk.classify.apply_features(self.extract_features, tweets)
            #print training_set[2]
            self.classifier = nltk.NaiveBayesClassifier.train(self.training_set)
            #print classifier.show_most_informative_features(40)
        return self.classifier

        ## FOR AFTER CLASSIFIER HAS BEEN CREATED

    def classify(self, string):

        return self.classifier.classify(self.extract_features(self.tokenize_words(string)))
