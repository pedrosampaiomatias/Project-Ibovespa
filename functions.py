# functions.py
# Description: File with functions definitions data 23-30

import csv

# Function: convertToCSV()
# Description: Convert .txt file with daily stocks data to a .csv file

def convertToCSV(dataDay):

    # Reading data from .txt
    
    dataStock = {}
    header = ' '

    for line in dataDay:
        line = dataDay.readline()
        registerType = int(line[0:2])

        # Header
        if registerType == 0:
            header = line

        # Trailer
        elif registerType == 99:
            trailer = line

        # Stock price per day
        else:
            dataStockTmp = {
                "tradingDate"   : line[2:10].strip(),
                "BDICode"       : int(line[10:12].strip()),
                "tradingCode"   : line[12:24].strip(),
                "market"        : int(line[24:27].strip()),
                "name"          : line[27:39].strip(),
                "especification": line[39:49].strip(),
                "deadline"      : line[49:52].strip(),
                "currency"      : line[52:56].strip(),
                "openPrice"     : float(line[56:69].strip()) / 100,
                "maxPrice"      : float(line[69:82].strip()) / 100,
                "minPrice"      : float(line[82:95].strip()) / 100,
                "medPrice"      : float(line[95:108].strip()) / 100,
                "closePrice"    : float(line[108:121].strip()) / 100,
                "bestBuyPrice"  : float(line[121:134].strip()) / 100,
                "bestSellPrice" : float(line[134:147].strip()) / 100
            }

        dataStock.update({dataStockTmp["tradingCode"]:dataStockTmp})

    # Creating .csv file

    fileName = header[23:30]
    with open(fileName,'w') as newFile:
        csv_writer = csv.writer(newFile, delimiter=',')

        for line in dataStock:
            csv_writer.writerow(line)
