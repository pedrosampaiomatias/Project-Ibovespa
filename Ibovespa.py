# Read daily prices from Ibovespa

dataDay = open("D:\\Codes\\Python\\Projeto Ibovespa\\Data\\COTAHIST_D23032021.txt", 'r')
dataStock = {}

# Passing readline() 0
line = dataDay.readline()

# Reading data

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
            "BDICode"       : line[10:12].strip(),
            "tradingCode"   : line[12:24].strip(),
            "market"        : line[24:27].strip(),
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

# Data refination

