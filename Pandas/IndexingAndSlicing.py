import pandas as pd
notes = pd.read_csv("grades+(1).csv")
notes.columns = ["Name", "Lastname", "SSN",
                 "Test1", "Test2", "Test3",
                 "Test4", "Final" , "Grade"]
 
print(notes)

print(notes.loc[:, "Name"])
print(notes.loc[:5, "Name" : "Test4"])
print(notes.loc[:5, ["Name" , "Test4"]])
print(notes.loc[:5,: "Test2"])
print(notes.loc[::-1,: "Name"])