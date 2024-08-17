import csv
import json
def CSV_TO_JSON():
    jsondata = []
    with open('/Users/macbookair/Documents/CSV-TO-JSON/data1.csv', 'r') as file:
        data = list(csv.reader(file))
        colums = data[0]
        for row in data[1:]:
            allrows = dict()
            for index, value in enumerate(row):
                allrows[colums[index]] = value
                jsondata.append(allrows)
    with open('/Users/macbookair/Documents/CSV-TO-JSON/sample.json', 'w') as file:
        file.write(json.dumps(jsondata, indent = 5 ))
CSV_TO_JSON()
