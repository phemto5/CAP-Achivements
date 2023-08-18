# print("hello");
import pandas as pd
# import numpy
import math
# import csv

filePath = 'Spokane_Squadron_promotion_report_8_9_2023.csv'

with open(filePath) as file:
    # csvFile = csv.reader(file)
    # for lines in csvFile:
    #     print(lines)
    dataFrame = pd.read_csv(filePath, sep=",")

    for index, row in dataFrame.iterrows():
        print("|------------------------------------------------")
        print("|"+row["NameLast"] + ", " + row["NameFirst"])
        print("|-"+"Working on Acivement:" + row["AchvName"])
        for  kname in dataFrame.columns:
            if str(row[kname]).isdigit():
                    if float(row[kname]) == 0:
                        print(f"|-- {kname}")
            else:
                if pd.isna(row[kname]):
                    print(f"|-- {kname}")
        print("|------------------------------------------------\n")
