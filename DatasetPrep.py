"""
Prepare dataset for data processing.
As we scraped data from source, some datas were including dots(.) and additional blanks.
With this code part, we are creating a new csv file that what we want.
"""

import csv

with open("carInfosNew.csv", 'r') as read_obj:
    with open('carInfosNewVers3.csv', 'w', newline='') as csvfile:
        csv_reader = csv.reader(read_obj)
        readList = [row for row in csv_reader]
        csv_writer = csv.writer(csvfile, delimiter=',')
        for i in range(len(readList)):
            csv_writer.writerow((readList[i][0], readList[i][1], readList[i][2], readList[i][3], readList[i][4].replace(".",""), readList[i][5][:-2].strip(), readList[i][6][:-2].strip(), readList[i][7].replace(".","")))
