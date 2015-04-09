import csv
import json
from twokenizer import tokenize
import nltk

from political_model import PoliticalModel
from sentiment_model import SentimentModel



# create a report in Data/report.txt that will show the
# total performance of our model



def make_report(political_model):


    report = {}

    # report the sentiment breakdown of our model
    sents = {}
    sents['positive'] = 0
    sents['negative'] = 0
    sents['mixed'] = 0
    sents['other'] = 0
    report['sentiment_breakdown'] = sents

    # report candidate breakdown of our model
    cands = {}
    cands['obama'] = 0
    cands['mccain'] = 0
    cands['both'] = 0
    cands['neither'] = 0
    report['candidate_breakdown'] = cands

    # report view breakdown
    views = {}
    views['democrats'] = 0
    views['republicans'] = 0
    views['undecided'] = 0
    report['view_breakdown'] = views

    # report the sentiment accuracy, show details of correct/incorrect judges
    acc = {}

    acc['correct sents'] = 0
    correct = {}
    correct['positive'] = 0
    correct['negative'] = 0
    correct['mixed'] = 0
    correct['other'] = 0
    acc['correct_breakdown'] = correct

    acc['incorrect sents'] = 0
    incorrect = {}
    incorrect['positive'] = 0
    incorrect['negative'] = 0
    incorrect['mixed'] = 0
    incorrect['other'] = 0
    acc['incorrect_breakdown'] = incorrect
    acc['total sents'] = 0
    acc['accuracy'] = 0
    report['accuracy_breakdown'] = acc


    with open('../Data/debate08_sentiment_tweets.tsv', 'rU') as data:
        reader = csv.reader(data, dialect=csv.excel_tab)

        for k, row in enumerate(reader):
            if(k > 29):
                myresult = political_model.view(row[2])

                # update sents
                mysent = int(myresult['Sentiment'])
                if mysent == 1:
                    sents['negative'] = sents['negative'] + 1
                elif mysent == 2:
                    sents['positive'] = sents['positive'] + 1
                elif mysent == 3:
                    sents['mixed'] = sents['mixed'] + 1
                elif mysent == 4:
                    sents['other'] = sents['other'] + 1

                # update cands
                mycand = int(myresult['Candidate'])
                if mycand == 0:
                    cands['neither'] = cands['neither'] + 1
                elif mycand == 1:
                    cands['mccain'] = cands['mccain'] + 1
                elif mycand == 2:
                    cands['obama'] = cands['obama'] + 1
                elif mycand == 3:
                    cands['both'] = cands['both'] + 1

                # update view
                myview = myresult['View']
                if myview == 'Democrat':
                    views['democrats'] = views['democrats'] + 1
                elif myview == 'Republican':
                    views['republicans'] = views['republicans'] + 1
                elif myview == 'Undecided':
                    views['undecided'] = views['undecided'] + 1

                # update accuracy

                real_sent = int(row[5])
                we_were_right = (mysent == real_sent)
                if we_were_right == True:
                    acc['correct sents'] = acc['correct sents'] + 1
                    if real_sent == 1:
                        correct['negative'] = correct['negative'] + 1
                    elif real_sent == 2:
                        correct['positive'] = correct['positive'] + 1
                    elif real_sent == 3:
                        correct['mixed'] = correct['mixed'] + 1
                    elif real_sent == 4:
                        correct['other'] = correct['other'] + 1

                elif we_were_right == False:
                    acc['incorrect sents'] = acc['incorrect sents'] + 1
                    if real_sent == 1:
                        incorrect['negative'] = incorrect['negative'] + 1
                    elif real_sent == 2:
                        incorrect['positive'] = incorrect['positive'] + 1
                    elif real_sent == 3:
                        incorrect['mixed'] = incorrect['mixed'] + 1
                    elif real_sent == 4:
                        incorrect['other'] = incorrect['other'] + 1
                acc['total sents'] = acc['total sents'] + 1
        acc['accuracy'] = (float(acc['correct sents'])/float(acc['total sents']))


        ## Write everything to report.txt

        print report

        file = open('../Data/report.txt', 'r+')

        file.write(' POLITICAL MODEL REPORT \n \n')

        file.write('Sentiments\n')
        file.write('\t positive : ' +   repr(sents['positive']) + '\n')
        file.write('\t negative : ' +   repr(sents['negative']) + '\n')
        file.write('\t mixed : ' +      repr(sents['mixed']) + '\n')
        file.write('\t other : ' +      repr(sents['other']) + '\n')

        file.write('Candidates\n')
        file.write('\t obama : ' +      repr(cands['obama']) + '\n')
        file.write('\t mccain : ' +     repr(cands['mccain']) + '\n')
        file.write('\t bother : ' +     repr(cands['both']) + '\n')
        file.write('\t neither : ' +    repr(cands['neither']) + '\n')

        file.write('Views\n')
        file.write('\t democrats : ' +  repr(views['democrats']) + '\n')
        file.write('\t republicans : ' +repr(views['republicans']) + '\n')
        file.write('\t undecided : ' +  repr(views['undecided']) + '\n')

        file.write('Accuracy :' +       repr(acc['accuracy']) + '\n')
        file.write('\t Correct :' +     repr(acc['correct sents']) + '\n')
        file.write('\t\t positive : ' + repr(correct['positive']) + '\n')
        file.write('\t\t negative : ' + repr(correct['negative']) + '\n')
        file.write('\t\t mixed : ' +    repr(correct['mixed']) + '\n')
        file.write('\t\t other : ' +    repr(correct['other']) + '\n')
        file.write('\t Incorrect :' +   repr(acc['incorrect sents']) + '\n')
        file.write('\t\t positive : ' + repr(incorrect['positive']) + '\n')
        file.write('\t\t negative : ' + repr(incorrect['negative']) + '\n')
        file.write('\t\t mixed : ' +    repr(incorrect['mixed']) + '\n')
        file.write('\t\t other : ' +    repr(incorrect['other']) + '\n')
        file.write('\t Total : ' +      repr(acc['total sents']) + '\n')

        file.close()

        # put report as json in report.json
        f = open('../Data/report.json', 'r+')
        f.write(json.dumps(report))
        f.close()

        # return report if we want to use for visuals, etc.
        return report
