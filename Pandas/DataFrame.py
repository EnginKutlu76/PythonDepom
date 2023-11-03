import pandas as pd

data  = [10,20,30,40,50]
df = pd.DataFrame()
print(df)

data2 = [["Engin",18, "İstanbul"], ["Diyar", 9, "İstanbul"], ["Kutlu", 17, "Ankara"]]

df2 = pd.DataFrame(data2,columns = ["Name", "Age", "City"], index = [1,2,3])
print(df2)

data3 = {"Name" : ["Engin", "Diyar", "Kutlu"],
         "Age" : [18, 9, 17], 
         "City" : ["İstanbul", "İstanbul", "Ankara"]}

df3 = pd.DataFrame(data2,columns = ["Name", "Age", "City"], index = [1,2,3])
print(df3["Name"])


# del df3["Şehir"]

#df2.pop("Şehir")

print(df3.loc[2])
print(df3.loc(1))

df4 = df3.append(df2)
print(df4)
print(df4.head())
print(df4.tail())