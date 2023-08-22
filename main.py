import pandas as pd
import md2pdf.core as mp
filePath = 'Spokane_Squadron_promotion_report_8_9_2023.csv'
notCompletedMsg = "Not Completed"

def makeAllStrings(row, kname):
    if kname in row:
        if str(row[kname]).isdigit():
            if float(row[kname]) == 0:
                row[kname] = notCompletedMsg
        else:
            if pd.isna(row[kname] or row[kname] == 'h'):
                row[kname] = notCompletedMsg


with open(filePath) as file:
    dataFrame = pd.read_csv(filePath, sep=",")
    for index, row in dataFrame.iterrows():
        markdownFile = f'{row["Email"]}.md'
        with open(markdownFile, "w+") as mdf:
            lName = row["NameLast"]
            fName = row["NameFirst"]
            achvName = row["AchvName"]
            mdf.write("# "+lName + ", " + fName + "\n\n")
            mdf.write("### *Working on Achievement*:**" + achvName + "**\n\n")
            # mdf.write("> "+row["Email"]+"\n\n")
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
            mdf.write("\n")
            mdf.close()
            markdownFilePDF = markdownFile+".pdf"
            mp.md2pdf( pdf_file_path=markdownFilePDF,md_file_path=markdownFile,css_file_path='style.css')
