import pandas as pd
import md2pdf.core as mp
from PyPDF2 import PdfMerger
import sys
filePath = 'Spokane_Squadron_promotion_report_8_9_2023.csv'
notCompletedMsg = "Not Completed"
allCadetsFile = 'Cadets.All.pdf'


merger = PdfMerger()

def makeAllStrings(row, kname):
    if kname in row:
        if str(row[kname]).isdigit():
            if float(row[kname]) == 0:
                row[kname] = notCompletedMsg
        else:
            if pd.isna(row[kname] or row[kname] == 'h'):
                row[kname] = notCompletedMsg

def ProcessRecord(row):
    # print(f'Processing:{row["Email"]}')
    emailAddress = (f'{row["Email"]}')
    markdownFile = f'{emailAddress}.md'
    with open(markdownFile, "w+") as mdf:
        with open('./Exceptions.yaml') as exceptions:
            lName = row["NameLast"]
            fName = row["NameFirst"]
            achvName = row["AchvName"]
            mdf.write("# "+lName + ", " + fName + "\n\n")
            mdf.write('## Working on Achievement : **' + achvName + '** \n***\n')
            for kname in row.index:
                makeAllStrings(row, kname)
                match kname:
                    case  "AEInteractiveDate" | "AEModuleOrTest":
                        if kname in row:
                            if row["AEModuleOrTest"] != row["AEInteractiveDate"]:
                                row.pop("AEModuleOrTest")
                                row.pop("AEInteractiveDate")
                    case "EssayDate":
                        if achvName != "Achievement 8":
                            row.pop(kname)
                    case "SpeechDate":
                        if achvName != "Achievement 8":
                            row.pop(kname)
                    case "OralPresentationDate":
                        if achvName != "Achievement 8":
                            row.pop(kname)
                    case "TechnicalWritingAssignmentDate":
                        if achvName != "Achievement 8":
                            row.pop(kname)
                    case "TechnicalWritingAssignment":
                        if achvName != "Achievement 8":
                            row.pop(kname)
                    case _:
                        if row[kname] != notCompletedMsg:
                            row.pop(kname)
            mdf.writelines(row.to_markdown(index=True))
            mdf.write("\n\n")
            mdf.write(f'***\n{emailAddress}\n\n')
            mdf.close()
            markdownFilePDF = mdf.name +".pdf"
            mp.md2pdf(pdf_file_path=markdownFilePDF,
                                          md_file_path= mdf.name,
                                          css_file_path='style.css')
            merger.append(open(markdownFilePDF, 'rb'))

with open(filePath) as file:
    dataFrame = pd.read_csv(filePath, sep=",")
    for index, row in dataFrame.iterrows():
        fullName = str( row["NameLast"] + ", " + row["NameFirst"]).lower()
        skip = False
        with open('./Exceptions.yaml') as exceptions:
            for exception in exceptions:
                        if exception.lower().startswith(fullName):
                            skip = True
                            break
        if not skip:
            ProcessRecord( row )

with open(allCadetsFile, 'wb') as fout:
    merger.write(fout)
