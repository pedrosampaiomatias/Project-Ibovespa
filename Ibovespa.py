# Ibovespa.py
# Description: Main file for Ibovespa.py project

import os
import functions

# Read daily data from Ibovespa and creat .csv files for pandas

# Data folder path
dataPath = "D:\\Codes\\Python\\Projeto Ibovespa\\Project-Ibovespa\\Data"

os.chdir(dataPath)

for file in os.listdir():
    file_path = f"{dataPath}\\{file}"
    functions.convertToCSV(open(file_path), dataPath)