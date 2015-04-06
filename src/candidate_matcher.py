
import csv
from itertools import repeat


# 0 = neither  ,  1 = McCain   , 2 = Obama , 3 = both

def match(col_content, col_candidate):
    """
        insert will provide the column number that matching values should be placed in
    """

    with open('../Data/debate08_sentiment_tweets.tsv', 'rU') as tsvin, open('../Data/working_data.csv', 'wb') as csvout:
        print "opened tsv, created output.csv"
        tsvin = csv.reader(tsvin, dialect=csv.excel_tab)
        csvout = csv.writer(csvout)

        # move data to csv
        #all = []
        for k, row in enumerate(tsvin):
            if(k > 28):
                if(k==29):
                    ## place 'candidate' column after 'author.nickname'
                    row.insert(col_candidate, 'candidate')
                else:
                    candidate = 0
                    if(row[col_content].lower().find('mccain') > -1):
                        candidate = 1
                    if(row[col_content].lower().find('obama') > -1):
                        if(candidate==1):
                            candidate = 3
                        else:
                            candidate = 2
                    row.insert(col_candidate, candidate)
                csvout.writerow(row)
        print 'populated output.csv'

def match_candidate(string):
    """
        Matches a string to a candidate
        # 0 = neither  ,  1 = McCain   , 2 = Obama , 3 = both
    """
    candidate = 0
    if(string.lower().find('mccain') > -1):
        candidate = 1
    if(string.lower().find('obama') > -1):
        if(candidate==1):
            candidate = 3
        else:
            candidate = 2
    return candidate
