# print("hello");
import pandas as pd
# import csv

filePath = 'Spokane_Squadron_promotion_report_8_9_2023.csv'

with open(filePath) as file:
    # csvFile = csv.reader(file)
    # for lines in csvFile:
    #     print(lines)
    dataFrame = pd.read_csv(filePath, sep=",")

