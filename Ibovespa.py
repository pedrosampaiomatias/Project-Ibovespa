# Read daily data from Ibovespa

dataDay = open("D:\\Codes\\Python\\Projeto Ibovespa\\Project-Ibovespa\\Data\\COTAHIST_D26032021.txt", 'r')

# Reading Ibovespa index
dataIbov = open("D:\\Codes\\Python\\Projeto Ibovespa\\Project-Ibovespa\\Data\\IBOVDia_26-03-21.csv")

ibovStock = []

while True:
    line = dataIbov.readline()

    if not line:
        break

    ibovStockTmp = line[0:line.index(";")]    
    ibovStock.append(ibovStockTmp)

# # Getting top stocks

# topValuationStock = []

# for stock in dataStock:
#     if dataStock[stock]["tradingCode"] in ibovStock:
#         topValuationStock.append(dataStock[stock])

# topValuationStock.sort(key= lambda i: i['changeDayPercent'], reverse=True)

# print(topValuationStock[0:4])