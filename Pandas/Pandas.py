import pandas as pd
import numpy as np

data =  np.array(["Engin", "Diyar", "Kutlu"])
s = pd.Series(data, index= [1,2,3])

print(s)

data2 = {"Matematik" : 10, "Fizik" : 20, "Beden Eğitimi": 100}
s2 = pd.Series(data2,index = ["Fizik", "Matematik", "Beden Eğitimi"])
print(s2)

print(s2[0])

s3 = pd.Series(5, index = [1,2,3,4,5])
print(s3)

#notlar = pd.read_csv("grades.csv")

#print(notlar)