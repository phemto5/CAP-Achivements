import pandas as pd

filePath = 'Spokane_Squadron_promotion_report_8_9_2023.csv'

with open(filePath) as file:
    dataFrame = pd.read_csv(filePath, sep=",")
    for index, row in dataFrame.iterrows():
        markdownFile = f'{row["Email"]}.md'
        with open(markdownFile, "w+") as mdf:
            mdf.write("# "+row["NameLast"] + ", " + row["NameFirst"] + "\n")
            mdf.write(">*Working on Achievement*:\n" )
            mdf.write(">**" + row["AchvName"]+ "**\n\n")
            for  kname in dataFrame.columns:
                if str(row[kname]).isdigit():
                        if float(row[kname]) != 0:
                            row.pop(kname)
                else:
                    if not pd.isna(row[kname]):
                        row.pop(kname)
                    else:
                        row[kname] = 'Not Completed'
            mdf.writelines(row.to_markdown())
            mdf.write("\n")
            mdf.close()
