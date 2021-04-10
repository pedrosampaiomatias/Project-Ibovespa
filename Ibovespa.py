# Read daily data from Ibovespa

dataDay = open("D:\\Codes\\Python\\Projeto Ibovespa\\Project-Ibovespa\\Data\\COTAHIST_D26032021.txt", 'r')

# Passing readline() 0
# line = dataDay.readline()

# Reading stocks data
dataStock = {}

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


# Close file after reading
dataDay.close

# Reading Ibovespa index
dataIbov = open("D:\\Codes\\Python\\Projeto Ibovespa\\Project-Ibovespa\\Data\\IBOVDia_26-03-21.csv")

ibovStock = []

while True:
    line = dataIbov.readline()

    if not line:
        break

    ibovStockTmp = line[0:line.index(";")]    
    ibovStock.append(ibovStockTmp)

# Getting top stocks

topValuationStock = []

for stock in dataStock:
    if dataStock[stock]["tradingCode"] in ibovStock:
        topValuationStock.append(dataStock[stock])

topValuationStock.sort(key= lambda i: i['changeDayPercent'], reverse=True)

print(topValuationStock[0:4])