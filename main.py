import pandas as pd
import mdpdf
# import aspose.words as aw
filePath = 'Spokane_Squadron_promotion_report_8_9_2023.csv'
notCompletedMsg = "Not Completed"
def makeAllStrings(row,kname):
                if str(row[kname]).isdigit():
                        if float(row[kname]) == 0:
                            # row.pop(kname)
                            row[kname] = notCompletedMsg
                else:
                    if pd.isna(row[kname] or row[kname] == 'h'):
                    #     row.pop(kname)
                    # else:
                        row[kname] = notCompletedMsg
                # return row
    
with open(filePath) as file:
    dataFrame = pd.read_csv(filePath, sep=",")
    for index, row in dataFrame.iterrows():
        markdownFile = f'{row["Email"]}.md'
        with open(markdownFile, "w+") as mdf:
            lName = row["NameLast"]
            fName = row["NameFirst"]
            achvName = row["AchvName"]
            mdf.write("# "+lName + ", " + fName + "\n")
            mdf.write("> *Working on Achievement*:\n" )
            mdf.write("> **" + achvName + "**\n\n")
            for  kname in row.index:
                row = makeAllStrings(row,kname)
                match kname:
                    case  "AEInteractiveDate" | "AEModuleOrTest":
                        if row["AEModuleOrTest"] != row["AEInteractiveDate"] :
                        # if(row["AEModuleOrTest"] ):
                            # testString =str(row["AEModuleOrTest"]) 
                            # if testString != '0' and testString != 'h':
                            #     row.pop(kname)
                            # else:
                            #     row[kname] = testString
                            # if row["AEModuleOrTest"] != notCompletedMsg:
                            row.pop("AEModuleOrTest")
                            row.pop("AEInteractiveDate")
                            # else:
                            #     row.pop("AEModuleOrTest")
                    # case "AEModuleOrTest"  :
                    #     if row["AEInteractiveDate"]:
                    #         if  not pd.isna(row["AEInteractiveDate"]):
                    #             row.pop(kname)
                    #         else:
                    #             row[kname] = notCompletedMsg
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
