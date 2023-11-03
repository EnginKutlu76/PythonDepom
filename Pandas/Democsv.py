import pandas as pd
notes = pd.read_csv("grades+(1).csv")
notes.columns = ["Name", "Lastname", "SSN",
                 "Test1", "Test2", "Test3",
                 "Test4", "Final" , "Grade"]
 
print(notes)
print(type(notes))
print(notes.head())
print(notes.tail())
print(notes["Final"])
print(notes.iloc[2])
print(notes[1:5])