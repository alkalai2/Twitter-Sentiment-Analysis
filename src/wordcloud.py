import csv


with open('../Data/wordcloud.csv') as data:
    reader = csv.reader(data, delimiter=',')
    file = open('../Data/wordcloud.txt', 'r+')
    for k, r in enumerate(reader):
        if(k > 1):
            freq = int(round(float(r[9])))*10
            #freq = int(r[5]*10)
            for f in range(0,freq):
                file.write(r[8] + '\n')
                print r[4]
    file.close()
